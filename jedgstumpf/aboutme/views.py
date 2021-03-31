from django.shortcuts import render
# from django.http import HttpResponse


def landing(request):
    return render(request, 'aboutme/landing.html')


def links(request):
    return render(request, 'aboutme/links.html', {'title': 'Links'})


def myblog(request):
    return render(request, 'aboutme/myblog.html', {'title': 'MyBlog'})


def achievements(request):
    return render(request, 'aboutme/achievements.html',
                  {'title': 'Achievements'})
