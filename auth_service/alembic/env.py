from logging.config import fileConfig

from sqlalchemy import engine_from_config
from sqlalchemy import pool

from alembic import context

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
# This line sets up loggers basically.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Add your model's MetaData object here for 'autogenerate' support
from app.config.db import Base  # Make sure this is the correct location of your Base
from app.models import role,user,user_role  # Make sure these are the correct models
target_metadata = Base.metadata  # Set metadata here for autogeneration of migration

import os
from dotenv import load_dotenv
load_dotenv()
run_mode = os.getenv("RUN_MODE")

DATABASE_NAME = os.getenv(f"DATABASE_NAME_{run_mode.upper()}")
DATABASE_PASSWORD = os.getenv(f"DATABASE_PASSWORD_{run_mode.upper()}")
DATABASE_USER_NAME = os.getenv(f"DATABASE_USER_NAME_{run_mode.upper()}")
DATABASE_HOST = os.getenv(f"DATABASE_HOST_{run_mode.upper()}") 
DATABASE_PORT = os.getenv(f"DATABASE_PORT_{run_mode.upper()}") 

DATABASE_URL = f"mysql+pymysql://{DATABASE_USER_NAME}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}"
if DATABASE_URL:
    config.set_main_option("sqlalchemy.url", DATABASE_URL)


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
