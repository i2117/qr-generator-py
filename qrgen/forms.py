from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import IntegerField, StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError, NumberRange


class GenerateForm(FlaskForm):
    fragment_size = IntegerField('Fragment size',
                           validators=[DataRequired(), NumberRange(1, 20)])
    fragment_count = IntegerField('Fragment count',
                           validators=[DataRequired(), NumberRange(10, 60)])
    common_name = StringField('Common name',
                        validators=[DataRequired(), Length(min=2, max=20)])
    delimeter = StringField('Delimeter',
                        validators=[DataRequired(), Length(min=0, max=5)])
    start_index = IntegerField('Start index',
                           validators=[DataRequired()])
    end_index = IntegerField('Start index',
                           validators=[DataRequired()])

    submit = SubmitField('Generate!')


class Aaa:



    def validate_fragment_size(self, username):
        user = False#User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different one.')

    def validate_fragment_count(self, email):
        user = False#User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken. Please choose a different one.')
