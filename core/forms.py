"""
Forms for the core app — Contact form.
"""

from django import forms
from .models import ContactMessage


class ContactForm(forms.ModelForm):
    """Contact form with styled widgets."""

    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Your Name',
                'class': 'w-full bg-slate-800/50 border border-slate-700 rounded-lg px-4 py-3 '
                         'text-slate-200 placeholder-slate-500 focus:outline-none focus:ring-2 '
                         'focus:ring-teal-500 focus:border-transparent transition duration-300',
                'aria-label': 'Your name',
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'your@email.com',
                'class': 'w-full bg-slate-800/50 border border-slate-700 rounded-lg px-4 py-3 '
                         'text-slate-200 placeholder-slate-500 focus:outline-none focus:ring-2 '
                         'focus:ring-teal-500 focus:border-transparent transition duration-300',
                'aria-label': 'Your email',
            }),
            'message': forms.Textarea(attrs={
                'placeholder': 'Your message...',
                'rows': 5,
                'class': 'w-full bg-slate-800/50 border border-slate-700 rounded-lg px-4 py-3 '
                         'text-slate-200 placeholder-slate-500 focus:outline-none focus:ring-2 '
                         'focus:ring-teal-500 focus:border-transparent transition duration-300 resize-none',
                'aria-label': 'Your message',
            }),
        }
