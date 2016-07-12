import os
from models import User, UserSchema
from flask import Flask
from flask_jwt import JWT, jwt_required, current_identity
from flaskext.bcrypt import Bcrypt
from database import db_session, init_db

# instantiate app
app = Flask(__name__)
bcrypt = Bcrypt(app)

# set app secret to base jwt token upon
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = os.environ.get('APP_SECRET', 'secret')
app.config['JWT_AUTH_URL_RULE'] = '/login'

# close db connection on teardown of app
@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

# list all users available
@app.route('/users')
def list():
    schema = UserSchema(many=True)
    return schema.dumps(User.query.all())

@app.route('/users/<id>')
def show(id):
    schema = UserSchema()
    return schema.dumps(User.query.get(id))

@app.route('/register/<name>/<password>')
def register(name, password):
    u = User(name, password)
    db_session.add(u)
    db_session.commit()

    #on success return empty 204 response
    return ('', 204)

# verify our token and return our identity
@app.route('/verify')
@jwt_required()
def verify():
    schema = UserSchema()
    return schema.dumps(current_identity)


if __name__ == '__main__':
    # initialize with a fresh db
    init_db()

    # create jwt insrtance
    jwt = JWT(app, User.authenticate, User.identity)

    # serve app on 0.0.0.0:5000
    app.run(host="0.0.0.0")
