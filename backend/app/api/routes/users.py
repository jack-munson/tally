from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def read_root():
    return {"This is the users API endpoint"}