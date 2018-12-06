from flask import Flask, render_template
import socket
app = Flask(__name__)

@app.route('/')
def main():
	hostname=socket.gethostname()
	logoFile=open('static/logo/projectLogo.txt')
	logo = logoFile.readline()
	return(render_template('main.html',logo=logo, hostname=hostname))

if __name__ == '__main__':
	app.run(debug=True,port=5050)