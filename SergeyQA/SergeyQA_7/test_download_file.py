import requests

url = 'https://www.selenium.dev/images/sponsors/browserstack.png'

response = requests.get(url, allow_redirects=True)

open('browserstack.png', 'wb').write(response.content)