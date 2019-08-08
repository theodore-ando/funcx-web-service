from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, TextAreaField
from wtforms.validators import DataRequired, Length

class EditForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=1, max=20)])
    desc = TextAreaField('Description', validators=[Length(min=0, max=500)])
    # language = SelectField('Language', choices=[('Python 3', 'python')], validators=[DataRequired()])
    entry_point = StringField('Entry Point', validators=[DataRequired()])
    code = TextAreaField('Code')
    submit = SubmitField('Save')

class ExecuteForm(FlaskForm):
    name = StringField('Task Name', validators=[DataRequired(), Length(min=1, max=20)])
    endpoint = SelectField('Endpoint', choices=[('endpoint 1', 'Endpoint 1'), ('endpoint 2', 'Endpoint 2')], validators=[DataRequired()])
    payload = TextAreaField('Payload', validators=[DataRequired()])
    submit = SubmitField('Run')

class DeleteForm(FlaskForm):
    delete = SubmitField('Delete')