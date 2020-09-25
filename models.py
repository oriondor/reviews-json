from app import db

class Products(db.Model):
	__tablename__ = 'products'

	product_id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String())
	asin = db.Column(db.String())


class Reviews(db.Model):
	__tablename__ = 'reviews'

	review_id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String())
	asin = db.Column(db.ForeignKey('products.asin'))
	review = db.Column(db.String())

	