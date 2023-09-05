from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

monthly_challenges = {
    "january:": "This works in january, eat fruits!",
    "february": "This works in february, study atleast 20 minutes",
    "march": "This works in march, eat veggies",
    "april": "This works in march, eat veggies",
    "may": "This works in march, eat veggies5",
    "june": "This works in march, eat veggies6",
    "july": "This works in march, eat veggies7",
    "august": "This works in march, eat veggies8",
    "september": "This works in march, eat veggies9",
    "october": "This works in march, eat veggies10",
    "november": "This works in march, eat veggies11",
    "december": "This works in march, eat veggies12"
}

# Create your views here.


def test1(request):
    return HttpResponse("test1")


def test2(request):
    return HttpResponse("test2")


def test3(request):
    return HttpResponse("test3")


def monthly_challenges_by_number(request, month):
    return HttpResponse(month)

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound("This month is not supported!")

    """if month == 'january':
        return HttpResponse("This works in january, eat fruits!")
    elif month == 'february':
        return HttpResponse("This works in february, study atleast 20 minutes")
    elif month == 'march':
        return HttpResponse("This works in march, eat veggies")
    else:
        return HttpResponseNotFound("this month is not registered")"""
    
