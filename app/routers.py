from fastapi import APIRouter


router = APIRouter()


@router.get("/")
async def first_view():
    return {"message": "TeSt"}
