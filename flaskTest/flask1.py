# encoding: utf-8
from flask import Flask


# 这是一个flask的使用例子
app = Flask(__name__)
print __name__
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

if __name__ == '__main__':
    app.run()