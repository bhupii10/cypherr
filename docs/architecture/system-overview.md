# Cypher Process Map

## Electron Main Process

Responsibilities:
- application lifecycle
- window creation
- IPC bridge
- backend process spawning

Dependencies:
- renderer process
- python backend

Failure Impact:
- full application failure

---

## Renderer Process

Responsibilities:
- holographic UI rendering
- animations
- user interaction
- stream visualization

Dependencies:
- IPC events

Failure Impact:
- UI unusable
- backend may still run

---

## Python Backend Process

Responsibilities:
- orchestration
- STT execution
- tool execution
- backend streaming

Dependencies:
- Faster Whisper
- CUDA runtime

Failure Impact:
- assistant execution unavailable
