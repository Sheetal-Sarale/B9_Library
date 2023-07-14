# exec(open(r"D:\python\djangoprojects\B9_Library\user_app\db_shell.py").read())

from django.contrib.auth.models import User

user = User.objects.get(id=1).profile.location

print(user)

# print(User.objects.all())
# User.objects.create_user(username="Anay", password="Python", email="Anay@gmail.com")                           # password is encrypted using create_user Query
# from django.utils.crypto import get_random_string
# print(get_random_string(5))