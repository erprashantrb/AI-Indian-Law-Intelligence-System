const chatWindow = document.getElementById("chatWindow");

function addMessage(text, type) {
    let div = document.createElement("div");
    div.classList.add("message");
    div.classList.add(type === "user" ? "user-msg" : "ai-msg");
    div.innerText = text;
    chatWindow.appendChild(div);
    chatWindow.scrollTop = chatWindow.scrollHeight;
}

function addTyping() {
    let div = document.createElement("div");
    div.id = "typing";
    div.className = "message ai-msg typing";
    div.innerText = "AI is typing...";
    chatWindow.appendChild(div);
}

function removeTyping() {
    let t = document.getElementById("typing");
    if (t) t.remove();
}

async function sendMessage() {
    const clause = document.getElementById("clauseInput").value;
    const userText = document.getElementById("userInput").value;

    if (!userText.trim()) return;

    addMessage(userText, "user");
    document.getElementById("userInput").value = "";

    addTyping();

    let res = await fetch("/api/chat", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({
            clause: clause,
            question: userText
        })
    });

    removeTyping();

    let data = await res.json();
    addMessage(data.reply, "ai");
}
