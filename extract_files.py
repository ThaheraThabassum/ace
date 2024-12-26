import pandas as pd
import json

# Path to the Excel file
excel_file_path = './app_template.xlsx'

# Read the Excel file
df = pd.read_excel(excel_file_path)

# Extract file names and paths
files = df['file'].tolist()
file_paths = df['file_path'].tolist()

# Create a JSON output
output = {
    'files': files,
    'file_paths': file_paths
}

# Write the output to a file
with open('changes.json', 'w') as f:
    json.dump(output, f)
