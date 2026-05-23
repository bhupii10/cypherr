# Cypher State Ownership

| State | Owner |
|---|---|
| microphone active state | renderer |
| holographic UI state | renderer |
| IPC routing state | electron main |
| execution queue | orchestrator |
| transcript stream | backend |
| tool registry | backend |
| whisper model lifecycle | inference runtime |
| CUDA runtime state | inference runtime |
| execution stream state | backend |
| persistent memory | storage subsystem |

---

## Current Risk Areas

- unclear execution ownership boundaries
- possible shared mutable state
- orchestrator state expansion risk
- renderer/backend synchronization complexity
