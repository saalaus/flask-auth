import jwt
from flask import current_app


def check_registration_form(username, password, confirm_password) -> "str | None":
    "Validate registration form. Return str if error, and None if successfull"
    if password != confirm_password:
        return "Passwords unique!"
    
    return None


def generate_token(**data):
    return jwt.encode(dict(data),
                      current_app.config["SECRET_KEY"],
                      algorithm="HS256")