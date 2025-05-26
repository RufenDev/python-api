import os
import importlib
from fastapi import APIRouter

router = APIRouter()

# Current path
api_dir = os.path.dirname(__file__)

# Function to import all possible routes that may 
# exist within a package (and its internal packages)
def import_all_routes(dirpath: str, filenames: str):
    for filename in filenames:
        if filename.endswith(".py") and filename != "__init__.py":
            file_path = os.path.relpath(dirpath, filename)[3:]
            module_path = f"{file_path.replace(os.sep, ".")}.{filename[:-3]}"
            module = importlib.import_module(module_path)
            
            if hasattr(module, "router"):
                router.include_router(module.router)

# Import all routes insidethe `/endpoints` package
endpoints_dir = os.path.join(api_dir, 'endpoints')
for dirpath, _, filenames in os.walk(endpoints_dir):
    import_all_routes(dirpath, filenames)
