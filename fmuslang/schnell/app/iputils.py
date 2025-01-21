import requests

def get_public_ip():
    try:
        # Use the ipify API to get your public IP address
        response = requests.get("https://api.ipify.org?format=json")
        
        # Check if the request was successful
        if response.status_code == 200:
            data = response.json()
            return data['ip']
        else:
            print("Failed to retrieve IP address.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Your public IP address is: 180.251.235.102
if __name__ == "__main__":
    public_ip = get_public_ip()
    if public_ip:
        print(f"Your public IP address is: {public_ip}")
