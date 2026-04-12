# Dependencies

## Use As-Is (no fork)
| Component | Repo | License | Why |
|---|---|---|---|
| MemPalace | github.com/milla-jovovich/mempalace | MIT | Solid memory core, active dev |
| Page Assist | github.com/n4ze3m/page-assist | MIT | Best-in-class browser capture |
| Ollama | ollama.ai | MIT | Standard local LLM runtime |
| n8n | n8n.io | Sustainable Use | Already deployed on Velocycle |

## Build Ourselves
| Component | Why not existing |
|---|---|
| Memory Consolidation Engine | No OSS implementation of Auto Dream pattern exists |
| Multi-AI capture normalizer | Each platform's export format differs; need unified schema |
| Georgian-aware chunking | Existing chunkers split Georgian poorly |
| Telegram → MemPalace bridge | Custom n8n workflow |

## Models
- **Gemma 4 26B A4B** — primary, local
- **nomic-embed-text** — embeddings, local
- **DeepSeek V3** (OpenRouter) — fallback for heavy reasoning