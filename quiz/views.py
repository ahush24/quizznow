from django.shortcuts import render

from quiz.models import Exam, Response

# Create your views here.
def home(request):

    # API LOGIC STARTS HERE 
    # response = requests.get('https://opentdb.com/api.php?amount=10&type=multiple')
    # todos = response.json()
    # print(todos.get('results')[9].get('question'))
    # 
    
    try:
        page_number = int(request.GET.get('page', '1'))
    except:
        page_number = 1
    
    question = Exam.objects.filter(id = page_number+10)
    print(Exam.objects.all().count())
    question_count = 10
    if page_number==question_count:
        context={"question":question,"next_page": min(question_count,page_number + 1), "prev_page": max(1, page_number - 1),"page":page_number}
    else:
        context={"question":question,"next_page": min(question_count, page_number + 1), "prev_page": max(1, page_number - 1),"page":page_number}

    if request.method=="POST":
        answer=request.POST.get("answer")
        
        if question.filter(Corrans=answer):
            response = Response()
            response.Question = answer
            response.solution = answer
            response.save()
            context={"question":question,"next_page": min(question_count,page_number + 1), "prev_page": max(1, page_number - 1),"correct":"true","finish":"true","page":page_number}
        else:
            context={"question":question,"next_page": min(question_count,page_number + 1), "prev_page": max(1, page_number - 1),"wrong":"true","finish":"true","page":page_number}
    
    if request.GET.get("finish")=="true":
        score = Response.objects.all().count()
        # print(score)
        context={"score":score,"question_count":question_count}
        Response.objects.all().delete()

    return render(request,"index.html",context)