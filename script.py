import os
import re
import socket
import contractions
from collections import Counter

# File paths
file1_path = "/home/data/IF-1.txt"
file2_path = "/home/data/AlwaysRememberUsThisWay-1.txt"
output_path = "/home/data/output/result.txt"

# Function to count words
def count_words(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read().lower()
        text = contractions.fix(text)  # Expand contractions like "don't" -> "do not"
        words = re.findall(r"\b[a-zA-Z]+\b", text)  # Extract only words, removing punctuation
    return words

# Read and count words from both files
words_file1 = count_words(file1_path)
words_file2 = count_words(file2_path)


count_file1 = len(words_file1)
count_file2 = len(words_file2)
total_count = count_file1 + count_file2

# Get top 3 frequent words in IF-1.txt
top_3_file1 = Counter(words_file1).most_common(3)

# Get top 3 frequent words in AlwaysRememberUsThisWay-1.txt
top_3_file2 = Counter(words_file2).most_common(3)

# Get container's IP address
ip_address = socket.gethostbyname(socket.gethostname())

# Write results to file
with open(output_path, "w") as f:
    f.write(f"Word count in IF-1.txt: {count_file1}\n")
    f.write(f"Word count in AlwaysRememberUsThisWay-1.txt: {count_file2}\n")
    f.write(f"Total word count: {total_count}\n")
    f.write(f"Top 3 words in IF-1.txt: {top_3_file1}\n")
    f.write(f"Top 3 words in AlwaysRememberUsThisWay-1.txt: {top_3_file2}\n")
    f.write(f"Container IP address: {ip_address}\n")

# Print results to console
with open(output_path, "r") as f:
    print(f.read())




