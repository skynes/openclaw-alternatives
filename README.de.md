# OpenClaw-Alternativen: Von Giganten zu Mikro-Agenten

*Zuletzt aktualisiert: März 2026*

**Übersetzungen:** [English](README.md) · [中文](README.zh-CN.md) · [Español](README.es.md) · [日本語](README.ja.md) · [Deutsch](README.de.md) · [Русский](README.ru.md)

![Titelbild](cover.png)

---

In dieser Übersicht stellen wir die aktuellen Projekte vor: vom Flaggschiff OpenClaw bis zu extrem leichtgewichtigen Lösungen wie NullClaw, die schneller starten als man blinzeln kann.

## 🧭 Was wählen? Schnell-Navigator

Wenn du schnell loslegen willst: Hier die Empfehlungen:

| Ziel | Empfohlenes Projekt | Warum? |
|------|---------------------|--------|
| **Universelle Wahl** | [**Nanobot**](https://github.com/HKUDS/nanobot) | Goldene Mitte: Python, aktive Community, Multi-Instanz-Support, geringe Hardware-Anforderungen (RAM 300MB+) |
| **Maximale Leistung** | [**OpenClaw**](https://github.com/openclaw/openclaw) | Der Standard, mehr braucht man nicht zu sagen. 15+ Kommunikationskanäle, Sprache, Canvas-Support, RAM 2GB+ |
| **Für schwache Rechner** | [**ZeroClaw**](https://github.com/zeroclaw-labs/zeroclaw) | Rust-Engine, verbraucht nur ~5MB RAM |
| **IoT und Edge** | [**PicoClaw**](https://github.com/sipeed/picoclaw) | Läuft auf Hardware für $10 (ESP32 und ähnlich) |
| **Sicherheit** | [**IronClaw**](https://github.com/nearai/ironclaw) | WebAssembly-Sandbox und paranoider Ansatz zur Privatsphäre |
| **Minimalismus** | [**TinyClaw**](https://github.com/jlia0/tinyclaw) | Nur 400 Zeilen Code. Ideal zum Lernen |

## 📊 Vergleichstabelle

Sortiert nach Beliebtheit und Projektaktivität auf GitHub (Daten Stand März 2026).

| Projekt | ⭐ Stars | Sprache | Typ | Merkmale |
|---------|---------|---------|-----|----------|
| [**OpenClaw**](https://github.com/openclaw/openclaw) | 306k | TypeScript | KI-Agent | Basisprojekt, MCP- und AWS-EC2-Support |
| [**Nanobot**](https://github.com/HKUDS/nanobot) | 32k | Python | KI-Agent | Multi-Instanz, ultra-leichtgewichtig |
| [**ZeroClaw**](https://github.com/zeroclaw-labs/zeroclaw) | 26k | Rust | KI-Agent | Speicherverbrauch ~5MB, schneller Start |
| [**PicoClaw**](https://github.com/sipeed/picoclaw) | 24k | Go | Edge/IoT | Läuft als Knoten im Gateway, günstige Hardware |
| [**AstrBot**](https://github.com/AstrBotDevs/AstrBot) | 22k | Python | Chatbot | Fokus auf IM-Plattformen (TG, WhatsApp) |
| [**NanoClaw**](https://github.com/qwibitai/nanoclaw) | 21k | TypeScript | KI-Agent | Containerisierung, Fokus auf Business-Messenger |
| [**IronClaw**](https://github.com/nearai/ironclaw) | 9.6k | Rust | KI-Agent | WASM-Sandbox, maximale Isolation |

## 🛠 Nischen-Alternativen und «Mikro-Hummer»

Für spezifische Anforderungen — von Bare-Metal bis Erlang-Systeme.

### Leistung und Edge

- [**NullClaw**](https://github.com/nullclaw/nullclaw) (Zig): Fantastische Leistung. 678KB-Binary, Start <2ms. Geeignet für Arduino und RPi.
- [**MimiClaw**](https://github.com/memovai/mimiclaw) (C): Läuft auf ESP32-S3 Bare-Metal. Lösungskosten ~$5.
- [**SubZeroClaw**](https://github.com/jmlago/subzeroclaw) (C): Nur 54KB.

### Sicherheit und Fehlertoleranz

- [**ZeptoClaw**](https://github.com/qhkm/zeptoclaw): 7-Schichten-Sicherheitssystem in Rust.
- [**BeamClaw**](https://github.com/peterdmv/beamclaw): In Erlang/OTP für verteilte Systeme geschrieben.
- [**Safeclaw**](https://github.com/princezuda/safeclaw): Läuft ohne LLM (Intent-Erkennung), garantiert 100% Vorhersagbarkeit.

## 🚀 Schnellstart

Für alle, die schon lange ausprobieren wollten — hier die Befehle für die beliebtesten Branches. Einrichtungszeit: bis zu 3 Minuten.

### 1. Nanobot (schnellster Einstieg)

```bash
git clone https://github.com/HKUDS/nanobot.git && cd nanobot
docker compose run --rm nanobot-cli onboard
# API-Key in ~/.nanobot/config.json eintragen
docker compose up -d nanobot-gateway
```

### 2. ZeroClaw (minimale Konfiguration)

```bash
git clone https://github.com/zeroclaw-labs/zeroclaw.git && cd zeroclaw
cp .env.example .env   # API_KEY setzen
docker compose up -d
```

### 3. PicoClaw

```bash
git clone https://github.com/sipeed/picoclaw.git && cd picoclaw
docker compose -f docker/docker-compose.yml --profile gateway up   # erster Lauf
vim docker/data/config.json   # API keys, Bot-Tokens
docker compose -f docker/docker-compose.yml --profile gateway up -d
```

### 4. OpenClaw

```bash
git clone https://github.com/openclaw/openclaw.git && cd openclaw
./docker-setup.sh   # Assistent, Image-Build, erster Lauf
```

## Nützliche Ressourcen

- **Skills / Ressourcen:** [clawhub](https://github.com/clawhub) / [awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills)

---

## 💡 Weitere Projekte vorschlagen

**Haben wir etwas vergessen? Sag Bescheid!** Öffne ein [Issue](https://github.com/skynes/openclaw-alternatives/issues) oder sende einen Pull Request — wir vergleichen und fügen es der Übersicht hinzu.
