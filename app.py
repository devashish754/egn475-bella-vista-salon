
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
