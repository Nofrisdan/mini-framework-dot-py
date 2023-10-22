import os
from dotenv import load_dotenv
from fastapi import FastAPI

app = FastAPI()
load_dotenv()


# instance routes
from routes.mainRoutes import main_routes

# END POINT
END_POINT = os.getenv("END_POINT")

# run all routes
app.include_router(main_routes,tags=["MAIN ROUTES"],prefix=END_POINT)


