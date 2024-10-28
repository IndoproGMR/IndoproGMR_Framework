from fastapi import Depends
from .baseRouter import *


from sqlalchemy.orm import Session


from UserCode.modelsData.modelsCRUD import Demo as crudDemo
from UserCode.modelsData.modelsTable import Demo as mTDemo
from UserCode.modelsData.modelsSchemas import Demo as mSDemo


# membuat table pada sql
mTDemo.Base.metadata.create_all(bind=engine)

# !set dependencies global
# ?from APP.dependencies.dependencies import get_token_request
router = APIRouter(
    prefix="/sql",
    tags=["demoSQL"],
    # ?dependencies=[Depends(get_token_request)],
)


@router.post("/user/create", response_model=mSDemo.user)
async def createUser(user: mSDemo.user_update, db: Session = Depends(get_db)):
    return crudDemo.createUser(db=db, user=user)


@router.get("/user/get", response_model=list[mSDemo.user])
async def method_name(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    user = crudDemo.readAllUser(db, skip=skip, limit=limit)
    return user


@router.get("/umur/update", response_model=mSDemo.user)
async def umur_update(user_id: int, umur: int, db: Session = Depends(get_db)):

    data = crudDemo.updateUserUmur(db, umur, user_id)
    if data:
        return data

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="user not found")
