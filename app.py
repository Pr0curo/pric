from flask import Flask
from flask import render_template

app = Flask(__name__)


def start_app() -> Flask:
    app.config.from_object("config.Config")

    return app


@app.route("/")
def index():
    text = "Hello World"
    return render_template("base.html", text=text)


if __name__ == "__main__":
    start_app().run()
