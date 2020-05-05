"""Contient le formulaire de connexion

@author: Tanguy Cavagna
@copyright: Copyright 2020, TPI
@version: 1.0.0
@date: 2020-05-05
@see: https://hackersandslackers.com/flask-login-user-authentication/
"""
from wtforms import Form, StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length, Optional

class LoginForm(Form):
    """Forumlaire d'inscription"""
    email = StringField('Email',
                        validators=[
                            Length(min=6, message="Choisissez un email plus long"),
                            Email(message='Entrez un email valide'),
                            DataRequired(message="Ce champ est obligatoire")
                        ])
    
    password = PasswordField('Mot de passe',
                            validators=[
                                DataRequired(message="Ce champ est obligatoire")
                            ])

    submit = SubmitField('Connexion')