
<div align="center">
  <img src="https://img.shields.io/badge/Python-3.13-blue?logo=python&style=for-the-badge" alt="Python">
  <img src="https://img.shields.io/badge/Flask-2.x-black?logo=flask&style=for-the-badge" alt="Flask">
  <img src="https://img.shields.io/badge/requests-2.x-green?logo=python&style=for-the-badge" alt="requests">
  <img src="https://img.shields.io/badge/Chart.js-4.x-purple?logo=chartdotjs&style=for-the-badge" alt="Chart.js">
</div>

<h1 align="center">python-ddos-sim</h1>
<p align="center"><b>Educational DDoS Simulation Tool</b></p>

<div align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=22&pause=1000&color=36BCF7&center=true&vCenter=true&width=500&lines=Simulate+DDoS+attacks+for+learning!;Modern+dashboard+with+live+stats;Ethical+and+educational+use+only!" alt="Typing SVG">
</div>

---

<details open>
<summary><h2>🚨 IMPORTANT LEGAL DISCLAIMER</h2></summary>

> <b>This tool is for <u>educational purposes only</u>. <br>Do <u>NOT</u> use it against any server without explicit authorization. Unauthorized use is illegal and unethical. The authors are not responsible for misuse.</b>

</details>

---

## 📑 Table of Contents

- [Technologies Used](#technologies-used)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Examples](#examples)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)
- [Related Resources](#related-resources)

---

## 🚀 Technologies Used

<table>
  <tr>
    <th>Technology</th>
    <th>Version</th>
    <th>Purpose</th>
  </tr>
  <tr>
    <td><img src="https://img.shields.io/badge/Python-3.13-blue?logo=python" alt="Python" height="20"> Python</td>
    <td>3.13+</td>
    <td>Core language</td>
  </tr>
  <tr>
    <td><img src="https://img.shields.io/badge/Flask-black?logo=flask" alt="Flask" height="20"> Flask</td>
    <td>2.x</td>
    <td>Test server & API</td>
  </tr>
  <tr>
    <td><img src="https://img.shields.io/badge/requests-green?logo=python" alt="requests" height="20"> requests</td>
    <td>2.x</td>
    <td>HTTP requests</td>
  </tr>
  <tr>
    <td><img src="https://img.shields.io/badge/flask--cors-yellow?logo=python" alt="flask-cors" height="20"> flask-cors</td>
    <td>3.x</td>
    <td>CORS support</td>
  </tr>
  <tr>
    <td><img src="https://img.shields.io/badge/Chart.js-purple?logo=chartdotjs" alt="Chart.js" height="20"> Chart.js</td>
    <td>4.x</td>
    <td>Dashboard charts</td>
  </tr>
</table>

---

## 🛠 Prerequisites

- Python 3.13 or higher
- pip (Python package manager)
- Git (optional, for cloning)

---

## ⚡ Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Mohammed-ES/python-ddos-sim.git
   cd python-ddos-sim
   ```
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

---

## ▶️ Usage

1. **Start the test server:**
   ```bash
   python test_server.py
   ```
2. **Run the DDoS tool:**
   ```bash
   python ddos_tool.py --url http://127.0.0.1:5000 --threads 10 --duration 30
   ```
3. **View the dashboard:**
   - Open `dashboard.html` in your browser while the test server is running.

---

## ⚙️ Configuration

You can configure the DDoS tool with the following command-line arguments:

| Argument      | Description                        | Default                |
|-------------- |------------------------------------|------------------------|
| `--url`       | Target URL                         | `http://127.0.0.1:5000`|
| `--threads`   | Number of threads                  | `10`                   |
| `--duration`  | Duration of attack (seconds)       | `30`                   |

---

## 💡 Examples

Start a test server and run a 30-second DDoS simulation with 20 threads:

```bash
python test_server.py
python ddos_tool.py --url http://127.0.0.1:5000 --threads 20 --duration 30
```

---


## 🗂 Project Structure

```text
python-ddos-sim/
├── ddos_tool.py         # Main DDoS simulation script
├── test_server.py       # Flask test server
├── requirements.txt     # Python dependencies
├── README.md            # Project documentation
├── static/
│   ├── dashboard.html   # Modern dashboard UI
│   ├── style.css        # Dashboard styles
│   └── script.js        # Dashboard logic
└── ...
```

---


## 📂 File Explanations


### `ddos_tool.py`

- **Role:** Main script that simulates a DDoS (Distributed Denial of Service) attack for educational purposes.
- **Detailed operation:**
  - Uses the `threading` module (for multithreading) and `requests` (to send HTTP GET requests).
  - Command-line arguments allow you to set:
    - the target URL (`--url`)
    - the number of threads (`--threads`)
    - the attack duration in seconds (`--duration`)
  - Each thread runs a loop that continuously sends HTTP GET requests for the specified duration.
  - Responses are counted (success, errors, HTTP codes).
  - At the end, the script prints a statistical summary (total requests, success/failure rate).
- **Typical structure:**
  - `main()`: Parses arguments, starts threads, manages the global timer.
  - `attack_thread()`: Function run by each thread, sends requests and updates counters.
  - Real-time or end-of-execution statistics display.
- **Example usage:**

  ```bash
  python ddos_tool.py --url http://127.0.0.1:5000 --threads 10 --duration 30
  ```
  (Replace the URL, thread count, and duration as needed)


### `test_server.py`

- **Role:** Flask web server that simulates a DDoS target and provides real-time statistics.
- **Detailed operation:**
  - Runs a Flask server on `http://127.0.0.1:5000`.
  - Counts every request received and keeps statistics (total, per second, etc.).
  - Exposes a `/stats` endpoint that returns statistics as JSON (for the dashboard).
  - Can simulate a "down" (offline) state after a certain number of requests to illustrate the impact of an attack.
  - Serves the dashboard interface (`dashboard.html`) for real-time visualization.
- **Typical structure:**
  - `@app.route('/')`: Home page, displays a message or server status.
  - `@app.route('/stats')`: Returns statistics as JSON for the dashboard.
  - Global variables to count requests and manage server state.
  - Uses `flask_cors` to allow AJAX requests from the dashboard.
- **Example usage:**

  ```bash
  python test_server.py
  ```
  (The server starts. You can then launch the DDoS tool and open the dashboard)

### `dashboard.html`

- **Role:** This is the main file for the modern, animated web dashboard.
- **Purpose:**
  - Provides a real-time, interactive visualization of the DDoS simulation statistics (requests per second, server status, etc.).
  - Uses Chart.js for live-updating charts and a professional, responsive UI.
  - Connects to the Flask server's `/stats` endpoint to fetch and display live data.
- **How to use:**
  - Open `dashboard.html` in your browser while the Flask test server is running.
  - The dashboard will automatically update with real-time stats from the backend.
  - Useful for monitoring and understanding the impact of simulated DDoS attacks in a safe, educational environment.

---

---

## 🤝 Contributing

Contributions are welcome! Please open issues or submit pull requests for improvements, bug fixes, or new features.

---

## 📄 License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

---


## 🔗 Related Resources

- [OWASP: Denial of Service Attacks](https://owasp.org/www-community/attacks/Denial_of_Service)
- [Python Official Documentation](https://docs.python.org/3/)
- [Flask Official Documentation](https://flask.palletsprojects.com/en/2.3.x/)
- [requests Official Documentation](https://requests.readthedocs.io/en/latest/)
- [flask-cors Documentation](https://flask-cors.readthedocs.io/en/latest/)
- [Chart.js Official Documentation](https://www.chartjs.org/docs/latest/)
- [Threading in Python](https://docs.python.org/3/library/threading.html)

