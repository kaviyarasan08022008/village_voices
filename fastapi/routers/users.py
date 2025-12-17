from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from dependencies import connect_to_db
from schemas.users import UserCreate, UserResponse 
from models.users import User


router = APIRouter(
    prefix="/users",
    tags=["users"]
)

@router.get("/")
def get_all_users(dbs: Session = Depends(connect_to_db)):
    return dbs.query(User).all()

@router.post("/")
def create_user(user: UserCreate, db: Session = Depends(connect_to_db)):

    new_user = User(
        first_name = user.first_name,
        last_name = user.last_name,
        email = user. email,
        user_name = user. user_name,
        password = user. password,
        state = user. state,
        district = user. district,
        village_town = user. village_town,
        user_role = user. user_role
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.get("/{user_id}")
def read_user(user_id: int, db: Session = Depends(connect_to_db)):
    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return user

@router.put("/{user_id}")
def update_user(
    user_id: int,
    updated_data: UserCreate,
    db: Session = Depends(connect_to_db)
):
    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    for key, value in updated_data.dict().items():
        setattr(user, key, value)

    db.commit()
    db.refresh(user)
    return user

@router.delete("/{user_id}")
def delete_user(user_id: int, db: Session = Depends(connect_to_db)):
    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    db.delete(user)
    db.commit()
    return {"detail": "User deleted successfully"}