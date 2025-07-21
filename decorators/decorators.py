# decorators

import logging
import pickle
import hashlib
import time
from functools import wraps
from datetime import datetime, timedelta
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError
import redis
import os
from models.db import SessionLocal # type: ignore

#-------------------------------------------------------

if not os.path.exists("logs"):
    os.makedirs("logs")
logger = logging.getLogger("maintenance_logger")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler("logs/errors.log")
file_handler.setLevel(logging.ERROR)
formatter = logging.Formatter('[%(asctime)s] [%(levelname)s] %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

#-------------------------------------------------------

redis_client = redis.Redis(host='localhost', port=6379, db=0)

#-------------------------------------------------------

def use_session(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        session = SessionLocal()
        try:
            return func(session, *args, **kwargs)
        finally:
            session.close()
    return wrapper

#-------------------------------------------------------

def cache_query(timeout=300):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:

                key_raw = f"{func.__name__}:{args}:{kwargs}"
                
                key = hashlib.sha256(key_raw.encode()).hexdigest()
                

                
                cached_result = redis_client.get(key)
            
                if cached_result is not None:
                    return pickle.loads(cached_result)
            
                result = func(*args, **kwargs)
            
                redis_client.setex(key, timeout, pickle.dumps(result))

                return result
            except Exception as e:
                print(f"[Cache Error] {e}")
                return func(*args, **kwargs)
            
        
        return wrapper
    return decorator

#-----------------------------------------------------

def handle_exceptions(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except SQLAlchemyError as e:
            logger.error(f"Database error in {func.__name__}:{str(e)}", exc_info=True)
            return None
        except Exception as e:
            logger.error(f"Understand error in {func.__name__}:{str(e)}", exc_info=True)
            return None
    return wrapper