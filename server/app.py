from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
	return render_template("index071402_copy.html")

if __name__ == "__main__":
	#app.debug = True
	app.run()

	#app.run(debug=False, host = '0.0.0.0' , port = 5000)