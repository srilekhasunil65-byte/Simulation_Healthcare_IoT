import asyncio
import json
import sqlite3

from aiocoap import Context, Message, Code
from aiocoap import resource


DB_NAME = "healthcare.db"


def get_latest_patient_data():
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            p.patient_id,
            p.patient_name,
            d.heart_rate,
            d.temperature,
            d.spo2,
            d.timestamp
        FROM patient_data d
        LEFT JOIN patients p
            ON p.patient_id = CAST(
                SUBSTR(CAST(d.patient_id AS TEXT), 2) AS INTEGER
            )
        ORDER BY d.id DESC
        LIMIT 1
    """)

    row = cursor.fetchone()
    connection.close()

    if row is None:
        return {
            "message": "No patient data available"
        }

    return {
        "patient_id": row[0],
        "patient_name": row[1],
        "heart_rate": row[2],
        "temperature": row[3],
        "spo2": row[4],
        "timestamp": row[5],
        "data_type": "Simulated Patient Data"
    }


class PatientResource(resource.Resource):

    async def render_get(self, request):

        patient_data = get_latest_patient_data()

        return Message(
            code=Code.CONTENT,
            payload=json.dumps(
                patient_data,
                indent=4
            ).encode("utf-8")
        )


async def main():

    root = resource.Site()

    root.add_resource(
        ["patient", "vitals"],
        PatientResource()
    )

    await Context.create_server_context(
        root,
        bind=("127.0.0.1", 5683)
    )

    print("CoAP Server Started Successfully!")
    print("SQLite Database Connected!")
    print("Server: coap://127.0.0.1:5683/patient/vitals")

    await asyncio.get_running_loop().create_future()


if __name__ == "__main__":

    try:
        asyncio.run(main())

    except KeyboardInterrupt:
        print("CoAP Server Stopped.")