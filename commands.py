def message(c, arg):
    user = get_key(c)
    for client in users.values():
        if client != c: 
            client.send(bytes(user+" :"+arg, 'utf-8'))


commands = {
        "msg": message
        }


users = dict()


def com_split(statement):
    words = statement.split(':')
    return words[0], words[1]


def join(c):
    name = c.recv(1024).decode()
    if name in users:
        c.send(bytes("error", 'utf-8'))
        return False
    else:
        users[name] = c
        print("User"+name+" has been added")
        print(users.keys())
        c.send(bytes("Welcome " + name, 'utf-8'))
        return True 


def get_key(val):
    for key, value in users.items():
        if val == value:
            return key


def client_commands(c):
    exist = join(c)
    if exist:
        while True:
            usr_input = c.recv(1024).decode()
            if usr_input.startswith("quit"):
                c.send(bytes("exit", 'utf-8'))
                break
            command, argument = com_split(usr_input)
            execute = commands[command](c, argument)
        key = get_key(c)
        users.pop(key)
        print(users)
    c.close()
