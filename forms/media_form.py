from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, HiddenField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField, FileAllowed, FileRequired


class MediaAddForm(FlaskForm):
    upload = FileField('image',
                       validators=[FileRequired(), FileAllowed(['jpg', 'png', 'gif', 'mp4'], 'Допустимы только JPG, PNG, GIF, MP4')])
    title = StringField("Название", validators=[DataRequired()])
    descr = TextAreaField("Описание")
    submit = SubmitField('Отправить')


class MediaEditForm(FlaskForm):
    title = StringField("Название", validators=[DataRequired()])
    descr = TextAreaField("Описание")
    submit = SubmitField('Сохранить')


class MediaDelForm(FlaskForm):
    pic_id = HiddenField()
    submit = SubmitField('Удалить')
