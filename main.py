
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class Property(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(255), nullable=False)

@app.route('/')
def index():
    properties = Property.query.all()
    return render_template('index.html', properties=properties)

@app.route('/owner/login', methods=['GET', 'POST'])
def owner_login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username, password=password).first()
        if user and user.role == 'owner':
            return redirect(url_for('owner_dashboard'))
        else:
            flash('Invalid credentials')
    return render_template('owner_login.html')

@app.route('/owner/properties')
def owner_dashboard():
    properties = Property.query.filter_by(owner_id=current_user.id).all()
    return render_template('owner_dashboard.html', properties=properties)

@app.route('/properties/<property_id>')
def property_details(property_id):
    property = Property.query.get(property_id)
    return render_template('property_details.html', property=property)

@app.route('/user/login', methods=['GET', 'POST'])
def user_login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username, password=password).first()
        if user and user.role == 'user':
            return redirect(url_for('user_dashboard'))
        else:
            flash('Invalid credentials')
    return render_template('user_login.html')

@app.route('/user/dashboard')
def user_dashboard():
    bookings = Booking.query.filter_by(user_id=current_user.id).all()
    return render_template('user_dashboard.html', bookings=bookings)

@app.route('/bookings', methods=['GET', 'POST'])
def booking_management():
    if request.method == 'POST':
        property_id = request.form['property_id']
        start_date = request.form['start_date']
        end_date = request.form['end_date']
        booking = Booking(property_id=property_id, user_id=current_user.id, start_date=start_date, end_date=end_date)
        db.session.add(booking)
        db.session.commit()
        flash('Booking successful')
        return redirect(url_for('user_dashboard'))
    return render_template('booking_management.html')

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
