#!/usr/bin/python3
from models.user import User

print(type(User.first_name) is str)
print(User.first_name == "")
