import os 

EMAIL_USER = os.environ.get('EMAIL_USER')
EMAIL_PASS = os.environ.get('EMAIL_PASS')
SECRET_KEY = os.environ.get('SECRET_KEY')

new_pass='DJANGO123'

print(EMAIL_USER)
print(EMAIL_PASS)
print(SECRET_KEY)