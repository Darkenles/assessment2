import requests

def handleRequest(request):
    try:
        response = requests.get(request.environ['API_URL'])
        data = response.json()
        return data, 200
    except Exception as e:
        print(f"Error: {e}")
        return "Internal Server Error", 500