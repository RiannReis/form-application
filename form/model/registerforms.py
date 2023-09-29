from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, EmailField, TelField
from wtforms.validators import DataRequired, NumberRange

class RegisterForm(FlaskForm):
    name = StringField('* Name:', validators=[DataRequired()], id='name')
    email = EmailField('* Email:', validators=[DataRequired()], id='email')
    number = TelField('* Phone:', validators=[DataRequired()], id='number')
    age = IntegerField('Age:', validators=[NumberRange(min=0, max=100)], id='age')
    occupation = StringField('Occupation:', id='occupation')