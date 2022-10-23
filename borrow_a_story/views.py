from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.views import generic, View
from .models import Author, Book, Issue, User_Detail
from .forms import IssueForm, ProfileForm
from django.http import HttpResponseRedirect
import random


class BookCatalogue(generic.ListView):
    model = Book
    queryset = Book.objects.order_by('title')
    paginate_by = 9
    template_name = 'index.html'


class BookIssue(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Book.objects.all()
        book = get_object_or_404(queryset, slug=slug)
        form = IssueForm()

        context = {
            'book': book,
            'form': form,
        }

        return render(request, 'book_issue.html', context)

    def post(self, request, slug, *args, **kwargs):
        queryset = Book.objects.all()
        book = get_object_or_404(queryset, slug=slug)
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

        # Generating list of random books
        # ------------------------------
        random_books = []
        last = queryset.count()
        while len(random_books) < 3:
            random_no = random.randint(0, last-1)
            fetch_random = Book.objects.all()[random_no]
            if fetch_random not in random_books:
                random_books.append(fetch_random)
        # ------------------------------
        context = {
            'book': book,
            'form': form_content,
            'random_books': random_books,
        }

        return render(request, 'issued.html', context)


class BookReturn(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Book.objects.all()

        # Generating list of random books
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
        issue.update(return_status=True)
        book.save()

        context = {
            'book': book,
            'random_books': random_books,
        }

        return render(request, 'book_return.html', context)


class UserProfile(View):

    def get(self, request, *args, **kwargs):
        if request.user.id:
            try:
                queryset = User_Detail.objects.all()
                user_info = get_object_or_404(queryset, user=request.user)
            except:
                user_info = {
                    'address': 'No details',
                    'contact_no': 'No details'
                    }
            profile_form = ProfileForm()

            borrowed_books = Issue.objects.filter(
                issued_to=request.user,
                return_status=False
                )
            
            book_queryset = Book.objects.all()
            bookmarks = []
            for book in book_queryset:
                if book.bookmarked.filter(id=request.user.id).exists():
                    bookmarks.append(book)

            context = {
                'user_info': user_info,
                'profile_form': profile_form,
                'borrowed_books': borrowed_books,
                'bookmarks': bookmarks,
            }

            return render(request, 'profile.html', context)
        else:
            return render(request, 'profile.html')

    def post(self, request, *args, **kwargs):
        try:
            queryset = User_Detail.objects.all()
            user_info = get_object_or_404(queryset, user=request.user)
            profile_form = ProfileForm()
            user_form = ProfileForm(request.POST, instance=user_info)
            if user_form.is_valid():
                user_update = user_form.save(commit=False)
                user_update.user = request.user
                user_update.save()
            else:
                user_form = ProfileForm()
        except:
            user_info = {'address': 'No details', 'contact_no': 'No details'}
            profile_form = ProfileForm()
            user_form = ProfileForm(request.POST)
            if user_form.is_valid():
                user_update = user_form.save(commit=False)
                user_update.user = request.user
                user_update.save()
            else:
                user_form = ProfileForm()

        borrowed_books = Issue.objects.filter(
                issued_to=request.user,
                return_status=False
                )
        book_queryset = Book.objects.all()
        bookmarks = []    
        for book in book_queryset:
            if book.bookmarked.filter(id=request.user.id).exists():
                bookmarks.append(book)
 
        context = {
            'user_info': user_info,
            'profile_form': user_form,
            'borrowed_books': borrowed_books,
            'bookmarks': bookmarks,
        }

        return render(request, 'profile.html', context)


class Bookmark(View):
    
    def post(self, request, slug):
        queryset = Book.objects.all()
        book = get_object_or_404(queryset, slug=slug)

        if book.bookmarked.filter(id=request.user.id).exists():
            book.bookmarked.remove(request.user)
        else:
            book.bookmarked.add(request.user)

        return HttpResponseRedirect(reverse('home'))


class Test(View):

    def get(self, request):
        books = Book.objects.all()
        bookmarks = []
        for book in books:
            bookmarks.append(book.bookmarked.all())
        context = {
            'books': books,
            'bookmarks': bookmarks,
        }
        return render(request, 'test.html', context)


