# Cypher System Overview

## Core Philosophy

- local-first
- modular
- deterministic
- scalable
- offline-capable

---

## Current Stack

- Electron
- Python backend
- Faster Whisper large-v3
- CUDA acceleration
- IPC bridge
- backend event streaming
- modular tool runtime
- push-to-talk execution loop

---

## Current Goals

- stabilize architecture
- identify unsafe abstractions
- enforce clean subsystem boundaries
- prepare for scalable Phase 2 development
- preserve existing functionality
- prevent architectural entropy

---

## Current Runtime Structure

Renderer UI
↓
Electron IPC
↓
Electron Main Process
↓
Python Backend
↓
Orchestrator
↓
Tool Runtime
↓
Inference + Execution Systems

---

## Current Known Risks

- IPC scaling complexity
- orchestrator overgrowth
- hidden shared state
- async synchronization risks
- backend/frontend coupling
- streaming pipeline instability
