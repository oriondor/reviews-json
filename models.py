from app import db

class Products(db.Models):
	__tablename__ = 'products'

	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String())
	asin = db.Column(db.String())


class Reviews(db.Models):
	__tablename__ = 'reviews'

	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String())
	asin = db.Column(ForeignKey('products.asin'))
	review = db.Column(db.String())

	