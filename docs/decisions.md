# Architecture Decisions

## ADR-001: Gemma 4 26B A4B as Primary Local LLM
**Status:** Accepted | **Date:** 2026-04

**Context:** Need local LLM that runs on Xeon E5-2620 v4 / 62GB RAM with usable speed for background scanning and consolidation.

**Decision:** Gemma 4 26B A4B (active-4B MoE variant).

**Rationale:** Benchmarked at 7+ tok/s on target hardware — sufficient for background work. Strong multilingual (Georgian + English). Apache 2.0 license. Fits comfortably in RAM alongside other VM workloads.

**Consequences:** No GPU required. Real-time scanner feasible. Heavy reasoning still offloadable to OpenRouter/DeepSeek when needed.

---

## ADR-002: Gemma as Background Scanner (Dual Mode)
**Status:** Accepted

**Decision:** Single Gemma instance serves both real-time tagging and nightly consolidation.

**Rationale:** Avoids model-swap overhead. Same context window, same prompt library. Mode switch is just a different system prompt + batch size.

**Consequences:** Scheduler must prevent overlap between real-time and consolidation runs. n8n handles queue.

---

## ADR-003: Memory Consolidation Engine = Phase 1 Core
**Status:** Accepted

**Decision:** Build the Auto Dream four-phase engine (orient/gather/consolidate/prune) as a Phase 1 deliverable, not a Phase 3+ enhancement.

**Rationale:** Without consolidation, captured atoms become noise within weeks. The engine *is* the product — capture alone is solved territory.

**Consequences:** Phase 1 timeline tighter. Justified — defers other features but de-risks the core value proposition.