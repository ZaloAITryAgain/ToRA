import json

def convert_json_to_jsonl(json_file, jsonl_file):
    with open(json_file, 'r') as f:
        data = json.load(f)

    with open(jsonl_file, 'w') as f:
        for obj in data:
            json_line = json.dumps(obj, ensure_ascii=False)
            f.write(json_line + '\n')

def add_idx(jsonl_file):
    with open(jsonl_file, 'r') as f:
        data = f.readlines()

    with open(jsonl_file, 'w') as f:
        for line in data:
            obj = json.loads(line)
            obj['idx'] = obj['id']
            json_line = json.dumps(obj, ensure_ascii=False)
            f.write(json_line + '\n')


if __name__ == '__main__':
    src = "test.json"
    dst = "test.jsonl"
    # convert_json_to_jsonl(src, dst)
    add_idx(src)