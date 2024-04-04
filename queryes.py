import django
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

if __name__ == "__main__":
    from apps.db_train_alternative.models import Blog, Author, AuthorProfile, Entry, Tag



    # obj = Entry.objects.filter(author__name__contains='author')
    # print(obj)
    #
    # obj = Entry.objects.filter(author__authorprofile__city=None)
    # print(obj)
    #
    # print(Entry.objects.get(id__exact=4))
    # print(Entry.objects.get(id=4))  # Аналогично exact
    # print(Blog.objects.get(name__iexact="Путешествия по миру"))
    #
    # print(Entry.objects.filter(headline__contains='мод'))
    #
    # print(Entry.objects.filter(id__in=[1, 3, 4]))
    #
    # print(Entry.objects.filter(number_of_comments__in='123'))

    inner_qs = Blog.objects.filter(name__contains='Путешествия')
    entries = Entry.objects.filter(blog__in=inner_qs)
    print(entries)













