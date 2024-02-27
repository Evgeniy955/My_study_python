import os


def get_favorite_color():
    return 'super-duper color'


def get_favorite_number():
    return 13


IS_NOT_REGRESS_PATH = os.environ.get("IS_NOT_REGRESS_PATH", os.path.dirname(__file__))