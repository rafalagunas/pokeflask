from flask import Flask, render_template
from flask import Flask
from flask import Flask, render_template, request
from flask import Flask, render_template, json, request

app = Flask(__name__)


@app.route("/")
def main():
    return render_template('index.html')


@app.route("/home")
def Home():
	return render_template('home.html')


@app.route('/SignUp', methods=['POST'])
def LogIn():

#Crear variables que reciban los formularios
	_Email = request.form['inputEmail']
	_password = request.form['inputPassword']
	_Latitud = request.form['inputLatitud']
	_Longitud = request.form['inputLongitud']




if __name__ == "__main__":
    app.run()

