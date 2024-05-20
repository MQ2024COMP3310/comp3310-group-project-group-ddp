from flask import (
    Blueprint, render_template, request,
    flash, redirect, url_for, send_from_directory,
    current_app, make_response
)
from .models import Photo
from sqlalchemy import asc, text
from . import db
import os

from flask_login import login_required, current_user
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash

main = Blueprint('main', __name__)

# This is called when the home page is rendered. It fetches all images sorted by filename.


@main.route('/')
def homepage():
    photos = db.session.query(Photo).order_by(asc(Photo.file))
    return render_template('index.html', photos=photos)


@main.route('/uploads/<name>')
def display_file(name):
    return send_from_directory(current_app.config["UPLOAD_DIR"], name)


@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)


# Upload a new photo
@main.route('/upload/', methods=['GET', 'POST'])
def newPhoto():
    if request.method == 'POST':
        file = None
        if "fileToUpload" in request.files:
            file = request.files.get("fileToUpload")
        else:
            flash("Invalid request!", "error")

        if not file or not file.filename:
            flash("No file selected!", "error")
            return redirect(request.url)

        filepath = os.path.join(
            current_app.config["UPLOAD_DIR"], file.filename)
        file.save(filepath)

        newPhoto = Photo(name=request.form['user'],
                         caption=request.form['caption'],
                         description=request.form['description'],
                         file=file.filename)
        db.session.add(newPhoto)
        flash('New Photo %s Successfully Created' % newPhoto.name)
        db.session.commit()
        return redirect(url_for('main.homepage'))
    else:
        return render_template('upload.html')


# This is called when clicking on Edit. Goes to the edit page.
@main.route('/photo/<int:photo_id>/edit/', methods=['GET', 'POST'])
@login_required
def editPhoto(photo_id):
    editedPhoto = db.session.query(Photo).filter_by(id=photo_id).one()
    if request.method == 'POST':
        # # Authentication needed before an edit is allowed
        # email = request.form.get('email')
        # password = request.form.get('password')
        # remember = True if request.form.get('remember') else False

        # user = User.query.filter_by(email=email).first()

        # if not user or not check_password_hash(user.password, password):
        #     flash('Please check your login details and try again.')
        #     current_app.logger.warning("User failed to login")
        #     # if the user doesn't exist or password is wrong, reload the page
        #     return redirect(url_for('main.homepage'))

        # # Returns the edit page for the user
        # login_user(user, remember=remember)
        # return redirect(url_for('main.profile'))
        if request.form['user']:
            editedPhoto.name = request.form['user']
            editedPhoto.caption = request.form['caption']
            editedPhoto.description = request.form['description']
            db.session.add(editedPhoto)
            db.session.commit()
            flash('Photo Successfully Edited %s' % editedPhoto.name)
            return redirect(url_for('main.homepage'))
    else:
        return render_template('edit.html', photo=editedPhoto)


# This is called when clicking on Delete.
@main.route('/photo/<int:photo_id>/delete/', methods=['GET', 'POST'])
def deletePhoto(photo_id):
    fileResults = db.session.execute(
        text('select file from photo where id = ' + str(photo_id)))
    filename = fileResults.first()[0]
    filepath = os.path.join(current_app.config["UPLOAD_DIR"], filename)
    os.unlink(filepath)
    db.session.execute(text('delete from photo where id = ' + str(photo_id)))
    db.session.commit()

    flash('Photo id %s Successfully Deleted' % photo_id)
    return redirect(url_for('main.homepage'))
