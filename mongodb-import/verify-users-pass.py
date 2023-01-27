import bcrypt
import json

passwd = 'pass1234'
bytes = passwd.encode('utf-8')

myusers_data = json.load(open('mongodb-import/users.json'))

for myuser in myusers_data:
    if bcrypt.checkpw(bytes, myuser['password'].encode('utf-8')):
        print("match")
    else:
        print("does not match")