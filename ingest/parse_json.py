import json

def load_json_data(filepath):
    with open(filepath, 'r') as f:
        data = json.load(f)
    return data

if __name__ == "__main__":
    data = load_json_data('../data/sample_data.json')
    for item in data:
        print(item)
