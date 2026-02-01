from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SQLACHEMY_TRACK_MODIFICATIONS'] = False     

db = SQLAlchemy(app)

from models import Post

@app.route("/")
def home():
    name = "Peter"
    return render_template('home.html', name=name)


@app.route("/about")
def about():
    name = "Peter"
    framework = "Flask"
    return render_template('about.html', name=name, framework=framework)

@app.route("/posts")
def post():
    posts = Post.query.all()
    return render_template('post.html', posts=posts)


if __name__ == "__main__":
    app.run(debug=True)