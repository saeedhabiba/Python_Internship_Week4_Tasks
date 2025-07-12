import os
import re

#correctly formatted folder path (raw string used)
folder_path = r"C:\Users\f1116cs027.pafiast\Desktop\GITHUB\Technik Nest Pvt Ltd Internship\Repositries"

#regex pattern: starts with "report" and ends with ".txt"
pattern = re.compile(r'^report.*\.txt$', re.IGNORECASE)

#list all files in that folder
all_files = os.listdir(folder_path)

#filter only matching .txt files
matching_files = [f for f in all_files if pattern.match(f)]

#print results
print("Matching .txt files:")
for file in matching_files:
    print(f"{file}")
