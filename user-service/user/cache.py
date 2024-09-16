# cache.py
from flask_caching import Cache

# Create a Cache object
cache = Cache(config={'CACHE_TYPE': 'SimpleCache', 'CACHE_DEFAULT_TIMEOUT': 300})

def init_cache(app):
    cache.init_app(app)
