import os
import requests
from flask import Flask

server = Flask('authentication_server')

# definition of the API address

api_address = 'fastapi'
# API port
api_port = 8000

# requête
r = requests.get(
    url='http://{address}:{port}/permissions'.format(address=api_address, port=api_port),
    params= {
        'username': 'alice',
        'password': 'wonderland'
    }
)
output = '''
============================
    Authentication test
============================
request done at "/permissions"
| username="alice"
| password="wonderland"
expected result = 200
actual restult = {status_code}
==>  {test_status}
'''
# query status
status_code = r.status_code
# display the results
if status_code == 200:
    test_status = 'SUCCESS'
else:
    test_status = 'FAILURE'

           
@server.route('/')
def index():
    return output.format(status_code=status_code, test_status=test_status)

if __name__ == '__main__':
    server.run(host='0.0.0.0', port=5000)
    
if os.environ.get('LOG') == 1:
    with open('api_test.log', 'a') as file:
        file.write(output)