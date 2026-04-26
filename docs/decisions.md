# Architecture Decision Records

## ADR-001: Primary Local LLM

**Decision:** Gemma 4 26B via Ollama as the primary local LLM.

**Reasoning:** Confirmed 7+ tokens/second on available hardware (62GB RAM).
Sufficient performance for real-time interaction and background processing.

**Status:** Accepted

---

## ADR-002: Background Scanner

**Decision:** Gemma 4 26B dual-mode background scanner using the same Ollama instance.

**Modes:**
- Real-time tagging of incoming memory atoms
- Nightly consolidation of accumulated knowledge

**Status:** Accepted

---

## ADR-003: Memory Consolidation Engine

**Decision:** Auto Dream pattern as the core consolidation algorithm.

**Pattern:** orient → gather → consolidate → prune

**Reasoning:** Mirrors human sleep-cycle memory consolidation. Runs nightly
to surface connections, remove redundancy, and strengthen important memories.

**Status:** Accepted

---

## ADR-004: Memory Backend

**Decision:** mcp-memory-service via pip install in Python venv at /opt/continuum/venv/

**Reasoning:** Clean isolation from system Python. Easy to update and reproduce.

**Status:** Accepted

### Revision — 2026-04-25: Storage backend canonicalized

The original ADR-004 was silent on the underlying storage backend within
mcp-memory-service. This revision makes the choice explicit.

**Decision:** `sqlite_vec` is the canonical storage backend for Phase 1.

**Context:** chromadb installation failed during Phase 0 deployment.
`sqlite_vec` (bundled with mcp-memory-service) was used as the fallback
and confirmed working in production.

**Configuration:**
- `MCP_MEMORY_STORAGE_BACKEND=sqlite_vec`
- Config file: `/opt/continuum/config/.env`
- ChromaDB dependency dropped.

**Verification (Phase 1 Sprint 1.1):**
- Memory create: success
- Semantic search: 117ms, similarity score 0.806
- 6 memories persisted across service restarts
- API endpoint: `http://localhost:8100/api/` (POST /api/memories, POST /api/search)

**Consequences:** No further action required. `sqlite_vec` is the default
fallback in `mcp_memory_service.config`. `dependencies.md` updated to
reflect the canonical backend.

---

## ADR-005: Memory Dashboard

**Decision:** mcp-memory-service native web UI (port 8000) as the memory dashboard.

**Reasoning:** No additional tooling required. Accessible via memory.velocycle.us

**Status:** Accepted
