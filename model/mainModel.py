from pydantic import BaseModel


# create model
class ADD_MODEL:
    say:str


# model_serializer
def model_serializer(data):
    return {
        "say":data['say']
    }


def all_model_serializer(alldata):
    return [model_serializer(data) for data in alldata]