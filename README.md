# Article resources

This repository contains code referred to from the GitHub ReadME guide,
"Middleware in Web Applications".

Feel free to use the issue tracker to ask any questions or clarifications. 
Hope you find the article useful!

- [Article resources](#article-resources)
  - [Go](#go)
  - [Javascript](#javascript)
  - [Python](#python)

## Go

The Go code samples are available [here](./go). You will need Go 1.18+ (Earlier
versions may also work, not guaranteed):

- [Client](./go/client/)
- [Server](./go/server/)

To run the client:

```
$ cd go/client
$ go build
$ ./client
```

To run the server:

```
$ cd go/server
$ go build
$ ./server
```


## Javascript

The Javascript code samples are available [here](./javascript/). I used Node v18.10.0
and npm 8.19.2 for the samples:

- [Client](./javascript/client/using-axios/)
- [Server](./javascript/server/using-express/)

To run the client:

```
$ cd javascript/client/using-axios
$ npm install
$ node client.js
```

To run the server:

```
$ cd javascript/client/using-express
$ npm install
$ node index.js
```

## Python

The Python code samples are available [here](./python/). I used Python 3.10 and
[Poetry 1.1](https://python-poetry.org/) for package management:

Client:

- [requests](./python/client/using-requests/)
- [aiohttp](./python/client/using-aiohttp/)

Server:

- [flask](./python/server/using-flask/)
- [fastapi](./python/server/using-fastapi/)

To run any of the clients:

```
$ cd python/client/<using-axios><using-requests>
$ poetry install
$ poetry run python client.py

```

To run the Flask application

```
$ cd python/server/using-flask
$ poetry install
$ poetry run python app.py
```

To run the FastAPI application:

```
$ cd python/server/using-fastapi
$ poetry install
$ poetry run gunicorn app:app --workers 1 --worker-class  uvicorn.workers.UvicornWorker --bind 127.0.0.1:8000
```