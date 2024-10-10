import asyncio

from sqlalchemy import create_engine, engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from APP.config.log import LogProses
from APP.config.manager import filemanager
from APP.config.dotenvfile import GetEnv

fileProses = filemanager.create("")

if GetEnv("database_type").str() == "sqlite":
    lokasi = GetEnv("database_sqlite_path", "SpecialDir/SQLitedb").str()
    lokasiSQLite = f"./{lokasi}/"

    try:
        asyncio.create_task(fileProses.SaveFolder(lokasi))

    except Exception as e:
        LogProses(f"gagal membuat lokasiSQLite di {lokasiSQLite}: {e}")
        raise

    try:
        SQLALCHEMY_DATABASE_URL = f"sqlite:///{lokasiSQLite}{GetEnv('database_name','SQLite_Database').str()}.db"

        engine = create_engine(
            SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
        )
    except Exception as e:
        LogProses(f"gagal membuat sqlite database: {e}")
        raise


else:

    if GetEnv("Plugin_Docker", "False").str() != "True":
        link_url = f"{GetEnv('database_type').str()}://{GetEnv('database_user').str()}:{GetEnv('database_password').str()}@{GetEnv('database_host').str()}/{GetEnv('database_name').str()}"

        SQLALCHEMY_DATABASE_URL = GetEnv("database_URL", link_url).str()

    else:
        link_url = f"mysql+pymysql://dockerRoot:dockerRoot@mysql:3307/dockerRootDB"

        SQLALCHEMY_DATABASE_URL = link_url

    try:
        # SQLALCHEMY_DATABASE_URL = link_url
        engine = create_engine(SQLALCHEMY_DATABASE_URL)
    except Exception as e:
        LogProses(f"gagal membuat database engine {link_url}: {e}")
        raise


# engine
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
