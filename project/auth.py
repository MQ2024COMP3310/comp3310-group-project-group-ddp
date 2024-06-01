from flask import Blueprint, render_template, request, flash, redirect, url_for, current_app
from flask_login import login_user, login_required, logout_user
from sqlalchemy import text
from project.models import Photo, User, Comment
from . import db
from werkzeug.security import generate_password_hash, check_password_hash
import re
import time
import bleach
auth = Blueprint('auth', __name__)
comment_limit = {}

@auth.route('/login')
def login():
    return render_template('login.html')


@auth.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    user = User.query.filter_by(email=email).first()

    # check if the user actually exists
    # take the user-supplied password and compare it with the stored password
    if not user or not check_password_hash(user.password, password):
        flash('Please check your login details and try again.')
        current_app.logger.warning("User login failed")
        # if the user doesn't exist or password is wrong, reload the page
        return redirect(url_for('auth.login'))

    # if the above check passes, then we know the user has the right credentials
    login_user(user, remember=remember)
    return redirect(url_for('main.homepage'))


@auth.route('/signup')
def signup():
    return render_template('signup.html')


@auth.route('/signup', methods=['POST'])
def signup_post():
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')

    query = 'select * from user where email = :email'
    user = db.session.execute(text(query), {"email": email}).all()
    if len(user) > 0:  # if a user is found, we want to redirect back to signup page so user can try again
        # 'flash' function stores a message accessible in the template code.
        flash('Email address already exists')
        current_app.logger.debug("User email already exists")
        return redirect(url_for('auth.signup'))

    # create a new user with the form data using hashed password so the plaintext version isn't saved.
    new_user = User(email=email, name=name, password=generate_password_hash(
        password, method='pbkdf2:sha256:600000', salt_length=16))

    # add the new user to the database
    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for('main.homepage'))

# Chatgpt assisted Code, currently not working. Currently not sure how to get photo id of the page user was just on so maybe have to tweak something in Edit html.
#@auth.route('/photo', methods=['POST'])
# def addcomment():
  #  comment = bleach.clean(request.form.get('comment', ''))
   # comment = re.sub('<[^<]+?>', '', comment)
    # Make sure it isn't too long
  #  if len(comment) > 400:
  #      flash('Comment is too long')
  #      return redirect(url_for('main.homepage'))
    # Rate Limiting
  #  user_id = login_user.id  # Assuming current_user is available
# if user_id in comment_limit and time.time() - comment_limit[user_id] < 60:
 #       flash('Rate limit exceeded')
  #      return redirect(url_for('main.homepage'))
  #  comment_limit[user_id] = time.time()

    # Not working code to get photo id of the comment as each comment has a photo id (that it is attached to)
    # photo = Photo.query.get(photo_id)

    # Update the photo's comment if a comment was provided
  #  if comment:
  #  new_comment = Comment(user_id, photo_id=photo_id, comment=comment, username=login_user.name)
  #  db.session.add(new_comment)
  #  db.session.commit()

    # Redirect back to the photo detail page or another appropriate page
  #  return redirect(url_for('main.homepage'))



@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.homepage'))

# See https://www.digitalocean.com/community/tutorials/how-to-add-authentication-to-your-app-with-flask-login for more information
