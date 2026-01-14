from flask import Flask, render_template
from flask_cors import CORS

from api.upload import upload_bp
from api.chat import chat_bp
from api.compare import compare_bp


def create_app():
    app = Flask(
        __name__,
        template_folder="templates",
        static_folder="static"
    )

    CORS(app)

    # API routes
    app.register_blueprint(upload_bp, url_prefix="/api")
    app.register_blueprint(chat_bp, url_prefix="/api")
    app.register_blueprint(compare_bp, url_prefix="/api")

    # Frontend routes
    @app.route("/")
    @app.route("/dashboard")
    def dashboard():
        return render_template("dashboard.html", title="Dashboard")

    @app.route("/upload")
    def upload_page():
        return render_template("upload.html", title="Upload Document")

    @app.route("/chat")
    def chat_page():
        return render_template("chat.html", title="AI Chat")

    @app.route("/compare")
    def compare_page():
        return render_template("compare.html", title="Compare Clauses")

    return app


app = create_app()

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False, port=5000)
