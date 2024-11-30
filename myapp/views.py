from django.shortcuts import render, redirect
from .forms import ContactFeedbackForm
from django.core.mail import send_mail
from django.conf import settings

def home(request):
    context = {
        'site_name': 'Rayzin Media',
        'hero_title': 'Unleash Your Creativity',
        'hero_subtitle': 'Your Partner in Professional Graphic Design',
    }
    return render(request, '../index.html', context)

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def logo_design(request):
    return render(request, 'logo_design.html')

def branding(request):
    return render(request, 'branding.html')

def web_design(request):
    return render(request, 'web_design.html')

def social_media(request):
    return render(request, 'social_media.html')

def print_design(request):
    return render(request, 'print_design.html')

def contact(request):
    if request.method == 'POST':
        form = ContactFeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save()
            try:
                # Send email to the admin after form submission
                send_mail(
                    subject=f"New Contact Feedback from {feedback.name}",
                    message=feedback.message,
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=['maxwel.cheruiyot3790@gmail.com'],  # Your admin email
                    fail_silently=False,
                    headers={'Reply-To': feedback.email},  # Include sender's email as reply-to
                )
            except Exception as e:
                print(f"Error sending email: {e}")
            return redirect('my_contact_success')  # Redirect to success page
    else:
        form = ContactFeedbackForm()
    return render(request, 'contact.html', {'form': form})

def contact_success(request):
    return render(request, 'contact_success.html')
