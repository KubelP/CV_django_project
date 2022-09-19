from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView, ListView, DetailView
from jpportfolio.models import MyContact, PortfolioCV, Comments, Portfolio, CV
from jpportfolio.forms import CommentsForm, ContactForm
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy


def about_me(request):
    about_me_cv = get_object_or_404(PortfolioCV, id=1)
    comments = Comments.objects.all()
    
    if request.method == 'POST':
        comment_form = CommentsForm(request.POST)

        if comment_form.is_valid():
            comment_form.save()
            return HttpResponseRedirect(reverse('jpportfolio:about_me'))
    else: 
        comment_form = CommentsForm()
    return render(request, 'about_me.html', {
                                            'amc': about_me_cv,
                                            'comments': comments,
                                            'comment_form': comment_form
                                            }) 


def my_contact(request):
    me = get_object_or_404(MyContact, id=1)
    
    if request.method == 'POST':
        contact_form = ContactForm(request.POST)

        if contact_form.is_valid():
            contact_form.save()
            return HttpResponseRedirect(reverse('jpportfolio:success'))
    else: 
        contact_form = ContactForm()
    return render(request, 'contact.html', {
                                            'me': me,
                                            'contact_form': contact_form
                                            }) 


class PortfolioView(ListView):
    template_name = 'my_portfolio.html'
    model = Portfolio
    context_object_name = 'projects'


class CV(ListView):
    template_name = 'my_cv.html'
    model = CV
    context_object_name = 'cvs'
