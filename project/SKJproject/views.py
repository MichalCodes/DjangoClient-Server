from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.db.models import Q
from .models import Person, Case, CriminalHistory, Witnes, Defendant, Evidence
from .forms import PersonForm, CaseForm, WitnessForm, EvidenceForm, CriminalHistoryForm, DefendantForm, PersonSearchForm
# Create your views here.
case_ID = 1

def index(request):
    query = request.GET.get('query')
    if query:
        persons = Person.objects.filter(
            fname__icontains=query) | Person.objects.filter(
            lname__icontains=query)
    else:
        persons = Person.objects.all()

    persons_with_criminal_record_count = Person.objects.exclude(criminalhistory__isnull=True).count()
    total_persons_count = Person.objects.count()
    persons_with_criminal_record_percent = round((persons_with_criminal_record_count / total_persons_count) * 100, 2)
    top_crimes = list(CriminalHistory.objects.values_list('crime', flat=True).distinct().order_by('-crime')[:3])

    return render(request, 'SKJproject/index.html', {'persons': persons, 'persons_with_criminal_record_percent': persons_with_criminal_record_percent, 'top_crimes': top_crimes, 'form': PersonSearchForm()})

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
    query = request.GET.get('q')
    if query:
        all_cases = Case.objects.filter(
            Q(name__icontains=query) | Q(case_type__icontains=query)
        )
    else:
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
