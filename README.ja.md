# OpenClaw 代替案：巨人からマイクロエージェントまで

*最終更新：2026年4月*

**翻訳：** [English](README.md) · [中文](README.zh-CN.md) · [Español](README.es.md) · [日本語](README.ja.md) · [Deutsch](README.de.md) · [Русский](README.ru.md)

![カバー](cover.png)

---

この概要では、フラッグシップの OpenClaw から、瞬きより速く起動する NullClaw のような極軽量ソリューションまで、現在のプロジェクトを紹介します。

## 🧭 何を選ぶ？クイックナビゲーター

すぐに始めたい方へ：

| 目的 | 推奨プロジェクト | 理由 |
|------|------------------|------|
| **汎用選択** | [**Nanobot**](https://github.com/HKUDS/nanobot) | バランス重視：Python、活発なコミュニティ、マルチインスタンス対応、ハードウェア要求低（RAM 300MB+） |
| **最大性能** | [**OpenClaw**](https://github.com/openclaw/openclaw) | 業界標準。15+ 通信チャネル、音声、Canvas 対応、RAM 2GB+ |
| **自己改善 / 研究** | [**Hermes Agent**](https://github.com/NousResearch/hermes-agent) | Nous Research：学習ループ、スキルと記憶、MCP、ゲートウェイ；OpenClaw から移行（`hermes claw migrate`） |
| **低スペック機** | [**ZeroClaw**](https://github.com/zeroclaw-labs/zeroclaw) | Rust エンジン、わずか ~5MB RAM |
| **IoT・Edge** | [**PicoClaw**](https://github.com/sipeed/picoclaw) | $10 のハードウェアで動作（ESP32 など） |
| **セキュリティ** | [**IronClaw**](https://github.com/nearai/ironclaw) | WebAssembly サンドボックス、プライバシー重視 |
| **Go / スケール** | [**GoClaw**](https://github.com/nextlevelbuilder/goclaw) | Go で再実装した OpenClaw。マルチテナント、5 層セキュリティ、ネイティブ並行 |
| **ミニマリズム** | [**TinyClaw**](https://github.com/jlia0/tinyclaw) | わずか 400 行。学習に最適 |

## 📊 比較表

GitHub の人気・活動度でソート（2026年4月データ）。

| プロジェクト | ⭐ Stars | 言語 | タイプ | 特徴 |
|-------------|---------|------|--------|------|
| [**OpenClaw**](https://github.com/openclaw/openclaw) | 357k | TypeScript | AIエージェント | 基盤プロジェクト、MCP・AWS EC2 対応 |
| [**Hermes Agent**](https://github.com/NousResearch/hermes-agent) | 86k | Python | AIエージェント | 学習ループ、スキル、ゲートウェイ、OpenClaw 移行 |
| [**Nanobot**](https://github.com/HKUDS/nanobot) | 39k | Python | AIエージェント | マルチインスタンス、超軽量 |
| [**ZeroClaw**](https://github.com/zeroclaw-labs/zeroclaw) | 30k | Rust | AIエージェント | メモリ使用 ~5MB、高速起動 |
| [**AstrBot**](https://github.com/AstrBotDevs/AstrBot) | 29k | Python | チャットボット | IM プラットフォーム対応（TG、WhatsApp） |
| [**PicoClaw**](https://github.com/sipeed/picoclaw) | 28k | Go | Edge/IoT | ゲートウェイノード、低コストハードウェア |
| [**NanoClaw**](https://github.com/qwibitai/nanoclaw) | 27k | TypeScript | AIエージェント | コンテナ化、ビジネスメッセンジャー向け |
| [**IronClaw**](https://github.com/nearai/ironclaw) | 11.8k | Rust | AIエージェント | WASM サンドボックス、最大分離 |
| [**GoClaw**](https://github.com/nextlevelbuilder/goclaw) | 2.7k | Go | AIエージェント | マルチテナント、5 層セキュリティ、MCP、Postgres |

*星数は概算。[scripts/data/github_stats.json](scripts/data/github_stats.json) に正確な値。ライブバッジ: [shields.io](https://shields.io/badges/git-hub-repo-stars)（`https://img.shields.io/github/stars/<owner>/<repo>`）。*

## 🛠 ニッチ代替と「マイクロロブスター」

特定のニーズ向け — ベアメタルから Erlang システムまで。

### パフォーマンスと Edge

- [**NullClaw**](https://github.com/nullclaw/nullclaw) (Zig)：驚異的な性能。678KB バイナリ、起動 <2ms。Arduino・RPi 対応。
- [**MimiClaw**](https://github.com/memovai/mimiclaw) (C)：ESP32-S3 ベアメタルで動作。ソリューションコスト約 $5。
- [**SubZeroClaw**](https://github.com/jmlago/subzeroclaw) (C)：わずか 54KB。

### セキュリティと耐障害性

- [**ZeptoClaw**](https://github.com/qhkm/zeptoclaw)：Rust の 7 層セキュリティシステム。
- [**BeamClaw**](https://github.com/peterdmv/beamclaw)：Erlang/OTP 製、分散システム向け。
- [**Safeclaw**](https://github.com/princezuda/safeclaw)：LLM 不要（意図認識）、100% 予測可能性を保証。

## 🚀 クイックスタート

人気ブランチの起動コマンドをまとめました。セットアップは 3 分以内。

### 1. Nanobot（最速）

```bash
git clone https://github.com/HKUDS/nanobot.git && cd nanobot
docker compose run --rm nanobot-cli onboard
# ~/.nanobot/config.json に API key を追加
docker compose up -d nanobot-gateway
```

### 2. ZeroClaw（最小構成）

```bash
git clone https://github.com/zeroclaw-labs/zeroclaw.git && cd zeroclaw
cp .env.example .env   # API_KEY を設定
docker compose up -d
```

### 3. PicoClaw

```bash
git clone https://github.com/sipeed/picoclaw.git && cd picoclaw
docker compose -f docker/docker-compose.yml --profile gateway up   # 初回実行
vim docker/data/config.json   # API keys、ボットトークン
docker compose -f docker/docker-compose.yml --profile gateway up -d
```

### 4. OpenClaw

```bash
git clone https://github.com/openclaw/openclaw.git && cd openclaw
./docker-setup.sh   # ウィザード、イメージビルド、初回実行
```

## 便利なリソース

- **Skills / リソース：** [clawhub](https://github.com/clawhub) / [awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills)
- **他のリポジトリ：** GitHub トピック [`openclaw-alternative`](https://github.com/topics/openclaw-alternative)

---

## 💡 他のプロジェクトを提案

**見落としがあれば教えてください！** [Issue](https://github.com/skynes/openclaw-alternatives/issues) を開くか Pull Request を送信 — 比較して概要に追加します。
