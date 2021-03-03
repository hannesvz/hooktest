import json
import urllib


from bottle import route, get, post, request, response, template, run

from platformshconfig import Config
config = Config()


@get('<path:path>')
def index(path):
    print(f'GET request received for {path}')
    return('<h1>Excelsior!</h1>')


print(' --- server starting ---')
run(port=int(config.port))
