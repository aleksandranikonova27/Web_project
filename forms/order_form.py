from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, DateField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length, Regexp


class OrderForm(FlaskForm):
    name = StringField('Имя', validators=[DataRequired()])
    phone = StringField('Укажите номер телефона для связи с вами:',
                             validators=[DataRequired(), Length(min=10, max=10), Regexp(regex='^[+-]?[0-9]$')])
    type_of_event = StringField('Тип мероприятия:', validators=[DataRequired()])
    count_of_goest = IntegerField('Укажите количество гостей:', validators=[DataRequired()])
    need_date = DateField("Когда планируется мероприятие?", validators=[DataRequired()])
    wishes = TextAreaField('Расскажите подробнее о своих пожеланиях:', validators=[DataRequired()])
    submit = SubmitField('Отправить заявку')