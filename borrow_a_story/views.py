from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib import messages
from django.views import generic, View
from .models import Author, Book, Issue, User_Detail
from .forms import IssueForm, ProfileForm, BookAddForm, AuthorAddForm, EditBookForm
from django.http import HttpResponseRedirect
from django.utils.text import slugify
import random


# Index Page View
class BookCatalogue(generic.ListView):
    model = Book
    queryset = Book.objects.order_by('title')
    paginate_by = 9
    template_name = 'index.html'


# Book Issue Page
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


# Page Rendered After Returning A Book
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


# User Profile Page
class UserProfile(View):

    def get(self, request, *args, **kwargs):
        if request.user.id:
            try:
                queryset = User_Detail.objects.all()
                user_info = get_object_or_404(queryset, user=request.user)
                profile_form = ProfileForm(instance=user_info)
            except:
                user_info = {
                    'address': 'No details',
                    'contact_no': 'No details'
                    }
                profile_form = ProfileForm()

            # Get list of borrowed books by the user
            borrowed_books = Issue.objects.filter(
                issued_to=request.user,
                return_status=False
                )

            # Get list of books bookmarked by user
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

                messages.success(request, "Profile Updated!")
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
                messages.success(request, "Profile Updated!")
            else:
                user_form = ProfileForm()

        # Get list of borrowed books by the user
        borrowed_books = Issue.objects.filter(
                issued_to=request.user,
                return_status=False
                )

        # Get list of books bookmarked by user
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


# Bookmark action handler
class Bookmark(View):

    def post(self, request, slug):
        queryset = Book.objects.all()
        book = get_object_or_404(queryset, slug=slug)

        if book.bookmarked.filter(id=request.user.id).exists():
            book.bookmarked.remove(request.user)
        else:
            book.bookmarked.add(request.user)

        return HttpResponseRedirect(reverse('home'))


# Book Add/Delete by the Admin
class AdminControl(View):

    def get(self, request, *args, **kwargs):
        queryset = Book.objects.all()
        book_list = queryset
        bookform = BookAddForm()
        authorform = AuthorAddForm()
        context = {
            'book_list': book_list,
            'bookform': bookform,
            'authorform': authorform,
        }

        return render(request, 'managebook.html', context)

    def post(self, request, *args, **kwargs):
        book = BookAddForm(request.POST, request.FILES)
        if book.is_valid():
            newbook = book.save(commit=False)
            newbook.slug = slugify(newbook.title)
            newbook.available = True
            newbook.save()

        messages.success(request, "Book Added!")
        return redirect(reverse('manage_book'))


# Author Add by Admin
class AddAuthor(View):

    def post(self, request):
        queryset = Author.objects.all()
        authorform = AuthorAddForm(request.POST)
        if authorform.is_valid():
            authorform.save()

            messages.success(request, "Author Added!")
            return redirect(reverse('manage_book'))
        else:
            authorform = AuthorAddForm()
            print("Invalid")
            return redirect(reverse('manage_book'))


# Remove Book by Admin
class DeleteBook(View):

    def post(self, request, slug, *args, **kwargs):
        queryset = Book.objects.all()
        book = get_object_or_404(queryset, slug=slug)
        book.delete()

        messages.warning(request, 'Book Deleted!')
        return redirect(reverse('manage_book'))


# Edit Book By Admin
class EditBook(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Book.objects.all()
        fetch_book = get_object_or_404(queryset, slug=slug)
        editbook = EditBookForm(instance=fetch_book)

        context = {
            'book': fetch_book,
            'editbook': editbook
        }

        return render(request, 'editbook.html', context)

    def post(self, request, slug, *args, **kwargs):
        queryset = Book.objects.all()
        book = get_object_or_404(queryset, slug=slug)
        editbook = EditBookForm(request.POST, request.FILES, instance=book)

        if editbook.is_valid():
            editbook.save()

            messages.success(request, 'Book edited!')
            return redirect('manage_book')

        else:
            editbook = EditBookForm()

            messages.error(request, 'Wrong Information!')
            return redirect(reverse('edit_book'))
