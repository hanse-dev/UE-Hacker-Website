# Übergangshacker Website - Projekt Übersicht

## Zweck der WebApp
**Lernplattform für Jugendliche zum Programmieren lernen in Python**

Die Website dient als zentrale Anlaufstelle für:
- Schulungen und Kurse für Kids/Jugendliche
- Bereitstellung von Lernmaterialien
- Downloads von Hausaufgaben und Cheat Sheets

## Zielgruppe
- Kinder und Jugendliche die Programmieren lernen möchten
- Fokus auf Python-Programmierung

## Geplante Kurse & Inhalte

### Aktueller Kursplan:
1. **12-Wochen Python Grundkurs** 
   - Bereitstellung von Kursmaterialien
   - Hausaufgaben zum Download
   - Cheat Sheets

2. **Weitere Kurse** (geplant)
   - Erweiterbare Struktur für zukünftige Kurse

## Design-Anforderungen
- **Zielgruppe**: Jugendliche (ansprechend, aber nicht zu verspielt)
- **Farbschema**: Gelbes Design mit roten Akzenten
- **Framework**: Vue
- **Styling**: CSS
- **Modern und clean**, professionell aber jugendgerecht

## Funktionale Anforderungen

### Content Management:
- Total einfach, Dateien in einem Ordner sollen nach der Struktur auf der Website angezeigt werden

### Technische Features:
- SEO-optimiert
- Docker-Deployment ready

## Deployment & Docker

This project is fully configured to run with Docker and Docker Compose, simplifying both development and deployment.

### Local Development with Docker

To start the development server with live-reloading, run:

```bash
docker-compose up dev
```

The website will be available at `http://localhost:5173`.

### Production with Docker

To build and run the production-ready version of the website, run:

```bash
docker-compose up -d --build prod
```

The website will be served by Nginx at `http://localhost:8080`.

This setup is ideal for deploying the website to a Virtual Private Server (VPS).
- Performance-optimiert
- SEO/Meta-Tags für bessere Auffindbarkeit

## Chat-Einstiegspunkt
Diese Datei dient als Referenz für zukünftige Entwicklungsarbeiten und Kontext für neue Chat-Sessions.

---
*Erstellt: $(date)*
*Letzte Aktualisierung: Bei größeren Änderungen*

