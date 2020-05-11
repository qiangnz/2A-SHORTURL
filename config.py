import os

# current directory of config.py
path = os.path.dirname(__file__)


# define port
options = {
    "port": 8080
}

# set static path and template_path
# default debug = false, whereas it should be switched to true in developing mode
# set xsrf_cookies to True, starting the XSRF protection
settings = {
    "debug": True,
    "autoreload": True,
    "xsrf_cookies": True,
    "cookie_secret": "586610e97b5142838e51ff6cd2cc73dc",
    "template_path": os.path.join(path, "template"),
    "static_path": os.path.join(path, "static"),
    "model_path": os.path.join(path, "model"),
    "ip2Region_DB_path":os.path.join(path,"static/ip2region-master/data/ip2region.db")
}

# print("##################")
# print(settings['ip2Region_DB_path'])
# print(settings['model_path'])

# define mysql_db config
mysql_db = dict(
    host="127.0.0.1",
    dbname="shorturl_2A",
    port=3306,
    admin="root",
    password="root"
)
