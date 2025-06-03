import os
import requests
from flask import Flask

server = Flask('authorization_server')

# definition of the API address
api_address = 'fastapi'
# API port
api_port = 8000
version = 'v1'
username='bob'
password='builder'
sentence='that sucks'

# The 4 requests
r = requests.get(
    url='http://{address}:{port}/{v}/sentiment'.format(address=api_address, port=api_port,v=version),
    params= {
        'username': '{uname}'.format(uname=username),
        'password': '{pw}'.format(pw=password),
        'sentence': '{s}'.format(s=sentence)
    }
)

software_version = r.json()['version']
score = r.json()['score']
# if auth:
output = '''
============================
    Authorization test
============================
request done at "/{software_version}/sentiment"
| username={username}
| password={password}
Software version: {software_version}
User is permitted to use this software version
| sentence={sentence}
| score={score}
SUCCES >>>

'''

status_code = r.status_code

# display the results
if status_code == 200:
    test_status = 'SUCCESS'
else:
    test_status = 'FAILURE'

# printing in a file
if os.environ.get('LOG') == 1:
    with open('api_test.log', 'a') as file:
        file.write(output)
        
@server.route('/')
def index():
    return output.format(status_code=status_code, test_status=test_status,software_version=software_version,score=score,username=username,password=password,sentence=sentence)

if __name__ == '__main__':
    server.run(host='0.0.0.0', port=6000)
