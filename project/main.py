from urllib.parse import urljoin, urlparse
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
from werkzeug.utils import secure_filename

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


# Check whether the target url is under the scope of our host
def is_safe_url(target):
    ref_url = urlparse(request.host_url)
    test_url = urlparse(urljoin(request.host_url, target))
    return test_url.scheme in ('http', 'https') and ref_url.netloc == test_url.netloc


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
            # check whether the target url is under the scope of our host
            if is_safe_url(request.url):
                return redirect(request.url)
            else:
                return redirect(main.homepage)
            
        file.filename = secure_filename(file.filename)
        filepath = os.path.join(
            # sanitise filename before using
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
@login_required
def deletePhoto(photo_id):
    # mitigated SQL injection using Object-Relational Mapping (ORM) approach
    targetPhoto = db.session.query(Photo).filter_by(id=photo_id).one()
    filename = targetPhoto.file
    filepath = os.path.join(current_app.config["UPLOAD_DIR"], filename)
    os.unlink(filepath)
    db.session.delete(targetPhoto)
    db.session.commit()

    flash('Photo id %s Successfully Deleted' % photo_id)
    return redirect(url_for('main.homepage'))
