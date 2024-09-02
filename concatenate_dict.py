#Concatenate two dictionaries and return the sum of each key value of the new dictionary

def merge(dict1, dict2):
    merged_dict = {}
    for key in dict1:
        merged_dict[key] = dict1[key]
    for key in dict2:
        merged_dict[key] = dict2[key]
    return merged_dict


def total_score(score_dict):
    sum = 0
    for key in score_dict:
        sum += score_dict[key]
    return sum



dictionary1 = {
    "Raul": 2,
    "Ana": 5,
    "Cristi": 1
}
dictionary2 = {
    "Dan": 0,
    "Olga": 9,
    "Ana": 10,
}

print(merge(dictionary1, dictionary2))
print(total_score(merge(dictionary1, dictionary2)))