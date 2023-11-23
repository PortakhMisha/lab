from flask import Flask
from waitress import serve

app = Flask(__name__)

@app.route('/api/v1/hello-world-19')
def hello_world_4():
    return "Hello World 19", 200

if __name__ == '__main__':
    serve(app, host='127.0.0.1', port=5000)


# http://localhost:5000/api/v1/hello-world-19