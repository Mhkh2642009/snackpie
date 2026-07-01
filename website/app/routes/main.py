from flask import Blueprint, render_template

main_bp = Blueprint('main', __name__)


@main_bp.route('/')
def index():
    """Homepage with hero, features, quick start, CTA."""
    return render_template('index.html')


@main_bp.route('/download')
def download():
    """Download/install instructions."""
    return render_template('download.html')