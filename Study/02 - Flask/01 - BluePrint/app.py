# https://github.com/italomaia/flask-empty/
# https://programwithus.com/learn/python/pip-virtualenv-windows
   
from flask import Flask
from module1 import module1
from module2 import module2

app = Flask(__name__)
app.register_blueprint(module1)
app.register_blueprint(module2)

if __name__ == '__main__':
   # app.run(debug=True)
   app.run(debug=True, use_reloader=True)