# {
#     "server": {
#         "host": "127.0.0.1",
#         "port": "10"
#     },
#     "configuration": {
#         "ssh": {
#             "access": "true",
#             "login": "Ivan",
#             "password": "qwerty"
#         }
#     }
# }



data = dict()
# до этого что то происходит
print(data.get('server'))
data['server'] = {
        "host": "127.0.0.1",
        "port": "10"
}

# до этого что то происходит
if data.get('configuration',{}).get('ssh',{}).get('login',{}):
    print('В структуре уже есть логин')
print(data.get('configuration',{}).get('ssh',{}).get('login',{}))
data['configuration'] = {
    'ssh': {
        'access': 'true',
        'login': 'Ivan',
        'password': 'qwerty'
    }
}

print(data)
# print(data['server']['port'])
# data['configuration']['ssh']['login'] = 'Vova'
# print(data['configuration']['ssh']['login'])
# print()
#
# for i_value in data.values():
#     for j_key in i_value:
#         print(j_key, i_value[j_key])


