const { contextBridge, ipcRenderer } = require("electron");

contextBridge.exposeInMainWorld("cypherAPI", {

    runCommand: () =>
        ipcRenderer.invoke("run-command"),

    minimizeWindow: () =>
        ipcRenderer.send("minimize-window"),

    closeWindow: () =>
        ipcRenderer.send("close-window"),

    onBackendEvent: (callback) =>
        ipcRenderer.on(
            "backend-event",
            (event, data) => callback(data)
        )
});