from flask import Flask, request
from flask_restful import Api, Resource, abort, fields, marshal_with, reqparse

app = Flask(__name__)
api = Api(app)

# Dados
POSTS = {
    'post1': {'title': 'Gol do dale'},
    'post2': {'title': 'Gol do flamengo'},
    'post3': {'title': 'Gol do internacional'}
}

def abort_if_todo_doesnt_exist(post_id):
    if post_id not in POSTS:
        abort(404, message="Todo {} doesn't exist".format(post_id))

parser = reqparse.RequestParser()
parser.add_argument('title')

# Post API
# Mostra um unico post e o permite deleta-lo
class Post(Resource):
    def get(self, post_id):
        abort_if_todo_doesnt_exist(post_id)
        return POSTS[post_id]

    def delete(self, post_id):
        abort_if_todo_doesnt_exist(post_id)
        del POSTS[post_id]
        return '', 204
    
    def put(self, post_id):
        args = parser.parse_args()
        title = {'title': args['title']}
        POSTS[post_id] = title
        return title, 201

# Posts List
# Mostra uma lista de todos posts e aceita POST para adicionar novos posts.
   
class PostList(Resource):
    def get(self):
        return POSTS

    def post(self):
        args = parser.parse_args()
        post_id = int(max(POSTS.keys()).lstrip('post')) + 1
        post_id = 'post%i' % post_id
        POSTS[post_id] = {'post': args['title']}
        return POSTS[post_id], 201

# Rotas
api.add_resource(PostList, '/posts')
api.add_resource(Post, '/posts/<string:post_id>')

if __name__ == '__main__':
    app.run(debug=True)