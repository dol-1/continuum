# Roadmap

## Timeline: 6-7 Weeks

---

## Phase 0 — Foundation (Week 1)

**Goal:** Core infrastructure live on Velocycle server.

- [ ] Clone repo to /opt/continuum/
- [ ] Python venv setup + mcp-memory-service install
- [ ] Gemma 4 26B verify/pull via Ollama
- [ ] ChromaDB initialization
- [ ] Cloudflare Tunnel → memory.velocycle.us
- [ ] Health checks + Uptime Kuma monitoring

**Milestone:** memory.velocycle.us live, Gemma responding, ChromaDB ready.

---

## Phase 1 — Memory Core (Weeks 2-3)

**Goal:** Memory capture and consolidation working end-to-end.

- [ ] n8n workflows for memory ingestion
- [ ] nomic-embed-text embeddings pipeline
- [ ] Auto Dream consolidation (nightly Gemma scan)
- [ ] Memory Dashboard operational
- [ ] Basic search and retrieval

**Milestone:** First memory atom captured, consolidated, and retrieved.

---

## Phase 2 — Capture Layer (Weeks 3-4)

**Goal:** Multi-source capture operational.

- [ ] Page Assist browser extension configured
- [ ] Telegram @VeloCycleBot capture pipeline
- [ ] Claude/ChatGPT/Gemini conversation capture
- [ ] Tagging and categorization

**Milestone:** All capture sources feeding into memory system.

---

## Phase 3 — Intelligence Layer (Weeks 4-5)

**Goal:** Gemma background scanner fully operational.

- [ ] Real-time tagging pipeline
- [ ] Nightly consolidation scheduler
- [ ] Connection surfacing (orient → gather → consolidate → prune)
- [ ] Memory quality scoring

**Milestone:** Nightly consolidation running autonomously.

---

## Phase 4 — Interface (Weeks 5-6)

**Goal:** Seamless user experience.

- [ ] Open WebUI memory context integration
- [ ] Memory Dashboard search and visualization
- [ ] Telegram query interface
- [ ] Mobile-friendly access

**Milestone:** Full query-response loop via Telegram and web.

---

## Phase 5 — Polish (Week 7)

**Goal:** Stable, documented, open source ready.

- [ ] Performance optimization
- [ ] Backup and recovery procedures
- [ ] Full documentation
- [ ] MIT open source release

**Milestone:** Public release on GitHub.

---

## Subdomains

| Subdomain | Service |
|-----------|---------|
| chat.velocycle.us | Open WebUI |
| memory.velocycle.us | Memory Dashboard |