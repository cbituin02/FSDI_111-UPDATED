from flask import (
    Flask,
    request
)

from datetime import datetime

from app.database import user

app = Flask(__name__)
VERSION = "1.0.0"


@app.get("/version")
def get_version():
    out = { 
        "server_time": datetime.now().strftime("%F %H:%M:%S"),
        "version": VERSION
    }
    return out

@app.get("/users")
def get_all_users():
    user_list = user.scan()
    resp = {
        "status" : "ok",
        "message": "success",
        "users": user_list
    }
    return resp

@app.get("/users/<int:pk>/")
def get_user_by_id(pk):
    target_user = user.select_by_id(pk)
    resp = {
        "status": "ok",
        "message": "success"
    }
    if target_user:
        resp["user"] = target_user
        return resp
    else:
        resp["status"] = "error"
        resp["message"] = "User not found"
        return resp, 404

@app.post("/users/")
def create_user():
    user_data = request.json
    user.insert(user_data)
    return "", 204


@app.put("/users/<int:pk>/")
def update_user(pk):
    user_data = request.json
    user.update(pk, user_data)
    return "", 204

@app.delete("/users/<int:pk>/")
def deactivate_user(pk):
    user.deactivate(pk)
    return "", 204

