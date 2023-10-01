import os 

db_user = os.environ.get('db_user')
db_password = os.environ.get('db_pass')

new_pass='DJANGO123'

print(db_user)
print(db_password)