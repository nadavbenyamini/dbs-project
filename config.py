# from sshtunnel import SSHTunnelForwarder
USE_SSH = True
DEBUG = not USE_SSH
HOST = "0.0.0.0"
PORT = 40444
BASE_URL = HOST + ":" + str(PORT)

