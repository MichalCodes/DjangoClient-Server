from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Person, Case, CriminalHistory, Witnes, Defendant, Evidence
from .forms import PersonForm, CaseForm, WitnessForm, EvidenceForm, CriminalHistoryForm, DefendantForm
# Create your views here.
case_ID = 1

def index(request):
    persons = Person.objects.all()
    person_form = PersonForm()
    return render(request, 'SKJproject/index.html', {'Persons' : persons, 'person_form' : person_form})

def person(request, person_id):
    person = get_object_or_404(Person, pk=person_id)
    criminal_history = CriminalHistory.objects.filter(person_id=person_id)
    return render(request, 'SKJproject/person.html', {'person': person, 'criminal_history': criminal_history })

def addperson(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            try:
                person = Person(
                    fname=data['fname'],
                    lname=data['lname'],
                    birthdate=data['birthdate'],
                    sex=data['sex'],
                    address=data['address']
                )
                person.save()
                return redirect('index')
            except Exception as e:
                print(e)  # Výpis chyby pro kontrolu
                return render(request, 'SKJproject/addperson.html', {'form': form})
        else:
            print(form.errors)  # Výpis chyb formuláře pro kontrolu
            return render(request, 'SKJproject/addperson.html', {'form': form})
    else:
        form = PersonForm()
    return render(request, 'SKJproject/addperson.html', {'form': form})

    
def cases(request):
    all_cases = Case.objects.all()
    return render(request, 'SKJproject/cases.html', {'all_cases': all_cases})


def addcase(request):
    if request.method == 'POST':
        form = CaseForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            try:
                case = Case(
                    name=data['name'],
                    case_type=data['case_type'],
                    detective=data['detective'],
                    judge=data['judge'],
                    start_date=data['start_date'],
                    end_date=data['end_date'],
                    description=data['description']
                )
                case.save()
                return redirect('cases')
            except Exception as e:
                print(e)  # Výpis chyby pro kontrolu
                return render(request, 'SKJproject/addcase.html', {'form': form})
        else:
            print(form.errors)  # Výpis chyb formuláře pro kontrolu
            return render(request, 'SKJproject/addcase.html', {'form': form})
    else:
        form = CaseForm()
    return render(request, 'SKJproject/addcase.html', {'form': form})


def showCase(request, case_id):
    case = get_object_or_404(Case, pk=case_id)
    witnesses = Witnes.objects.filter(case_id=case_id)
    witness_form = WitnessForm()
    return render(request, 'SKJproject/show_case.html', {'case': case, 'witnesses': witnesses, 'witness_form': witness_form})

def showEvidence(request, case_id):
    case = get_object_or_404(Case, pk=case_id)
    evidences = Evidence.objects.filter(case_id=case_id)
    return render(request, 'SKJproject/show_evidence.html', {'case': case, 'evidences': evidences})

def show_witness(request, case_id):
    case = get_object_or_404(Case, pk=case_id)
    witnesses = Witnes.objects.filter(case_id=case_id)
    return render(request, 'SKJproject/show_witness.html', {'case': case, 'witnesses': witnesses})

def addEvidence(request, case_id):
    if request.method == 'POST':
        form = EvidenceForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            try:
                evidence = Evidence(
                    e_type=data['e_type'],
                    description=data['description'],
                    case_id=Case.objects.get(pk=case_id)
                )
                evidence.save()
                return redirect('show_case', case_id=case_id)
            except Exception as e:
                print(e)  # Výpis chyby pro kontrolu
                return render(request, 'SKJproject/add_evidence.html', {'form': form})
        else:
            print(form.errors)  # Výpis chyb formuláře pro kontrolu
            return render(request, 'SKJproject/add_evidence.html', {'form': form})
    else:
        form = EvidenceForm()
    return render(request, 'SKJproject/add_evidence.html', {'form': form, 'case_id': case_id})

def addWitness(request, case_id):
    case = get_object_or_404(Case, pk=case_id)
    if request.method == 'POST':
        form = WitnessForm(request.POST)
        if form.is_valid():
            witness = form.save(commit=False)
            witness.case_id = case
            witness.save()
            return redirect('show_case', case_id=case_id)
    else:
        form = WitnessForm()
    return render(request, 'SKJproject/add_witness.html', {'form': form, 'case_id': case_id})

def addDefendant(request, case_id):
    case = Case.objects.get(id=case_id)
    if request.method == 'POST':
        form = DefendantForm(request.POST)
        if form.is_valid():
            defendant = form.save(commit=False)
            defendant.case = case  # Přiřadíme případ k obžalovanému
            defendant.save()
            return redirect('show_case', case_id=case.id)
    else:
        form = DefendantForm()
    return render(request, 'SKJproject/add_defendant.html', {'form': form})

def addCriminalRecord(request, case_id):
    case = get_object_or_404(Case, pk=case_id)
    if request.method == 'POST':
        form = CriminalHistoryForm(request.POST)
        if form.is_valid():
            criminal_history = form.save(commit=False)
            criminal_history.case_id = case
            criminal_history.save()
            return redirect('show_case', case_id=case_id)
    else:
        form = CriminalHistoryForm()
    return render(request, 'SKJproject/add_evidence.html', {'form': form, 'case_id': case_id})