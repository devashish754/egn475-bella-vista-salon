
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to Bella Vista Salon"

@app.route("/about")
def about():
    return "Bella Vista Salon Appointment Booking System"

if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, render_template

app = Flask(__name__)

services = [
    {"id": 1, "name": "Haircut", "duration": 30, "price": 25},
    {"id": 2, "name": "Hair Coloring", "duration": 90, "price": 80},
    {"id": 3, "name": "Hair Styling", "duration": 45, "price": 40},
    {"id": 4, "name": "Facial", "duration": 60, "price": 55}
]

@app.route("/")
def home():
    return render_template("services.html", services=services)

@app.route("/services")
def show_services():
    return render_template("services.html", services=services)

@app.route("/book/<int:service_id>")
def choose_datetime(service_id):
    service = next(
        (s for s in services if s["id"] == service_id),
        None
    )

    if service is None:
        return "Service not found", 404

    return f"Choose a date and time for {service['name']}"

@app.route("/about")
def about():
    return "Bella Vista Salon Appointment Booking System"

if __name__ == "__main__":
    app.run(debug=True)
