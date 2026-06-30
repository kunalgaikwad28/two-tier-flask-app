from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return '<h1>Hello from Flask running in Docker!</h1><p>Deployed by Kunal</p>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
