from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import IntegerField, StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError, NumberRange


class GenerateForm(FlaskForm):
    fragment_size = IntegerField('Fragment size',
                           validators=[DataRequired(), NumberRange(1, 20)], default=5)
    fragment_count = IntegerField('Fragment count',
                           validators=[DataRequired(), NumberRange(10, 60)], default=20)
    common_name = StringField('Common name',
                        validators=[DataRequired(), Length(min=2, max=20)], default='mark')
    delimeter = StringField('Delimeter',
                        validators=[DataRequired(), Length(min=0, max=5)], default='_')
    start_index = IntegerField('Start index',
                           validators=[DataRequired()], default=1)
    end_index = IntegerField('End index',
                           validators=[DataRequired()], default=5)

    def validate_end_index(self, end_index):
        if self.start_index.data > self.end_index.data:
            raise ValidationError('End index must be greater than start index')

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
