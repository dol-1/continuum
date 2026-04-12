markdown# Architecture

Continuum is a 5-layer integration system. Each layer is replaceable.

## Layer Overview
┌─────────────────────────────────────────────────────┐
│  L5: INTERFACES                                     │
│  Page Assist · Telegram Bot · Obsidian (optional)   │
└────────────────────┬────────────────────────────────┘
│
┌────────────────────▼────────────────────────────────┐
│  L4: ORCHESTRATION                                  │
│  n8n workflows · webhooks · schedulers              │
└────────────────────┬────────────────────────────────┘
│
┌────────────────────▼────────────────────────────────┐
│  L3: INTELLIGENCE (Background Scanner)              │
│  Gemma 4 26B · real-time mode · consolidation mode  │
│  Memory Consolidation Engine (Auto Dream pattern)   │
└────────────────────┬────────────────────────────────┘
│
┌────────────────────▼────────────────────────────────┐
│  L2: MEMORY CORE                                    │
│  MemPalace · vector store (nomic-embed-text)        │
└────────────────────┬────────────────────────────────┘
│
┌────────────────────▼────────────────────────────────┐
│  L1: INFRASTRUCTURE                                 │
│  Ollama · Docker · Cloudflare Tunnel · Ubuntu VM    │
└─────────────────────────────────────────────────────┘

## Data Flow: Capture → Consolidate
[Claude.ai/ChatGPT/Gemini]
│ Page Assist extension
▼
[n8n webhook] ──► [MemPalace ingest] ──► [vector store]
│                                       │
│                                       ▼
│                            [Gemma scanner: real-time]
│                                       │
▼                                       ▼
[Telegram capture] ─────────────────► [memory atoms]
│
┌─────────────────┘
▼
[Consolidation Engine — nightly]
orient → gather → consolidate → prune
│
▼
[consolidated memories + index]

## Memory Consolidation Engine

Four-phase Auto Dream pattern (Anthropic-inspired):

1. **Orient** — scan recent atoms, identify themes
2. **Gather** — cluster related atoms across time
3. **Consolidate** — Gemma synthesizes clusters into durable memories
4. **Prune** — archive duplicates, keep canonical versions

Runs in two modes:
- **Real-time**: lightweight tagging on ingest
- **Consolidation**: heavy nightly batch via cron