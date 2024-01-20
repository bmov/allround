import hashlib
from random import randrange

from app.environment import env

secret = env['APP_SECRET']


class Password:
    def __init__(self):
        self.passwd = None

    def gen_salt(self):
        char_list = 'abcdefghijklmnopqrstuvwxyz'\
                    'ABCDEFGHIJKLMNOPQRSTUVWXYZ'\
                    '1234567890-_'
        result = ''

        for i in range(0, 16):
            random = randrange(0, 63)
            result += char_list[random]

        return result

    def password_hash(self, salt=None):
        if not salt:
            salt = self.gen_salt()

        # Generate a hash with salt and passwd
        hash_mixed = secret + salt + self.passwd
        hashed_passwd = hashlib.sha256(
            hash_mixed.encode('utf-8')).hexdigest()

        return salt + '$' + hashed_passwd

    def verify_passwd(self, hash):
        # Split the salt value of a hash
        hash_split = hash.split('$')
        salt = hash_split[0]

        # Generate a hash with salt and passwd
        hash_mixed = secret + salt + self.passwd
        hashed_passwd = hashlib.sha256(
            hash_mixed.encode('utf-8')).hexdigest()

        # Mix hashed_passwd and salt of the hash
        target = salt + '$' + hashed_passwd

        if hash == target:
            return True
        else:
            return False
