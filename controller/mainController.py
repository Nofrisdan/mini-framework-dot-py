from fastapi import status,HTTPException
from fastapi.responses import JSONResponse


# helper
from helper import *

# model serializer
from model.mainModel import all_model_serializer

def main_controller():
    return all_model_serializer(response())