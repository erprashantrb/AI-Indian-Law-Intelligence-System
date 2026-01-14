async function compareClauses() {
    let a = document.getElementById("clauseA").value;
    let b = document.getElementById("clauseB").value;

    if (!a || !b) {
        alert("Enter both clauses.");
        return;
    }

    document.getElementById("compareResult").innerText = "Comparing…";

    let res = await fetch("/api/compare", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({
            clauseA: a,
            clauseB: b
        })
    });

    let data = await res.json();

    document.getElementById("compareResult").innerText = data.result;
}
