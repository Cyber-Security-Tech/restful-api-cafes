API_KEY = "TopSecretAPIKey"

def is_authorized(request):
    user_key = request.headers.get("x-api-key")
    return user_key == API_KEY
