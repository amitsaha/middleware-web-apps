from flask import Flask

from auth_header_check import AuthHeaderCheck

app = Flask(__name__)
app.wsgi_app = AuthHeaderCheck(app.wsgi_app, included_patterns=["/api"])

@app.route("/")
def hello():
    return "Hello world!"

@app.route("/api/protected")
def protected():
    return "This is a protected resource"

app.run(port=8000)
