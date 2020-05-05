from flask import redirect, render_template, flash, Blueprint, request, url_for
from flask import current_app as app
from flask_login import login_required, current_user, login_user
from .packages.forms.LoginForm import LoginForm
from .packages.forms.SignupForm import SignupForm
import hashlib

# Configuration du Blueprint
auth_bp = Blueprint('auth_bp', __name__,
                    template_folder='templates',
                    static_folder='static')

@auth_bp.route('/signup', methods=['GET', 'POST'])
def signup():
    """Affiche la page d'inscription ou inscrit un utilisateur

        GET: Affiche la page
        POST: Si les informations de connexion sont valides, redirection sur l'accueil
    """
    signup_form = SignupForm(request.form) # Rempli les champs créer dans le SignupForm avec les valeurs du forumlaire corerspondantes au nom donné au champs
    # Les champs créer dans le SignupForm peuvent être parcouru grâce à la methode __setitem__ et __getitem__.
    if request.method == 'POST':
        if signup_form.validate(): # Utilise les validators renseignés dans SignupForm pour vérifier les valeurs des champs
            email = signup_form.email.data
            nickname = signup_form.nickname.data
            password = signup_form.password.data

            if not UserController().exists(email):
                hashed_password = hashlib.sha256(password.encode('utf8')).hexdigest()
                user = UserController().insert(email, hashed_password, nickname)
                UserController().setup_default_lists(user.id)
                login_user(user)
                return redirect(url_for('main_bp.home'))
            flash('Un utlisateur utilise déjà cette adresse mail')
            return redirect(url_for('auth_bp.signup'))

    return render_template('signup.html',
                           current_user=current_user,
                           form=signup_form)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    """Affiche la page de connexion ou connect l'utilisateur
    """
    login_form = LoginForm(request.form) # Rempli les champs créer dans le LoginForm avec les valeurs du forumlaire corerspondantes au nom donné au champs
    if request.method == 'POST': # Utilise les validators renseignés dans LoginForm pour vérifier les valeurs des champs
        if login_form.validate():
            email = login_form.email.data
            password = login_form.password.data
            hashed_password = hashlib.sha256(password.encode('utf8')).hexdigest()

            if UserController().check_password(email, hashed_password):
                user = UserController().get_by_email(email)
                login_user(user)
                return redirect(url_for('main_bp.home'))
            flash('Combinaison email/mot de passe invalide')
            return redirect(url_for('auth_bp.login'))

    return render_template('login.html',
                           current_user=current_user,
                           form=login_form)