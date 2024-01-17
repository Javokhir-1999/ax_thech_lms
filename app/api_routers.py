from fastapi import APIRouter
from app.controllers import book_controller, author_controller, user_controller, member_controller
from app.controllers.gb_api import gb_search_controller 

router = APIRouter()

# app api
router.include_router(book_controller.router, prefix="/books", tags=["books"])
router.include_router(author_controller.router, prefix="/authors", tags=["authors"])
router.include_router(user_controller.router, prefix="/users", tags=["users"])
router.include_router(member_controller.router, prefix="/members", tags=["members"])

# gb api
router.include_router(gb_search_controller.router, prefix="/gb", tags=["gb"])
