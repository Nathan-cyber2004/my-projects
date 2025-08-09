# This code logic allows for the AI Agent to read and summarize various files

import os
import json
import csv
from langchain.tools import tool

def summarize_text(text, max_lines=5):
    lines = text.strip().splitlines()
    return "\n".join(lines[:max_lines]) + ("\n..." if len(lines) > max_lines else "")

def read_txt(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    return summarize_text(content)

def read_csv(file_path, max_rows=5):
    summary = []
    with open(file_path, 'r', encoding='utf-8') as csv_file:
        reader = csv.reader(csv_file)
        headers = next(reader)
        summary.append("Headers: " + ", ".join(headers))
        for index, row in enumerate(reader):
            if index >= max_rows:
                break
            summary.append("Row {}: {}".format(index + 1, ", ".join(row)))
    return "\n".join(summary)

def read_json(file_path, max_items=5):
    with open(file_path, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)

    if isinstance(data, list):
        summary = data[:max_items]
    elif isinstance(data, dict):
        summary = dict(list(data.items())[:max_items])
    else:
        return str(data)
    return json.dumps(summary, indent=2)

@tool
def summarize_file(file_path):
    """
       This function can summarize any text as long as it is either .txt, .csv. or .json. 
       This function also requires that the correct file path is given
    """
    if not os.path.exists(file_path):
        return "File does not exist."

    extension = os.path.splitext(file_path)[1].lower() # This allows us to grab the file extension
    
    try:
        if extension == ".txt":
            return read_txt(file_path)
        elif extension == ".csv":
            return read_csv(file_path)
        elif extension == ".json":
            return read_json(file_path)
        else:
            return f"Unsupported file format: {extension}"
    except Exception as E:
        return f"Error reading file: {E}"