from flask import *
from flask import current_app as app
from flask_login import current_user, login_required, logout_user
from .packages.controllers.SqliteController import SqliteController
from .packages.controllers.UserController import UserController

# Configuration du Blueprint
main_bp = Blueprint('main_bp', __name__,
                    template_folder='templates',
                    static_folder='static')

@main_bp.route('/', methods=['GET'])
def home():
    """Affiche l'index
    """
    if current_user.is_authenticated:
        return render_template('index.html',
                            users=UserController().get_all(),
                            current_user=current_user)
    else:
        return redirect(url_for('auth_bp.login'))

@main_bp.route('/setup/sqlite', methods=['GET'])
def setup():
    """Créer la base de données sqlite
    """
    setup = SqliteController().setup_user_table() and SqliteController().setup_role_table()
    return jsonify({'Status' : setup})

@main_bp.route('/test', methods=['GET'])
def test():
    return jsonify({'Status' : UserController().insert()})

@main_bp.route('/get/user', methods=['POST'])
def get_user():
    return jsonify({'User' : UserController().get_by_id(request.json.get('idUser')).serialize()})

@main_bp.route('/set/user', methods=['PUT'])
def set_user():
    id = request.json.get('idUser')
    email = request.json.get('emailUser')
    last_name = request.json.get('lastnameUser')
    first_name = request.json.get('firstnameUser')
    phone = request.json.get('phoneUser')

    return jsonify({'User' : UserController().set_by_id(id, email, last_name, first_name, phone)})

@main_bp.route('/delete/user', methods=['DELETE'])
def delete_user():
    return jsonify({'Status' : UserController().delete_by_id(request.json.get('idUser'))})
