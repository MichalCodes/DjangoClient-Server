from django.contrib import admin
from .models import Person
from .models import Case
from .models import Witnes
from .models import CriminalHistory
from .models import Evidence
from .models import Defendant

# Register your models here.
admin.site.register(Person)
admin.site.register(Case)
admin.site.register(Witnes)
admin.site.register(CriminalHistory)
admin.site.register(Evidence)
admin.site.register(Defendant)
