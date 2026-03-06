import json

from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

# Create your views here.
@csrf_exempt
@require_POST
def login_user(request):
    try:
        data = json.loads(request.body or "{}")
    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON"}, status=400)

    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return JsonResponse({"error": "username and password are required"}, status=400)

    user = authenticate(username=username, password=password)

    if user:
        login(request, user)
        return JsonResponse({"message": "Login successful"})
    return JsonResponse({"error": "Invalid credentials"}, status=400)

@csrf_exempt
@require_POST
def logout_user(request):
    logout(request)
    return JsonResponse({"message":"logged out"})