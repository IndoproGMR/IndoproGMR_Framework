from .baseCrud import *

from UserCode.modelsData.modelsTable import Demo as mTDemo
from UserCode.modelsData.modelsSchemas import Demo as mSDemo


def createUser(db: Session, user: mSDemo.user_update):
    db_user = mTDemo.user_table(name=user.name, umur=user.umur)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user


def updateDiskripsiUser(db: Session, user: mSDemo.data_user_update):
    db_diskripsi = mTDemo.data_user_table(
        id_user=user.id_user, diskripsi=user.diskripsi
    )
    db.add(db_diskripsi)
    db.commit()
    db.refresh(db_diskripsi)
    return db_diskripsi


def readAllUser(db: Session, skip: int = 0, limit: int = 10):
    return db.query(mTDemo.user_table).offset(skip).limit(limit).all()


def updateUserUmur(db: Session, umur_update: int, id_user: int):
    # db.query(mTDemo.user_table).filter_by(umur>=1)
    user = (
        db.query(mTDemo.user_table)
        .with_for_update()
        .filter(mTDemo.user_table.id == id_user)
        .first()
    )

    if user:
        user.umur = umur_update
        db.commit()
        db.refresh(user)
        return user
    return None
