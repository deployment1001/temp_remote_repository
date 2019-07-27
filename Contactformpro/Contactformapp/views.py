from django.shortcuts import render
from .forms import ContactForm
from .models import ContactData
from django.http.response import HttpResponse
def Contactview(request):
    if request.method == "POST":
        cform=ContactForm(request.POST)
        if cform.is_valid():
            name1 = request.POST.get('name', '')
            location1 = request.POST.get('location', '')
            salary1 = request.POST.get('salary', '')
            email = request.POST.get('email', '')
            a = ContactData(name=name1,
                            location=location1,
                            salary=salary1,
                            email=email)
            a.save()
            cform = ContactForm()
            return render(request,'ContactForm.html',{'abcd':cform})
        else:
            return HttpResponse("Invlid User Data")
    else:
        cform = ContactForm()
        return render(request, 'ContactForm.html', {'abcd': cform})

def Fetchingdata(request):
        data = ContactData.objects.all()
        return render(request, 'DisplayData.html', {'data': data})





