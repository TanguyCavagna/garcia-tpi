"""Flask config class."""
import os

class ProdConfig:
    TESTING = False
    DEBUG = False
    TEMPLATES_AUTO_RELOAD = False

class DevConfig:
    TESTING = True
    DEBUG = True
    TEMPLATES_AUTO_RELOAD = True