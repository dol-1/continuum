# Continuum

A local-first personal memory and knowledge integration layer.

Continuum connects your AI conversations, browser activity, and notes into
a single searchable memory system — running entirely on your own hardware.

## What It Does

- Captures context from multiple AI assistants (Claude, ChatGPT, Gemini)
- Stores and indexes everything locally using ChromaDB
- Runs a local LLM (Gemma 4 26B) for nightly memory consolidation
- Provides a web dashboard for memory exploration
- Integrates with Telegram for mobile capture

## Architecture

    Browser (Page Assist) ──┐
    Telegram Bot ───────────┼──► n8n Orchestration ──► mcp-memory-service ──► ChromaDB
    AI Conversations ───────┘         │
                                      ▼
                              Gemma 4 26B (Ollama)
                              Background Scanner +
                              Memory Consolidation

## Stack

| Component | Technology |
|-----------|------------|
| Local LLM | Gemma 4 26B via Ollama |
| Memory Backend | mcp-memory-service + ChromaDB |
| Orchestration | n8n |
| Browser Capture | Page Assist |
| Mobile Capture | Telegram @VeloCycleBot |
| Dashboard | mcp-memory-service native UI |

## Hardware Requirements

- RAM: 32GB minimum, 62GB recommended
- Storage: 100GB+
- OS: Ubuntu 24.04 recommended

## Quick Start

    git clone https://github.com/dol-1/continuum
    cd continuum
    cp .env.example .env
    docker compose up -d

## Project Status

Active Development — Phase 0

## License

MIT 2026 dol-1