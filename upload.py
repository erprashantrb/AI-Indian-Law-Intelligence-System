from flask import Blueprint, request, jsonify
import os
from utils.pdf_reader import read_pdf
from services.llm import extract_clauses

upload_bp = Blueprint("upload_bp", __name__)


@upload_bp.route("/upload", methods=["POST"])
def upload():
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["file"]
    filename = file.filename

    path = f"backend/uploads/{filename}"
    file.save(path)

    text = read_pdf(path)
    clauses = extract_clauses(text)

    return jsonify({
        "status": "success",
        "filename": filename,
        "clauses": clauses
    })
