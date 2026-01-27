from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes

POSTS = [
    {"id": 1, "title": "First post", "content": "This is the first post."},
    {"id": 2, "title": "Second post", "content": "This is the second post."},
]


def find_post_by_id(post_id):
    """Fetch a single post by its unique ID."""
    return next((p for p in POSTS if p['id'] == post_id), None)


def generate_next_id():
    """Calculate the next available integer ID for a new post."""
    return max([post['id'] for post in POSTS], default=0) + 1


def validate_post_data(data):
    """Check for missing required fields in the request body."""
    required = ['title', 'content']
    return [f for f in required if not data or f not in data or not data[f]]



@app.route('/api/posts', methods=['GET'])
def get_posts():
    """List all posts with optional sorting by title or content."""
    sort_field = request.args.get('sort')
    direction = request.args.get('direction', 'asc').lower()

    res = list(POSTS)

    if sort_field:
        if sort_field not in ['title', 'content'] or direction not in ['asc', 'desc']:
            return jsonify({"error": "Bad Request", "message": "Invalid sort parameters."}), 400

        res.sort(key=lambda x: x[sort_field].lower(), reverse=(direction == 'desc'))

    return jsonify(res)


@app.route('/api/posts', methods=['POST'])
def add_post():
    """Create a new blog post and return it with a generated ID."""
    data = request.get_json()
    missing = validate_post_data(data)

    if missing:
        return jsonify({"error": "Bad Request", "message": f"Missing: {', '.join(missing)}"}), 400

    new_post = {
        "id": generate_next_id(),
        "title": data['title'],
        "content": data['content']
    }
    POSTS.append(new_post)
    return jsonify(new_post), 201


@app.route('/api/posts/<int:post_id>', methods=['DELETE'])
def delete_post(post_id):
    """Remove a post from the list by its ID."""
    global POSTS
    post = find_post_by_id(post_id)

    if not post:
        return jsonify({"error": "Not Found", "message": "Post not found."}), 404

    POSTS = [p for p in POSTS if p['id'] != post_id]
    return jsonify({"message": f"Post {post_id} deleted."}), 200


@app.route('/api/posts/<int:post_id>', methods=['PUT'])
def update_post(post_id):
    """Update fields of an existing post while keeping others intact."""
    data = request.get_json()
    post = find_post_by_id(post_id)

    if not post:
        return jsonify({"error": "Not Found", "message": "Post not found."}), 404

    post['title'] = data.get('title', post['title'])
    post['content'] = data.get('content', post['content'])
    return jsonify(post), 200


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5002, debug=True)
