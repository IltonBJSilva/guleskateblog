from django.shortcuts import render
from .models import Mod


def mod_list(request):
    mods = Mod.objects.all()

    return render(
        request,
        "mods/list.html",
        {
            "mods": mods
        }
    )