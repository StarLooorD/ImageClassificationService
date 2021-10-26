from fastapi import status, APIRouter

api_router = APIRouter(prefix="/health", tags=["Health"])


@api_router.get("", status_code=status.HTTP_200_OK)
def check_health():
    return {"message": "ImageClassification API launched!"}
