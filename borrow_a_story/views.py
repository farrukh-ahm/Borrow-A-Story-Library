from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.views import generic, View
from .models import Author, Book, Issue, User_Detail
from .forms import IssueForm, ProfileForm
import random


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
        form_content = IssueForm(request.POST)
        if form_content.is_valid():
            book.available = False
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
        # ------------------------------
        random_books = []
        last = queryset.count()
        while len(random_books) < 3:
            random_no = random.randint(0, last-1)
            fetch_random = Book.objects.all()[random_no]
            if fetch_random not in random_books:
                random_books.append(fetch_random)
        # ------------------------------
        book = get_object_or_404(queryset, slug=slug)
        issue = book.issue.filter(return_status=False)
        book.available = True
        # issue.return_status = True
        issue.update(return_status=True)
        # issued.book = book
        # issued.save()
        book.save()

        context = {
            'book': book,
            'random_books': random_books,
        }

        return render(request, 'book_return.html', context)


class UserProfile(View):

    def get(self, request, *args, **kwargs):
        try:
            queryset = User_Detail.objects.all()
            user_info = get_object_or_404(queryset, user=request.user)
        except:
            queryset = []
            user_info = {'address': 'No details', 'contact_no': 'No details'}
        # user_info = get_object_or_404(queryset, user=request.user)
        profile_form = ProfileForm()

        context = {
            'user_info': user_info,
            'profile_form': profile_form,
        }

        return render(request, 'profile.html', context)

    def post(self, request, *args, **kwargs):
        user = User.objects.filter(username=reque.user)
        user_info = user.user.all()