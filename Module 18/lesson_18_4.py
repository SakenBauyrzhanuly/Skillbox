import  requests
import json
#
# my_req = requests.get('https://swapi.dev/api/planets/8/')
# # print(my_req.text)
#
# data = json.loads(my_req.text)
# data['rotation_period'] = 100
# print(data['name'])
#
# with open('my_test.json', 'w') as file:
#     json.dump(data, file, indent=4)
#
#
# with open('my_test.json', 'r') as file:
#     data = json.load(file)
#
# print(data)
import requests
import json

response = requests.get("https://swapi.dev/api/people/3/")
if response.status_code == 200:
    json_dict = json.loads(response.text)
    json_dict['name'] = input("Введите имя: ")
    with open("swap.json", "w") as file:
        json_text = json.dump(json_dict, file, indent=4)

    # Доп:
    result_homeworld = requests.get(json_dict['homeworld'])
    print(result_homeworld.text)