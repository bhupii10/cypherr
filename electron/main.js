const { app, BrowserWindow, ipcMain } = require("electron");

const path = require("path");

const { spawn } = require("child_process");

let mainWindow;

function createWindow() {

    mainWindow = new BrowserWindow({

        width: 500,
        height: 700,

        frame: false,
        transparent: true,
        resizable: false,

        webPreferences: {
            preload: path.join(__dirname, "preload.js"),
            contextIsolation: true,
            nodeIntegration: false
        }
    });

    mainWindow.loadFile(
        path.join(__dirname, "../frontend/index.html")
    );
}

app.whenReady().then(() => {
    createWindow();
});

ipcMain.on("minimize-window", () => {
    mainWindow.minimize();
});

ipcMain.on("close-window", () => {
    mainWindow.close();
});

ipcMain.handle("run-command", async () => {

    return new Promise((resolve) => {

        const pythonPath = path.resolve(
            __dirname,
            "../backend/venv/Scripts/python.exe"
        );

        const scriptPath = path.resolve(
            __dirname,
            "../backend/main.py"
        );

        const pythonProcess = spawn(
            pythonPath,
            [scriptPath],
            {
                cwd: path.resolve(__dirname, "../backend")
            }
        );

        let finalResult = null;

        pythonProcess.stdout.on("data", (data) => {

            const lines = data
                .toString()
                .trim()
                .split("\n");

            for (const line of lines) {

                try {

                    const event = JSON.parse(line);

                    mainWindow.webContents.send(
                        "backend-event",
                        event
                    );

                    finalResult = event;

                } catch (err) {

                    console.log(
                        "Invalid JSON:",
                        line
                    );
                }
            }
        });

        pythonProcess.stderr.on("data", (data) => {

            console.error(
                "PYTHON ERROR:",
                data.toString()
            );
        });

        pythonProcess.on("close", () => {

            resolve(finalResult);
        });
    });
});