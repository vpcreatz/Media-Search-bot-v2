import re
from os import environ

id_pattern = re.compile(r'^.\d+$')

# Bot information
SESSION = environ.get('SESSION', 'Media_search')
API_ID = int(environ['20960397'])
API_HASH = environ['d68d847d3abb2087bf74f5d0683c2993']
BOT_TOKEN = environ['5880821820:AAGzh_tMCLtrHN6RTvPxTWAYlsE_johGbIY']

# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', False))

# Admins, Channels & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ['1327973537'].split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ['-1001695882245'].split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('1327973537').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_channel = environ.get('-1001695882245')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else auth_channel
AUTH_GROUPS = [int(admin) for admin in environ.get("-1001695882245").split()]

# MongoDB information
DATABASE_URI = environ['mongodb+srv://vpcreation:VPCREATION@atlascluster.hocwhdz.mongodb.net/?retryWrites=true&w=majority']
DATABASE_NAME = environ['AtlasCluster']
COLLECTION_NAME = environ.get('Telegram_files')

# Messages
default_start_msg = """
**Hi, I'm Media Search Bot or you can call me as Auto-Filter Bot**
Here you can search files in Inline mode as well as PM, Use the below buttons to search files or send me the name of file to search.
"""
START_MSG = environ.get('START_MSG', default_start_msg)

FILE_CAPTION = environ.get("")
OMDB_API_KEY = environ.get("9b8a4248")
if FILE_CAPTION.strip() == "":
    CUSTOM_FILE_CAPTION=None
else:
    CUSTOM_FILE_CAPTION=FILE_CAPTION
if OMDB_API_KEY.strip() == "9b8a4248":
    API_KEY=None
else:
    API_KEY=OMDB_API_KEY
