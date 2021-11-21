from random import randint

from django.http import HttpResponse
import requests
from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics



# Create your views here.
from tablesapi.models import Pictures
from .filters import PictureFilter
from .pagination import StandardResultsSetPagination

from .serializers import PicturesSerializer


class PicturesList(generics.ListAPIView):
    queryset = Pictures.objects.all()
    serializer_class = PicturesSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = [DjangoFilterBackend]
    filterset_class = PictureFilter


def index(request):

    # print('---photos----')
    # r = requests.get('https://jsonplaceholder.typicode.com/photos')
    # photos = r.json()
    # for i in range(0, 5):
    #     print(photos[i])
    # print('Длина = ' + str(len(photos)))
    #
    # print('---users----')
    # r = requests.get('http://fakeapi.jsonparseronline.com/users')
    # users = r.json()
    # for i in range(0, 5):
    #     print(users[i])
    # print('Длина = ' + str(len(users)))
    #
    # print('---albums----')
    # r = requests.get('https://jsonplaceholder.typicode.com/albums')
    # albums = r.json()
    # for i in range(0, 5):
    #     print(albums[i])
    # print('Длина = ' + str(len(albums)))
    #
    # result = []
    # for i in range (0, len(photos)):
    #     random_photo = photos[randint(0, len(photos) - 1)]
    #     random_album = albums[randint(0, len(albums) - 1)]
    #     random_user = users[randint(0, len(users) - 1)]
    #     result.append({
    #         'uid': str(random_photo['id']),
    #         'title': random_photo['title'],
    #         'url': random_photo['url'],
    #         'thumbnailUrl': random_photo['thumbnailUrl'],
    #         'album': random_album['title'],
    #         'authorFirstName': random_user['firstName'],
    #         'authorLastName': random_user['lastName'],
    #         'authorUserName': random_user['username'],
    #     })
    # for i in range (0, len(result)):
    #     print('Row: ', i)
    #     pic = Pictures(**result[i])
    #     pic.save()


    # for i in range(0, 5):
    #     print(result[i])
    # print('Длина = ' + str(len(result)))

    # result0 = {
    #     'uid': '2447',
    #     'title': 'voluptatibus cum id numquam suscipit fuga',
    #     'url': 'https://via.placeholder.com/600/ade44d',
    #     'thumbnailUrl': 'https://via.placeholder.com/150/ade44d',
    #     'album': 'omnis neque exercitationem sed dolor atque maxime aut cum',
    #     'authorFirstName': 'Praesent',
    #     'authorLastName': 'Congue',
    #     'authorUserName': 'praesentcongue'}


    return HttpResponse("Hello, world. ")
