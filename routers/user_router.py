from fastapi import Request, Response, APIRouter, status
from schemas.userSchema.user import SignUpModel
from models.users.user import User

userRouter = APIRouter(prefix="/user", tags=["user"])

@userRouter.get('/me')
async def user_me(request: Request):
    return {"message": "User me"}


@userRouter.post('/sign-up', status_code=status.HTTP_201_CREATED)
async def sign_up(user: SignUpModel):
    print("User sign up", user)
    await User.create(**user.model_dump())
    return {"message": "Sign up"}

