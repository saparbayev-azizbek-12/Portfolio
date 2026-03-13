"""
Views for the core app — Single Page Home and Contact submission handling.
"""

from django.views.generic import TemplateView, View
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

from .models import Experience, Project, ContactMessage
from .forms import ContactForm


class HomeView(TemplateView):
    """Single page landing with all sections."""
    template_name = 'core/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['projects'] = Project.objects.all()
        context['experiences'] = Experience.objects.all()
        context['form'] = ContactForm()
        return context


class ContactSubmitView(View):
    """Handle contact form submission via POST."""
    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save()
            try:
                send_mail(
                    subject=f'Portfolio Contact: {contact.name}',
                    message=f"From: {contact.name} ({contact.email})\n\n{contact.message}",
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[settings.CONTACT_EMAIL],
                    fail_silently=False,
                )
                messages.success(request, 'Thank you! Your message has been sent successfully.')
            except Exception as e:
                # Log the error to console for debugging purposes
                print(f"Error sending email: {e}")
                messages.success(request, 'Your message was saved, but we encountered an issue sending the email notification. Azizbek will check it soon.')
        else:
            messages.error(request, 'There was an error with your submission. Please check the form.')
        
        # Redirect back to the contact section of the homepage
        return redirect(f"{reverse_lazy('core:home')}#contact")
