from django.http import HttpResponse
from django.shortcuts import render
import operator


def homepage(request):
    return render(request, 'home.html', {'hithere': 'This is me'})


def count(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()

    word_dictionary = {}

    for word in wordlist:
        if word in word_dictionary:
            #increase
            word_dictionary[word] += 1

        else:
            # Add to dictionary
            word_dictionary[word] = 1

    sorted_words = sorted(word_dictionary.items(), key=operator.itemgetter(1), reverse= True)
    print(operator.itemgetter(1))



    return render(request, 'count.html', {'fulltext': fulltext, 'count': len(wordlist), 'word_dictionary': sorted_words})


def about(request):
    return render(request, 'about.html')