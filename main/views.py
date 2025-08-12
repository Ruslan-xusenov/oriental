from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import send_mail
from django.contrib import messages
from django.contrib.auth import login, logout
from django.conf import settings
from .models import Country, Institution, News
from .forms import ContactForm, RegisterForm

def home(request):
    countries = Country.objects.all()
    latest_news = News.objects.all()[:3]
    return render(request, "main/home.html", {
        "countries": countries,
        "latest_news": latest_news
    })

def about(request):
    return render(request, "main/about.html")

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            
            send_mail(
                subject,
                f"Message from {name} ({email}):\n\n{message}",
                settings.DEFAULT_FROM_EMAIL,
                ["qabuloriental@gmail.com"],
                fail_silently=False,
            )
            
            return redirect('success_page')
    else:
        form = ContactForm()
    
    return render(request, 'main/contact.html', {'form': form})

def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            send_mail(
                subject=f"{subject} - {name}",
                message=f"Yuboruvchi: {name}\nEmail: {email}\n\nXabar:\n{message}",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=["sizning_emailingiz@gmail.com"],  # o‘zingizning emailingiz
                fail_silently=False,
            )

            messages.success(request, "Xabaringiz muvaffaqiyatli yuborildi!")
            return redirect("contact")
    else:
        form = ContactForm()

    return render(request, "main/contact.html", {"form": form})

def success_page(request):
    return render(request, "main/contact_success.html")

from django.shortcuts import render
from .models import Institution, Country

def countries_list(request):
    country_id = request.GET.get('country')
    institutions = Institution.objects.all()
    if country_id:
        institutions = institutions.filter(country_id=country_id)
    countries = Country.objects.all()
    context = {
        'institutions': institutions,
        'countries': countries,
        'selected_country_id': int(country_id) if country_id else None,
    }
    return render(request, 'main/countries_list.html', context)

def institutions_by_country(request, country_id):
    country = get_object_or_404(Country, id=country_id)
    institutions = Institution.objects.filter(country=country)
    context = {
        'country': country,
        'institutions': institutions,
    }
    return render(request, 'institutions_by_country.html', context)

def institution_detail(request, pk):
    institution = get_object_or_404(Institution, pk=pk)
    return render(request, 'institution_detail.html', {'institution': institution})

def about(request):
    return render(request, "main/about.html")

def news_list(request):
    news_items = News.objects.all()
    return render(request, "main/news_list.html", {"news_items": news_items})

def news_detail(request, pk):
    news = get_object_or_404(News, pk=pk)
    return render(request, "main/news_detail.html", {"news": news})

def logout_view(request):
    logout(request)  # Foydalanuvchi sessiyasini tozalash
    return redirect('home')

def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
    else:
        form = RegisterForm()
    return render(request, "register.html", {"form": form})

def countries_overview(request):
    countries = Country.objects.all()
    return render(request, 'countries_overview.html', {'countries': countries})