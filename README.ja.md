# OpenClaw 代替案：巨人からマイクロエージェントまで

*最終更新：2026年3月*

**翻訳：** [English](README.md) · [中文](README.zh-CN.md) · [Español](README.es.md) · [日本語](README.ja.md) · [Deutsch](README.de.md) · [Русский](README.ru.md)

---

この概要では、フラッグシップの OpenClaw から、瞬きより速く起動する NullClaw のような極軽量ソリューションまで、現在のプロジェクトを紹介します。

## 🧭 何を選ぶ？クイックナビゲーター

すぐに始めたい方へ：

| 目的 | 推奨プロジェクト | 理由 |
|------|------------------|------|
| **汎用選択** | **Nanobot** | バランス重視：Python、活発なコミュニティ、マルチインスタンス対応、ハードウェア要求低（RAM 300MB+） |
| **最大性能** | **OpenClaw** | 業界標準。15+ 通信チャネル、音声、Canvas 対応、RAM 2GB+ |
| **低スペック機** | **ZeroClaw** | Rust エンジン、わずか ~5MB RAM |
| **IoT・Edge** | **PicoClaw** | $10 のハードウェアで動作（ESP32 など） |
| **セキュリティ** | **IronClaw** | WebAssembly サンドボックス、プライバシー重視 |
| **ミニマリズム** | **TinyClaw** | わずか 400 行。学習に最適 |

## 📊 比較表

GitHub の人気・活動度でソート（2026年3月データ）。

| プロジェクト | ⭐ Stars | 言語 | タイプ | 特徴 |
|-------------|---------|------|--------|------|
| **OpenClaw** | 306k | TypeScript | AIエージェント | 基盤プロジェクト、MCP・AWS EC2 対応 |
| **Nanobot** | 32k | Python | AIエージェント | マルチインスタンス、超軽量 |
| **ZeroClaw** | 26k | Rust | AIエージェント | メモリ使用 ~5MB、高速起動 |
| **PicoClaw** | 24k | Go | Edge/IoT | ゲートウェイノード、低コストハードウェア |
| **AstrBot** | 22k | Python | チャットボット | IM プラットフォーム対応（TG、WhatsApp） |
| **NanoClaw** | 21k | TypeScript | AIエージェント | コンテナ化、ビジネスメッセンジャー向け |
| **IronClaw** | 9.6k | Rust | AIエージェント | WASM サンドボックス、最大分離 |

## 🛠 ニッチ代替と「マイクロロブスター」

特定のニーズ向け — ベアメタルから Erlang システムまで。

### パフォーマンスと Edge

- **NullClaw** (Zig)：驚異的な性能。678KB バイナリ、起動 <2ms。Arduino・RPi 対応。
- **MimiClaw** (C)：ESP32-S3 ベアメタルで動作。ソリューションコスト約 $5。
- **SubZeroClaw** (C)：わずか 54KB。

### セキュリティと耐障害性

- **ZeptoClaw**：Rust の 7 層セキュリティシステム。
- **BeamClaw**：Erlang/OTP 製、分散システム向け。
- **Safeclaw**：LLM 不要（意図認識）、100% 予測可能性を保証。

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

---

## 💡 他のプロジェクトを提案

**見落としがあれば教えてください！** [Issue](https://github.com/skynes/openclaw-alternatives/issues) を開くか Pull Request を送信 — 比較して概要に追加します。
