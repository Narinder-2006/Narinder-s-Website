
from flask import Flask,render_template


app = Flask(__name__)

students = [
        {"name": "Aryan Sharma", "rank": 512, "university": "IIT Bombay", "batch": "2023"},
        {"name": "Neha Verma", "rank": 1203, "university": "IIT Delhi", "batch": "2022"},
        {"name": "Rohit Mehta", "rank": 2345, "university": "NIT Trichy", "batch": "2023"},
        {"name": "Simran Kaur", "rank": 3421, "university": "BITS Pilani", "batch": "2021"},
        {"name": "Aditya Singh", "rank": 4532, "university": "IIIT Hyderabad", "batch": "2024"}
    ]


@app.route('/')
def home():
    return render_template("file.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)
