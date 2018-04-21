from django.contrib import admin
from .models import User, Question, Round, Answer, Language, Game
# Register your models here.


admin.site.register(User)
admin.site.register(Question)
admin.site.register(Round)
admin.site.register(Answer)
admin.site.register(Language)
admin.site.register(Game)
