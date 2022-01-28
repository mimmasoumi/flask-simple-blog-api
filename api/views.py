from flask import Blueprint, jsonify, request, session

from api.models import News, User
from api.utils import check_login, check_password
from . import db


main = Blueprint('main', __name__)

# index page
@main.route("/", methods=["GET", "POST"])
def index():
    return "index"

# register
@main.route("/register", methods=["POST"])
def register():

    res = request.get_json()

    user = User.query.filter_by(username=res["username"], password=res["password1"]).first()

    if user:
        return {"error": "an account with this username/email exists"}

    else:
        if check_password(res["password1"], res["password2"]) == True:
            user = User(username=res["username"], password=res["password1"], email=res["email"])
            db.session.add(user)
            db.session.commit()

            return {"message": "User created."}, 201
        else:
            return {"error": check_password(res["password1"], res["password2"])}

# login
@main.route("/login", methods=["POST"])
def login():

    res = request.get_json()

    if check_login():
        return {"message": "user logged in currently."}
    else: 
        user = User.query.filter_by(username=res["username"], password=res["password"]).first()
        if user:
            session["logged_in"] = True
            session["username"] = res["username"]
            return {"message": "user logged in."}    

        else:
            return {"error": "user not exists."}

# logout
@main.route("/logout", methods=["POST"])
def logout():
    if check_login():
        session.pop("logged_in")
        session.pop("username")
        return {"message": "logout succesfully."}
    else:
        return {"message": "you are not logged in."}

# add post
@main.route("/add_news", methods=["POST"])
def add_news():
    if check_login():
        res = request.get_json()
        news = News(title=res["title"], description=res["description"])
        db.session.add(news)
        db.session.commit()
        return {"message": "post created."}, 201
    else:
        return {"message": "you are not logged in."}

# post single
@main.route("/news<int:news_id>", methods=["GET"])
def news_single(news_id):
    news = News.query.filter_by(id=news_id).first()

    if news:
        news.view += 1
        db.session.commit()
        return {"news": news.as_dict()}
    else:
        return {"error": "post not found."}

# delete post
@main.route("/delete_news<int:news_id>", methods=["DELETE"])
def delete_new(news_id):
    if check_login():
        news = News.query.filter_by(id=news_id).first()

        if news:
            db.session.delete(news)
            db.session.commit()
            return {"message": "post post deleted successfully."}
        else:
            return {"error": "post not found."}
    else:
        return {"error": "you are not logged in."}

# update post
@main.route("/update_news<int:news_id>", methods=["PUT"])
def update_new(news_id):
    if check_login():
        news = News.query.filter_by(id=news_id).first()
        res = request.get_json()
        if news:
            news.title = res["title"]
            news.description = res["description"]
            db.session.commit()
            return {"message": "post updated successfully."}
        else:
            return {"error": "post not found."}
    else:
        return {"error": "you are not logged in."}
