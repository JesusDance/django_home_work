import os

from django.http import HttpResponse
import base64

class BasicAuthMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.username = os.getenv("AUTH_USERNAME")
        self.password = os.getenv("AUTH_PASSWORD")

    def __call__(self, request):
        auth = request.META.get('HTTP_AUTHORIZATION')
        if auth:
            method, data = auth.split(' ', 1)
            if method.lower() == "basic":
                decoded = base64.b64decode(data).decode()
                username, password = decoded.split(":", 1)
                if username == self.username and password == self.password:
                    return self.get_response(request)
        response = HttpResponse("Unauthorized", status=401)
        response['WWW-Authenticate'] = 'Basic realm="Demo"'
        return response
