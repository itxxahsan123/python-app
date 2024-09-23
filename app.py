from flask import Flask
import socket

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World! This is my CodePipeline Project and Successfully Running and Fucking Running........!!! I\'m host %s' % socket.gethostname()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
