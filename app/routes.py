from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
	user = {'username': 'BotenAqua'}
	posts = [
		{
			'author': {'username' : 'BotenAqua'},
			'body': 'Ej no bez jaj ze to dziala! ^_^'
		},
		{
			'author': {'username' : 'BotenFaja'},
			'body': 'XDXDXDXD Ale fazaaaaaaaaaa.....'
		}
		]
	return render_template('index.html', title='Glowna', user=user, posts=posts)
