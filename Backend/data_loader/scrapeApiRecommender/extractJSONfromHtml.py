import json
import re
import os

def extract_json_from_html(html_content):
    try:
        # Regular expression to find the JSON content
        json_pattern = re.compile(r'<pre>({.*?})<\/pre>', re.DOTALL)
        match = json_pattern.search(html_content)
        if match:
            json_data = match.group(1)
            return json.loads(json_data)
        else:
            print("JSON data not found in HTML content.")
            return None
    except Exception as e:
        print(f"Error extracting JSON data: {e}")
        return None

def save_json_to_file(json_data, output_file):
    try:
        with open(output_file, 'w', encoding='utf-8') as json_file:
            json.dump(json_data, json_file, indent=4)
        print(f"JSON data saved to {output_file}")
    except Exception as e:
        print(f"Error saving JSON data to file: {e}")

def main():
    # Get the directory of the current script
    script_dir = os.path.dirname(os.path.realpath(__file__))
    
    # Path to the HTML file
    html_file_path = os.path.join(script_dir, 'redoc_page_source2.txt')
    # Path to the output JSON file
    output_json_file = os.path.join(script_dir, 'redoc_data.json')

    # Read the HTML content from the file
    try:
        with open(html_file_path, 'r', encoding='utf-8') as html_file:
            html_content = html_file.read()
    except Exception as e:
        print(f"Error reading HTML file: {e}")
        return

    # Extract JSON data from the HTML content
    json_data = extract_json_from_html(html_content)
    if json_data:
        # Save the extracted JSON data to a file
        save_json_to_file(json_data, output_json_file)

if __name__ == "__main__":
    main()
