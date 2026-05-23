const body = document.body;

const stateText = document.getElementById("state");

const minimizeBtn = document.getElementById("min-btn");

const closeBtn = document.getElementById("close-btn");

const talkBtn = document.getElementById("talk-btn");


function setVisualState(state) {

    body.classList.remove(
        "idle",
        "listening",
        "processing",
        "executing",
        "error"
    );

    switch(state) {

        case "LISTENING":
            body.classList.add("listening");
            break;

        case "PROCESSING":
            body.classList.add("processing");
            break;

        case "EXECUTING":
            body.classList.add("executing");
            break;

        case "ERROR":
            body.classList.add("error");
            break;

        default:
            body.classList.add("idle");
    }

    stateText.innerText = state;
}


minimizeBtn.addEventListener("click", (event) => {

    event.stopPropagation();

    window.cypherAPI.minimizeWindow();
});


closeBtn.addEventListener("click", (event) => {

    event.stopPropagation();

    window.cypherAPI.closeWindow();
});


window.cypherAPI.onBackendEvent((event) => {

    console.log("BACKEND EVENT:", event);

    if (event.type === "state") {

        setVisualState(event.data);
    }

    else if (event.type === "error") {

        console.error(event.data);

        setVisualState("ERROR");
    }
});


talkBtn.addEventListener("click", async (event) => {

    event.stopPropagation();

    try {

        await window.cypherAPI.runCommand();

    } catch (err) {

        console.error(err);

        setVisualState("ERROR");
    }
});