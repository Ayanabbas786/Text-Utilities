# This file is created by me - Ayan

from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def analyze(request):
    text = request.POST.get('userText', 'no text')
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    capitalizefirst = request.POST.get('capitalizefirst', 'off')
    lowerall = request.POST.get('lowerall', 'off')
    removenewline = request.POST.get('removenewline', 'off')
    removeextraspace = request.POST.get('removeextraspace', 'off')
    charcount = request.POST.get('charcount', 'off')
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

    if removepunc == 'on':
        analyzed_text = ""
        for char in text:
            if char not in punctuations:
                analyzed_text = analyzed_text + char
        text = analyzed_text

    if fullcaps == 'on':
        analyzed_text = ""
        analyzed_text = text.upper()
        text = analyzed_text

    if capitalizefirst == 'on':
        analyzed_text = ""
        analyzed_text = text.capitalize()
        text = analyzed_text

    if lowerall == 'on':
        analyzed_text = ""
        analyzed_text = text.lower()
        text = analyzed_text

    if removenewline == 'on':
        analyzed_text = ""
        for char in text:
            if char != '\n' and char != '\r':
                analyzed_text = analyzed_text + char
        text = analyzed_text

    if removeextraspace == 'on':
        analyzed_text = ""
        for index, char in enumerate(text):
            if not(text[index] == " " and text[index + 1] == " "):
                analyzed_text = analyzed_text + char
        text = analyzed_text

    if charcount == 'on':
        analyzed_text = ""
        analyzed_text = f"Number of characters(including space) in your text after doing the changes is {len(text)}"

    if text == "":
        return HttpResponse('<h1>Error! No input is given.</h1>')
    elif removepunc == 'off' and fullcaps == 'off' and capitalizefirst == 'off' and lowerall == 'off' and removenewline == 'off' and removeextraspace == 'off' and charcount == 'off':
        return HttpResponse('<h1>Error! No option is chosen.</h1>')
    else:
        params = {'analyzed': analyzed_text}
        return render(request, 'analyze.html', params)
