from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, SelectField, RadioField
from wtforms.validators import DataRequired

class PostForm(FlaskForm):
	category_id = SelectField('Category',
		choices=[('1', 'Fitness'), ('2', 'Software'), ('3', 'Music'), ('4', 'Miscellaneous')])
	title = StringField('Title', validators=[DataRequired()])
	content = TextAreaField('Content', validators=[DataRequired()])

	mediatype = RadioField('Media Type',
		choices=[('NONE', 'None'), ('VIDEO', 'YouTube Video')],
		default='NONE')
	video_link = StringField('Video Link')

	submit = SubmitField('Post')

