from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, FloatField, DateField, IntegerField, BooleanField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired


class JobForm(FlaskForm):
    job = StringField("Job Title", validators=[DataRequired()])
    team_leader = IntegerField("Team Leader Id", validators=[DataRequired()])
    work_size = FloatField("Work Size", validators=[DataRequired()])
    collaborators = StringField("Collaborators", validators=[DataRequired()])
    # start_date = DateField("Начало")
    # end_date = DateField("Окончание")
    is_finished = BooleanField("Is job finished?")
    submit = SubmitField("Submit")
