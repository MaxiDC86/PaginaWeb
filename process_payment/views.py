from django.shortcuts import render

# Create your views here.
def process_payment(request):

    print("hello payment")
    print(request)

    return render(request,"PaginaWebApp/home.html" )