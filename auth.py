from flask import redirect, render_template, flash, Blueprint, request, url_for
from flask import current_app as app
from flask_login import login_required, current_user, login_user
import hashlib

# Configuration du Blueprint
auth_bp = Blueprint('auth_bp', __name__,
                    template_folder='templates',
                    static_folder='static')