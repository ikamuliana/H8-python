from flask import (
    make_response,
    abort,
)
from config import db
from models import (
    Directors,
    DirectorSchema,
)

#Read All
def read_all():
    """
    This function responds to a request for /api/directors
    with the complete lists of directors

    :return:        json string of list of people
    """
    # Create the list of people from our data
    director = Directors.query.order_by(Directors.id).limit(20)

    # Serialize the data for the response
    director_schema = DirectorSchema(many=True)
    # return person_schema.dump(people).data
    return director_schema.dump(director)

#Read by Id
def read_one(id):
    """
    This function responds to a request for /api/directors/{director_id}
    with one matching director from directors

    :param id:   ID of director to find
    :return:            director matching ID
    """
    # Get the person requested
    director = Directors.query \
        .filter(Directors.id == id) \
        .one_or_none()

    # Did we find a person?
    if director is not None:

        # Serialize the data for the response
        director_schema = DirectorSchema()
        # return person_schema.dump(person).data
        return director_schema.dump(director)

    # Otherwise, nope, didn't find that person
    else:
        abort(404, 'Director not found for Id: {id}'.format(id=id))

#read one name
def read_one_name(name):
        """
        This function responds to a request for /api/directors/{name}
        with one matching director name from directors
        :param id:   Name of director to find
        :return:            director matching name
        """
        # Build the initial query
        director = (
            Directors.query.filter(Directors.name == name)
            .one_or_none()
        )

        # Did we find a director?
        if director is not None:

            # Serialize the data for the response
            director_schema = DirectorSchema()
            data = director_schema.dump(director)
            return data

        # Otherwise, nope, didn't find that director
        else:
            abort(404, 'Director not found for name: {name}'.format(name=name))


#Create director
def create(director):
    """
    This function creates a new director in the directors structure
    based on the passed-in director data

    :param director:  director to create in directors structure
    :return:        201 on success, 406 on director exists
    """
    name = director.get("name")
    gender = director.get("gender")
    uid = director.get("uid")
    department = director.get("department")

    existing_director = (
        Directors.query.filter(Directors.name == name)
        .filter(Directors.gender == gender)
        .filter(Directors.uid == uid)
        .filter(Directors.department == department)
        .one_or_none()
    )

    # Can we insert this person?
    if existing_director is None:

        # Create a person instance using the schema and the passed-in person
        schema = DirectorSchema()
        # new_person = schema.load(person, session=db.session).data
        new_director = schema.load(director, session=db.session)

        # Add the person to the database
        db.session.add(new_director)
        db.session.commit()

        # Serialize and return the newly created person in the response
        # return schema.dump(new_person).data, 201
        # return schema.dump(new_person), 201
        data = schema.dump(new_director)
        return data, 201

    # Otherwise, nope, person exists already
    else:
        abort(409, f'Director with name: {name}, gender: {gender}, uid: {uid}, departement: {department} exists already')
        #  fname=fname, lname=lname
        #     ),
        # )

#Update 
def update(id, director):
    """
    This function updates an existing director in the directors structure
    Throws an error if a director with the name we want to update to
    already exists in the database.
    :param id:   Id of the director to update in the directors structure
    :param director:      director to update
    :return:            updated directors structure
    """
    # Get the person requested from the db into session
    update_director = Directors.query.filter(
        Directors.id == id
    ).one_or_none()

    # Try to find an existing person with the same name as the update
    name = director.get("name")
    gender = director.get("gender")
    uid = director.get("uid")
    department = director.get("department")

    existing_director = (
        Directors.query.filter(Directors.name == name)
        .filter(Directors.gender == gender)
        .filter(Directors.uid == uid)
        .filter(Directors.department == department)
        .one_or_none()
    )

    # Are we trying to find a person that does not exist?
    if update_director is None:
        abort(
            404,
            "Director not found for Id: {id}".format(id=id),
        )

    # Would our update create a duplicate of another person already existing?
    elif (
        existing_director is not None and existing_director.id != id
    ):
        abort(
            409,
            "Derector {name} {gender} {uid} {department} exists already".format(
                name=name, gender=gender, uid=uid, department=department
            ),
        )

    # Otherwise go ahead and update!
    else:

        # turn the passed in person into a db object
        schema = DirectorSchema()
        update = schema.load(director, session=db.session)

        # Set the id to the person we want to update
        update.id = update_director.id

        # merge the new object into the old and commit it to the db
        db.session.merge(update)
        db.session.commit()

        # return updated person in the response
        data = schema.dump(update_director)

        return data, 200

#Delete by Id
def delete(id):
    """
    This function deletes a director from the directors structure
    :param id:   Id of the director to delete
    :return:            200 on successful delete, 404 if not found
    """
    # Get the person requested
    director = Directors.query.filter(Directors.id == id).one_or_none()

    # Did we find a person?
    if director is not None:
        db.session.delete(director)
        db.session.commit()
        return make_response(
            "Director {id} deleted".format(id=id), 200
        )

    # Otherwise, nope, didn't find that person
    else:
        abort(
            404,
            "Director not found for Id: {id}".format(id=id),
        )