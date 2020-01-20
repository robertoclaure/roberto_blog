from flask import Blueprint, render_template
from myhomepage.models import User

errors = Blueprint('errors', __name__)


superuser=User.query.filter_by(email='robertoclaure@gmail.com').first()

@errors.app_errorhandler(404)
def error_404(error):
	return render_template('errors/404.html', superuser=superuser), 404

@errors.app_errorhandler(403)
def error_404(error):
	return render_template('errors/403.html', superuser=superuser), 403

@errors.app_errorhandler(500)
def error_404(error):
	return render_template('errors/500.html',superuser=superuser), 500
