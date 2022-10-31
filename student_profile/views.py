from django.shortcuts import render
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib, ssl
from django.contrib.auth import get_user_model
from .models import Student
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken



def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }
def login(request):
    user = get_user_model()
    users = user.objects.all()
    for i in users:
        send_email(i.email, 'New Post', html='''<h3>Some one uploaded a new Post, cilck 
                <a href="yashraniya.pythonanywhere.com ">here</a> to view it.  </h3>''')

    return render(request, 'login/login.html')


def send_email(sender_email, subject, text=None, html=None):
    message = MIMEMultipart("alternative")
    message["Subject"] = subject
    message["From"] = 'yashrsniya@gmail.com'
    email = 'yashrsniya@gmail.com'
    password = 'YasH*8938#'
    message["To"] = sender_email
    if text:
        part1 = MIMEText(text, "plain")
        message.attach(part1)
    if html:
        part2 = MIMEText(html, "html")
        message.attach(part2)

    context = ssl.create_default_context()
    # showwarning('error', 'code is commented')
    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(email, password)
            server.sendmail(
                sender_email, sender_email, message.as_string()
            )

    except smtplib.SMTPRecipientsRefused as e:
        print(e)


class login_api(APIView):
    permission_classes = [AllowAny]

    def post(self, request):

        if request.data.get('mobile_number', '') and request.data.get('password', ''):
            mobile = request.data.get('mobile_number')
            password = request.data.get('password')
            try:
                user_obj = authenticate(mobile_number=mobile, password=password)
                if user_obj is None:
                    return Response({'status': '400', 'message': 'User or Password must be wrong'},
                                    status=status.HTTP_400_BAD_REQUEST)
                user_obj = Student.objects.get(mobile_number=mobile)

            except Student.DoesNotExist:
                return Response({'status': '400', 'message': 'User or Password must be wrong'},
                                status=status.HTTP_400_BAD_REQUEST)

            ss = student_data_serializers(user_obj)

            return Response(ss.data, status.HTTP_200_OK)
        else:

            return Response({'status': 400}, status.HTTP_400_BAD_REQUEST)


class signUp(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        ser = student_login_serializers(data=request.data)
        if ser.is_valid():
            ser.is_active=True
            ser.save()
            mobile=request.data.get('mobile_number')
            obj=Student.objects.get(mobile_number=mobile)
            ser=student_data_serializers(obj)
            return Response(ser.data,status.HTTP_200_OK)
        else:
            data={'status':400}
            data.update(ser.errors)
            return Response(data, status.HTTP_400_BAD_REQUEST)

