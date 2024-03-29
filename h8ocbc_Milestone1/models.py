from datetime import datetime
from config import db, ma
from marshmallow import fields

class Directors(db.Model):
    __tablename__ = 'directors'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50), index = True)
    gender = db.Column(db.Integer, nullable = False)
    uid = db.Column(db.Integer, nullable = False)
    department = db.Column(db.Text, nullable = False)
    movies = db.relationship(
        'Movies',
        backref='director',
        cascade='all, delete, delete-orphan',
        single_parent=True,
        order_by='desc(Movies.id)'
    )

class Movies(db.Model):
    __tablename__ = 'movies'
    id = db.Column(db.Integer, primary_key = True)
    original_title = db.Column(db.Text, nullable = False)
    budget = db.Column(db.Integer, nullable = False)
    popularity = db.Column(db.Integer, nullable = False)
    release_date = db.Column(db.Text, nullable = False)
    revenue = db.Column(db.Integer, nullable = False)
    title = db.Column(db.Text, nullable = False)
    vote_average = db.Column(db.Float, nullable = False)
    vote_count = db.Column(db.Integer, nullable = False)
    overview = db.Column(db.Text, nullable = False)
    tagline = db.Column(db.Text, nullable = False)
    uid = db.Column(db.Integer, nullable = False)
    director_id = db.Column(db.Integer, db.ForeignKey('directors.id'))

#Schema
class DirectorSchema(ma.SQLAlchemyAutoSchema):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    class Meta:
        model = Directors
        # sqla_session = db.session
        load_instance = True

    movies = fields.Nested('DirectorMovieSchema', default=[], many=True)

class DirectorMovieSchema(ma.SQLAlchemyAutoSchema):
    """
    This class exists to get around a recursion issue
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    id = fields.Int()
    original_title = fields.Str()
    budget = fields.Int()
    popularity = fields.Int()
    release_date = fields.Str()
    revenue = fields.Int()
    title = fields.Str()
    vote_average = fields.Float()
    vote_count = fields.Int()
    overview = fields.Str()
    tagline = fields.Str()
    uid = fields.Int()
    director_id = fields.Int()


class MovieSchema(ma.SQLAlchemyAutoSchema):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    class Meta:
        model = Movies
        # sqla_session = db.session
        load_instance = True

    director = fields.Nested("MovieDirectorSchema", default=None)


class MovieDirectorSchema(ma.SQLAlchemyAutoSchema):
    """
    This class exists to get around a recursion issue
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    id = fields.Int()
    name = fields.Str()
    gender = fields.Int()
    uid = fields.Int()
    department = fields.Str()