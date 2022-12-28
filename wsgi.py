from application import init_app
import os
from dotenv import load_dotenv

app = init_app()

if __name__ == "__main__":
	load_dotenv()
	app.run(host=os.getenv('SPOTIPY_CLIENT_ID'))