# log_parser.py

keywords = ["unauthorized", "failed", "error"]  # Alert keywords

with open("logs/example.log", "r") as file:  # Open test log
    for line_number, line in enumerate(file, start=1):  # Read each line with its number
        for word in keywords:  # Loop through each alert word
            if word in line.lower():  # Case-insensitive check
                print(f"[ALERT] Line {line_number}: {line.strip()}")  # Print flagged line
