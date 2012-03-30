# _*_ coding: utf-8 _*_
CELERY_RESULT_BACKEND = "redis"

CELERY_REDIS_HOST = "localhost"
CELERY_REDIS_PORT = 6379
CELERY_REDIS_DB = 0

BROKER_URL = 'redis://localhost:6379/0'
MONGO_HOST = '127.0.0.1'
MONGO_PORT = 27017
DB_NAME = "xia"
PAGE_LIMIT = 10
DEFAULT_LIMIT = 10
DEBUG = True
#状态码
ST_CODE = {
    'norm': 0,
    'del': 1,
    'v': 2,
}
# one or more directories
MAKO_DIR = 'templates'
# optional, if specified Mako will cache to this directory
MAKO_CACHEDIR = '/tmp/mako'
# optional, if specified Mako will respect the cache size
MAKO_CACHESIZE = 500
CONTENT_TYPE_LIST = [
    "audio/midi",                     
    "audio/mpeg",                      
    "audio/ogg",                       
    "audio/x-m4a",                     
    "audio/x-realaudio",               
    "video/3gpp",                      
    "video/mp4",                       
    "video/mpeg",                      
    "video/quicktime",                 
    "video/webm",                      
    "video/x-flv",                     
    "video/x-m4v",                     
    "video/x-mng",                     
    "video/x-ms-asf",                  
    "video/x-ms-wmv",                      
    "video/x-msvideo",                     
]
