from django import forms 
from .models import Person
from .models import Case
from .models import Witnes
from .models import Evidence
from .models import CriminalHistory
from .models import Defendant

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = '__all__'
        
class CaseForm(forms.ModelForm):
    class Meta:
        model = Case
        fields = ['name', 'case_type', 'detective', 'judge', 'start_date', 'end_date', 'description']
        exclude = ['criminal_histoy_id']
              
class EvidenceForm(forms.ModelForm):
    class Meta:
        model = Evidence
        fields =  '__all__'
        
class CriminalHistoryForm(forms.ModelForm):
    class Meta:
        model = CriminalHistory
        fields = ['crime', 'trest_type', 'start_date', 'end_date', 'person_id']
        exclude = ['case id']

class WitnessForm(forms.ModelForm):
    class Meta:
        model = Witnes
        fields = ['statement', 'protection', 'person_id']
        exclude = ['case id']
        
class DefendantForm(forms.ModelForm):
    class Meta:
        model = Defendant
        fields = '__all__'