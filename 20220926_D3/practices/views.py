from django.shortcuts import render

# Create your views here.
def index(request, _number):
    if (_number % 2) == 1:
        res = "홀수"
    if _number == 0:
        res = "0"
    else:
        res = "짝수"
    context = {
        "number": _number,
        "result": res,
    }
    return render(request, "practices/index.html", context)


def ping(request):
    return render(request, "practices/ping.html")


def pong(request):
    # print(request)
    # name = request.GET.get('ball')
    # context = {
    #     'name': name,
    # }

    return render(request, "practices/pong.html", {"name": request.GET.get("ball")})


def calc(request, a, b):
    plus = a + b
    minu = a - b
    mult = a * b
    div = a // b
    context = {
        "a": a,
        "b": b,
        "plus": plus,
        "minu": minu,
        "mult": mult,
        "div": div,
    }
    return render(request, "practices/calc.html", context)
