import json

INPUT_FILE = "input.csv"

def csv_to_list_dict(INPUT_FILE, delimiter=",", new_line="\n") -> list[dict]:
    list_dict = []
    with open(INPUT_FILE,'r') as f:
        data = f.readlines()
        headers = [line.rstrip(new_line) for line in data[0].split(delimiter)]
        for row in data[1:]:
            dictionary = {}
            row = [line.rstrip(new_line) for line in row.split(delimiter)]
            for i in range(len(row)):
                dictionary[headers[i]] = row[i]
            list_dict.append(dictionary)

    return list_dict

print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
