# Cypher IPC Map

## Renderer → Electron Main

### START_MIC

Purpose:
- begin voice capture

---

### STOP_MIC

Purpose:
- stop voice capture

---

### EXECUTE_PROMPT

Purpose:
- send transcript for execution

---

## Electron Main → Python Backend

### START_STT

Purpose:
- initialize speech-to-text pipeline

---

### STOP_STT

Purpose:
- terminate speech-to-text pipeline

---

### RUN_TOOL

Purpose:
- execute backend tool

---

## Python Backend → Renderer

### TRANSCRIPT_PARTIAL

Purpose:
- stream partial transcript

---

### TRANSCRIPT_FINAL

Purpose:
- send final transcript

---

### STREAM_TOKEN

Purpose:
- stream execution response

---

### EXECUTION_COMPLETE

Purpose:
- signal execution completion
- 
