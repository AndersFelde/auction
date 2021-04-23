from django.shortcuts import render
#  from webpage.models import TestModal


def formPage(request):
    if request.method == "POST":
        data = request.POST

        inputs = []
        for key in data:
            out = f"{key}: {data[key]}"
            print(out)
            inputs.append(out)

        return render(request,
                      "webpage/formPage.html",
                      context={"inputs": inputs})
    else:
        return render(request, "webpage/formPage.html")
