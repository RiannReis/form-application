from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

class TokenAuth(FlaskForm):
    token = StringField('Access token below:', validators=[DataRequired()], id='token')