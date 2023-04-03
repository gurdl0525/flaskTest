from flask import Flask
import os

app = Flask(__name__)


@app.route("/")
def index():
    return 'Hellow World'


if __name__ == "__main__":
    app.run("0.0.0.0", int(os.environ.get("PORT", 8080)))
