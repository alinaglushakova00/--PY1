import json
INPUT_FILE = "input.csv"

def csv_to_list_dict(filename,delimiter = ",",new_line = "\n") -> list[dict]:
    with open(filename) as f:
        dict1 = {}
        dict2 = {}
        dict3 = {}
        dict4 = {}
        heads = []
        res = [dict1,dict2,dict3,dict4]
        for index, line in enumerate(f):
            if index == 0:
                list_str = line.strip(new_line)
                list_spl = list_str.split(delimiter)
                for word in list_spl:
                    heads.append(word)
            else:
                list_str = line.strip(new_line)
                list_spl - list_str.split(delimiter)
                for i,j in enumerate(heads):
                    if index == 1:
                        dict1[heads[i]] = list_spl[i]
                    elif index == 2:
                        dict2[heads[i]] = list_spl[i]
                    elif index == 3:
                        dict3[heads[i]] = list_spl[i]
                    elif index == 4:
                        dict4[heads[i]] = list_spl[i]
    return res

print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
