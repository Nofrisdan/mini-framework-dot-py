import os
import argparse
import subprocess

# error message
INVALID_FILE_IS_EXIST = "Error: File %s is exist"
INVALID_FILE_IS_NOT_EXIST = "Error: File %s is not exist"

# validate_file
def validate_file(file_name, check = False):

    if check == False:
        if validate_path(file_name):

            print(INVALID_FILE_IS_EXIST%(file_name))
            quit()
    else: 
          if not validate_path(file_name):
            print(INVALID_FILE_IS_NOT_EXIST%(file_name))
            quit()
    return



# validate path
def validate_path(file_name, check = False):
    projectPath = os.getcwd()

    if check == False:
        for root,dirs, files in os.walk(projectPath):
            if 'venv' not in root:
                if file_name in files:
                    return True # file is exist
    else :
        for root,dirs, files in os.walk(projectPath):
            if 'venv' not in root:
                if file_name in files:
                    return False # file is not exist


# make 
def make(args):

    # validate
    controllerFile = args.make[0] +"Controller.py"
    routesFile = args.make[0] +"Routes.py"
    modelFile = args.make[0] +"Model.py"

    validate_file(controllerFile)
    validate_file(routesFile)
    validate_file(modelFile)


    # makemodel
    make_model(args)
    # makecontroller
    make_controller(args)
    # makeroutes
    make_routes(args)
    # add routes to main
    make_main(args)
    

    # print result 
    print("Controller, Model, And Routes has been created")


# remove file
def remove_file(args):

    # validate file
    controllerFile = args.remove[0] +"Controller.py"
    routesFile = args.remove[0] +"Routes.py"
    modelFile = args.remove[0] +"Model.py"

    validate_file(controllerFile,True)
    validate_file(routesFile, True)
    validate_file(modelFile, True)

    # removing file
    os.unlink(os.getcwd()+"/controller/"+controllerFile)
    os.unlink(os.getcwd()+"/routes/"+routesFile)
    os.unlink(os.getcwd()+"/model/"+modelFile)

    # remove script in main
    routes_name = args.remove[0]
    script = 'app.include_router(main_routes,tags=["%s ROUTES"],prefix=END_POINT+"%s")'%(routes_name.upper(),"/"+routes_name)
    with open('main.py','r') as file:
        lines = file.readlines()
    lines = [line for line in lines if line.strip() != script]
    with open('main.py','w') as file:
        file.writelines(lines)


    print("File Controller, Model, and Routes Has Been Removed")
    


# running project
def running_serve():
    subprocess.run(['uvicorn','main:app','--reload'])


# make controller
def make_controller(args):
      controllerFile = args.make[0] +"Controller.py"
      folder_project = os.getcwd()
      controller_path = folder_project+"/controller/"+controllerFile
      
      with open(controller_path,'w') as file:

        controller_code = """
from fastapi import status,HTTPException
from fastapi.responses import JSONResponse
# helper
from helper import *

# model serializer
from model.%sModel import all_model_serializer

def %s_controller():
    return all_model_serializer(response())
    """ % (args.make[0],args.make[0])
        
        file.write(controller_code)
        return True
      
# make routes
def make_routes(args):
      controllerFile = args.make[0] +"Routes.py"
      folder_project = os.getcwd()
      routes_path = folder_project+"/routes/"+controllerFile
      
      with open(routes_path,'w') as file:

        controller_code = """
# routes
from fastapi import APIRouter


# model
from model.%sModel import ADD_MODEL

# controller
from controller.%sController import *

# instance routes
%s_routes = APIRouter()



# create routes
@%s_routes.get("/")
async def get_all_data_main():
    return main_controller()


    """ % (args.make[0],args.make[0],args.make[0],args.make[0])
        
        file.write(controller_code)
        return True


# make model
def make_model(args):
      controllerFile = args.make[0] +"Model.py"
      folder_project = os.getcwd()
      model_path = folder_project+"/model/"+controllerFile
      
      with open(model_path,'w') as file:

        model_code = """
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
    """
        file.write(model_code)
        return True

# make main
def make_main(args):
    routes_name = args.make[0]
    script = '\napp.include_router(main_routes,tags=["%s ROUTES"],prefix=END_POINT+"%s")\n'%(routes_name.upper(),"/"+routes_name)
    with open("main.py","a") as file:
        file.write(script)

# main
def main():

    # banner
    parser = argparse.ArgumentParser(description="Miniframework Dot Py")


    # adding parser arguments
    parser.add_argument("-m","--make",type=str,nargs=1,metavar="make",default=None,help="Make Controller")
    parser.add_argument("-r","--remove",type=str,nargs=1,metavar="remove", default=None,help="Remove File Controller, Model and routes")
    parser.add_argument("-s","--serve",type=str,nargs="?",metavar="serve", default=None,help="Running server")
    

    # parser the arguments
    args = parser.parse_args()


    # calling arguments
    if args.make != None:
        make(args)
    elif args.remove != None:
        remove_file(args)
    elif args.serve != None:
        running_serve()



if __name__ == "__main__":
    main()