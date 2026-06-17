<template>
  <div class="teaser">
    <!-- Background blobs -->
    <div class="blob blob-1"></div>
    <div class="blob blob-2"></div>

    <!-- Floating code snippets -->
    <div
      v-for="(s, i) in floats"
      :key="i"
      class="code-float"
      :style="s.style"
    >{{ s.text }}</div>

    <!-- Main content -->
    <div class="content">
      <div class="logo-wrap">
        <img src="/logo.png" alt="Übergangshacker" />
      </div>

      <div class="chip">Workshop · Coding · Community</div>

      <h1>
        <span class="ue">Über</span><span class="gangs">gangs</span><span class="hacker">hacker</span>
      </h1>

      <div class="divider"></div>

      <p class="tagline">
        Wir sind heute hier — und du kannst <strong>einfach vorbeikommen.</strong><br />
        Lern programmieren, stell Fragen, mach mit.
      </p>

      <div class="cta">
        <span class="cta-arrow">→</span>
        <span class="cta-text">Komm gerne rein &amp; schau vorbei!</span>
        <span class="cta-arrow">←</span>
      </div>
    </div>

    <div class="bottom-bar"></div>
  </div>
</template>

<script>
export default {
  name: 'Teaser',
  setup() {
    const snippets = [
      'print("Hallo Welt!")', 'for i in range(10):', 'def lernen():',
      'if kreativ == True:', 'import python', 'x = input("Dein Name?")',
      'while True: coden()', 'class Hacker:', '# TODO: Welt verbessern',
      'return neues_wissen', 'liste = [✨, 🚀, 💡]', 'print(f"Level: {level}")',
    ];
    const cols = [80, 220, 420, 620, 820, 1020, 1200, 1400, 1600, 1780];
    const floats = cols.map((left, i) => ({
      text: snippets[i % snippets.length],
      style: {
        left: left + 'px',
        bottom: '-60px',
        animationDuration: (18 + i * 2.5) + 's',
        animationDelay: (i * 1.8) + 's',
      },
    }));
    return { floats };
  },
};
</script>

<style scoped>
.teaser {
  position: fixed;
  inset: 0;
  width: 100vw;
  height: 100vh;
  overflow: hidden;
  background: #0d1117;
  font-family: 'Segoe UI', system-ui, sans-serif;
  color: #fff;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

/* Grid background */
.teaser::before {
  content: '';
  position: absolute;
  inset: 0;
  background-image:
    linear-gradient(rgba(41,57,109,0.18) 1px, transparent 1px),
    linear-gradient(90deg, rgba(41,57,109,0.18) 1px, transparent 1px);
  background-size: 60px 60px;
  animation: gridMove 20s linear infinite;
}

@keyframes gridMove {
  from { background-position: 0 0; }
  to   { background-position: 60px 60px; }
}

/* Blobs */
.blob {
  position: absolute;
  border-radius: 50%;
  filter: blur(120px);
  opacity: 0.25;
  animation: blobPulse 6s ease-in-out infinite;
}
.blob-1 { width: 600px; height: 600px; background: #29396D; top: -150px; left: -150px; }
.blob-2 { width: 500px; height: 500px; background: #EF533A; bottom: -100px; right: -100px; animation-delay: 3s; }

@keyframes blobPulse {
  0%, 100% { transform: scale(1);    opacity: 0.25; }
  50%       { transform: scale(1.15); opacity: 0.35; }
}

/* Floating code */
.code-float {
  position: absolute;
  font-family: 'Courier New', monospace;
  font-size: 15px;
  color: rgba(239,83,58,0.2);
  white-space: nowrap;
  animation: floatUp linear infinite;
  user-select: none;
  pointer-events: none;
  z-index: 1;
}

@keyframes floatUp {
  from { transform: translateY(0);       opacity: 0; }
  10%  { opacity: 1; }
  90%  { opacity: 0.15; }
  to   { transform: translateY(-110vh);  opacity: 0; }
}

/* Content */
.content {
  position: relative;
  z-index: 10;
  display: flex;
  flex-direction: column;
  align-items: center;
}

/* Logo */
.logo-wrap {
  margin-bottom: 36px;
  animation: fadeDown 1s ease-out both;
}

.logo-wrap img {
  height: clamp(120px, 18vh, 200px);
  width: auto;
  filter: drop-shadow(0 8px 32px rgba(239,83,58,0.35));
}

/* Chip */
.chip {
  background: rgba(239,83,58,0.15);
  border: 1px solid rgba(239,83,58,0.5);
  color: #EF533A;
  font-size: clamp(14px, 1.5vw, 18px);
  font-weight: 600;
  letter-spacing: 4px;
  text-transform: uppercase;
  padding: 8px 28px;
  border-radius: 100px;
  margin-bottom: 28px;
  animation: fadeDown 1s ease-out 0.2s both;
}

/* Heading */
h1 {
  font-size: clamp(72px, 9vw, 130px);
  font-weight: 900;
  line-height: 1;
  text-align: center;
  letter-spacing: -3px;
  animation: fadeDown 1s ease-out 0.4s both;
  margin: 0;
}

.ue     { color: #fff; }
.gangs  { color: rgba(255,255,255,0.3); }
.hacker { color: #EF533A; }

/* Divider */
.divider {
  width: 120px;
  height: 4px;
  background: #EF533A;
  border-radius: 2px;
  margin: 32px 0;
  animation: grow 1s ease-out 0.7s both;
}

@keyframes grow {
  from { width: 0; opacity: 0; }
  to   { width: 120px; opacity: 1; }
}

/* Tagline */
.tagline {
  font-size: clamp(22px, 2.5vw, 36px);
  font-weight: 300;
  color: rgba(255,255,255,0.75);
  text-align: center;
  line-height: 1.5;
  animation: fadeUp 1s ease-out 0.8s both;
}

.tagline strong {
  color: #fff;
  font-weight: 600;
}

/* CTA */
.cta {
  margin-top: 44px;
  display: flex;
  align-items: center;
  gap: 20px;
  animation: fadeUp 1s ease-out 1.1s both;
}

.cta-arrow {
  font-size: 28px;
  color: #EF533A;
  animation: bounce 1.5s ease-in-out infinite;
}

@keyframes bounce {
  0%, 100% { transform: translateX(0); }
  50%       { transform: translateX(8px); }
}

.cta-text {
  font-size: clamp(20px, 2.2vw, 30px);
  font-weight: 700;
  letter-spacing: 0.5px;
}

/* Bottom bar */
.bottom-bar {
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  height: 5px;
  background: linear-gradient(90deg, #29396D, #EF533A, #29396D);
  background-size: 200% 100%;
  animation: shimmer 4s linear infinite;
}

@keyframes shimmer {
  from { background-position: 0% 0%; }
  to   { background-position: 200% 0%; }
}

@keyframes fadeDown {
  from { opacity: 0; transform: translateY(-24px); }
  to   { opacity: 1; transform: translateY(0); }
}

@keyframes fadeUp {
  from { opacity: 0; transform: translateY(16px); }
  to   { opacity: 1; transform: translateY(0); }
}
</style>
