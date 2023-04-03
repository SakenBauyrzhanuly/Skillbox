server_data = {
    "server": {
        "host": "127.0.0.1",
        "port": "10"
    },

    "configuration": {
        "access": "true",
        "login": "Ivan",
        "password": "qwerty"
    }
}
for i_serv, i_n in server_data.items():
    print(i_serv)
    for i_key, i_value in i_n.items():
        print(' ', i_key, ': ', i_value)


