from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello world'

@app.route('/author')
def my_name():
    return 'Matheus Oliveira'

@app.route('/age')
def my_age():
    return '21'

if __name__ == '__main__':
    app.run()