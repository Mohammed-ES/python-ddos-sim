from flask import Flask, jsonify, request
from flask_cors import CORS
import threading
import time



app = Flask(__name__)
CORS(app)

stats = {
    'requests': 0,
    'last_request': None,
    'down': False,
}

# Threshold after which the site is considered 'down'
THRESHOLD = 2000

@app.route('/')
def index():
    if stats['down']:
        return '<title>CyberAtlas - Attacked</title><div style="font-size:2em;">Site unavailable!<br>Service interrupted due to simulated DDoS.</div>', 503
    stats['requests'] += 1
    stats['last_request'] = time.time()
    if stats['requests'] > THRESHOLD:
        stats['down'] = True
        return '<div style="font-size:2em;">Site unavailable!<br>Service interrupted due to simulated DDoS.</div>', 503
    return '<title>CyberAtlas - Secure</title><div style="font-size:2em;">Welcome! Test server is online.</div>', 200

@app.route('/stats')
def get_stats():
    return jsonify({
        'requests': stats['requests'],
        'last_request': stats['last_request'],
        'down': stats['down']
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
