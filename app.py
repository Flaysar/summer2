from flask import Flask, render_template, redirect, url_for, flash, request
from config import Config
from forms import CustomerForm, WorkerForm, JobForm, OrderForm
from models import db, Customer, Worker, Job, Order

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template('index.html')

# Routes for customers
@app.route('/customers')
def view_customers():
    customers = Customer.query.all()
    return render_template('customers.html', customers=customers)

@app.route('/customer/add', methods=['GET', 'POST'])
def add_customer():
    form = CustomerForm()
    if form.validate_on_submit():
        customer = Customer(name=form.name.data, phone=form.phone.data)
        db.session.add(customer)
        db.session.commit()
        flash('Клиент добавлен успешно!')
        return redirect(url_for('view_customers'))
    return render_template('edit_customer.html', form=form)

@app.route('/customer/edit/<int:id>', methods=['GET', 'POST'])
def edit_customer(id):
    customer = Customer.query.get_or_404(id)
    form = CustomerForm(obj=customer)
    if form.validate_on_submit():
        customer.name = form.name.data
        customer.phone = form.phone.data
        db.session.commit()
        flash('Клиент обновлен успешно!')
        return redirect(url_for('view_customers'))
    return render_template('edit_customer.html', form=form)

@app.route('/customer/delete/<int:id>', methods=['POST'])
def delete_customer(id):
    customer = Customer.query.get_or_404(id)
    db.session.delete(customer)
    db.session.commit()
    flash('Клиент удален успешно!')
    return redirect(url_for('view_customers'))

# Routes for workers
@app.route('/workers')
def view_workers():
    workers = Worker.query.all()
    return render_template('workers.html', workers=workers)

@app.route('/worker/add', methods=['GET', 'POST'])
def add_worker():
    form = WorkerForm()
    if form.validate_on_submit():
        worker = Worker(name=form.name.data, experience=form.experience.data)
        db.session.add(worker)
        db.session.commit()
        flash('Работник добавлен успешно!')
        return redirect(url_for('view_workers'))
    return render_template('edit_worker.html', form=form)

@app.route('/worker/edit/<int:id>', methods=['GET', 'POST'])
def edit_worker(id):
    worker = Worker.query.get_or_404(id)
    form = WorkerForm(obj=worker)
    if form.validate_on_submit():
        worker.name = form.name.data
        worker.experience = form.experience.data
        db.session.commit()
        flash('Работник обновлен успешно!')
        return redirect(url_for('view_workers'))
    return render_template('edit_worker.html', form=form)

@app.route('/worker/delete/<int:id>', methods=['POST'])
def delete_worker(id):
    worker = Worker.query.get_or_404(id)
    db.session.delete(worker)
    db.session.commit()
    flash('Работник удален успешно!')
    return redirect(url_for('view_workers'))

# Routes for jobs
@app.route('/jobs')
def view_jobs():
    jobs = Job.query.all()
    return render_template('jobs.html', jobs=jobs)

@app.route('/job/add', methods=['GET', 'POST'])
def add_job():
    form = JobForm()
    if form.validate_on_submit():
        job = Job(description=form.description.data, price=form.price.data, duration=form.duration.data)
        db.session.add(job)
        db.session.commit()
        flash('Работа добавлена успешно!')
        return redirect(url_for('view_jobs'))
    return render_template('edit_job.html', form=form)

@app.route('/job/edit/<int:id>', methods=['GET', 'POST'])
def edit_job(id):
    job = Job.query.get_or_404(id)
    form = JobForm(obj=job)
    if form.validate_on_submit():
        job.description = form.description.data
        job.price = form.price.data
        job.duration = form.duration.data
        db.session.commit()
        flash('Работа обновлена успешно!')
        return redirect(url_for('view_jobs'))
    return render_template('edit_job.html', form=form)

@app.route('/job/delete/<int:id>', methods=['POST'])
def delete_job(id):
    job = Job.query.get_or_404(id)
    db.session.delete(job)
    db.session.commit()
    flash('Работа удалена успешно!')
    return redirect(url_for('view_jobs'))

# Routes for orders
@app.route('/orders')
def view_orders():
    orders = Order.query.all()
    return render_template('orders.html', orders=orders)

@app.route('/order/add', methods=['GET', 'POST'])
def add_order():
    form = OrderForm()
    if form.validate_on_submit():
        order = Order(description = form.description.data, customer_id=form.customer_id.data,
                      worker_id=form.worker_id.data, job_id=form.job_id.data, status = form.status.data)
        db.session.add(order)
        db.session.commit()
        flash('Заказ добавлен успешно!')
        return redirect(url_for('view_orders'))
    return render_template('edit_order.html', form=form)

@app.route('/order/edit/<int:id>', methods=['GET', 'POST'])
def edit_order(id):
    order = Order.query.get_or_404(id)
    form = OrderForm(obj=order)
    if form.validate_on_submit():
        order.customer_id = form.customer_id.data
        order.worker_id = form.worker_id.data
        order.job_id = form.job_id.data
        order.status = form.status.data
        db.session.commit()
        flash('Заказ обновлен успешно!')
        return redirect(url_for('view_orders'))
    return render_template('edit_order.html', form=form)

@app.route('/order/delete/<int:id>', methods=['POST'])
def delete_order(id):
    order = Order.query.get_or_404(id)
    db.session.delete(order)
    db.session.commit()
    flash('Заказ удален успешно!')
    return redirect(url_for('view_orders'))

if __name__ == '__main__':
    app.run(debug=True)