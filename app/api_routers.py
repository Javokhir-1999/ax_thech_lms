from fastapi import APIRouter
from app.controllers import book_controller, author_controller

router = APIRouter()

router.include_router(book_controller.router, prefix="/books", tags=["books"])
router.include_router(author_controller.router, prefix="/authors", tags=["authors"])
