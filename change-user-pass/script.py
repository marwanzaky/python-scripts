import bcrypt
import json

password = 'pass1234'
bytes = password.encode('utf-8')

myusers_data = json.load(open('change-user-pass/users.json'))

for myuser in myusers_data:
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(bytes, salt)

    i = myusers_data.index(myuser)
    myusers_data[i]['password'] = hashed.decode('utf-8')

with open('change-user-pass/new_users.json', 'w') as outfile:
    json.dump(myusers_data, outfile)