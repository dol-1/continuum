# Dependencies

## Hardware

| Component | Specification |
|-----------|--------------|
| Server | HP ProLiant DL180 Gen9 |
| RAM | 62GB |
| Storage | 490GB |
| OS | Ubuntu 24.04 |
| VM | MyOffice |
| Domain | velocycle.us |

## Core Services

| Service | Version | Port | URL |
|---------|---------|------|-----|
| Ollama | latest | 11434 | - |
| mcp-memory-service | latest (pip) | 8000 | memory.velocycle.us |
| Open WebUI | latest | 3000 | chat.velocycle.us |
| n8n | latest | 5678 | - |
| ChromaDB | via mcp-memory-service | - | - |

## Models

| Model | Tag | Size | Purpose |
|-------|-----|------|---------|
| Gemma 4 | gemma4:26b | ~18GB | Primary LLM + Background Scanner |
| nomic-embed-text | latest | ~274MB | Embeddings |

## Infrastructure

| Component | Technology |
|-----------|-----------|
| Containerization | Docker Compose |
| Container Management | Portainer |
| Tunnel | Cloudflare Tunnel + Zero Trust |
| Monitoring | Uptime Kuma |
| Auto-updates | Watchtower |

## Environment Variables

    MCP_MEMORY_STORAGE_BACKEND=chroma
    MCP_MEMORY_CHROMA_PATH=/opt/continuum/data/chroma_db
    MCP_MEMORY_BACKUPS_PATH=/opt/continuum/data/backups
    MCP_HTTP_ENABLED=true
    MCP_HTTP_PORT=8000
    MCP_ALLOW_ANONYMOUS_ACCESS=true
    OLLAMA_BASE_URL=http://localhost:11434

## Python Environment

    Location: /opt/continuum/venv/
    Python: 3.12+
    Install: pip install mcp-memory-service
    Run (HTTP mode): memory server --http