import threading
import time
import os
import sys
import uuid
import subprocess
from fake_useragent import UserAgent
import random

# Function to open a URL in Chrome incognito mode with a custom User-Agent
def open_url_incognito(url):
    try:
        ua = UserAgent()
        user_agent = ua.random  # Generate a random User-Agent

        if sys.platform.startswith("win"):  # Windows
            cmd = f'start chrome --incognito --user-agent="{user_agent}" "{url}"'
            subprocess.run(cmd, shell=True)

        elif sys.platform.startswith("darwin"):  # macOS
            cmd = ['open', '-a', 'Google Chrome', '--args', '--incognito', f'--user-agent={user_agent}', url]
            subprocess.run(cmd)

        elif sys.platform.startswith("linux"):  # Linux
            cmd = ['google-chrome', '--incognito', f'--user-agent={user_agent}', url]
            subprocess.run(cmd)

        else:
            print("Unsupported OS for Chrome incognito mode.")
    
    except Exception as e:
        print(f"Error opening {url} in incognito mode: {e}")

def main():
    # File containing the list
    file_name = r"C:\Project\openDouyinId\cosplay.txt"

    if not os.path.exists(file_name):
        print(f"File not found: {file_name}")
        return

    try:
        with open(file_name, "r", encoding="utf-8") as file:
            lines = file.readlines()

        element = 29  # Adjust the element index here
        chunk_size = 20
        start_index = (element - 1) * chunk_size
        end_index = min(start_index + chunk_size, len(lines))

        print("From", start_index, "to", end_index)
        print("Element number:", element)

        if start_index >= len(lines):
            print(f"Start index {start_index} is out of bounds. No more lines to process.")
            return

        selected_lines = lines[start_index:end_index]
        if not selected_lines:
            print("No lines available in the selected range.")
            return

        base_url = "https://www.douyin.com/root/search/{id}?aid={code}&type=general"
        urls = []

        for line in selected_lines:
            line = line.strip()
            if not line:
                print("Skipping empty line.")
                continue

            try:
                first_part = line.split()[0]
                code = str(uuid.uuid4())
                url = base_url.format(id=first_part, code=code)
                urls.append(url)
            except IndexError:
                print(f"Skipping malformed line: {line}")
                continue

        # Open each URL using threads
        threads = []
        for url in urls:
            thread = threading.Thread(target=open_url_incognito, args=(url,))
            threads.append(thread)
            thread.start()
            time.sleep(random.randint(2, 4))

        for thread in threads:
            thread.join()

        print("All URLs have been opened in Chrome incognito mode with random User-Agents.")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
