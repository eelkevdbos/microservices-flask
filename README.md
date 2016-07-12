Microservices with Flask
============================

Simple demo of microservices with docker and flask

Composed of 2 containers:
- blog
- auth

## Blog

The blog container lists and creates blog posts for authenticated users.

Endpoints:

- list: [GET /posts] list posts in json format
- show: [GET /posts/{id}] show a single post in json format
- create: [POST /posts] create a new post (requires authentication via JWT token)

## Auth

The authentication container registers and logs in users, providing them an authentication token.

Endpoints:

- list: [GET /users] list users in json format
- show: [GET /users/{id}] show a single user in json format
- register: [GET /register/{name}/{password}] register a new user with a password
- login: [POST /login] to retrieve a auth token based on username/password combination provided
- verify: [POST /verify] verify our token and return our identity


## Usage

1. Boot the containers via: `docker-compose up`
2. Register a username / password combination via [GET /register/{name}/{password}]
3. Login to retrieve an access token (JWT) via [POST /login] payload={"username":"myuser","password":"mypass"}
3. Create a post using the received token via [POST /posts] payload={"title": "Second post", "content": "Second post content"} headers={"Authorization": "JWT {token}"}
4. View the added post via [GET /posts]

