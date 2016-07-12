import os, requests, logging
from models import Post, PostSchema
from flask import Flask, request
from flask_httpauth import HTTPTokenAuth
from database import db_session, init_db
from itsdangerous import (JSONWebSignatureSerializer as Serializer, BadSignature)

# instantiate app
app = Flask(__name__)
auth = HTTPTokenAuth(scheme='JWT')

# set app secret to base jwt token upon
app.config['SECRET_KEY'] = os.environ.get('APP_SECRET', 'secret')


# verify our token by decoding it with our shared secret
@auth.verify_token
def verify_token(token):
    serializer = Serializer(app.config['SECRET_KEY'])
    try:
        # load token with serializer
        data = serializer.loads(token)
        # retrieve identity from token
        return str(data.get('identity', None))

    except BadSignature:
        return None

def verified_user(request):
    # extract token from auth header
    token = request.headers.get('authorization')[4:]

    # decode token
    return verify_token(token)

# close db connection on teardown of app
@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


# list all posts
@app.route('/posts')
def list():
    schema = PostSchema(many=True)
    return schema.dumps(Post.query.all())


# show a single post
@app.route('/posts/<int:id>')
def show(id):
    schema = PostSchema()
    return schema.dumps(Post.query.get(id))


@app.route('/posts', methods=['POST'])
@auth.login_required
def create():

    data = request.get_json(silent=True)
    data['user_id'] = verified_user(request)

    # on success, return new post
    return Post.create(data)


if __name__ == '__main__':
    # initialize with a fresh db
    init_db()

    # serve app on 0.0.0.0:5000
    app.run(host="0.0.0.0", port=5001)
