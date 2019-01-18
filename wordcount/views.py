from django.shortcuts import render
import operator

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def result(request):
    text = request.GET['fulltext']
    words = text.split()
    word_dictionary = {}

    for word in words:
        if word in word_dictionary:
            #increase
            word_dictionary[word]+=1
        else:
            # add to dictionary
            word_dictionary[word]=1

    sorted_dic = sorted(word_dictionary.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, 'result.html', {'full': text, 'total' : len(words), 'dictionary' : sorted_dic})    
