import webbrowser
import threading
import time

# Function to open a URL in a browser
def open_url(url):
    webbrowser.open(url)
    time.sleep(5)  # Keep the browser alive for 60 seconds (adjust as needed)

def main():
    # File containing the list
    file_name = r"C:\Project\openDouyinId\cosplay.txt"  # Raw string for Windows paths

    try:
        # Read the file
        with open(file_name, "r", encoding="utf-8") as file:
            lines = file.readlines()
        
        # Select the lines for the specified element
        element = 16  # Adjust the element index here
        chunk_size = 25  # Number of lines per chunk
        result = element * chunk_size
        print("result: ", result)
        if result> len(lines):
            print("final")
        start_index = (element - 1) * chunk_size
        end_index = min(start_index + chunk_size, len(lines))
        
        # Ensure the slice does not go out of bounds
        if start_index >= len(lines):
            print(f"Start index {start_index} is out of bounds. No more lines to process.")
            return
        
        selected_lines = lines[start_index:end_index]
        if not selected_lines:
            print("No lines available in the selected range.")
            return
        
        # Process each line: extract the first part and generate the URL
        base_url = "https://www.douyin.com/root/search/{id}?aid=cff74468-be3b-45e0-8ab4-5df9f47a2951&type=general"
        urls = []
        for line in selected_lines:
            line = line.strip()  # Remove extra spaces or newline characters
            if not line:  # Skip empty lines
                print("Skipping empty line.")
                continue
            
            try:
                first_part = line.split()[0]  # Extract the first part of the line
                url = base_url.format(id=first_part)  # Replace {id} with the first part
                urls.append(url)
            except IndexError:
                print(f"Skipping malformed line: {line}")
                continue
        
        # Open each URL using threads for simultaneous opening
        threads = []
        for url in urls:
            thread = threading.Thread(target=open_url, args=(url,))
            threads.append(thread)
            thread.start()
        
        # Wait for all threads to finish
        for thread in threads:
            thread.join()

        print("All URLs have been opened.")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
