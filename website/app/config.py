import os


class Config:
    """Base configuration."""
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev-secret-change-in-production')
    MAX_CONTENT_LENGTH = 10 * 1024  # 10KB max code size
    JSON_SORT_KEYS = False
    
    # Interpreter settings
    INTERPRETER_TIMEOUT = 2  # seconds
    INTERPRETER_MAX_MEMORY = 50 * 1024 * 1024  # 50MB
    
    # Rate limiting
    RATELIMIT_DEFAULT = "30 per minute"
    RATELIMIT_STORAGE_URL = "memory://"


class DevelopmentConfig(Config):
    """Development configuration."""
    DEBUG = True
    TESTING = False


class TestingConfig(Config):
    """Testing configuration."""
    DEBUG = True
    TESTING = True
    WTF_CSRF_ENABLED = False


class ProductionConfig(Config):
    """Production configuration."""
    DEBUG = False
    TESTING = False
    
    # Use env vars in production
    SECRET_KEY = os.getenv('SECRET_KEY', Config.SECRET_KEY)
    
    # Use Redis for rate limiting in production
    RATELIMIT_STORAGE_URL = os.getenv('REDIS_URL', 'memory://')


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig,
}