from flask import Flask, render_template
from flask_auth.db.db import db
from flask_auth.auth.auth import auth
from flask_auth.main.main import bp

def register_all_blueprint(app: Flask):
    app.register_blueprint(auth, url_prefix="/auth")
    app.register_blueprint(bp, url_prefix="/")


def create_app() -> Flask:
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SECRET_KEY"] = "super secret key"
    db.init_app(app)
    
    register_all_blueprint(app)

    return app


if __name__ == "__main__":
    create_app().run(debug=True)
