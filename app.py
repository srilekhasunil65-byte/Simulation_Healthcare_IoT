from flask import Flask, render_template_string
import sqlite3

app = Flask(__name__)

DB_NAME = "healthcare.db"


def get_all_patients():
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            p.patient_id,
            p.patient_name,
            p.age,
            p.gender,
            d.heart_rate,
            d.temperature,
            d.spo2,
            d.timestamp
        FROM patients p
        LEFT JOIN patient_data d
            ON p.patient_id = d.patient_id
            AND d.id = (
                SELECT MAX(id)
                FROM patient_data
                WHERE patient_id = p.patient_id
            )
        ORDER BY p.patient_id
    """)

    patients = cursor.fetchall()
    connection.close()

    return patients


HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Smart Healthcare Dashboard</title>

    <meta http-equiv="refresh" content="5">

    <style>
        body {
            font-family: Arial;
            background: #eaf4f4;
            text-align: center;
            padding: 25px;
        }

        h1 {
            color: #087e8b;
        }

        .container {
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
        }

        .card {
            background: white;
            width: 240px;
            padding: 20px;
            margin: 15px;
            border-radius: 12px;
            box-shadow: 0 3px 10px #cccccc;
        }

        .card h2 {
            color: #087e8b;
        }

        .value {
            font-size: 25px;
            font-weight: bold;
        }

        .footer {
            color: gray;
        }
    </style>
</head>

<body>

    <h1>SMART HEALTHCARE MONITORING SYSTEM</h1>
    <h3>Multiple Patient Monitoring Dashboard</h3>

    <div class="container">

    {% for p in patients %}

        <div class="card">

            <h2>{{ p[1] }}</h2>

            <p>Patient ID: P{{ "%03d"|format(p[0]) }}</p>
            <p>Age: {{ p[2] }}</p>
            <p>Gender: {{ p[3] }}</p>

            {% if p[4] is not none %}

                <p>Heart Rate</p>
                <div class="value">{{ p[4] }} BPM</div>

                <p>Temperature</p>
                <div class="value">{{ p[5] }} °C</div>

                <p>SpO2</p>
                <div class="value">{{ p[6] }} %</div>

                <p>Last Updated: {{ p[7] }}</p>

            {% else %}

                <p>Waiting for simulated readings...</p>

            {% endif %}

        </div>

    {% else %}

        <h3>No Patients Registered</h3>

    {% endfor %}

    </div>

    <p class="footer">
        Simulated Patient Data | Auto Refresh: 5 Seconds
    </p>

</body>
</html>
"""


@app.route("/")
def dashboard():
    patients = get_all_patients()

    return render_template_string(
        HTML,
        patients=patients
    )


if __name__ == "__main__":
    app.run(debug=True)