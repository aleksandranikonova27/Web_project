from flask_wtf import FlaskForm
from wtforms import PasswordField, SubmitField, EmailField, BooleanField, StringField, IntegerField, DateField
from wtforms.validators import DataRequired

class OrderForm(FlaskForm):
    name = StringField('Имя', validators=[DataRequired()])
    phone = StringField('Укажите номер телефона для связи с вами:', validators=[DataRequired()])
    type_of_event = StringField('Тип мероприятия:', validators=[DataRequired()])
    count_of_goest = IntegerField('Укажите количество гостей:', validators=[DataRequired()])
    need_date = DateField("Когда планируется мероприятие?", validators=[DataRequired()])
    wishes = StringField('Расскажите подробнее о своих пожеланиях:', validators=[DataRequired()])

