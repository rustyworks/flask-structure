from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required


class SimpleForm(Form):
    name = StringField('Your name', validators=[Required()])
    submit = SubmitField('Submit')
