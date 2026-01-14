async function uploadDocument() {
    let file = document.getElementById("fileUpload").files[0];
    if (!file) {
        alert("Please select a file.");
        return;
    }

    let form = new FormData();
    form.append("file", file);

    document.getElementById("uploadResult").innerText = "Uploading…";

    let res = await fetch("/api/upload", {
        method: "POST",
        body: form
    });

    let data = await res.json();
    document.getElementById("uploadResult").innerText = JSON.stringify(data, null, 2);
}
