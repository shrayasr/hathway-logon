import requests

import conf

url_params = {
        "action":"doLoginSubmit",
        "flowId":"UserLogin"
        }
payload = {
        "username":conf.username,
        "password":conf.password,
        "Submit":"Login"
        }

url=conf.url

r = requests.post(url, data=payload, params=url_params)
