from flask import Flask
from flask_restful import reqparse, abort, Api, Resource

app = Flask(__name__)
api = Api(app)

@app.route('/api/v1/post', methods=['POST'])
def create_post():
    

if __name__ == '__main__':
    app.run(debug=True)