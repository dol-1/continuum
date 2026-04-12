# 🧠 Continuum

> Personal "second brain" integration layer — local-first, open source.

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Status](https://img.shields.io/badge/status-alpha-orange.svg)]()

---

**Continuum** is a personal "second brain" integration layer that unifies MemPalace, Page Assist, local Gemma 4 26B, n8n, and a Telegram bot into one living memory system.

## Why?

Modern AI tools (Claude, ChatGPT, Gemini) are brilliant but forgetful. Every conversation starts from zero. Continuum captures those conversations, analyzes them locally with Gemma, and builds a personal, searchable, permanent memory layer that grows with you.

## Core Features

- 🔒 **Local-first** — your data never leaves your server
- 🌐 **Multi-AI capture** — Claude.ai, ChatGPT, and Gemini in one place
- 🧬 **Memory Consolidation Engine** — Anthropic Auto Dream pattern (orient / gather / consolidate / prune)
- 📱 **Telegram integration** — capture from anywhere
- 👁️ **Obsidian-compatible** — optional desktop viewer
- 🔌 **Modular** — every layer is replaceable

## Architecture

Continuum is a 5-layer integration system:

1. **Infrastructure** — Ollama, Docker, Cloudflare Tunnel
2. **Memory Core** — MemPalace + vector store
3. **Intelligence** — Gemma 4 26B background scanner
4. **Orchestration** — n8n workflows
5. **Interfaces** — Page Assist, Telegram, Obsidian

See [docs/architecture.md](docs/architecture.md) for full diagrams and data flow.

## Roadmap

6–7 weeks, 5 phases. See [docs/roadmap.md](docs/roadmap.md).

## Built On

- [MemPalace](https://github.com/milla-jovovich/mempalace) — memory core
- [Page Assist](https://github.com/n4ze3m/page-assist) — browser capture
- [Ollama](https://ollama.ai) + Gemma 4 26B — local inference
- [n8n](https://n8n.io) — workflow orchestration

## Status

Alpha. Under active development. Not yet recommended for production use.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

MIT — see [LICENSE](LICENSE).