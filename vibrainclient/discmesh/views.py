from django.shortcuts import render

# Create your views here.
from django.http import FileResponse

def index(response):

    img = open('static/mesh.png', 'rb')

    response = FileResponse(img)

    return response