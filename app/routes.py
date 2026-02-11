from flask import Flask, render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import check_password_hash
from .forms import PostForm, PostDelete, LoginForm
from .models import Post, Admin
from .extensions import db


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
        posts = Post.query.all()
        return render_template('post.html', posts=posts)

    @app.route("/post/<int:id>")
    def post_detail(id):
        post = Post.query.get_or_404(id)
        return render_template("post_detail.html", post=post)

    @app.route('/create-post', methods=['GET', 'POST'])
    @login_required
    def create_post():
        form = PostForm()
        if form.validate_on_submit():
            post = Post(title=form.title.data, content=form.content.data)
            db.session.add(post)
            db.session.commit()
            flash('Post created successfully!', 'success')
            return redirect(url_for('posts'))
        return render_template('create_post.html', form=form)

    @app.route('/delete-post/<int:id>', methods=['GET', 'POST'])
    @login_required
    def delete_post(id):
        post = Post.query.get_or_404(id)  
        form = PostDelete()
        
        if form.validate_on_submit():
            db.session.delete(post)
            db.session.commit()
            flash(f'Post "{post.title}" deleted successfully!', 'success')
            return redirect(url_for('posts'))
        
        return render_template('delete_post.html', form=form, post=post)

    @app.route('/update-post/<int:id>', methods=['GET', 'POST'])
    @login_required
    def update_post(id):
        post = Post.query.get_or_404(id)
        form = PostForm(obj=post)  

        if form.validate_on_submit():
            post.title = form.title.data
            post.content = form.content.data
            db.session.commit()
            flash('Post updated successfully!', 'success')
            return redirect(url_for('post_detail', id=post.id))

        return render_template('update_post.html', form=form, post=post)
    
    @app.route('/admin-login', methods=['GET', 'POST'])
    def login():
        form = LoginForm()
        if form.validate_on_submit():
            admin = Admin.query.filter_by(username=form.username.data).first()

            if admin and check_password_hash(admin.password_hash, form.password.data):
                login_user(admin)
                return redirect(url_for('posts'))
            
            flash('Invalid credentials')
        return render_template('login.html', form=form)

    @app.route('/logout')
    @login_required
    def logout():
        logout_user()
        return redirect(url_for('posts'))