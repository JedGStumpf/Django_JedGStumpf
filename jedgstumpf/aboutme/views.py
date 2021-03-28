from django.shortcuts import render
# from django.http import HttpResponse


def landing(request):
    return render(request, 'aboutme/landing.html')


def links(request):
    return render(request, 'aboutme/links.html', {'title': 'Links'})


def resume(request):
    return render(request, 'aboutme/resume.html', {'title': 'Resume'})


def achievements(request):
    return render(request, 'aboutme/achievements.html',
                  {'title': 'Achievements'})
