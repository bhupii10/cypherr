# Cypher Execution Flow

## Push-To-Talk Runtime Flow

1. User presses push-to-talk key

2. Renderer detects input

3. Renderer sends IPC event to Electron Main

4. Electron Main forwards execution request to Python backend

5. Backend activates speech-to-text pipeline

6. Faster Whisper processes audio input

7. Transcript stream generated

8. Transcript enters orchestrator

9. Orchestrator determines execution path

10. Tool runtime executes selected action

11. Execution result streamed back through backend events

12. Electron receives streamed events

13. Renderer updates holographic UI

---

## Current Async Boundaries

- renderer → electron main
- electron main → python backend
- backend → whisper runtime
- orchestrator → tool execution
- backend → renderer streaming

---

## Current Potential Risk Areas

- IPC event synchronization
- streaming backpressure
- blocking inference operations
- orchestrator over-coupling
- shared mutable state
