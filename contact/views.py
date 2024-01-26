from .models import GoogleAppsScript
from django.shortcuts import render, redirect
from django.contrib import messages
import requests

def contact_us(request):
    if request.method == 'POST':
        name = request.POST.get('your_name')
        number = request.POST.get('your_number')
        email = request.POST.get('your_email')
        message = request.POST.get('message')

        data = {
            'your-name': name,
            'your-number': number,
            'your-email': email,
            'message': message
        }

        google_apps_script = GoogleAppsScript.objects.first()

        if google_apps_script and google_apps_script.url:
            response = requests.post(google_apps_script.url, data=data)

            if response.status_code == 200:
                messages.success(request, '')
            else:
                messages.error(request, 'Error submitting form')
        else:
            messages.error(request, 'Google Apps Script URL not found')

        return redirect('contact-us')

    return render(request, 'contact-us.html')