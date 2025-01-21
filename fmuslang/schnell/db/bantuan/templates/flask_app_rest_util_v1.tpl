import binascii, hashlib, os
from project.main.extensions import pwd_context



def hash_pass( password ):
	"""Hash a password for storing."""
	return pwd_context.hash(password)


def hash_pass2( password ):
	"""Hash a password for storing."""
	salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
	pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'), salt, 100000)
	pwdhash = binascii.hexlify(pwdhash)
	return (salt + pwdhash) # return bytes


def hashing1(stored_password):
	salt = stored_password[:64]
	stored_password = stored_password[64:]

	pwdhash = hashlib.pbkdf2_hmac('sha512', 
		provided_password.encode('utf-8'), 
		salt.encode('ascii'), 
		100000)

	pwdhash = binascii.hexlify(pwdhash).decode('ascii')
	return pwdhash

def hashing2(supplied_password, stored_password):	
	return pwd_context.verify(supplied_password, stored_password)

def verify_pass(provided_password, stored_password):
	"""Verify a stored password against one provided by user"""
	print(f'flask/apps/user/util/verify_pass #1 = terima = [{provided_password}] db = [{stored_password}], jenis = {type(stored_password)}')
	if not isinstance(stored_password, str):
		stored_password = stored_password.decode('ascii')


	# pwdhash = hashing1(stored_password)
	# print(f'flask/apps/user/util/verify_pass #2 = hitung = [{pwdhash}] db = [{stored_password}], jenis = {type(stored_password)}')
	# return pwdhash == stored_password

	return hashing2(provided_password, stored_password)

