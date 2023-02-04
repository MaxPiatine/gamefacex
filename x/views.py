from django.shortcuts import render
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.core.exceptions import ValidationError
from django.core.mail import send_mail

from x.models import Quota, Partner
import environ

# Create your views here.

def home_page(request):
    return render(request, 'home.html')

def alfy(request):
    return render(request, 'work/alfy.html')

def folkhen(request):
    return render(request, 'work/folkhen.html')

def kingboozer(request):
    return render(request, 'work/kingboozer.html')

def kingland(request):
    return render(request, 'work/kingland.html')

def mudbuddy(request):
    return render(request, 'work/mudbuddy.html')

def work_page(request):
    return render(request, 'work/gallery.html')

def service_page(request):
    return render(request, 'services/services.html')

def quote(request):
    return render(request, 'quote/quote.html')

def sending_quote(request):
    if request.POST:
        name = request.POST.get('name')
        email = request.POST.get('email')
        socials = request.POST.get('socials')
        services = request.POST.get('services')
        budget = request.POST.get('budget')
        details = request.POST.get('details')
        traffic = request.POST.get('traffic')
        
        if not name or not email or not socials or not services or not budget or not details or not traffic:
            return JsonResponse({'msg': 'Please insert all Fields'}, status=400)
        
        
        quota = Quota.objects.create(
                name=name,
                email=email,
                socials=socials,
                services=services,
                budget=budget,
                details=details,
                traffic=traffic
            )
        
        try:
            quota.save()
        except ValidationError:
            return JsonResponse({'msg': 'Error: Enter fields correctly'}, status=400)
        
        message = 'budget: %s, \n services: %s, \n details: %s, \n socials: %s, \n traffic: %s' % (budget, services, details, socials, traffic)
        
        html = render_to_string('email/quota-email.html',{
            'name': name,
            'email': email,
            'socials': socials,
            'services': services,
            'budget': budget,
            'details': details,
            'traffic': traffic
        })
        
        try:
            send_mail(
                "Quota",
                message,
                'maximpiatine@hotmail.com',
                ['max.piatine@hotmail.com', 'y.edwardv@gmail.com', 'info@danielandrade.ca'],
                html_message=html)
        except ConnectionRefusedError:
            return JsonResponse({'msg': 'Failed to send your Data'}, status=400)
        
        return render(request, 'quote/quote-success.html')
        
    return JsonResponse({}, status=405)

def insights_page(request):
    return render(request, 'insights/insights.html')

def partner_page(request):
    return render(request, 'insights/partner.html')

def partner_sign_up(request):
    if request.POST:
        name = request.POST.get('name')
        email = request.POST.get('email')
        socials = request.POST.get('socials')
        stream = request.POST.get('stream')
        followers = request.POST.get('followers')
        details = request.POST.get('details')
        
        if not name or not email or not socials or not details:
            return JsonResponse({'msg': 'Please insert all required Fields'}, status=400)
        
        if not stream:
            stream = None
        if not followers:
            followers = None   
        
        partner = Partner.objects.create(
            name=name,
            email=email,
            socials=socials,
            stream=stream,
            followers=followers,
            details=details
        )
        
        
        
        try:
            partner.save()
        except ValidationError:
            return JsonResponse({'msg': 'Error: Enter fields correctly'}, status=400)
        
        
        html = render_to_string('email/partner-email.html',{
            'name': name,
            'email': email,
            'socials': socials,
            'stream': stream,
            'followers': followers,
            'details': details
        })
        
        try:
            send_mail(
                "Partnership from %s" % name,
                "Partner",
                env('EMAIL_0'),
                [env('EMAIL_1'), env('EMAIL_2'), env('EMAIL_3')],
                html_message=html)
        except ConnectionRefusedError:
            return JsonResponse({'msg': 'Failed to send your Data'}, status=400)
        
        return render(request, 'quote/quote-success.html')
    
    return JsonResponse({}, status=405)

def gfx_story_page(request):
    return render(request, 'insights/GamefaceX-a-new-beginning.html')
