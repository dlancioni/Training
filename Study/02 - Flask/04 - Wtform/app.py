# http://wtforms.simplecodes.com/docs/1.0.3/validators.html
 
from flask import Flask
from module1 import module1

app = Flask(__name__)
app.register_blueprint(module1)
app.config['SECRET_KEY'] = '3d6f45a5fc12445dbac2f59c3b6c7cb1'  

if __name__ == '__main__':
   app.run(debug=True)