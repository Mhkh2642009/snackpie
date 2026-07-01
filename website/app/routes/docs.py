from flask import Blueprint, render_template

docs_bp = Blueprint('docs', __name__)


@docs_bp.route('/')
def index():
    """Documentation hub."""
    return render_template('docs/index.html')


@docs_bp.route('/tutorial')
def tutorial():
    """Step-by-step guided lessons."""
    return render_template('docs/tutorial.html')


@docs_bp.route('/reference')
def reference():
    """Complete language reference."""
    return render_template('docs/reference.html')


@docs_bp.route('/cookbook')
def cookbook():
    """Common patterns and recipes."""
    return render_template('docs/cookbook.html')