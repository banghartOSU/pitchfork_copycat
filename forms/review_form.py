from flask_wtf import FlaskForm
from wtforms import StringField, TextField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length, Email


class ReviewForm(FlaskForm):
    """Review Form"""
    
    review_select = SelectField('Rating:', [DataRequired()])
    body = TextField(
        "Message",
        [DataRequired(), Length(min=5, message=("Your message is too short."))],
    )
    firstname = StringField("First Name", [DataRequired()])
    lastname = StringField("Last Name", [DataRequired()])
    email = StringField(
        "Email", [Email(message=("Not a valid email address.")), DataRequired()]
    )
    submit = SubmitField("Submit")
