import jwt
from datetime import datetime, timedelta

def create_token(user_id, key):
    payload = {
        'user_id': user_id,
        'exp': datetime.utcnow() + timedelta(days=1)
    }
    token = jwt.encode(payload, key, algorithm='HS256')
    return token

def decode_token(token, key):
    return jwt.decode(token, key, algorithms=['HS256'])