from django.shortcuts import render

posts = [
    {
        'author': 'Jonas Pettersson',
        'title': 'Blog post 1',
        'content': 'First post contents',
        'date_posted': 'May 5, 2020'
    },
    {
        'author': 'Tanja Pettersson',
        'title': 'Blog post 2',
        'content': 'Second post contents',
        'date_posted': 'May 6, 2020'
    }
]


def home(request):
    context = {'posts': posts}
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html')
