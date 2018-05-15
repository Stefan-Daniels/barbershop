from django.shortcuts import render

# Create your views here.
def home_page(request):
    if request.method == "POST":
        
        post_dict = request.POST
        customer_name = post_dict.get("customer_name")
        time = post_dict.get("time")
        barber_name = post_dict.get("barber_name")

        context = {"time": time, "barber_name": barber_name, "customer_name": customer_name}

        return render(request, "appointment/home_page.html", context)
    if request.method == "GET":
        return render(request, "appointment/home_page.html")