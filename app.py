from flask import Flask, render_template
from flask import Flask
app = Flask(__name__)


@app.route("/")
def main():
    return render_template('index.html')


@app.route("/home")
def Home():
	return render_template('home.html')



if __name__ == "__main__":
    app.run()

