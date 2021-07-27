from flask import Flask, request
import clss
app = Flask(__name__)
host = '0.0.0.0'
port = 8080

@app.route('/')
def hello():
    return "<h1>hello</h1>"

@app.route("/post",methods=['POST'])
def post():
    value = request.form['imgurl']
    position = clss.finder(value)

    return position

if __name__ == '__main__':
    app.run(host=host, port=port)