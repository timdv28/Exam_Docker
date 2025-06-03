import os
import requests
from flask import Flask

server = Flask('content_server')

# definition of the API address
api_address = 'fastapi'
# API port
api_port = 8000
version = 'v1'
username='alice'
password='wonderland'


# 2 requests
r1 = requests.get(
    url='http://{address}:{port}/{v}/sentiment'.format(address=api_address, port=api_port,v=version),
    params= {
        'username': '{uname}'.format(uname=username),
        'password': '{pw}'.format(pw=password),
        'sentence': 'life is beautiful'
    }
)

r2 = requests.get(
    url='http://{address}:{port}/{v}/sentiment'.format(address=api_address, port=api_port,v=version),
    params= {
        'username': '{uname}'.format(uname=username),
        'password': '{pw}'.format(pw=password),
        'sentence': 'that sucks'
    }
)

software_version = r1.json()['version']
score1 = r1.json()['score']
score2 = r2.json()['score']

if score1 > 0 and score2 < 0:
    output = '''
    ======================
        Content test
    ======================
    request done at "/{software_version}/sentiment"
    | username={username}
    | password={password}
    Software version: {software_version}

    The sentence 'life is beautiful' scores: {score1}
    The sentence 'that sucks' scores: {score2}
    The sentiment analysis works correctly
    SUCCES >>>
    
    '''
else:
    output = '''
    ======================
        Content test
    ======================
    request done at "/{software_version}/sentiment"
    | username={username}
    | password={password}
    Software version: {software_version}

    The sentence 'life is beautiful' scores: {score1}
    The sentence 'that sucks' scores: {score2}
    The sentiment does not work correctly
    FAILURE >>>
    
    '''

# printing in a file
if os.environ.get('LOG') == 1:
    with open('api_test.log', 'a') as file:
        file.write(output)
        
@server.route('/')
def index():
    return output.format(software_version=software_version,score1=score1,score2=score2,username=username,password=password)

if __name__ == '__main__':
    server.run(host='0.0.0.0', port=7000)
