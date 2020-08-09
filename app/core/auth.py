"""Handle actions associated with authentication."""
from . import core
from .. import mongo, logger
from ..core.forms import LoginForm, RegisterForm
from ..models.user import User, Integrations
from ..models.integrations.twitter_integration import TwitterIntegration
from flask import current_app as app
from flask import render_template, redirect, url_for, request
from flask_login import login_user, logout_user
from werkzeug.security import generate_password_hash


@core.route('/login', methods=['GET', 'POST'])
def login():
    """Handle the login process."""
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User.objects.get(username=form.username.data)
        logger.debug("User: %s" % user)
        if user and user.validate_login(form.password.data):
            login_user(user, remember=True)
            next = request.args.get('next')
            return redirect(next or url_for('core.root'))
    errors = ','.join([value[0] for value in list(form.errors.values())])
    logger.error("bad login " + form.username.data)
    return render_template('login.html', message=errors)


@core.route('/logout')
def logout():
    """Handle the logout process."""
    logout_user()
    return redirect(url_for('core.login'))


@core.route('/register', methods=['GET', 'POST'])
def register():
    """Render the register page."""
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User(
            username=form.username.data,
            email=form.email.data,
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            password=generate_password_hash(form.password.data)
        )
        logger.debug("User: %s" % user)
        user.save()
        next = request.args.get('next')
        return redirect(next or url_for('core.login'))
    errors = ','.join([value[0] for value in list(form.errors.values())])
    return render_template('register.html', message=errors)


@core.route('/forgot-password')
def forgot_password():
    """Handle the forgot password process."""
    # TODO: Implement a forgot password function
    return redirect(url_for('core.login'))
