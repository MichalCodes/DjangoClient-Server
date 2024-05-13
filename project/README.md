# Policejní databáze
Využil jsem databázový model policejní databáze z DS zjednodušený o jednu tabulku.
### Modely:
- **Person**
    - fname
    - lname
    - birthdate
    - sex 
    - address
- **Witness**
    - statement
    - protection
    - person_id
    - case_id
- **CriminalHistory**
    - trest_type
    - crime
    - start_date
    - end _date
    - person_id
    - case_id
- **Defendants**
    - person
    - case
- **Cases**
    - name
    - detective
    - judge
    - detective
    - start_date
    - end_date
    - description
- **Evidence**
    - e_type
    - description
    - case_id

### Formuláře:
- **PersonForm**
- **CaseForm**
- **EvidenceForm**
- **WitnessForm**
- **CriminalHistoryForm**
- **DefendantForm**
### Templates:
- index
- person
- add_person
- show_witnesses
- show_evidence
- add_witness
- add_criminal_history_record
- add_defendant
- addcase
- addperson
- cases
- add_evidence

*Templaty jsou ve složce templates*

## Persons
První co se ukáže je seznam lidí vedených v databázi Na každého se dá kliknout a zobrazit si jeho záznamy v trestním rejstříku. Pod záznamy najdete tlačítko na přidání záznamu. Po kliknutí se vám ukáže formulář na přidání nového člověka. Vpravo dole je pak tlačítko show cases po kliknutí se ukáže seznam případů vedených v databázi

## Cases
V cases můžeme přidat případ. a v levo dole se přesunout do Presons. Po kliknutí na případ se nám ukáže detail případu kde si můžeme zobrazit důkazy a svědky. Obžalované vydíme přímo na stránce. A potom můžeme přidávat důkazy svědky a záznamy do trestního rejstříku (na každou věc je formulář).

## Spuštění
Server se rozběhne ```$ python3 manage.py runserver``` ten potom běží na localhost ```127.0.0.1:8000```
Pokud nemáte nainstalované django nebo python bude ho třeba nainstalovat
