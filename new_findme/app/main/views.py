from flask import render_template, redirect, url_for, abort, flash, Response
from flask_login import login_required, current_user
from . import main
from .forms import EditProfileForm, UploadPicture
from .. import db
from ..models import Role, User
from ..decorators import admin_required


@main.route('/')
def index():
    return render_template('index.html')

@main.route('/home')
def home():
    return render_template('homepage.html')

@main.route('/<username>')
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    return render_template('user.html', user=user)

@main.route('/edit-profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EditProfileForm()
    if form.validate_on_submit():
        current_user.name = form.name.data
        current_user.location = form.location.data
        current_user.about_me = form.about_me.data
        current_user.email = form.email.data
        current_user.facebook = form.facebook.data
        current_user.linkedin = form.linkedin.data
        current_user.github = form.github.data
        current_user.youtube = form.youtube.data
        current_user.twitter = form.twitter.data
        current_user.instagram = form.instagram.data
        current_user.snapchat = form.snapchat.data
        current_user.medium = form.medium.data
        current_user.tiktok = form.tiktok.data
        db.session.add(current_user._get_current_object())
        db.session.commit()
        return redirect(url_for('.user', username=current_user.username))
    form.name.data = current_user.name
    form.location.data = current_user.location
    form.about_me.data = current_user.about_me
    form.email.data = current_user.email
    form.facebook.data = current_user.facebook
    form.linkedin.data = current_user.linkedin
    form.github.data = current_user.github
    form.youtube.data = current_user.youtube
    form.twitter.data = current_user.twitter
    form.instagram.data = current_user.instagram
    form.snapchat.data = current_user.snapchat
    form.medium.data = current_user.medium
    form.tiktok.data = current_user.tiktok
    return render_template('edit_profile.html', form=form)

@main.route('/upload-picture', methods=['GET', 'POST'])
@login_required
def upload_picture():
    form = UploadPicture()
    if form.validate_on_submit():
        current_user.profile_picture = form.profile_picture.data.read()
        db.session.add(current_user._get_current_object())
        db.session.commit()
        return redirect(url_for('.user', username=current_user.username))
    return render_template('upload_picture.html', form=form)


@main.route('/user/profile-picture/<int:user_id>')
def get_profile_picture(user_id):
    user = User.query.get_or_404(user_id)
    return Response(user.profile_picture, mimetype='image/png')
"""
@main.route('/edit-profile/<int:id>', methods=['GET', 'POST'])
@login_required
@admin_required
def edit_profile_admin(id):
    user = User.query.get_or_404(id)
    form = EditProfileAdminForm(user=user)
    if form.validate_on_submit():
        user.email = form.email.data
        user.username = form.username.data
        user.confirmed = form.confirmed.data
        user.role = Role.query.get(form.role.data)
        user.name = form.name.data
        user.location = form.location.data
        user.about_me = form.about_me.data
        db.session.add(user)
        db.session.commit()
        flash('The profile has been updated.')
        return redirect(url_for('.user', username=user.username))
    form.email.data = user.email
    form.username.data = user.username
    form.confirmed.data = user.confirmed
    form.role.data = user.role_id
    form.name.data = user.name
    form.location.data = user.location
    form.about_me.data = user.about_me
    return render_template('edit_profile.html', form=form, user=user)
"""
