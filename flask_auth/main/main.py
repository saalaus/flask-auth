from flask import Blueprint, session, current_app, render_template
import jwt

bp = Blueprint("main", __name__, template_folder="templates")

@bp.route("/")
def index():
    token = session["session"]
    data = jwt.decode(token, current_app.config["SECRET_KEY"],
                          algorithms=["HS256"])
    
    return render_template("main.html", username=data["username"], id=data["id"])