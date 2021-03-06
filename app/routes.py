from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm
import os
import markdown


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

@app.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		flash('{} chce sie zalogowac i {} byc zapamietany'.format(form.username.data, form.remember_me.data))
		return redirect(url_for('index'))
	return render_template('login.html', title='Zaloguj sie', form=form)

@app.route('/md')
def markdown_posts():
	# To do: cleanup & DRY
	# fix content
	file_dir = os.path.dirname(os.path.realpath(__file__)) + url_for('static', filename='posts/test.md')
	with open(file_dir) as file_reader:
		md_post = file_reader.read()
	md = markdown.Markdown(extensions=['meta'])
	content = md.convert(md_post)
	return render_template('markdown_post.html', meta = md.Meta, post = content)
