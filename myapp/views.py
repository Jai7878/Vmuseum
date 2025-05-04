from django.shortcuts import render
from .models import NewsletterSubscription, ContactQuery

# Create your views here.

# def problem_statement(request):
#     return render(request,"problem_statement.html")

# def service_details(request):
#     return render(request,"service-details.html")

# def login_page(request):
#     return render(request, "login.html")
 
def index(request):
    return render(request, 'index.html')


def contact(request):
    return render(request, 'contact.html')


def gallery(request):
    return render(request, 'gallery.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def starter(request):
    return render(request, 'starter.html')

def gallerys(request):
    return render(request, 'gallerys.html')


from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from .models import NewsletterSubscription, ContactQuery

def subscribe_newsletter(request):
    if request.method == "POST":
        email = request.POST.get("email")

        if not email:
            return JsonResponse({"success": False, "error": "Email field cannot be empty."})

        if NewsletterSubscription.objects.filter(email=email).exists():
            return JsonResponse({"success": False, "error": "This email is already subscribed."})

        NewsletterSubscription.objects.create(email=email)
        return JsonResponse({"success": True, "message": "You have subscribed successfully!"})

    return JsonResponse({"success": False, "error": "Invalid request method."})

def unsubscribe_newsletter(request):
    token = request.GET.get("token")

    if not token:
        return HttpResponse("Invalid request.", status=400)

    try:
        subscription = NewsletterSubscription.objects.get(unsubscribe_token=token)
        subscription.delete()
        return HttpResponse("You have been unsubscribed successfully.")
    except NewsletterSubscription.DoesNotExist:
        return HttpResponse("Invalid or expired unsubscribe link.", status=400)

def submit_contact_form(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        if name and email and message and subject:
            ContactQuery.objects.create(name=name, email=email, message=message, subject=subject)
            return JsonResponse({"success": True, "message": "Your query has been received successfully!"})
        else:
            return JsonResponse({"success": False, "error": "All fields are required!"})

    return JsonResponse({"success": False, "error": "Invalid request method."})


@login_required(login_url='/login/')
def admin_dashboard(request):
    newsletter_data = NewsletterSubscription.objects.all()
    query_data = ContactQuery.objects.all()
    return render(request, "dashboard.html", {
        "newsletter_data": newsletter_data,
        "query_data": query_data
    })

def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("admin-dashboard")
        else:
            return render(request, "login.html", {
                "error": "Invalid username or password."
            })
    

def user_logout(request):
    logout(request)
    return redirect("login")

# ======================= Normal pages =======================

# Create your views here.
