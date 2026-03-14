async function getStock(){

    const tickers = document.getElementById("tickers").value.split(",");
    const start = document.getElementById("start").value;
    const end = document.getElementById("end").value;

    if(!tickers[0] || !start || !end){
        alert("Please fill all fields");
        return;
    }

    document.getElementById("loading").style.display = "flex";

    const res = await fetch("/get_stock",{
        method:"POST",
        headers:{
            "Content-Type":"application/json"
        },
        body:JSON.stringify({
            tickers:tickers,
            start_date:start,
            end_date:end
        })
    });

    const data = await res.json();

    document.getElementById("loading").style.display = "none";

    const tbody = document.querySelector("#stockTable tbody");

    tbody.innerHTML = "";

    let count = 0;

    data.forEach(row => {

        const tr = document.createElement("tr");

        tr.innerHTML = `
        <td>${row.Date}</td>
        <td>${row.Open}</td>
        <td>${row.High}</td>
        <td>${row.Low}</td>
        <td>${row.Close}</td>
        <td>${row.Volume}</td>
        `;

        tbody.appendChild(tr);

        count++;

    });

    document.getElementById("stocksCount").innerText = tickers.length;

    document.getElementById("dataCount").innerText = count;

}