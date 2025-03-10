from django.http import JsonResponse
from django.contrib.auth import login, authenticate
import json
from django.views.decorators.csrf import csrf_exempt
import logging
from django.contrib.auth.models import User
from django.contrib.auth import logout
from myproject.models import Athlete, Recruiter


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

        if Athlete.objects.filter(user=user).exists():
            userType = "Athlete"
        elif Recruiter.objects.filter(user=user).exists():
            userType = "Recruiter"

        data = {"username": username, "status": "Authenticated", "userType": userType}
    return JsonResponse(data)


@csrf_exempt
def signup_user(request):
    data = json.loads(request.body)
    username = data['username']
    password = data['password']
    username_exist = False

    try:
        User.objects.get(username=username)
        username_exist = True
    except:
        logger.debug("{} is new user".format(username))

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


@csrf_exempt
def create_role(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        role = data.get('role')

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return JsonResponse({"status": False, "error": "User not found"})

        if role == 'athlete':
            athlete = Athlete.objects.create(user=user)
            athlete.save()
        elif role == 'recruiter':
            recruiter = Recruiter.objects.create(user=user)
            recruiter.save()

        return JsonResponse({"status": True})

    return JsonResponse({"status": False, "error": "Invalid request"})


def get_profile(request, username):
    try:
        user = User.objects.get(username=username)

        try:
            athlete = Athlete.objects.get(user=user)
            profile_data = {
                "username": user.username,
                "first_name": athlete.first_name,
                "last_name": athlete.last_name,
                "sport": athlete.sport,
                "height": athlete.height,
                "weight": athlete.weight,
                "bio": athlete.bio,
                "location": athlete.location,
                "gender": athlete.gender,
                #"profile_picture": athlete.profile_picture.url if athlete.profile_picture else None
            }
            return JsonResponse(profile_data)
        except Athlete.DoesNotExist:
            pass

        try:
            recruiter = Recruiter.objects.get(user=user)
            profile_data = {
                "username": user.username,
                "first_name": recruiter.first_name,
                "last_name": recruiter.last_name,
                "organization": recruiter.organization,
                "title": recruiter.title,
                "bio": recruiter.bio,
                "location": recruiter.location,
                "sport": recruiter.sport,
                "gender": recruiter.gender,
                #"profile_picture": recruiter.profile_picture.url if recruiter.profile_picture else None
            }
            return JsonResponse(profile_data)
        except Recruiter.DoesNotExist:
            pass

        return JsonResponse({"error": "Profile not found"}, status=404)

    except User.DoesNotExist:
        return JsonResponse({"error": "User not found"}, status=404)


@csrf_exempt
def update_profile (request, username):
    try:
        data = json.loads(request.body)
        user = User.objects.get(username=username)

        try:
            athlete = Athlete.objects.get(user=user)

            athlete.first_name = data.get('first_name', athlete.first_name)
            athlete.last_name = data.get('last_name', athlete.last_name)
            athlete.sport = data.get('sport', athlete.sport)
            athlete.height = data.get('height', athlete.height)
            athlete.weight = data.get('weight', athlete.weight)
            athlete.bio = data.get('bio', athlete.bio)
            athlete.location = data.get('location', athlete.location)
            athlete.gender = data.get('gender', athlete.gender)
            athlete.save()

            return JsonResponse({'message': 'Profile updated successfully'}, status=200)

        except Athlete.DoesNotExist:
            try:
                recruiter = Recruiter.objects.get(user=user)

                recruiter.first_name = data.get('first_name', recruiter.first_name)
                recruiter.last_name = data.get('last_name', recruiter.last_name)
                recruiter.organization = data.get('organization', recruiter.organization)
                recruiter.title = data.get('title', recruiter.title)
                recruiter.bio = data.get('bio', recruiter.bio)
                recruiter.location = data.get('location', recruiter.location)
                recruiter.sport = data.get('sport', recruiter.sport)
                athlete.gender = data.get('gender', athlete.gender)
                recruiter.save()

                return JsonResponse({'message': 'Profile updated successfully'}, status=200)

            except Recruiter.DoesNotExist:
                return JsonResponse({"error": "User is neither athlete nor recruiter"}, status=404)

    except User.DoesNotExist:
        return JsonResponse({"error": "User not found"}, status=404)
    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON"}, status=400)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=400)
