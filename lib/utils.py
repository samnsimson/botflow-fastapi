from passlib.hash import bcrypt


def hash_password(password: str) -> str:
    hash = bcrypt.hash(password)
    return hash


def verify_password(password: str, hash: str) -> bool:
    return bcrypt.verify(password, hash)
