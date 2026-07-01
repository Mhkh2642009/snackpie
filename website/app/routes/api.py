from flask import Blueprint, request, jsonify
from app.services.interpreter import SnackPieRunner

api_bp = Blueprint('api', __name__)
runner = SnackPieRunner(timeout=2)


@api_bp.route('/run', methods=['POST'])
def run_code():
    """Execute SnackPie code and return output."""
    data = request.get_json()
    
    if not data or 'code' not in data:
        return jsonify({
            "success": False,
            "error": "No code provided"
        }), 400
    
    code = data['code']
    stdin_input = data.get('input', '')
    
    # Validate code length
    if len(code) > 10000:
        return jsonify({
            "success": False,
            "error": "Code too long (max 10KB)"
        }), 400
    
    if not code.strip():
        return jsonify({
            "success": True,
            "output": "",
            "error": None
        })
    
    result = runner.run(code, stdin_input)
    
    return jsonify(result)


@api_bp.route('/validate', methods=['POST'])
def validate_code():
    """Check SnackPie syntax without executing."""
    data = request.get_json()
    
    if not data or 'code' not in data:
        return jsonify({
            "valid": False,
            "errors": ["No code provided"]
        }), 400
    
    code = data['code']
    result = runner.validate(code)
    
    return jsonify(result)