from django.shortcuts import render
from django.http import JsonResponse
from .models import Register
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.utils import timezone
from datetime import timedelta
from django.db import transaction 

def index(request):
    return render(request,'index.html')

def register(request):
    return render(request,'registrationform.html')

def send_registration_email(student_data):
    subject = 'Welcome to Ignite Innovation!'
    from_email = 'vemalivardhan@gmail.com'  
    recipient_list = [student_data['email']]

    event_date =timezone.datetime(2024, 8, 3, 9, 30, 0, tzinfo=timezone.now().tzinfo)
    now = timezone.now()
    time_difference = event_date - now

    days, seconds = time_difference.days, time_difference.seconds
    hours = days * 24 + seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60

    context = {
        'name': student_data['name'],
        'days': str(days).zfill(2), 
        'hours': str(hours).zfill(2),
        'minutes': str(minutes).zfill(2),
        'seconds': str(seconds).zfill(2),
        'slot_number':student_data['slot_number']
    }

    html_content = render_to_string('registration_confirmation_email.html', context)
    text_content = strip_tags(html_content)

    email = EmailMultiAlternatives(subject, text_content, from_email, recipient_list)
    email.attach_alternative(html_content, "text/html")
    try:
        email.send()
        print("Email sent successfully!")  
    except Exception as e:
        print(f"Error sending email: {str(e)}")


@csrf_exempt  
def submit_registration(request):
    if request.method == 'POST':
        register_number = request.POST.get('register_number')
        if Register.objects.filter(register_number=register_number).exists():
            return JsonResponse({'success': False, 'message': 'Student with this Register Number already exists!'})
        else:
            with transaction.atomic(): 
                last_slot = Register.objects.select_for_update().order_by('-slot_number').first()  # Lock the table for consistent slot assignment
                last_slot_number = last_slot.slot_number if last_slot else 0
                next_slot_number = last_slot_number + 1

                registration = Register(
                    register_number=register_number,
                    name=request.POST.get('student_name'),
                    email=request.POST.get('email'),
                    branch=request.POST.get('department'),
                    year=request.POST.get('year'),
                    concept_to_present=request.POST.get('concept'),
                    slot_number=next_slot_number 
                )
                registration.save()
                student_data = {
                    'name': registration.name,
                    'email': registration.email,
                    'slot_number':next_slot_number
                }
                send_registration_email(student_data)

                return JsonResponse({'success': True, 'message': 'Registration successful!'})
    else:
        return JsonResponse({'success': False, 'message': 'Invalid request method!'})
