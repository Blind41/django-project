from django.shortcuts import render

# Create your views here.

def hello(request):
    return render(request, """
    <h1> HOLAAAA YA FUNCIONA </h1>
    """)
