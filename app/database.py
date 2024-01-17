from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

import os
from app.config import DevelopmentConfig, TestingConfig, ProductionConfig

env = os.getenv('FASTAPI_ENV', 'development')

if env == 'production':
    app_config = ProductionConfig()
elif env == 'testing':
    app_config = TestingConfig()
else:
    app_config = DevelopmentConfig()

engine = create_async_engine(app_config.SQLALCHEMY_DATABASE_URI, echo=True)
SessionLocal = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)
Base = declarative_base()

async def get_db():
    async with SessionLocal() as session:
        yield session