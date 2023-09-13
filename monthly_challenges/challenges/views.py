from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, Http404
from django.urls import reverse
from django.template.loader import render_to_string

monthly_challenges = {
    "january": "This works in january, eat fruits!",
    "february": "This works in february, study atleast 20 minutes",
    "march": "This works in march, eat veggies",
    "april": "This works in march, eat veggies",
    "may": "This works in may, eat veggies5",
    "june": "This works in june, eat veggies6",
    "july": "This works in july, eat veggies7",
    "august": "This works in august, eat veggies8",
    "september": "This works in september, eat veggies9",
    "october": "This works in october, eat veggies10",
    "november": "This works in november, eat veggies11",
    "december": None,
    "drug test": "This works in drug test, eat veggies12"
}

# Create your views here.


def index(request):
    months = list(monthly_challenges.keys())

    return render(request, "challenges/index.html", {
        "months": months
    })

    # old way
    """for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("month-challenge", args=[month])
        list_items += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"

    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)"""


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
    # /challenges/january
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)

    # static way
    """return HttpResponseRedirect("/challenges/" + redirect_month)"""


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]

        # shorter way
        """return render(request, "challenges/challenge.html")"""
        return render(request, "challenges/challenge.html", {
            "text": challenge_text,
            "mes": month
        })

        # longer way
        """responde_data = render_to_string("challenges/challenge.html")"""
        """return HttpResponse(responde_data)"""
    except:
        # short way
        raise Http404()

        # long way
        """error_response = render_to_string("404.html")
        return HttpResponseNotFound(error_response)"""
