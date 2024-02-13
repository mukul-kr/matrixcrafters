
from fastapi.middleware.cors import CORSMiddleware
import logging
from src.data_structure.hash_map_tree import HashMapTree
from src.db.db import CustomDatabase
from src.helper.utils import check_if_key_exists, convert_data_to_string, convert_string_to_data, find_the_line_number_of_id
from fastapi import FastAPI
from src.routes import router as routes_router

logging.basicConfig(encoding='utf-8', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


app = FastAPI()

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(routes_router, prefix="/routes", tags=["routes"])

