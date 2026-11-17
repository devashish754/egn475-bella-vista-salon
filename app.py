
from flask import Flask, render_template, request

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

    return render_template(
        "choose_datetime.html",
        service=service
    )


@app.route("/review/<int:service_id>")
def review_booking(service_id):
    service = next(
        (s for s in services if s["id"] == service_id),
        None
    )

    if service is None:
        return "Service not found", 404

    date = request.args.get("date", "")
    time = request.args.get("time", "")

    if not date or not time:
        return "Please select a date and time", 400

    return render_template(
        "review_booking.html",
        service=service,
        date=date,
        time=time
    )


@app.route("/about")
def about():
    return "Bella Vista Salon Appointment Booking System"


if __name__ == "__main__":
    app.run(debug=True)
