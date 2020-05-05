from flask import *
from flask_login import LoginManager
from .packages.controllers.UserController import UserController
from .config import *

login_manager = LoginManager()

app = Flask(__name__)
app.config.from_object(DevConfig())
app.secret_key = "8185c8ac4656219f4aa5541915079f7b3743e1b5f48bacfcc3386af016b55320"
login_manager.init_app(app)

with app.app_context():
    from . import routes, auth

    app.register_blueprint(routes.main_bp)
    app.register_blueprint(auth.auth_bp)

# ================
#      OTHER
# ================
@login_manager.user_loader
def load_user(user_id):
    """Test si l'utilisateur est connecté sur toutes les pages. Si oui, retourne l'utilisateur"""
    if user_id is not None:
        return UserController().get_by_id(user_id)
    return None

@login_manager.unauthorized_handler
def unauthorized():
    """Renvoie sur la page login si tentative d'accès à une page nécessitant d'être connecté"""
    flash('Vous devez être connecté pour voir cette page.')
    return redirect(url_for('auth_bp.login'))

# ================
#       Run
# ================
if __name__ == "__main__":
    app.run()