from flask import Flask

app = Flask(__name__)

@app.route('/')
def hallo_welt():
    return 'Hallo Welt'

if __name__ == '__main__':
    app.run()