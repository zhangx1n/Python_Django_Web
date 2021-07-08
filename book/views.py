from django.shortcuts import render
from django.http import HttpResponse
from book.models import BookInfo, PeopleInfo

# Create your views here.

def index(request):

    book = BookInfo.objects.all()
    people = PeopleInfo(
        name='猪八戒',
        gender=0,
        book_id=1

    )
    context = {
        'books': book,

    }

    return render(request, 'index.html', context=context)