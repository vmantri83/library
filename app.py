from flask import Flask
# from controller import user_controller
app=Flask(__name__)


@app.route('/') #these are called decorators
def demo():
    return "Helllloooo"

from controller import *

if __name__ == "__main__":
    app.run(debug=True)