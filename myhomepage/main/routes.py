from flask import Blueprint

from flask import render_template, request
from myhomepage.models import Post, User
from myhomepage.practice1 import completePoem
from myhomepage.yt_embed import getVideoID

main = Blueprint('main', __name__)


@main.context_processor
def inject_user():
	return dict(superuser=User.query.filter_by(email='robertoclaure@gmail.com').first())


@main.route("/poem/")
def poem():
	content = completePoem()
	video = getVideoID("https://www.youtube.com/watch?v=Isb7Q4jEA04")
	# return render_template('poemPage.html', authorValue=author, poemBody=poemLines)
	return render_template('poemPage.html', content=content, video=video)


@main.route("/")
@main.route("/home/")
def home():
	page = request.args.get('page', 1, type=int)
	posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
	return render_template('home.html', posts=posts.items, pages=posts)

