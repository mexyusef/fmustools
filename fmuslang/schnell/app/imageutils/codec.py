import base64


# from schnell.app.imageutils.codec import encode_image_to_base64
def encode_image_to_base64(image_path):
    """
    Encodes a PNG image as a base64 string.
    
    Args:
        image_path (str): The file path of the PNG image.
        
    Returns:
        str: The base64-encoded string representation of the image.
    """
    # with open(image_path, "rb") as image_file:
    #     encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
    # return encoded_string
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

def test_encode_image_to_base64(image_path = "image.png"):
    encoded_image = encode_image_to_base64(image_path)

    json_response = {
        'image_data': encoded_image
    }
    from ..printutils import print_json
    print_json(json_response)
