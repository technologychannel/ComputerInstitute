from django.shortcuts import render
from django.http import HttpResponse
from .models import Contact
from .forms import ContactForm

# Create your views here.
def index(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            # Show js alert
            return HttpResponse('<script>alert("Your message has been sent successfully!");</script>')
    else:
        form = ContactForm()
    return render(request, 'mainapp/index.html', {'form': form})