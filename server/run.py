from app import app
from config import SERVER_IP, SERVER_PORT, DEBUG


app.run(host=SERVER_IP, port=SERVER_PORT, debug=DEBUG)
