import hashlib
import bcrypt

from app.environment import env

secret = env['APP_SECRET']


class Password:
    def __init__(self):
        self.passwd: str = ''

    def gen_salt(self):
        return bcrypt.gensalt()

    def password_hash(self, salt: bytes = b''):
        if not salt:
            salt = self.gen_salt()

        hashed_passwd = hashlib.sha256(
            self.passwd.encode('utf-8')).digest()

        # Generate a hash with salt and passwd
        out_hash = bcrypt.hashpw(
            hashed_passwd, salt).decode()

        return out_hash

    def verify_passwd(self, hash: str):
        hashed_passwd = hashlib.sha256(
            self.passwd.encode('utf-8')).digest()

        return bcrypt.checkpw(
            hashed_passwd, hash.encode('utf-8'))
