# routes
from fastapi import APIRouter


# model
from model.mainModel import ADD_MODEL

# controller
from controller.mainController import *

# instance routes
main_routes = APIRouter()



# create routes
@main_routes.get("/")
async def get_all_data_main():
    return main_controller()

