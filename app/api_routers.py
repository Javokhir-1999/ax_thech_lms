from fastapi import APIRouter
from app.controllers import book_controller, author_controller, user_controller

router = APIRouter()

router.include_router(book_controller.router, prefix="/books", tags=["books"])
router.include_router(author_controller.router, prefix="/authors", tags=["authors"])
router.include_router(user_controller.router, prefix="/users", tags=["users"])
