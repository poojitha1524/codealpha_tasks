import os
import shutil

source_folder = "path/to/source"
destination_folder = "path/to/destination"

# Create destination folder if it doesn't exist
os.makedirs(destination_folder, exist_ok=True)

for file in os.listdir(source_folder):
    if file.lower().endswith(".jpg"):
        src_path = os.path.join(source_folder, file)
        dest_path = os.path.join(destination_folder, file)
        shutil.move(src_path, dest_path)
        print(f"Moved: {file}")

print("✔ All .jpg files moved successfully!")
import re

input_file = "input.txt"
output_file = "emails.txt"

# Regex pattern for email
pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

with open(input_file, "r") as f:
    content = f.read()

emails = re.findall(pattern, content)

with open(output_file, "w") as f:
    for email in emails:
        f.write(email + "\n")

print(f"✔ Extracted {len(emails)} email(s) to {output_file}")
import requests
import re

url = "https://example.com"     # Replace with the fixed page
output_file = "page_title.txt"

response = requests.get(url)
html = response.text

# Regex to extract <title>...</title>
match = re.search(r"<title>(.*?)</title>", html, re.IGNORECASE | re.DOTALL)

title = match.group(1).strip() if match else "No title found"

with open(output_file, "w") as f:
    f.write(title)

print(f"✔ Page title saved to {output_file}")
