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

    # def get_queryset(self):
    #     queryset = Book.objects.order_by('title').filter(id=1) 
        # book = get_object_or_404(queryset, slug=self.slug)
        # bookmarked = []
        # for bookmark in queryset.bookmarked.all():
        #     if bookmark.username == request.user.id:
        #         bookmarked.append(bookmark)
        # return bookmarked


class BookIssue(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Book.objects.all()
        book = get_object_or_404(queryset, slug=slug)
        form = IssueForm()

        # bookmarked = False
        # if book.bookmarked.filter(id=self.request.user.id).exists():
        #     bookmarked = True

        context = {
            'book': book,
            'form': form,
            'bookmarked': bookmarked,
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

        # bookmarked = False
        # if book.bookmarked.filter(id=self.request.user.id).exists():
        #     bookmarked = True
        
        context = {
            'book': book,
            'issue': issue,
            'form': form_content,
            'bookmarked': bookmarked,
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
        issue.update(return_status=True)
        book.save()

        # bookmarked = False
        # if book.bookmarked.filter(id=self.request.user.id).exists():
        #     bookmarked = True

        context = {
            'book': book,
            'random_books': random_books,
            'bookmarked': bookmarked,
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

        # queryset2 = Issue.objects.all()
        borrowed_books = Issue.objects.filter(issued_to=request.user, return_status=False)
        # print(borrowed_books)
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

    def post(self, request, *args, **kwargs):
        # user = User.objects.filter(username=request.user)
        # user_info = user.user.all()
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
            # queryset = []
            user_info = {'address': 'No details', 'contact_no': 'No details'}
            # user_info = get_object_or_404(queryset, user=request.user)
            profile_form = ProfileForm()
            user_form = ProfileForm(request.POST)
            if user_form.is_valid():
                user_update = user_form.save(commit=False)
                user_update.user = request.user
                user_update.save()
            else:
                user_form = ProfileForm()
            
        for book in book_queryset:
            if book.bookmarked.filter(id=request.user.id).exists():
                bookmarks.append(book)
 
        context = {
            'user_info': user_info,
            'profile_form': user_form,
            'bookmarks': bookmarks,
        }

        return render(request, 'profile.html', context)
        # return redirect(reverse('user_profile'))


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