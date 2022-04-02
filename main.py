import datetime

from flask import Flask, render_template, redirect, url_for, flash, abort
# from flask_bootstrap import Bootstrap
# from flask_ckeditor import CKEditor
# from datetime import date
# from functools import wraps
# from werkzeug.security import generate_password_hash, check_password_hash
# from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy.orm import relationship
# from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
# from forms import LoginForm, RegisterForm, CreatePostForm, CommentForm
# from flask_gravatar import Gravatar

app = Flask(__name__)
app.config['SECRET_KEY'] = '8knqjkwhfwqkjhfwqoikjckqhfopiuqwihfnqwjkln;vljqwhvqu;lifjqw;kuehwq;lufjqwjlkvwq'
current_year = datetime.datetime.now().year


@app.route("/")
def main_page():
    return render_template("index.html")


@app.route("/about")
def about_page():
    return render_template("about.html")


@app.route("/contact")
def contact_page():
    return render_template("contact.html")


@app.route("/pricing")
def pricing_page():
    return render_template("pricing.html")


@app.route("/faq")
def faq_page():
    return render_template("faq.html")


@app.route("/blog")
def blog_page():
    return render_template("blog-home.html")


@app.route("/blog_post")
def blog_post_page():
    return render_template("blog-post.html")


if __name__ == "__main__":
    app.run(debug=True)
