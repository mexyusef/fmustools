import cloudinary
import cloudinary.uploader
import requests

def upload_to_imgur(image_path, client_id):
    """Uploads an image to Imgur and returns the URL."""
    headers = {'Authorization': f'Client-ID {client_id}'}
    url = "https://api.imgur.com/3/upload"

    with open(image_path, 'rb') as image_file:
        response = requests.post(url, headers=headers, files={'image': image_file})

    if response.status_code == 200:
        data = response.json()
        return data['data']['link']  # Image URL
    else:
        raise Exception(f"Error uploading to Imgur: {response.status_code} {response.text}")

def upload_to_imagebb(image_path, api_key):
    """Uploads an image to ImageBB and returns the URL."""
    url = "https://api.imgbb.com/1/upload"

    with open(image_path, 'rb') as image_file:
        payload = {
            'key': api_key,
            'image': image_file.read()
        }
        response = requests.post(url, data=payload)

    if response.status_code == 200:
        data = response.json()
        return data['data']['url']  # Image URL
    else:
        raise Exception(f"Error uploading to ImageBB: {response.status_code} {response.text}")

def upload_to_postimage(image_path, token):
    """Uploads an image to PostImage and returns the URL."""
    url = "https://postimages.org/json"
    files = {'file': open(image_path, 'rb')}
    payload = {'token': token, 'upload_session': 'your-session'}
    response = requests.post(url, files=files, data=payload)

    if response.status_code == 200:
        data = response.json()
        return data['url']  # Image URL
    else:
        raise Exception(f"Error uploading to PostImage: {response.status_code} {response.text}")

def upload_to_cloudinary(image_path, cloud_name, api_key, api_secret):
    """Uploads an image to Cloudinary and returns the URL."""
    cloudinary.config(
        cloud_name=cloud_name,
        api_key=api_key,
        api_secret=api_secret
    )

    result = cloudinary.uploader.upload(image_path)
    if 'url' in result:
        return result['url']  # Image URL
    else:
        raise Exception("Error uploading to Cloudinary")

def upload_image(service, image_path, **kwargs):
    """
    Uploads an image using the specified service (imgur, imagebb, postimage, cloudinary).
    :param service: The image hosting service ('imgur', 'imagebb', 'postimage', 'cloudinary').
    :param image_path: Path to the image file.
    :param kwargs: Additional arguments like API keys or tokens.
    :return: URL of the uploaded image.
    """
    if service == 'imgur':
        return upload_to_imgur(image_path, kwargs.get('client_id'))
    elif service == 'imagebb':
        return upload_to_imagebb(image_path, kwargs.get('api_key'))
    elif service == 'postimage':
        return upload_to_postimage(image_path, kwargs.get('token'))
    elif service == 'cloudinary':
        return upload_to_cloudinary(image_path, kwargs.get('cloud_name'), kwargs.get('api_key'), kwargs.get('api_secret'))
    else:
        raise ValueError(f"Unsupported service: {service}")
