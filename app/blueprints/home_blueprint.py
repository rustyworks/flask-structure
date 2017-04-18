from flask import Blueprint, abort, redirect, render_template, session, url_for
from app.forms.simple_form import SimpleForm


home_blueprint = Blueprint('home', __name__, template_folder='templates')


@home_blueprint.route('/', methods=['POST', 'GET'])
def index():
    form = SimpleForm()
    if form.validate_on_submit():
        session['name'] = form.name.data
        return redirect(url_for('home.index'))
    else:
        try:
            return render_template('home/index.html', form=form, name=session.get('name'))
        except TemplateNotFound:
            abort(404)
