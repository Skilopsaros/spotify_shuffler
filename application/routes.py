from flask import render_template, request
from flask import current_app as app
from .core import shuffle_playlist
from turbo_flask import Turbo

turbo = Turbo(app)

@app.route('/', methods=["GET", "POST"])
def home():
	"""Homepage."""
	if request.method == "POST":
		if request.form.get('shuffle_button') == 'SHUFFLE':
			print("DID A THING")
			playlist_id=request.form['playlist_id']
			if not playlist_id:
				playlist_id = "7ahUCiyzYRB0SljkSQdily"
			for each in shuffle_playlist(playlist_id):
				name, num, length = each
				turbo.push(turbo.replace(f"<b, id='track'>Track {num+1}/{length}: {name}</b>", 'track'))
				
	return render_template("main.html")