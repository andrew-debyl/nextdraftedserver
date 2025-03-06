from django.http import JsonResponse
from django.contrib.auth import login, authenticate
import json
from django.views.decorators.csrf import csrf_exempt
import logging
from django.contrib.auth.models import User
from django.contrib.auth import logout


logger = logging.getLogger(__name__)


@csrf_exempt
def login_user(request):
    # Get username and password from request.POST dictionary
    data = json.loads(request.body)
    username = data['username']
    password = data['password']
    # Try to check if provide credential can be authenticated
    user = authenticate(username=username, password=password)
    data = {"username": username}
    if user is not None:
        # If user is valid, call login method to login current user
        login(request, user)
        data = {"username": username, "status": "Authenticated"}
    return JsonResponse(data)

@csrf_exempt
def signup_user(request):
    data = json.loads(request.body)
    username = data['username']
    password = data['password']
    username_exist = False

    try:
        # Check if user already exists
        User.objects.get(username=username)
        username_exist = True
    except:
        # If doesnt exist
        logger.debug("{} is new user".format(username))

    # If not a new user
    if not username_exist:
        user = User.objects.create_user(username=username,password=password)
        login(request, user)
        data = {"username": username, "status": "Authenticated"}
        return JsonResponse(data)
    else:
        data = {"username": username, "status": "User already exists"}
        return JsonResponse(data)
    
def logout_request(request):
    logout(request)
    data = {"username":""}
    return JsonResponse(data)