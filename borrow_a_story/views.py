from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.views import generic, View
from .models import Author, Book, Issue
from .forms import IssueForm


class BookCatalogue(generic.ListView):
    queryset = Book.objects.order_by('title')
    paginate_by = 9
    template_name = 'index.html'

    # def get_queryset(self):
    #     # user = User.objects.get(username=self.kwargs['username'])
    #     book = Book.objects.all()
    #     issue = book.issue.filter(issued_to=request.user.get_username())
    #     return issue



class BookIssue(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Book.objects.all()
        book = get_object_or_404(queryset, slug=slug)
        # issue = book.issue.filter(issued_to=request.user)
        # issuer = False
        # if book.issue.filter(issued_to=self.request.user).exists():
        #     issuer = True
        form = IssueForm()
        context = {
            'book': book,
            # 'issue': issue,
            'form': form,
            # 'issuer': issuer
        }

        return render(request, 'book_issue.html', context)

    def post(self, request, slug, *args, **kwargs):
        queryset = Book.objects.all()
        book = get_object_or_404(queryset, slug=slug)
        issue = book.issue.all()
        book.available = False
        form_content = IssueForm(request.POST)
        if form_content.is_valid():
            form_content.instance.issued_to = request.user
            issued = form_content.save(commit=False)
            issued.book = book
            issued.save()
            book.save()
        else:
            form_content = IssueForm()
        
        context = {
            'book': book,
            'issue': issue,
            'form': form_content,
        }

        return render(request, 'book_issue.html', context)


class BookReturn(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Book.objects.all()
        book = get_object_or_404(queryset, slug=slug)
        issue = book.issue.filter(return_status=False)
        book.available = True
        issue.return_status = True
        issue.update()
        # issued.book = book
        # issued.save()
        book.save()

        context = {
            'book': book,
        }

        return render(request, 'book_return.html', context)
