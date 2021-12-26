from datetime import datetime
from config import db, ma
from marshmallow import fields
from sqlalchemy.orm import backref


class Avocado(db.Model):
    __tablename__ = 'avocado'
    date = db.Column(db.Text)
    avgprice = db.Column(db.Float)
    totalvol = db.Column(db.Integer, primary_key=True)
    avo_a = db.Column(db.Integer)
    avo_b = db.Column(db.Float)
    avo_c = db.Column(db.Float)
    type = db.Column(db.Integer)
    regionid = db.Column(db.Integer)


class Avoregion(db.Model):
    __tablename__ = 'avoregion'
    regionid = db.Column(db.Integer, primary_key=True)
    region = db.Column(db.String(60))
    # avocados = db.relationship(
    #     'Avocado',
    #     backref='avoregion',
    #     cascade='all, delete, delete-orphan',
    # )


class Avotype(db.Model):
    __tablename__ = 'avotype'
    typeid = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(60))
    # avocados = db.relationship(
    #     'Avocado',
    #     backref='avotype',
    #     cascade='all, delete, delete-orphan',
    # )


#Schema
class AvocadoSchema(ma.SQLAlchemyAutoSchema):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    class Meta:
        model = Avocado
        sqla_session = db.session
        load_instance = True

    # regionid = fields.Nested('TAvoregionSchema', default=None)


class AvoregionSchema(ma.SQLAlchemyAutoSchema):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    class Meta:
        model = Avotype
        sqla_session = db.session
        load_instance = True

    # avocado = fields.Nested("TAvocadoSchema", default=[], many=True)


class AvotypeSchema(ma.SQLAlchemyAutoSchema):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    class Meta:
        model = Avotype
        sqla_session = db.session
        load_instance = True

    # avocado = fields.Nested("TAvocadoSchema", default=[], many=True)


# class TAvocadoSchema(ma.SQLAlchemyAutoSchema):
#     """
#     This class exists to get around a recursion issue
#     """

#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)

#     date = fields.Str()
#     avgprice = fields.Float()
#     totalvol = fields.Int()
#     avo_a = fields.Int()
#     avo_b = fields.Float()
#     avo_c = fields.Float()
#     type = fields.Int()
#     regionid = fields.Int()


# class TAvoregionSchema(ma.SQLAlchemyAutoSchema):
#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)

#     regionid = fields.Int()
#     region = fields.Str()

# class TAvotypeSchema(ma.SQLAlchemyAutoSchema):
#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)

#     typeid = fields.Int()
#     type = fields.Str()