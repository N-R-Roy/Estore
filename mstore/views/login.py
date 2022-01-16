
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from mstore.models import User


def login(request):
    if request.method == "GET":
        print(dict(request.session))
        request.session["hi"] = "Hello"
        request.session["dct"] = {"n1": 500, "n2": 700, "n3": 900}
        print(dict(request.session))
        return render(request, "mstore/login.html")
    else:
        data = request.POST

        email = data.get("email")
        password = data.get("password")

        user = None
        try:
            user = User.objects.get(email=email)
        except:
            user = None

        err_msg = ""
        if user:
            if check_password(password, user.password):
                return redirect("mstore:index")
            else:
                err_msg = "Invalid email or password"
        else:
            err_msg = "Invalid email or password"

        return render(request, "mstore/login.html", {'error': err_msg})


