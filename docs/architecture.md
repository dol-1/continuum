# Architecture

## Overview

Continuum is a five-layer local-first memory integration system.
All data remains on personal hardware. No cloud dependencies for core functionality.

## System Layers

    ┌─────────────────────────────────────────────────────┐
    │                   CAPTURE LAYER                     │
    │  Page Assist (browser)  │  Telegram @VeloCycleBot   │
    │  Claude / ChatGPT / Gemini conversations            │
    └─────────────────────┬───────────────────────────────┘
                          │
    ┌─────────────────────▼───────────────────────────────┐
    │               ORCHESTRATION LAYER                   │
    │                    n8n                              │
    │         Routing │ Triggers │ Workflows              │
    └─────────────────────┬───────────────────────────────┘
                          │
    ┌─────────────────────▼───────────────────────────────┐
    │                 MEMORY LAYER                        │
    │            mcp-memory-service                       │
    │         ChromaDB │ Embeddings (nomic)               │
    └──────────┬──────────────────────┬───────────────────┘
               │                      │
    ┌──────────▼──────────┐  ┌────────▼───────────────────┐
    │   PROCESSING LAYER  │  │      INTERFACE LAYER        │
    │   Gemma 4 26B       │  │  Open WebUI (chat)          │
    │   via Ollama        │  │  Memory Dashboard (port 8000)│
    │   Real-time tagging │  │  chat.velocycle.us          │
    │   Nightly consolid. │  │  memory.velocycle.us        │
    └─────────────────────┘  └────────────────────────────┘

## Memory Consolidation (Auto Dream Pattern)

Runs nightly via Gemma 4 26B background scanner:

    1. ORIENT    — identify recent memory atoms
    2. GATHER    — cluster related concepts
    3. CONSOLIDATE — merge and strengthen connections
    4. PRUNE     — remove redundancy and noise

## Data Flow

    Input → n8n → mcp-memory-service → ChromaDB
                        │
                   nomic-embed-text
                   (vector embeddings)
                        │
                   Gemma 4 26B
                   (tagging + consolidation)

## Storage Structure

    /opt/continuum/
    ├── data/
    │   ├── chroma_db/      ← vector database
    │   └── backups/        ← automated backups
    ├── logs/               ← service logs
    ├── config/             ← configuration files
    └── venv/               ← Python virtual environment

## Infrastructure

    Cloudflare Tunnel → Zero Trust → MyOffice (Ubuntu 24.04)
                                          │
                                    Docker Compose
                                          │
                    ┌─────────────────────┼─────────────────────┐
                    │                     │                     │
                 Ollama            mcp-memory-service          n8n
               (port 11434)         (port 8000)           (port 5678)