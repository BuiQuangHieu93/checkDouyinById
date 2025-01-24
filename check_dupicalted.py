from collections import Counter

def check_duplicates(file_path):
    # Open the file and read the lines into a list with the specified encoding
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # Strip newline characters from each line
    lines = [line.strip() for line in lines]

    # Use Counter to count occurrences of each line
    line_counts = Counter(lines)

    # Find lines that appear more than once (duplicates)
    duplicates = {line: count for line, count in line_counts.items() if count > 1}

    return duplicates

# Example usage
file_path = r'C:\Project\openDouyinId\cosplay.txt'  # Replace with your file path
duplicates = check_duplicates(file_path)

if duplicates:
    print("Duplicated lines found:")
    for line, count in duplicates.items():
        print(f"Line: '{line}', Occurrences: {count}")
else:
    print("No duplicates found.")
