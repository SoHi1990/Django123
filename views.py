'''
Created on Jan 8, 2016

@author: sohi
'''

from django.shortcuts import get_object_or_404,render
from django.core.urlresolvers import reverse
from Django123.models import Question,Choice
from django.http.response import HttpResponseRedirect,HttpResponse
from django.views import generic

def Hello(request):
    return HttpResponse("Hello")
    
def vote(request, question_id):
    question = Question.objects.all()
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('results', args=(question.id,)))
    
def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'results.html', {'question': question})
    
class IndexView(generic.ListView):
    template_name = "index.html"
    context_object_name = "latest_question_list"
    
    def IndexView(self):
        return Question.objects.order_by('-pub_date')[:5]
    
class DetailView(generic.DeleteView):
    model = Question
    template_name = 'detail.html'
    
class ResultView(generic.DeleteView):
    model = Question
    template_name = 'results.html'