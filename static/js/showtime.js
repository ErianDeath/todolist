const showTime = document.getElementById('time');

function updateTime() {
    const date = new Date().toLocaleString();
    showTime.innerHTML = date;
}

setInterval(updateTime, 1000);