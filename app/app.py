from flask import Flask, request
from itertools import product


student_id = 6


tools = list(product(('python 3.8.*', 'python 3.7.*', 'python 3.6.*'),
    ('venv + requirements.txt', 'virtualenv + requirements.txt', 'poetry', 'pipenv')
    ))[student_id - 1]


tools = tuple(tool.replace('*', f'{student_id}') for tool in tools)

app = Flask(__name__)

@app.route(f'/api/v1/hello-world-{student_id}')
@app.route('/') 
def index():
    status_code = 200
    return(f'<h1>Hello World {student_id}</h1> <p>TOOLS: {", ".join(tools)}</p>', status_code)


if __name__ == '__main__':
    app.run(debug=True)