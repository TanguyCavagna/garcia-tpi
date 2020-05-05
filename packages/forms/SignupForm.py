"""Contient le formulaire d'inscription

@author: Tanguy Cavagna
@copyright: Copyright 2020, TPI
@version: 1.0.0
@date: 2020-05-05
@see: https://hackersandslackers.com/flask-login-user-authentication/
"""
from wtforms import Form, StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length, Optional

class SignupForm(Form):
    """Forumlaire d'inscription"""
    email = StringField('Email',
                        validators=[
                            Length(min=6, message="Choisissez un email plus long"),
                            Email(message='Entrez un email valide'),
                            DataRequired(message="Ce champ est obligatoire")
                        ])
    
    last_name = StringField('Nom',
                            validators=[
                                DataRequired(message="Ce champ est obligatoire")
                            ])

    first_name = StringField('Prénom',
                            validators=[
                                DataRequired(message="Ce champ est obligatoire")
                            ])

    phone = StringField('Télephone',
                        validators=[
                            DataRequired(message="Ce champ est obligatoire")
                        ])
    
    password = PasswordField('Mot de passe',
                            validators=[
                                Length(min=6, message='Choisissez un mot de passe plus fort'),
                                DataRequired(message="Ce champ est obligatoire")
                            ])

    confirm = PasswordField('Pseudo',
                            validators=[
                                EqualTo('password', message='Les mots de passes doivent correspondre'),
                                DataRequired(message="Ce champ est obligatoire")
                            ])

    submit = SubmitField('Inscription')