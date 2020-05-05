from flask import *
from flask import current_app as app
from flask_login import current_user, login_required, logout_user
from .packages.controllers.SqliteController import SqliteController

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

@main_bp.route('/setup/sqlite', methods=['GET'])
def setup():
    """Créer la base de données sqlite
    """
    setup = SqliteController().setup_user_table() and SqliteController().setup_role_table()
    return jsonify({'Status' : setup})