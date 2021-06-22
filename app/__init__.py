@app.route('/posts')
def index():
    posts = Post.query.order_by(Post.id).all()
    if len(posts) == 0:
        abort(404)    
        
    return jsonify({
        'success': True,
        'posts': posts
    })

@app.route('/posts', methods=['POST'])
def store():
    body = request.get_json()
    name = body.get('name', None)
    age = body.get('age', None)    try:
        user = User(name=name, age=age)
        user.create()        
        
    return jsonify({
            'success': True,
            'created': user.format()
        })
    except:
        abort(422)