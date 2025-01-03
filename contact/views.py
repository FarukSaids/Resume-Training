from django.http import JsonResponse
from django.shortcuts import render
from contact.models import Message
from contact.forms import ContactForm


# Create your views here.
def contact_form(request):
      if request.method == 'POST':
        contact_form = ContactForm(request.POST or None) #post ise valide et istek post değilse none geciyor
        if contact_form.is_valid():
            name = request.POST.get('name') #req post bir obje olarak gelir (json) html icindeki name="name kısmı
            email = request.POST.get('email')
            subject = request.POST.get('subject')
            message = request.POST.get('message')
            Message.objects.create(name=name, email=email, subject=subject, message=message)


            success = True
            message = 'Contact form sent successfully!'

        else:
            success:False
            message = 'Contact form not sent '
        context = {
            'success': success,
            'message': message,
        }
        return JsonResponse(context)


def contact(request):
    contact_form = ContactForm()
    context = {
        'contact_form': contact_form,
    }

    return render(request, 'contact.html',context)
