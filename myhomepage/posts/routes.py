from flask import Blueprint
from flask import render_template, url_for, flash, redirect, request, abort
from flask_login import current_user, login_required
from myhomepage import db
from myhomepage.models import Post, User
from myhomepage.posts.forms import PostForm

from myhomepage.yt_embed import getVideoID

posts = Blueprint('posts', __name__)

@posts.context_processor
def inject_user():
	return dict(superuser=User.query.filter_by(email='robertoclaure@gmail.com').first())


@posts.route("/post/new/", methods=['GET', 'POST'])
@login_required
def new_post():
	form = PostForm()
	if form.validate_on_submit():
		yt_vid_id = getVideoID(form.video_link.data)
		post = Post(category_id= form.category_id.data, title=form.title.data,
				content=form.content.data, author=current_user, yt_link=yt_vid_id)
		db.session.add(post)
		db.session.commit()
		flash('Your post has been created!', 'success')
		return redirect(url_for('main.home'))
	return render_template('create_post.html', title='New Post',
		form=form, legend='New Post')


@posts.route("/post/<int:post_id>/")
def post(post_id):
	post = Post.query.get_or_404(post_id)
	return render_template('post.html', title=post.title, post=post)


@posts.route("/post/<int:post_id>/update/", methods=['GET', 'POST'])
@login_required
def update_post(post_id):
	post = Post.query.get_or_404(post_id)
	if post.author != current_user:
		abort(403)

	if post.yt_link:
		form = PostForm(category_id=post.category_id,
		mediatype="VIDEO",
		video_link="www.youtube.com/watch?v=" + post.yt_link)
	else:
		form = PostForm(category_id=post.category_id)

	if form.validate_on_submit():
		post.category_id = form.category_id.data
		post.title = form.title.data
		post.content = form.content.data
		if form.video_link.data:
			post.yt_link = getVideoID(form.video_link.data)
		db.session.commit()
		flash('Post has been updated!', 'success')
		return redirect(url_for('posts.post', post_id=post.id))
	elif request.method == 'GET':
		form.title.data = post.title
		form.content.data = post.content
	return render_template('create_post.html', title='Update Post',
		form=form, legend='Update Post')


@posts.route("/post/<int:post_id>/delete/", methods=['POST'])
@login_required
def delete_post(post_id):
	post = Post.query.get_or_404(post_id)
	if post.author != current_user:
		abort(403)
	db.session.delete(post)
	db.session.commit()
	flash('Post has been deleted!', 'success')
	return redirect(url_for('main.home'))
