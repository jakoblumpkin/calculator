from django.shortcuts import render

# Create your views here.

def home(request):
    context={}
    if request.method=='POST':
        answer=eval(request.POST["nameC"])
        context={"answer": answer}
    return render(request, 'index.html', context)