"""
This is the people module and supports all the REST actions for the
people data
"""

from flask import make_response, abort
from config import db
from models import Avocado, AvocadoSchema


def read_all():
    """
    This function responds to a request for /api/people
    with the complete lists of people
    :return:        json string of list of people
    """
    # Create the list of people from our data
    avocado = Avocado.query.all()

    # Serialize the data for the response
    avocado_schema = AvocadoSchema(many=True)
    data = avocado_schema.dump(avocado)
    return data


def read_one(regionid):
    """
    This function responds to a request for /api/people/{person_id}
    with one matching person from people
    :param person_id:   Id of person to find
    :return:            person matching id
    """
    # Build the initial query
    avocado = (
        # Avocado.query.filter(Avocado.regionid == regionid)
        Avocado.query.join(Avocado, Avocado.regionid == Avoregion.regionid)
        .outerjoin(Avoregion)
        .one_or_none()
    )

    # Did we find a person?
    if avocado is not None:

        # Serialize the data for the response
        avocado_schema = AvocadoSchema()
        data = avocado_schema.dump(regionid)
        return data

    # Otherwise, nope, didn't find that person
    else:
        abort(404, f"Avocado not found for region Id: {regionid}")


def create(regionid, avocado):
    """
    This function creates a new note related to the passed in person id.
    :param person_id:       Id of the person the note is related to
    :param note:            The JSON containing the note data
    :return:                201 on success
    """
    # get the parent person
    avocado = Avocado.query.filter(Avocado.regionid == regionid).one_or_none()

    # Was a person found?
    if avocado is None:
        abort(404, f"Person not found for Id: {regionid}")

    # Create a note schema instance
    schema = NoteSchema()
    new_avocado = schema.load(avocado, session=db.session)

    # Add the note to the person and database
    avocado.avocados.append(new_avocado)
    db.session.commit()

    # Serialize and return the newly created note in the response
    data = schema.dump(new_avocado)

    return data, 201

def update(regionid, avocado):
    """
    This function updates an existing person in the people structure
    :param person_id:   Id of the person to update in the people structure
    :param person:      person to update
    :return:            updated person structure
    """
    # Get the person requested from the db into session
    update_avocado = Avocado.query.filter(
        Avocado.regionid == regionid
    ).one_or_none()

    # Did we find an existing person?
    if update_avocado is not None:

        # turn the passed in person into a db object
        schema = AvocadoSchema()
        update = schema.load(avocado, session=db.session)

        # Set the id to the person we want to update
        update.regionid = update_avocado.regionid

        # merge the new object into the old and commit it to the db
        db.session.merge(update)
        db.session.commit()

        # return updated person in the response
        data = schema.dump(update_avocado)

        return data, 200

    # Otherwise, nope, didn't find that person
    else:
        abort(404, f"Avocado not found for region Id: {regionid}")


def delete(regionid):
    """
    This function deletes a person from the people structure
    :param person_id:   Id of the person to delete
    :return:            200 on successful delete, 404 if not found
    """
    # Get the person requested
    # avocado = Avocado.query.filter(Avocado.regionid == regionid).one_or_none()
    Avoregion.query.join(Avocado, Avocado.regionid == Avoregion.regionid).one_or_none()
    # .filter(Avocado.regionid == regionid).one_or_none()

    # Did we find a person?
    if avocado is not None:
        db.session.delete(avocado)
        db.session.commit()
        return make_response(f"Region {regionid} deleted", 200)

    # Otherwise, nope, didn't find that person
    else:
        abort(404, f"Avocado not found for region Id: {regionid}")