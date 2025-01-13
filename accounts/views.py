from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render, redirect
import random
import string
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from .forms import EmailForm, RegisterForm
#for otp verification
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.conf import settings
from .forms import EmailForm
import random
import string



def landing_page(request):


    return render(request,'accounts/landing_page.html')


# Generate OTP function
def generate_otp():
    otp = ''.join(random.choices(string.digits, k=6))  # 6-digit OTP
    return otp

# View to send OTP
# Register view
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            # Get cleaned data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            verify_password = form.cleaned_data['verfy_password']
            email = form.cleaned_data['email']

            # Check if passwords match
            if password != verify_password:
                form.add_error('verfy_password', 'Passwords do not match')
            else:
                # Save user data in session
                request.session['username'] = username
                request.session['password'] = password
                request.session['email'] = email

                # Generate and send OTP
                otp = generate_otp()
                request.session['otp'] = otp  # Save OTP in session
                print(f"Generated OTP: {otp}")  # Debugging purpose
                # Send OTP via email
                subject = 'Your OTP Code'
                message = f'Your OTP code is {otp}. Please enter this code to verify your email.'
                send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [email])

                # Redirect to OTP verification view
                return redirect('send_otp')
    else:
        form = RegisterForm()

    return render(request, 'accounts/register.html', {'form': form})

# OTP verification view
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

@csrf_exempt  # Use this decorator if you're testing without CSRF token (for production, ensure CSRF is handled)
def send_otp(request):
    if request.method == 'POST':
        action = request.POST.get('action')

        if action == 'resend_otp':
            # Generate and resend OTP
            otp = generate_otp()
            request.session['otp'] = otp  # Store OTP in session
            email = request.session.get('email')
            if email:
                # Send OTP via email
                subject = 'Your New OTP Code'
                message = f'Your new OTP code is {otp}. Please enter this code to verify your email.'
                send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [email])
                return JsonResponse({"status": "success", "message": "A new OTP has been sent to your email."})
            else:
                return JsonResponse({"status": "error", "message": "Session expired. Please try registering again."})

        elif action == 'validate_otp':
            # Handle OTP verification
            entered_otp = request.POST.get('otp', '').strip()
            otp = str(request.session.get('otp'))  # Convert session OTP to string
            if otp is None:
                return JsonResponse({"status": "error", "message": "Session expired. Please try registering again."})

            if otp == entered_otp:
                # OTP verified successfully
                username = request.session.get('username')
                email = request.session.get('email')
                password = request.session.get('password')

                # Save the user to the database (replace with your User model logic)
                # User.objects.create(username=username, email=email, password=password)
                print(f"User registered: {username}, {email}, {password}")
                # Clear session data
                request.session.flush()

                return JsonResponse({"status": "success", "message": "User registered successfully!"})
            else:
                return JsonResponse({"status": "error", "message": "Invalid OTP. Please try again."})
    else:
        return render(request, 'accounts/verify_otp.html')
