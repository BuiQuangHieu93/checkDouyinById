import threading
import time
import os
import sys

# Function to open a URL in Chrome incognito mode
def open_url_incognito(url):
    try:
        if sys.platform.startswith("win"):  # Windows
            os.system(f'start chrome --incognito "{url}"')
        elif sys.platform.startswith("darwin"):  # macOS
            os.system(f'open -a "Google Chrome" --args --incognito "{url}"')
        elif sys.platform.startswith("linux"):  # Linux
            os.system(f'google-chrome --incognito "{url}"')
        else:
            print("Unsupported OS for Chrome incognito mode.")

        time.sleep(1)  # Delay before opening the next URL
    except Exception as e:
        print(f"Error opening {url} in incognito mode: {e}")

def main():
    # File containing the list
    file_name = r"C:\Project\openDouyinId\cosplay.txt"

    try:
        with open(file_name, "r", encoding="utf-8") as file:
            lines = file.readlines()

        element = 27  # Adjust the element index here
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

        base_url = "https://www.douyin.com/root/search/{id}?aid=234db4a8-97aa-404b-a3e6-679166a903be&type=general"
        urls = []

        for line in selected_lines:
            line = line.strip()
            if not line:
                print("Skipping empty line.")
                continue

            try:
                first_part = line.split()[0]
                url = base_url.format(id=first_part)
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

        for thread in threads:
            thread.join()

        print("All URLs have been opened in Chrome incognito mode.")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
