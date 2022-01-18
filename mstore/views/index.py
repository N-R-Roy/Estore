
from django.shortcuts import render, redirect
from mstore.models.user import User


def index(request):
    user_email = request.session.get("user_email")
    if user_email:

        user = User.objects.get(email=user_email)

        return render(request, "mstore/index.html", {'user': user})

    else:

        return redirect("mstore:login")


