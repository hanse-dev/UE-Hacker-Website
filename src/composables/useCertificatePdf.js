import { assetUrl } from '../utils/assetUrl';

const COURSE_TITLE = {
  de: 'Python 12-Wochen-Grundkurs',
  en: 'Python 12-Week Basics Course',
};

const TEXT = {
  de: {
    certificate: 'Zertifikat',
    awardedTo: 'verliehen an',
    weekLabel: (n) => `Woche ${n}`,
    learnedHeading: 'Was du gelernt hast',
    dateLabel: (d) => `Ausgestellt am ${d}`,
    footer: 'Übergangshacker - Dein Einstieg ins Coding: Loslegen. Ausprobieren. Verstehen.',
  },
  en: {
    certificate: 'Certificate',
    awardedTo: 'awarded to',
    weekLabel: (n) => `Week ${n}`,
    learnedHeading: 'What you learned',
    dateLabel: (d) => `Issued on ${d}`,
    footer: 'Übergangshacker - Your start into coding: Get started. Experiment. Understand.',
  },
};

function formatDate(lang) {
  const now = new Date();
  return now.toLocaleDateString(lang === 'en' ? 'en-GB' : 'de-DE', {
    year: 'numeric',
    month: 'long',
    day: 'numeric',
  });
}

// Simple greedy word-wrap using the given font's width metric.
function wrapText(text, font, size, maxWidth) {
  const words = text.split(/\s+/);
  const lines = [];
  let current = '';
  for (const word of words) {
    const attempt = current ? `${current} ${word}` : word;
    if (font.widthOfTextAtSize(attempt, size) > maxWidth && current) {
      lines.push(current);
      current = word;
    } else {
      current = attempt;
    }
  }
  if (current) lines.push(current);
  return lines;
}

// The standard PDF fonts only support WinAnsi (~Windows-1252) — strip characters they can't
// encode (emoji from notebook/markdown titles, etc.) instead of letting pdf-lib throw.
function sanitizeForPdfFont(text, font) {
  return Array.from(text || '')
    .filter((ch) => {
      try {
        font.widthOfTextAtSize(ch, 10);
        return true;
      } catch {
        return false;
      }
    })
    .join('')
    .replace(/\s+/g, ' ')
    .trim();
}

function sanitizeForFilename(text) {
  return text
    .normalize('NFKD')
    .replace(/[̀-ͯ]/g, '')
    .replace(/[^a-zA-Z0-9]+/g, '_')
    .replace(/^_+|_+$/g, '');
}

export async function generateCertificatePdfBytes({ weekNumber, weekTitle, lernziele, learnerName, lang = 'de', courseTitle }) {
  const { PDFDocument, StandardFonts, rgb } = await import('pdf-lib');
  const t = TEXT[lang] || TEXT.de;

  const doc = await PDFDocument.create();
  const page = doc.addPage([841.89, 595.28]); // A4 landscape
  const { width, height } = page.getSize();

  const font = await doc.embedFont(StandardFonts.Helvetica);
  const fontBold = await doc.embedFont(StandardFonts.HelveticaBold);

  const gold = rgb(0.72, 0.53, 0.04);
  const dark = rgb(0.18, 0.18, 0.2);
  const gray = rgb(0.4, 0.4, 0.42);

  // Border
  const margin = 24;
  page.drawRectangle({
    x: margin,
    y: margin,
    width: width - margin * 2,
    height: height - margin * 2,
    borderColor: gold,
    borderWidth: 3,
  });
  page.drawRectangle({
    x: margin + 8,
    y: margin + 8,
    width: width - (margin + 8) * 2,
    height: height - (margin + 8) * 2,
    borderColor: gold,
    borderWidth: 0.75,
  });

  let cursorY = height - 90;

  // Logo (best effort — certificate still renders fine without it)
  try {
    const logoRes = await fetch(assetUrl('logo.png'));
    if (logoRes.ok) {
      const logoBytes = await logoRes.arrayBuffer();
      const logoImage = await doc.embedPng(logoBytes);
      const logoHeight = 48;
      const logoWidth = (logoImage.width / logoImage.height) * logoHeight;
      page.drawImage(logoImage, {
        x: (width - logoWidth) / 2,
        y: cursorY - logoHeight + 20,
        width: logoWidth,
        height: logoHeight,
      });
      cursorY -= 40;
    }
  } catch {
    // Logo is decorative — ignore fetch/embed failures.
  }

  const drawCentered = (text, y, { size, useFont = font, color = dark } = {}) => {
    const textWidth = useFont.widthOfTextAtSize(text, size);
    page.drawText(text, { x: (width - textWidth) / 2, y, size, font: useFont, color });
  };

  cursorY -= 20;
  drawCentered(t.certificate.toUpperCase(), cursorY, { size: 30, useFont: fontBold, color: gold });

  cursorY -= 34;
  const courseTitleText = (courseTitle && (courseTitle[lang] || courseTitle.de)) || COURSE_TITLE[lang] || COURSE_TITLE.de;
  drawCentered(courseTitleText, cursorY, { size: 14, color: gray });

  cursorY -= 40;
  drawCentered(t.awardedTo, cursorY, { size: 13, color: gray });

  cursorY -= 30;
  drawCentered(sanitizeForPdfFont(learnerName, fontBold), cursorY, { size: 24, useFont: fontBold, color: dark });

  cursorY -= 36;
  // The week title from the notebook front-matter already starts with "Woche N – …" /
  // "Week N – …" — strip that so it isn't duplicated after our own "Woche N:" prefix.
  const cleanTitle = sanitizeForPdfFont(weekTitle, fontBold).replace(/^(Woche|Week)\s*\d+\s*[-–:]*\s*/i, '');
  const weekHeading = cleanTitle ? `${t.weekLabel(weekNumber)}: ${cleanTitle}` : t.weekLabel(weekNumber);
  drawCentered(weekHeading, cursorY, { size: 15, useFont: fontBold, color: dark });

  cursorY -= 34;
  drawCentered(t.learnedHeading, cursorY, { size: 12, useFont: fontBold, color: gold });

  cursorY -= 22;
  const bulletSize = 11;
  const maxTextWidth = width - margin * 2 - 120;
  const bulletLines = [];
  for (const goal of lernziele || []) {
    const cleanGoal = sanitizeForPdfFont(goal, font);
    if (!cleanGoal) continue;
    const lines = wrapText(cleanGoal, font, bulletSize, maxTextWidth);
    lines.forEach((line, i) => bulletLines.push(i === 0 ? `• ${line}` : `   ${line}`));
  }
  // Draw as one left-aligned block (centered as a whole) instead of centering each line on
  // its own — centering every bullet individually made the list look raggedly indented.
  const blockWidth = bulletLines.reduce((max, line) => Math.max(max, font.widthOfTextAtSize(line, bulletSize)), 0);
  const blockX = (width - blockWidth) / 2;
  for (const line of bulletLines) {
    page.drawText(line, { x: blockX, y: cursorY, size: bulletSize, font, color: dark });
    cursorY -= 16;
  }

  drawCentered(t.dateLabel(formatDate(lang)), margin + 46, { size: 10, color: gray });
  drawCentered(t.footer, margin + 28, { size: 9, color: gray });

  return doc.save();
}

export async function downloadCertificatePdf(options) {
  const bytes = await generateCertificatePdfBytes(options);
  const { weekNumber, learnerName, lang = 'de' } = options;
  const namePart = sanitizeForFilename(learnerName || 'Zertifikat');
  const prefix = lang === 'en' ? 'Certificate_Week' : 'Zertifikat_Woche';
  const filename = `${prefix}_${weekNumber}_${namePart}.pdf`;

  const blob = new Blob([bytes], { type: 'application/pdf' });
  const a = document.createElement('a');
  a.href = URL.createObjectURL(blob);
  a.download = filename;
  a.click();
  // Revoking immediately after click() races the browser's download start — it can silently
  // drop the download, especially noticeable when several certificates are downloaded back to
  // back. Defer the revoke instead of doing it synchronously.
  setTimeout(() => URL.revokeObjectURL(a.href), 2000);
}
