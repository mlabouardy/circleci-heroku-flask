from flask import Flask, render_template, json, jsonify, request
import flask
from database import Database
import os

app = Flask(__name__)
db = Database()

db.create_table()


@app.route('/api/movies', methods=['GET', 'POST'])
def get_movies():
	try:
		if flask.request.method == 'POST':
			db.insert_movie(request.json['name'], request.json['cover'])
			return jsonify(request.json), 201
		else:
			movies = db.fetch_movies()
			return jsonify(movies), 200
	except Exception as e:
		return jsonify(status='ERROR', message=str(e)), 500

@app.route('/')
def index():
	return render_template('index.html')

if __name__ == "__main__":
	app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
