from gettext import install
from urllib import request
import pip
response = request.get("https://api.open-notify.org/astros.json")
print(response)
