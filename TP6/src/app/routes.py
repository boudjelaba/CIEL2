from flask import Blueprint, jsonify, request
from .models import db, Student

student_bp = Blueprint("student_bp", __name__, url_prefix="/students")

@student_bp.route("/", methods=["GET"])
def list_students():
    students = Student.query.all()
    result = [
        {"id": s.id, "name": s.name, "email": s.email}
        for s in students
    ]
    return jsonify(result)

@student_bp.route("/", methods=["POST"])
def add_student():
    data = request.get_json()

    if not data or not data.get("name") or not data.get("email"):
        return jsonify({"error": "Invalid data"}), 400

    student = Student(name=data["name"], email=data["email"])
    db.session.add(student)
    db.session.commit()

    return jsonify({"message": "Student added"}), 201