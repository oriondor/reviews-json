import os
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, request,make_response
from flask import jsonify
from flask_caching import Cache

import math

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['CACHE_TYPE'] = "simple"
db = SQLAlchemy(app)
cache = Cache(app)

from models import *

@app.route('/api/v1/<prod_id>', methods=['GET'])
@cache.cached(timeout=10,query_string=True)
def get_product(prod_id):
	product = Products.query.get(int(prod_id))
	if not product:
		return jsonify({
			'error':'Product not found',
			'code':404
			}), 404
	page = int(request.args.get('page',1))
	limit_reviews = 10
	fr,to = (page-1)*limit_reviews,page*limit_reviews
	reviews = Reviews.query.filter_by(asin=product.asin).offset(fr).limit(to)
	r = make_response(jsonify({
	'product':{'asin':product.asin,'title':product.title},
	'pages': math.ceil(reviews.count()/limit_reviews),
	'reviews':[{'id':review.review_id,'asin':review.asin,'title':review.title,'review':review.review} for review in reviews]
	}))
	r.headers.set('Access-Control-Allow-Origin','*')
	return r


# curl -i -H "Content-Type: application/x-www-form-urlencoded" -X PUT -d 'title=Example title&review=Example review' http://localhost:5000/api/v1/create_review/3
@app.route('/api/v1/create_review/<prod_id>', methods=['PUT'])
def create_new_review(prod_id):
	product = Products.query.get(int(prod_id))
	if not product:
		return jsonify({
			'error':'Product not found',
			'code':404
			}), 404
	if request.method == "PUT":
		try:
			title,review = request.form.get('title'),request.form.get('review')
			new_review = Reviews(asin=product.asin,title=title,review=review)
			db.session.add(new_review)
			db.session.commit()
			return jsonify({
				'status':'Review added',
				'code':201
				}), 201
		except Exception as e:
			return jsonify({
			'error':f"Error {e} occuired",
			'code':400
			}),400
	return jsonify({
		'error':f"This api endpoint accepts PUT, not {request.method}",
		'code':400
		}),400

if __name__ == '__main__':
	app.run()