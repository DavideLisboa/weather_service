from flask import Flask, request, jsonify
import random
import string
from datetime import datetime
from sqlalchemy.orm import Session
from .models import SessionLocal, WeatherData

app = Flask(__name__)


@app.route('/weather', methods=['POST'])
def collect_weather_data():
    data = request.get_json()

    user_defined_id = data.get('user_defined_id')
    if not user_defined_id:
        return jsonify({"message": "User defined ID is required"}), 400

    city_ids = data.get('city_ids')
    if not city_ids:
        return jsonify({"message": "City IDs are required"}), 400

    session = SessionLocal()
    try:
        for city_id in city_ids:
            temperature = random.uniform(20, 30)
            humidity = random.randint(50, 90)

            weather_data = WeatherData(
                user_defined_id=user_defined_id,
                city_id=city_id,
                temperature=temperature,
                humidity=humidity,
                datetime=datetime.now()
            )
            session.add(weather_data)

        session.commit()  # Commit changes to the database
        return jsonify({"message": "Data collected successfully"}), 201

    except Exception as e:
        session.rollback()  # Rollback changes on exception
        return jsonify({"message": str(e)}), 500

    finally:
        session.close()  # Always close the session


@app.route('/weather/<user_defined_id>', methods=['GET'])
def get_weather_progress(user_defined_id):
    session = SessionLocal()
    try:
        # Count the number of records for the given user_defined_id
        total_records = session.query(WeatherData).filter_by(
            user_defined_id=user_defined_id).count()
        return jsonify({"progress": total_records}), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500
    finally:
        session.close()


if __name__ == '__main__':
    app.run(debug=True)
