"""
This is the people module and supports all the REST actions for the
people data
"""

from flask import make_response, abort
from config import db
from models import Directors, Movies, MovieSchema


def read_all():
    """
    This function responds to a request for /api/movies
    with the complete list of movies, sorted by note timestamp
    :return:                json list of all movies 
    """
    # Query the database for all the notes
    movies = Movies.query.order_by(db.desc(Movies.id)).limit(20)

    # Serialize the list of notes from our data
    movies_schema = MovieSchema(many=True)
    data = movies_schema.dump(movies)
    return data


def read_one(director_id, movie_id):
    """
    This function responds to a request for
    /api/directors/{director_id}/movies/{movie_id}
    with one matching note for the associated person
    :param director_id:       Id of directors the movie is related to
    :param movie_id:         Id of the movie
    :return:                json string of note contents
    """
    # Query the database for the note
    movies = (
        Movies.query.join(Directors, Directors.id == Movies.director_id)
        # Note.query.join(Person, Person.person_id == Note.person_id, Note.note_id == note_id)
        .filter(Directors.id == director_id)
        .filter(Movies.id == movie_id)
        .one_or_none()
    )

    # Was a note found?
    if movies is not None:
        movie_schema = MovieSchema()
        data = movie_schema.dump(movies)
        return data

    # Otherwise, nope, didn't find that note
    else:
        abort(404, f"Movie not found for director Id: {director_id}")


def create(director_id, movie):
    """
    This function creates a new movie related to the passed in director id.
    :param director_id:       Id of the director the movie is related to
    :param movie:            The JSON containing the movie data
    :return:                201 on success
    """
    # get the parent person
    director = Directors.query.filter(Directors.id == director_id).one_or_none()

    # Was a person found?
    if director is None:
        abort(404, f"Director not found for Id: {director_id}")

    # Create a note schema instance
    schema = MovieSchema()
    new_movie = schema.load(movie, session=db.session)

    # Add the note to the person and database
    director.movies.append(new_movie)
    db.session.commit()

    # Serialize and return the newly created note in the response
    data = schema.dump(new_movie)

    return data, 201


def update(director_id, movie_id, movie):
    """
    This function updates an existing movie related to the passed in
    person id.
    :param director_id:       Id of the director the movie is related to
    :param movie_id:         Id of the movie to update
    :param content:            The JSON containing the movie data
    :return:                200 on success
    """
    update_movie = (
        Movies.query.filter(Directors.id == director_id)
        .filter(Movies.id == movie_id)
        .one_or_none()
    )

    # Did we find an existing note?
    if update_movie is not None:

        # turn the passed in note into a db object
        schema = MovieSchema()
        update = schema.load(movie, session=db.session)

        # Set the id's to the note we want to update
        update.director_id = update_movie.director_id
        update.id = update_movie.id

        # merge the new object into the old and commit it to the db
        db.session.merge(update)
        db.session.commit()

        # return updated note in the response
        data = schema.dump(update_movie)

        return data, 200

    # Otherwise, nope, didn't find that note
    else:
        abort(404, f"Movie not found for Id: {director_id}")


def delete(director_id, movie_id):
    """
    This function deletes a movie from the movie structure
    :param director_id:   Id of the director the movie is related to
    :param movie_id:     Id of the movie to delete
    :return:            200 on successful delete, 404 if not found
    """
    # Get the note requested
    movie = (
        # Note.query.filter(Person.person_id == person_id)
        Movies.query.join(Directors, Directors.id == Movies.director_id)
        .filter(Directors.id == director_id)
        .filter(Movies.id == movie_id)
        .one_or_none()
    )

    # did we find a note?
    if movie is not None:
        db.session.delete(movie)
        db.session.commit()
        return make_response(
            "Movie {movie_id} deleted".format(movie_id=movie_id), 200
        )

    # Otherwise, nope, didn't find that note
    else:
        abort(404, f"Movie not found for Id: {movie_id}")