from flask import Blueprint
from .models import User
from flask import render_template

user_bp = Blueprint('user',
                    import_name='user',
                    url_prefix='/user',
                    template_folder='./templates'
                    )
@user_bp.route('/register')
def register():
    return render_template('register.html')
@user_bp.route('/login')
def login():
    return render_template('login.html')
@user_bp.route('/info')
def info():
    return 'info'