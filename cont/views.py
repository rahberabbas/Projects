from django.shortcuts import render
from .models import Contact
from django.core.mail import send_mail
# Create your views here.
def contact(request):
    # if request.method == 'POST':
    #     name = request.POST['name']
    #     email = request.POST['email']
    #     phone = request.POST['phone']
    #     message = request.POST['message']
    #     contact = Contact(name=name, email=email, phone=phone, message=message)
    #     contact.save()

    if request.method == "POST":
        yname = request.POST['name']
        yphone=request.POST['phone']
        yemail=request.POST['email']
        ymessage=request.POST['message']

        cont = "Name: " + yname+ "\nPhone: " + yphone+ "\nEmail: " + yemail + "\nMessage: " + ymessage
        send_mail(
        '-:Contact:-',
        cont, # subject
        yemail, # from email
        [''], #to email
        )

        return render(request,'contact.html',{
        'yname':yname,
        'yphone':yphone,
        'yemail':yemail,
        'ymessage':ymessage
        })

    else:
     return render(request,'contact.html')
