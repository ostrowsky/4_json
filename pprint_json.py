import json


def load_data(filepath):
    with open(filepath, encoding='UTF-8') as f:
        lines = f.read()
        return json.loads(lines)


def pretty_print_json(data):
    return json.dumps(data, ensure_ascii = False, sort_keys=True, indent=4)


if __name__ == '__main__':
    filepath = input("Введите путь к файлу\n")
    data = load_data(filepath)
    print(pretty_print_json(data))