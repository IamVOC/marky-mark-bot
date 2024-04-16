from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from app.config import get_settings


settings = get_settings()
engine = create_async_engine(settings.DB_URL)
async_session = async_sessionmaker(engine)
