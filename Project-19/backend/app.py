from flask import Flask, request, jsonify
from flask_cors import CORS
from sqlalchemy import create_engine, Column, Integer, String, Date, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# Flask app
app = Flask(__name__)
CORS(app)

# Database setup
Base = declarative_base()
engine = create_engine('sqlite:///database.db', echo=True)
Session = sessionmaker(bind=engine)
session = Session()

# Certificate model
class Certificate(Base):
    __tablename__ = "certificates"
    id = Column(Integer, primary_key=True, autoincrement=True)
    cert_id = Column(String, unique=True, nullable=False)
    student_name = Column(String)
    course = Column(String)
    year = Column(String)
    institution = Column(String)

Base.metadata.create_all(engine)

# Routes
@app.route("/")
def home():
    return jsonify({"message": "Backend running!"})

@app.route("/api/verify/by-id", methods=["GET"])
def verify_by_id():
    cert_id = request.args.get("cert_id")
    cert = session.query(Certificate).filter_by(cert_id=cert_id).first()
    if cert:
        return jsonify({
            "status": "valid",
            "checks": {
                "idCheck": True,
                "nameCheck": True,
                "institutionCheck": True
            },
            "extracted": {
                "cert_id": cert.cert_id,
                "student_name": cert.student_name,
                "course": cert.course,
                "year": cert.year,
                "institution": cert.institution
            }
        })
    else:
        return jsonify({"status": "fake", "message": "Certificate not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)
