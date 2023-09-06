from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

monthly_challenges = {
    "january": "This works in january, eat fruits!",
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
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid month")
    
    redirect_month = months[month - 1]

    # dynamic way
    redirect_path = reverse("month-challenge", args=[redirect_month]) #/challenges/january
    return HttpResponseRedirect(redirect_path)

    # static way
    """return HttpResponseRedirect("/challenges/" + redirect_month)"""

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        responde_data = f"<h1>{challenge_text}</h1>"
        return HttpResponse(responde_data)
    except:
        return HttpResponseNotFound("<h1>This month is not supported!</h1>")

    """if month == 'january':
        return HttpResponse("This works in january, eat fruits!")
    elif month == 'february':
        return HttpResponse("This works in february, study atleast 20 minutes")
    elif month == 'march':
        return HttpResponse("This works in march, eat veggies")
    else:
        return HttpResponseNotFound("this month is not registered")"""
    
