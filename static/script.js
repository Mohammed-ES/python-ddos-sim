let elapsed = 0;
let interval = null;
let chart = null;
let chartData = {
    labels: [],
    data: []
};

function updateDashboard(stats) {
    document.getElementById('requests').textContent = stats.requests;
    document.getElementById('elapsed').textContent = elapsed + 's';
    const statusEl = document.getElementById('status');
    if (!stats.down) {
        statusEl.textContent = 'Active';
        statusEl.classList.add('active');
        statusEl.classList.remove('inactive');
    } else {
        statusEl.textContent = 'Inactive';
        statusEl.classList.add('inactive');
        statusEl.classList.remove('active');
    }
}

function updateChart(reqThisSec) {
    chartData.labels.push(elapsed + 's');
    chartData.data.push(reqThisSec);
    if (chartData.labels.length > 30) {
        chartData.labels.shift();
        chartData.data.shift();
    }
    if (chart) {
        chart.data.labels = chartData.labels;
        chart.data.datasets[0].data = chartData.data;
        chart.update();
    }
}

function fetchStatsAndUpdate() {
    fetch('http://127.0.0.1:5000/stats')
        .then(res => res.json())
        .then(stats => {
            let reqThisSec = elapsed === 0 ? stats.requests : stats.requests - (window.lastRequests || 0);
            window.lastRequests = stats.requests;
            updateDashboard(stats);
            updateChart(reqThisSec < 0 ? 0 : reqThisSec);
        })
        .catch(() => {
            document.getElementById('status').textContent = 'Inactive';
            document.getElementById('status').classList.add('inactive');
            document.getElementById('status').classList.remove('active');
        });
    elapsed++;
}

function startSimulation() {
    if (interval) return;
    document.getElementById('startBtn').disabled = true;
    document.getElementById('stopBtn').disabled = false;
    elapsed = 0;
    window.lastRequests = 0;
    chartData.labels = [];
    chartData.data = [];
    interval = setInterval(fetchStatsAndUpdate, 1000);
}

function stopSimulation() {
    document.getElementById('startBtn').disabled = false;
    document.getElementById('stopBtn').disabled = true;
    clearInterval(interval);
    interval = null;
}

window.onload = function() {
    // Chart.js setup
    const ctx = document.getElementById('requestsChart').getContext('2d');
    chart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: chartData.labels,
            datasets: [{
                label: 'Requests/sec',
                data: chartData.data,
                borderColor: '#3b82f6',
                backgroundColor: 'rgba(59,130,246,0.08)',
                borderWidth: 3,
                tension: 0.4,
                pointRadius: 0,
                fill: true,
            }]
        },
        options: {
            responsive: true,
            plugins: {
                legend: {
                    display: false
                }
            },
            scales: {
                x: {
                    grid: { color: '#334155' },
                    ticks: { color: '#f8fafc' }
                },
                y: {
                    grid: { color: '#334155' },
                    ticks: { color: '#f8fafc' }
                }
            },
            animation: {
                duration: 800,
                easing: 'easeOutQuart'
            }
        }
    });
    document.getElementById('startBtn').onclick = startSimulation;
    document.getElementById('stopBtn').onclick = stopSimulation;
    document.getElementById('stopBtn').disabled = true;
};
