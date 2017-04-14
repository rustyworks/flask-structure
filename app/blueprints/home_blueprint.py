from flask import Blueprint, abort, render_template


home_blueprint = Blueprint('home_page', __name__, template_folder='templates')


@home_blueprint.route('/')
def index():
    try:
        return render_template('home/index.html')
    except TemplateNotFound:
        abort(404)
