from django.contrib import admin
from .models import posts
from .models import comments
from .models import categories

admin.site.register(posts)
admin.site.register(comments)
admin.site.register(categories)
