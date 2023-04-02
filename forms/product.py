from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, FileField
from wtforms import SubmitField, IntegerField
from wtforms.validators import DataRequired


class ProductForm(FlaskForm):
    title = StringField('Заголовок', validators=[DataRequired()])
    content = TextAreaField("Содержание")
    coast = IntegerField("Цена")
    image = FileField("Фото товара")
    submit = SubmitField('Добавить')