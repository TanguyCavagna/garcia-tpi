from flask import *
from flask import current_app as app
from flask_login import current_user, login_required, logout_user

# Configuration du Blueprint
main_bp = Blueprint('main_bp', __name__,
                    template_folder='templates',
                    static_folder='static')

@main_bp.route('/', methods=['GET'])
def home():
    """Affiche l'index
    """
    return render_template('index.html',
                           current_user=current_user)