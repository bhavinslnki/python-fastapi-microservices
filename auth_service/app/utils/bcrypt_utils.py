import bcrypt

def hash_password(plain_password: str):
    return  bcrypt.hashpw(plain_password.encode('utf-8'), bcrypt.gensalt())  # Convert to string for storage

def verify_password(plain_password: str, hashed_password: str):
    return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))
