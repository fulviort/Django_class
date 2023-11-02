from datetime import date
from django.shortcuts import render

all_posts = [
    {
        "slug": "hike-in-the-mountain",
        "image": "mountains.jpg",
        "author": "Fulvio",
        "date": date(2023, 9, 8),
        "title": "Mountain Hiking",
        "excerpt": "There's nothing like the views from the mountains, and guess what? i wasn't even prepared for it.",
        "content": """
            Lorem ipsum dolor sit amet consectetur, adipisicing elit.
            Deleniti labore aliquid itaque, incidunt fuga est illum doloremque earum reprehenderit? 
            Maiores esse odio nostrum ducimus obcaecati numquam voluptate, dolorum ea officiis!
        """
    },
    {
        "slug": "programming-is-fun",
        "image": "coding.jpg",
        "author": "Fulvio",
        "date": date(2023, 9, 9),
        "title": "Programming is GREAT!",
        "excerpt": "Have you ever experienced the programming error that made you spent hours searching for the solution and find it at some point.",
        "content": """
            Lorem ipsum dolor sit amet consectetur, adipisicing elit.
            Deleniti labore aliquid itaque, incidunt fuga est illum doloremque earum reprehenderit? 
            Maiores esse odio nostrum ducimus obcaecati numquam voluptate, dolorum ea officiis!
        """
    },
    {
    "slug": "xes-is-fun",
        "image": "woods.jpg",
        "author": "XSY",
        "date": date(2023, 10, 10),
        "title": "XES is GREAT!",
        "excerpt": "This is the most incredible thought",
        "content": """
            Lorem ipsum dolor sit amet consectetur, adipisicing elit.
            Deleniti labore aliquid itaque, incidunt fuga est illum doloremque earum reprehenderit? 
            Maiores esse odio nostrum ducimus obcaecati numquam voluptate, dolorum ea officiis!
        """
    }
] # type: ignore

def get_date(post):
    return post['date']

# Create your views here

def starting_page(request):
    sorted_posts = sorted(all_posts, key=get_date)
    latest_posts = sorted_posts[-3:]
    return render(request, "blog/index.html", {
        "posts": latest_posts
    })

def posts(request):
    return render(request, "blog/all-posts.html")

def detailed_post(request, slug):
    return render(request, "blog/post-detail.html")