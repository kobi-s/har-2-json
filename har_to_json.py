import json
import argparse
import os

def get_default_output_filename(har_file_path, num_entries):
    filename = os.path.basename(har_file_path)
    domain_name = filename.rsplit('.', 1)[0]
    return f"{domain_name}_{num_entries}.json"

def convert_har_to_json(har_file_path, output_json_path=None):
    with open(har_file_path, 'r') as f:
        har_data = json.load(f)

    json_output = []

    for entry in har_data['log']['entries']:
        method = entry['request']['method']
        url = entry['request']['url']

        headersObject = {}
        for h in entry['request']['headers']:
            headersObject[h['name']] = h['value']

        # Check if postData exists, if not, assign an empty string
        data = entry['request'].get('postData', {}).get('text', "")

        json_output.append({
            "method": method,
            "url": url,
            "headers": headersObject,
            "data": data
        })

    num_entries = len(json_output)
    
    if output_json_path is None:
        output_json_path = get_default_output_filename(har_file_path, num_entries)

    with open(output_json_path, 'w') as f:
        json.dump(json_output, f, indent=4)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Convert HAR file to a JSON file with specific structure.")
    parser.add_argument("har_file_path", help="Path to the HAR file you want to convert.")
    parser.add_argument("-o", "--output", default=None, help="Path to the output JSON file.")

    args = parser.parse_args()

    if not args.har_file_path:
        print("Error: No HAR file path supplied.")
    else:
        convert_har_to_json(args.har_file_path, args.output)