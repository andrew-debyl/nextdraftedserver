from django.http import JsonResponse
from django.contrib.auth import login, authenticate
import json
from django.views.decorators.csrf import csrf_exempt
import logging
from django.contrib.auth.models import User
from django.contrib.auth import logout
from myproject.models import Athlete, Recruiter, SportPortfolio, SportPortfolioItem
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import AthleteSerializer, RecruiterSerializer, SportPortfolioSerializer, SportPortfolioItemSerializer
from django.shortcuts import get_object_or_404


logger = logging.getLogger(__name__)

@csrf_exempt
def login_user(request):
    data = json.loads(request.body)
    username = data['username']
    password = data['password']
    
    user = authenticate(username=username, password=password)
    data = {"username": username}

    if user is not None:
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
        user = get_object_or_404(User, username=username)

        if hasattr(user, 'athlete'):
            athlete = user.athlete
            serializer = AthleteSerializer(athlete)
            return JsonResponse(serializer.data)

        elif hasattr(user, 'recruiter'):
            recruiter = user.recruiter
            serializer = RecruiterSerializer(recruiter) 
            return JsonResponse(serializer.data)

        return JsonResponse({"error": "Profile not found"}, status=404)

    except User.DoesNotExist:
        return JsonResponse({"error": "User not found"}, status=404)


class ProfileUpdateView(APIView):
    def put(self, request, username):
        user = get_object_or_404(User, username=username)

        try:
            athlete = Athlete.objects.get(user=user)
            data = request.data.copy()

            if 'profile_picture' in request.FILES:
                # A file was uploaded, let the serializer handle it
                pass
            elif data.get('profile_picture') == 'null':
                # No file uploaded, and 'null' was sent, keep the existing picture
                data.pop('profile_picture') # remove profile_picture from data, so the serializer doesn't change it.

            athlete_serializer = AthleteSerializer(athlete, data=data, partial=True)

            if athlete_serializer.is_valid():
                athlete_serializer.save()
                return Response({"message": "Athlete profile updated successfully"}, status=status.HTTP_200_OK)
            else:
                print(f"Serializer errors for {username}: {athlete_serializer.errors}")
                return Response(athlete_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Athlete.DoesNotExist:
            try:
                recruiter = Recruiter.objects.get(user=user)
                data = request.data.copy()

                if 'profile_picture' in request.FILES:
                    pass
                elif data.get('profile_picture') == 'null':
                    data.pop('profile_picture')

                recruiter_serializer = RecruiterSerializer(recruiter, data=data, partial=True)

                if recruiter_serializer.is_valid():
                    recruiter_serializer.save()
                    return Response({"message": "Recruiter profile updated successfully"}, status=status.HTTP_200_OK)
                else:
                    print(f"Serializer errors for {username}: {recruiter_serializer.errors}")
                    return Response(recruiter_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            except Recruiter.DoesNotExist:
                return Response({"error": "User is neither an athlete nor a recruiter"}, status=status.HTTP_404_NOT_FOUND)
            

def get_portfolios(request, username):
    try:
        user = get_object_or_404(User, username=username)

        if hasattr(user, 'athlete'):
            athlete = user.athlete
            portfolios = SportPortfolio.objects.filter(athlete=athlete)
            serializer = SportPortfolioSerializer(portfolios, many=True) # Serialize a list
            data = serializer.data
            return JsonResponse({
                'first_name': athlete.first_name,
                'last_name': athlete.last_name,
                'portfolios': data,
            }, safe=False)

        elif hasattr(user, 'recruiter'):
            # Recruiters don't have SportPortfolios, so return an empty list or an error
            return JsonResponse([], safe=False) # Or: return JsonResponse({"error": "Recruiters do not have portfolios."}, status=400)

        return JsonResponse({"error": "Profile not found"}, status=404)

    except User.DoesNotExist:
        return JsonResponse({"error": "User not found"}, status=404)
    


def get_portfolio(request, username, portfolioId):
    try:
        user = get_object_or_404(User, username=username)

        if hasattr(user, 'athlete'):
            athlete = user.athlete
            portfolio = get_object_or_404(SportPortfolio, athlete=athlete, id=portfolioId)
            serializer = SportPortfolioSerializer(portfolio)
            portfolio_data = serializer.data

            items = SportPortfolioItem.objects.filter(sport_portfolio=portfolio).order_by('order')
            item_serializer = SportPortfolioItemSerializer(items, many=True)
            item_data = item_serializer.data

            return JsonResponse({
                'first_name': athlete.first_name,
                'last_name': athlete.last_name,
                'portfolios': portfolio_data,
                'items': item_data,
            }, safe=False)
        elif hasattr(user, 'recruiter'):
            return JsonResponse([], safe=False)

        return JsonResponse({"error": "Profile not found"}, status=404)

    except User.DoesNotExist:
        return JsonResponse({"error": "User not found"}, status=404)