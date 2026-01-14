from flask import Blueprint, request, jsonify
from services.llm import analyze_clause

chat_bp = Blueprint("chat_bp", __name__)

@chat_bp.route("/chat", methods=["POST"])
def chat():
    data = request.json
    clause = data.get("clause")
    question = data.get("question")

    reply = analyze_clause(clause, question)
    return jsonify({"reply": reply})
