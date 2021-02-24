from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
	username = StringField('Login', validators=[DataRequired()])
	password = PasswordField('Okon', validators=[DataRequired()])
	remember_me = BooleanField('Zapamietaj')
	submit = SubmitField('Zaloguj sie')
