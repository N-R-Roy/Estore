from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from mstore.models import User


def signup(request):
    if request.method == "GET":
        return render(request, "mstore/signup.html")
    else:
        data = request.POST

        fname = data.get('fname')
        lname = data.get('lname')
        email = data.get('email')
        password = data.get('password')

        user1 = User(first_name=fname,
                     last_name=lname,
                     email=email,
                     password=make_password(password))
        user1.save()

        request.session['user_email'] = email

        return redirect('mstore:index')
