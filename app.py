from flask import Flask
app = Flask(__name__)

def proper(name:str):
    return (name[0].upper()) + name[1:]

@app.route('/')
@app.route('/hello/')
def hello_world():
    return 'Hello World!\n'

@app.route('/hello/<username>') # dynamic route
def hello_user(username):

    return f'Hello {proper(username)}!\n'

if __name__ == '__main__':
    app.run(host='localhost', debug=True)     # open for everyone

# Credit to https://medium.com/@Joachim8675309/jenkins-ci-pipeline-with-python-8bf1a0234ec3
