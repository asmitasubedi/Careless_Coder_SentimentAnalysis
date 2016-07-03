import test
from flask import Flask, Response
from flask import render_template
from flask import url_for

app = Flask(__name__)

x = test.myfunction()
g = x[1]
b = x[0]

@app.route("/")
def hello():
	return render_template('index.html')

@app.route("/good")
def good():
	print(type(g))
	return render_template('goodNews.html', good=g)

@app.route("/bad")
def bad():
	return render_template('badNews.html', bad=b)


if __name__ == "__main__":
    app.run()

