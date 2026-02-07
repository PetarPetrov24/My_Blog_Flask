from flask import Flask, render_template
from models import Post

def register_app(app):
    @app.route("/")
    def intro():
        return render_template('intro.html')


    @app.route("/home")
    def home():
        name = "Peter"
        all_posts = Post.query.all()
        return render_template('home.html', name=name, posts=all_posts)

    @app.route("/about")
    def about():
        name = "Peter"
        framework = "Flask"
        return render_template('about.html', name=name, framework=framework)

    @app.route("/posts")
    def posts():
        all_posts = Post.query.all()
        return render_template('post.html', posts=all_posts)
    