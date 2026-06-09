from logging.config import fileConfig
import os
from dotenv import load_dotenv

# Load .env manually for Alembic
load_dotenv(os.path.join(os.path.dirname(os.path.dirname(__file__)), ".env"))

from sqlalchemy import pool
from sqlalchemy.ext.asyncio import create_async_engine
from alembic import context
from app.core.config import settings
from app.db.base import Base


config = context.config

if config.config_file_name is not None:
    fileConfig(config.config_file_name)

target_metadata = Base.metadata


def get_url():
    return settings.DATABASE_URL

print("ALEMBIC USING URL:", get_url())

def run_migrations_offline():
    context.configure(
        url=get_url(),
        target_metadata=target_metadata,
        literal_binds=True,
        compare_type=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    connectable = create_async_engine(
        get_url(),
        poolclass=pool.NullPool,
    )

    async def do_migrations():
        async with connectable.connect() as connection:
            await connection.run_sync(do_run_migrations)

    def do_run_migrations(connection):
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            compare_type=True,
        )
        with context.begin_transaction():
            context.run_migrations()

    import asyncio
    asyncio.run(do_migrations())

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
