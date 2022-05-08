membuat project django
    django-admin startproject mysite
masuk ke folder project
    cd mysite
migrasi tabel default project
    python manage.py migrate
jalankan server pengembangan
    python manage.py runserver
buka server pengembangan di browser 
    http://127.0.0.1:8000/
membuat aplikasi blog
    python manage.py startapp blog
desain skema data/models
    from django.db import models
    from django.utils import timezone
    from django.contrib.auth.models import User
    class Post(models.Model):
    STATUS_CHOICES = {
        ('draft','Draft'),
        ('published','Published'),
    }
    title = models.CharField(max_length=250) //Charfield -> vachar
    slug = models.SlugField(max_length=250, unique_for_date='publish')
        \\label singkat, seo friendly
    author = models.ForeignKey(User, related_name='blog_posts', on_delete=models.CASCADE) \\many to one relational
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)\\kapan postingan di publis
    created = models.DateTimeField(auto_now_add=True)\\kapan postingan di dibuat
    updated = models.DateTimeField(auto_now=True)\\posingan terbaru diupdate
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')\\menggunakan parameter choice

    class Meta:\\metadata
        ordering=('-publish',)\\urutkan desc kolom publis

    def __str__(self):\\merepresentasikan object agar dapat dipahami manusia
        return self.title\\kembalikan nilai title

aktivasi applikasi blog
    open setting.py
    tambahkan 'blog', di INSTALLED_APPS
buat migrasi models post
    python manage.py makemigrations blog
untuk melihat sql code yang akan dieksekusi django bisa menggnakan perintah
    python manage.py sqlmigrate blog 0001
migrasi models post
    python manage.py migrate
create administrasion site
create super user
    python manage.py createsuperuser
    isi username, email dan password
tambahkan model ke administration site
    open admin.py
    tulis admin.site.register(Post)
masuk ke admin site
    add post
    isi form dan simpan
mengatur tampilan di admin site
    class PostAdmin(admin.ModelAdmin):
        list_display = ('title', 'slug', 'author', 'publish', 'status' )
        list_filter = ('status', 'created', 'publish', 'author' )
        search_fields = ('title', 'body')
        prepopulated_fields = {'slug':('title',)}
        raw_id_fields = ('author',)
        date_hierarchy = 'publish' 
        ordering = ['status', 'publish']
    admin.site.register(Post, PostAdmin)
membuat list dan detail view
    
