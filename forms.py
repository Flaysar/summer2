from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, SelectField
from wtforms.validators import DataRequired
from models import Customer, Worker, Job

class CustomerForm(FlaskForm):
    name = StringField('Имя', validators=[DataRequired()])
    phone = StringField('Телефон')
    submit = SubmitField('Отправить')

class WorkerForm(FlaskForm):
    name = StringField('Имя', validators=[DataRequired()])
    experience = IntegerField('Опыт работы (лет)', validators=[DataRequired()])
    submit = SubmitField('Отправить')

class JobForm(FlaskForm):
    description = StringField('Описание работы', validators=[DataRequired()])
    price = IntegerField('Цена', validators=[DataRequired()])
    duration = IntegerField('Длительность', validators=[DataRequired()])
    submit = SubmitField('Отправить')

class OrderForm(FlaskForm):
    description = StringField('Описание работы', validators=[DataRequired()])
    customer_id = SelectField('Клиент', coerce=int, validators=[DataRequired()])
    job_id = SelectField('Работа', coerce=int, validators=[DataRequired()])
    worker_id = SelectField('Исполнитель', coerce=int, validators=[DataRequired()])
    status = SelectField('Статус', validators=[DataRequired()])
    submit = SubmitField('Отправить')

    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        self.customer_id.choices = [(c.id, c.name) for c in Customer.query.all()]
        self.job_id.choices = [(j.id, j.description) for j in Job.query.all()]
        self.worker_id.choices = [(w.id, w.name) for w in Worker.query.all()]
        self.status.choices = ['завершен', 'в процессе', 'ожидает мастера']