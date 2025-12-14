from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password, check_password
from .firebase import db
import uuid


#auth
@api_view(['POST'])
def signup(request):
    data = request.data
    user_id = str(uuid.uuid4())

    db.collection('users').document(user_id).set({
        'username': data.get('username', ''),
        'email': data['email'],
        'password': make_password(data['password'])
    })

    return Response({'message': 'Signup successful'})


@api_view(['POST'])
def login(request):
    data = request.data
    users = db.collection('users').where('email', '==', data['email']).stream()

    for user in users:
        if check_password(data['password'], user.to_dict()['password']):
            return Response({'token': user.id})

    return Response({'error': 'Invalid credentials'}, status=400)


#post
@api_view(['POST'])
def create_post(request):
    data = request.data

    db.collection('posts').add({
        'user_id': data['user_id'],
        'image_url': data['image_url'],
        'caption': data['caption'],
        'likes': 0
    })

    return Response({'message': 'Post created'})

#all post
@api_view(['GET'])
def all_posts(request):
    posts = db.collection('posts').stream()
    result = []

    for post in posts:
        p = post.to_dict()
        p['id'] = post.id
        result.append(p)

    return Response(result)


#follow
@api_view(['POST'])
def follow_user(request):
    data = request.data

    db.collection('follows').add({
        'follower': data['follower'],
        'following': data['following']
    })

    return Response({'message': 'Followed'})


#feed
@api_view(['GET'])
def feed(request, user_id):
    follows = db.collection('follows').where('follower', '==', user_id).stream()
    following_ids = [f.to_dict()['following'] for f in follows]

    if not following_ids:
        return Response([])

    posts = db.collection('posts').where('user_id', 'in', following_ids).stream()
    result = []

    for post in posts:
        p = post.to_dict()
        p['id'] = post.id
        result.append(p)

    return Response(result)

#like
@api_view(['POST'])
def like_post(request):
    post_id = request.data['post_id']
    ref = db.collection('posts').document(post_id)
    post_doc = ref.get()
    if post_doc.exists:
        post = post_doc.to_dict()
        ref.update({'likes': post.get('likes', 0) + 1})
        return Response({'message': 'Liked'})

    return Response({'error': 'Post not found'}, status=404)


#comment
@api_view(['POST'])
def add_comment(request):
    data = request.data

    db.collection('comments').add({
        'post_id': data['post_id'],
        'user_id': data['user_id'],
        'text': data['text']
    })

    return Response({'message': 'Comment added'})