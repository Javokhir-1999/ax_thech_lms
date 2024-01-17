import os

class Config:
    """Base configuration class (default configuration settings)."""
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://postgres:postgres1999@localhost:5432/lms_dev')

class DevelopmentConfig(Config):
    """Development configuration class."""
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.getenv('DEV_DATABASE_URL', 'postgresql://postgres:postgres1999@localhost:5432/lms_dev')

class TestingConfig(Config):
    """Testing configuration class."""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.getenv('TEST_DATABASE_URL', 'postgresql://postgres:postgres1999@localhost:5432/lms_test')

class ProductionConfig(Config):
    """Production configuration class."""
    SQLALCHEMY_DATABASE_URI = os.getenv('PROD_DATABASE_URL', 'postgresql://postgres:postgres1999@localhost:5432/lms_prod')
