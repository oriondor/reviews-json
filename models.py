from app import db

class Products(db.Model):
	__tablename__ = 'products'

	product_id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String())
	asin = db.Column(db.String())

	def __init__(self, title, asin):
		self.title = title
		self.asin = asin


class Reviews(db.Model):
	__tablename__ = 'reviews'

	review_id = db.Column(db.Integer, primary_key=True)
	asin = db.Column(db.ForeignKey('products.asin'))
	title = db.Column(db.String())
	review = db.Column(db.String())

	def __init__(self, asin, title, review):
		self.asin = asin
		self.title = title
		self.review = review
	