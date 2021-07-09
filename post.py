"""
This is the people module and supports all the REST actions for the
people data
"""

from flask import make_response, abort
from config import db
from models import Post, PostSchema


def read_all():
    """
    This function responds to a request for /api/post
    with the complete lists of posts

    :return:        json string of list of people
    """
    # Create the list of posts from our data
    post = Post.query.order_by(Post.id).all()

    # Serialize the data for the response
    post_schema = PostSchema(many=True)
    data = post_schema.dump(post)
    return data


def read_one(post_id):
    """
    This function responds to a request for /api/post/{post_id}
    with one matching post from request

    :param post_id:   Id of post to find
    :return:            post matching id
    """
    # Get the post requested
    post = Post.query.filter(Post.post_id == post_id).one_or_none()

    # Did we find a post?
    if post is not None:

        # Serialize the data for the response
        post_schema = PostSchema()
        data = post_schema.dump(post)
        return data

    # Otherwise, nope, didn't find that post
    else:
        abort(
            404,
            "Post not found for Id: {post_id}".format(post_id=post_id),
        )


def create(post):
    """
    This function creates a new post in the people structure
    based on the passed in post data

    :param post:  post to create in posts structure
    :return:        201 on success, 406 on person exists
    """
    id = post.get("id")
    title = post.get("title")

    existing_post = (
        Post.query.filter(Post.id == id)
        .one_or_none()
    )

    # Can we insert this person?
    if existing_post is None:

        # Create a person instance using the schema and the passed in person
        schema = PostSchema()
        new_post = schema.load(post, session=db.session)

        # Add the person to the database
        db.session.add(new_post)
        db.session.commit()

        # Serialize and return the newly created person in the response
        data = schema.dump(new_post)

        return data, 201

    # Otherwise, nope, post exists already
    else:
        abort(
            409,
            "Post id {id} exists already".format(
                id=id
            ),
        )


def update(post_id, person):
    """
    This function updates an existing person in the people structure
    Throws an error if a person with the name we want to update to
    already exists in the database.

    :param person_id:   Id of the person to update in the people structure
    :param person:      person to update
    :return:            updated person structure
    """
    # Get the person requested from the db into session
    update_post = Post.query.filter(
        Post.post_id == post_id
    ).one_or_none()

    # Try to find an existing person with the same name as the update
    post_id = Post.get("id")

    existing_post = (
        Post.query.filter(Post.id == post_id)
        .one_or_none()
    )

    # Are we trying to find a post that does not exist?
    if update_post is None:
        abort(
            404,
            "Post not found for Id: {post_id}".format(post_id=post_id),
        )

    # Would our update create a duplicate of another person already existing?
    elif (
        existing_post is not None and existing_post.post_id != post_id
    ):
        abort(
            409,
            "Post {post_id} and title exists already".format(
                post_id=post_id
            ),
        )

    # Otherwise go ahead and update!
    else:

        # turn the passed in person into a db object
        schema = PostSchema()
        update = schema.load(post_id, session=db.session)

        # Set the id to the person we want to update
        update.post_id = update_post.person_id

        # merge the new object into the old and commit it to the db
        db.session.merge(update)
        db.session.commit()

        # return updated person in the response
        data = schema.dump(update_post)

        return data, 200


def delete(post_id):
    """
    This function deletes a post from the people structure

    :param post_id:   Id of the post to delete
    :return:            200 on successful delete, 404 if not found
    """
    # Get the post requested
    post = Post.query.filter(Post.post_id == post_id).one_or_none()

    # Did we find a post?
    if post is not None:
        db.session.delete(post)
        db.session.commit()
        return make_response(
            "Post {post_id} deleted".format(post_id=post_id), 200
        )

    # Otherwise, nope, didn't find that post
    else:
        abort(
            404,
            "Post not found for Id: {post_id}".format(post_id=post_id),
        )
