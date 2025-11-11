from argon2 import PasswordHasher, exceptions as argon2_exceptions

PH = PasswordHasher()

def hash_password(password: str) -> str:
    hashed = PH.hash(password)
    return hashed

def verify_hashed_password(hashed: str, password: str) -> bool:
    try:
        PH.verify(hashed, password)
        return True
    except argon2_exceptions.VerifyMismatchError:
        return False
