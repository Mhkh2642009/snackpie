from flask import Blueprint, render_template

playground_bp = Blueprint('playground', __name__)


@playground_bp.route('/')
def index():
    """Full-screen playground with editor and output."""
    return render_template('playground.html')