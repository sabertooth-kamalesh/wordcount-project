import operator
from django.http import HttpResponse,JsonResponse
from django.shortcuts import render



def homepage(request):
    return render(request, 'home.html')

    # return 'Hello'


def about(request):
    return render(request, 'about.html')


def count(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()

    worddictionary = {}

    for word in wordlist:
        if word in worddictionary:
            worddictionary[word] += 1
        else:
            worddictionary[word] = 1

    sortedword = sorted(worddictionary.items(), key= operator.itemgetter(1), reverse=True)

    return render(request, 'count.html', {'fulltext': fulltext, 'count': len(wordlist), 'sortedword': sortedword})
