from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import os
import requests
import vlc
from PIL import Image
from dotenv import load_dotenv

# # Encryption key and initialization vector (IV)
# KEY = b'mysecretpassword'
# IV = b'mysecretpassword'
from cryptography.fernet import Fernet

# Generate a new encryption key, a new random 256-bit key
# ULIBPY_FERNET_KEY
# text_key = Fernet.generate_key()
from .envutils import env_get
# Encryption key and initialization vector (IV)
KEY = env_get('ULIBPY_KEY_IV').encode('utf8') # 16 byte -> AES-128, 40 byte -> AES-256
IV = KEY # AES-128/196/256 utk 16, 24, 32 byte.
# 128 => cipher = AES.new(KEY, AES.MODE_CBC, IV)
# 256 => cipher = AES.new(KEY, AES.MODE_CBC, IV)

text_key = env_get('ULIBPY_FERNET_KEY').encode('utf8') # jadikan byte
# Create a Fernet object using the key
fernet = Fernet(text_key)
# "Fernet key must be 32 url-safe base64-encoded bytes."
# fernet = Fernet(KEY)


"""
Based on the provided code, it seems that you are generating a new Fernet key each time the script runs with the line `text_key = Fernet.generate_key()`. Fernet keys are used for both encryption and decryption, and they need to be consistent in order to successfully decrypt the ciphertext.

In your scenario, when you encrypt the plaintext using `encrypt_text`, you generate a new Fernet key, encrypt the plaintext, and return the ciphertext. 
However, when you attempt to decrypt the ciphertext using `decrypt_text` in a different session, a new Fernet key is generated because `text_key` is not persisted across different runs of the script.

As a result, the newly generated Fernet key in the decryption session is different from the one used during encryption, causing the decryption to fail and raising an exception.

To resolve this issue, you need to ensure that the same Fernet key is used for both encryption and decryption. 
There are a couple of ways to achieve this:

1. Persist the Fernet key: Save the generated Fernet key (`text_key`) to a secure location (e.g., a file or a database) after generating it.
Then, when you want to decrypt the ciphertext, retrieve the key from the storage and use it for decryption.

2. Generate the Fernet key once and reuse it: Instead of generating a new Fernet key each time the script runs, generate it once and store it in a variable or a constant.
This way, the same key will be used for encryption and decryption within the same session.

Choose the approach that best suits your needs and modify your code accordingly to ensure consistent encryption and decryption with the same Fernet key.
"""

def encrypt_text(plaintext):
	# Convert plaintext to bytes
	plaintext = plaintext.encode()

	# Encrypt the plaintext and return the ciphertext
	ciphertext = fernet.encrypt(plaintext)
	return ciphertext.decode()


def decrypt_text(ciphertext):
	# Convert the ciphertext from string to bytes
	ciphertext = ciphertext.encode()

	# Decrypt the ciphertext and return the plaintext
	try:
		plaintext = fernet.decrypt(ciphertext)
		return plaintext.decode()
	except Exception as err:
		from .printutils import indah4
		indah4(f"Gagal: [{err}]. Mungkin terbalik decoded di encrypt? atau plain di decrypt?", warna='red')
		return f"Gagal: [{err}]. Mungkin terbalik decoded di encrypt? atau plain di decrypt?"


def sample_text():
	# Example usage
	plaintext = 'This is a secret message.'
	ciphertext = encrypt_text(plaintext)
	print(ciphertext)
	decrypted_text = decrypt_text(ciphertext)
	print(decrypted_text)


def encrypt_video(input_path, output_path=None):
	if not output_path:
		no_ext, ext = os.path.splitext(input_path)
		output_path = no_ext + '_wieked' + ext
	with open(input_path, 'rb') as f:
		plaintext = f.read()

	cipher = AES.new(KEY, AES.MODE_CBC, IV)
	ciphertext = cipher.encrypt(pad(plaintext, AES.block_size))

	with open(output_path, 'wb') as f:
		f.write(ciphertext)
	return output_path


def decrypt_video(input_path, output_path=None):
	if not output_path:
		no_ext, ext = os.path.splitext(input_path)
		output_path = no_ext + '_gaiaed' + ext
	with open(input_path, 'rb') as f:
		ciphertext = f.read()

	cipher = AES.new(KEY, AES.MODE_CBC, IV)
	plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)

	with open(output_path, 'wb') as f:
		f.write(plaintext)
	return output_path


def save_and_encrypt_video(url, save_dir):
	r = requests.get(url)
	filename = os.path.join(save_dir, 'video.mp4')
	with open(filename, 'wb') as f:
		f.write(r.content)
	encrypted_filename = os.path.join(save_dir, 'video_encrypted.mp4')
	encrypt_video(filename, encrypted_filename)


def play_decrypted_video(video_path):
	p = vlc.MediaPlayer(video_path)
	p.play()
	input('Press any key to stop playback\n')
	p.stop()


def sample_video():
	# Example usage
	url = 'https://sample-videos.com/video123/mp4/720/big_buck_bunny_720p_1mb.mp4'
	save_dir = 'C:/tmp'
	save_and_encrypt_video(url, save_dir)

	decrypted_filename = os.path.join(save_dir, 'video_decrypted.mp4')
	encrypted_filename = os.path.join(save_dir, 'video_encrypted.mp4')
	decrypt_video(encrypted_filename, decrypted_filename)

	play_decrypted_video(decrypted_filename)


def encrypt_image(input_path, output_path=None):
	if not output_path:
		no_ext, ext = os.path.splitext(input_path)
		output_path = no_ext + '_wieked' + ext
	with open(input_path, 'rb') as f:
		plaintext = f.read()
		
	cipher = AES.new(KEY, AES.MODE_CBC, IV)
	ciphertext = cipher.encrypt(pad(plaintext, AES.block_size))
	
	with open(output_path, 'wb') as f:
		f.write(ciphertext)
	return output_path


def decrypt_image(input_path, output_path=None):
	if not output_path:
		no_ext, ext = os.path.splitext(input_path)
		output_path = no_ext + '_gaiaed' + ext
	with open(input_path, 'rb') as f:
		ciphertext = f.read()
		
	cipher = AES.new(KEY, AES.MODE_CBC, IV)
	plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)
	
	with open(output_path, 'wb') as f:
		f.write(plaintext)
	return output_path


def save_and_encrypt_image(url, file_from_url, file_encrypted):
	r = requests.get(url)
	#filename = os.path.join(save_dir, 'image.jpg')
	with open(file_from_url, 'wb') as f:
		f.write(r.content)
	encrypt_image(file_from_url, file_encrypted)


def sample_image():
	# hasil simpan dari url
	file_from_url = 'c:/tmp/file_from_url.jpg'
	# hasil dekripsi
	file_decrypted = 'c:/tmp/file_decrypted.jpg'
	# hasil enkripsi
	file_encrypted = f'{file_decrypted}.enc'
	save_and_encrypt_image('https://picsum.photos/id/132/800/600', file_from_url, file_encrypted)
	decrypt_image(file_encrypted, file_decrypted)
	Image.open(file_decrypted).show()


def enkripsi(text, tampilkan=False):
	# pylint: disable=import-outside-toplevel
	# pylint: disable=unused-import
	from schnell.app.envutils import env_exist
	from schnell.app.dirutils import joiner
	from schnell.app.printutils import indah3, indah4
	result = None
	if not env_exist("ULIBPY_KEY_IV") or not env_exist("ULIBPY_FERNET_KEY"):
		from constants import sidoarjodir
		load_dotenv(joiner(sidoarjodir, "schnell/.env"))
	# text = request.removeprefix("enc=").strip()
	if text:
		result = encrypt_text(text)
		if tampilkan:
			indah3(result, warna="green")
	result = None


# from schnell.app.cryptoutils import dekripsi
def dekripsi(text, tampilkan=False):
	# pylint: disable=import-outside-toplevel
	# pylint: disable=unused-import
	from schnell.app.envutils import env_exist
	from schnell.app.dirutils import joiner
	from schnell.app.printutils import indah3, indah4
	result = None
	if not env_exist("ULIBPY_KEY_IV") or not env_exist("ULIBPY_FERNET_KEY"):
		from constants import sidoarjodir
		load_dotenv(joiner(sidoarjodir, "schnell/.env"))
	# text = request.removeprefix("dec=").strip()
	if text:
		result = decrypt_text(text)
		if tampilkan:
			indah3(result, warna="green")
	return result


if __name__ == '__main__':
	text_key = Fernet.generate_key()
	print(text_key)
