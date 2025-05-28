from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required, current_user
from .models import User
from . import db
from werkzeug.security import check_password_hash
from sqlalchemy import or_

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return "Welcome to the Welfare App!"  # Temporary homepage

@main.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')

        # Validate input
        if not username or not email or not password or not confirm_password:
            flash('Please fill out all fields.', 'error')
            return redirect(url_for('main.register'))

        if password != confirm_password:
            flash('Passwords do not match.', 'error')
            return redirect(url_for('main.register'))

        # Check if user exists
        existing_user = User.query.filter(
            or_(User.username == username, User.email == email)
        ).first()
        if existing_user:
            flash('Username or email already exists.', 'error')
            return redirect