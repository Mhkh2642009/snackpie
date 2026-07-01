import os
from flask import Flask


def create_app(config_name=None):
    """Application factory pattern."""
    app = Flask(__name__, 
                template_folder='templates',
                static_folder='static')
    
    # Configuration
    config_name = config_name or os.getenv('FLASK_ENV', 'development')
    
    if config_name == 'production':
        app.config.from_object('app.config.ProductionConfig')
    elif config_name == 'testing':
        app.config.from_object('app.config.TestingConfig')
    else:
        app.config.from_object('app.config.DevelopmentConfig')
    
    # Ensure instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    
    # Register blueprints
    from app.routes.main import main_bp
    from app.routes.api import api_bp
    from app.routes.playground import playground_bp
    from app.routes.docs import docs_bp
    from app.routes.examples import examples_bp
    
    app.register_blueprint(main_bp)
    app.register_blueprint(api_bp, url_prefix='/api')
    app.register_blueprint(playground_bp, url_prefix='/playground')
    app.register_blueprint(docs_bp, url_prefix='/docs')
    app.register_blueprint(examples_bp, url_prefix='/examples')
    
    # Error handlers
    @app.errorhandler(404)
    def not_found(e):
        from flask import render_template
        return render_template('errors/404.html'), 404
    
    @app.errorhandler(500)
    def server_error(e):
        from flask import render_template
        return render_template('errors/500.html'), 500
    
    # Context processors
    @app.context_processor
    def inject_global_vars():
        return {
            'site_name': 'SnackPie',
            'site_tagline': 'The Easiest Programming Language for Kid Chefs! 🥧',
        }
    
    return app