from flask import Blueprint, request, jsonify
from services.llm import compare_clauses

compare_bp = Blueprint("compare_bp", __name__)

@compare_bp.route("/compare", methods=["POST"])
def compare():
    data = request.json
    a = data.get("clauseA")
    b = data.get("clauseB")

    result = compare_clauses(a, b)
    return jsonify({"result": result})
