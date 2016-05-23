Microservices with Flask
============================

Simple demo of microservices with docker and flask

Composed of 3 containers:
- hello container
- name container
- concat container

## Hello container:

A small container that returns a single "hello" response on every GET request to http://hello:5000/

## Name container:

A small container that returns the first segment in the request URI to http://name:5000/<segment>

## Concat container:

A small container that calls both the Hello and the Name container in succession. The result is concatted and returned.

## Examples:

Assuming you installed docker + docker-compose locally.

1. Run docker-compose up

2. Execute a request to the concat container using the following url: http://127.0.0.1/eelke-van-den-bos

Will result in the following:

```
hello eelke-van-den-bos
```

