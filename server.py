from flask_app import app

from flask_app.controllers import users
from flask_app.controllers import tacs
from flask_app.controllers import neck_swings

if __name__=="__main__":
    app.run(debug=True)