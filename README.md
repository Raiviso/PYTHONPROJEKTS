# NBA Game Details Scraper README

## Izstrādātāji

- **Rūdolfs Elferts** - Datorsistēmas 1.kursa 12.grupa (R31RDB081)
- **Arvis Zīverts** - Automatikas un datortehnikas 1.kursa 9.grupa (R31RDB140)
- **Raivis Inozemcevs** - Informacijas tehnoloģiju 1.kursa 5.grupa (231RDB270)

## Projekta Apraksts un Uzdevums

Šis Python un Selenium bibliotēku izmantojošais skripts ir izstrādāts, lai iegūtu detalizētu informāciju par NBA spēlēm noteiktā datumā. Lietotājam tiek prasīts ievadīt gada, mēneša un dienas datus, pēc kuriem skripts apmeklē NBA oficiālo vietni un nolasa informāciju par attiecīgās dienas spēlēm.

## Funkcionalitāte

Kad lietotājs ir ievadījis datumu, skripts veic šādas darbības:

1. **Tīmekļa lapas apmeklējums**: Skripts atver NBA oficiālo vietni izmantojot Selenium WebDriver, un ielādē spēļu sarakstu noteiktajā datumā.
2. **Informācijas izgūšana**: Skripts iegūst spēļu rezultātus, komandu nosaukumus, spēles labāko spēlētāju datus, tostarp punktus, atlēkušās bumbas un rezultatīvas piespēles.
3. **Datu apstrāde**: Informācija tiek sakārtota un izvadīta konsoles logā, nodrošinot skaidru un saprotamu spēļu apskatu.

## Izmantotās Bibliotēkas un To Nozīme

- **`selenium`**: Šī bibliotēka tiek izmantota, lai automatizētu tīmekļa pārlūkprogrammu. Tā ļauj skriptam atvērt un vadīt pārlūkprogrammu, piekļūt konkrētām tīmekļa lapām, un iegūt nepieciešamo informāciju no tīmekļa lapas elementiem. Selenium nodrošina darbibas ar tīmekļa lapu, piemēram, klikšķināšanu uz pogām, informācijas lasīšanu no teksta laukiem un citām tāda veida darbībām.
- **`time`**: Šī bibliotēka tiek izmantota, lai izveidotu pauzes skripta izpildē. Tas ir svarīgi, lai nodrošinātu, ka tīmekļa lapas ir pilnībā ielādējušās pirms datu izgūšanas. Piemēram, pēc lapas atvēršanas ar Selenium, skripts izmanto time.sleep() funkciju, lai uzgaidītu pāris sekundes, pirms turpina darbību. Šī pauze ir nepieciešama, lai nodrošinātu, ka visi lapas elementi ir ielādēti un Selenium var veiksmīgi izlasīt nepieciešamo informāciju.

## Galvenās Skripta Daļas

1. **Datuma ievade**: Lietotājs ievada datumu formātā YYYY-MM-DD.
2. **Tīmekļa lapas apmeklējums**: Skripts izmanto Selenium, lai atvērtu NBA mājas lapu ar konkrētā datuma spēlēm.
3. **Informācijas izgūšana un apstrāde**: Skripts nolasa spēļu rezultātus,parāda viesu un mājas komandu, komandu nosaukumus, spēles labāko spēlētāju statistiku, triple double ieguvējus un atrod videoklipu saites no spēles karstākajiem momentiem.
4. **Rezultātu izvade**: Informācija tiek izvadīta konsoles logā.

## Lietošanas Instrukcijas

1. Ievadiet datumu formātā YYYY-MM-DD.
2. Palaidiet skriptu.
3. Apskatiet iegūto informāciju konsoles logā.

Šis skripts ir lielisks rīks tiem, kuri vēlas ātri un efektīvi iegūt detalizētu informāciju par NBA spēlēm. Tā vienkāršā lietošana un spēja izgūt plašu datu klāstu padara to par noderīgu palīgu jebkuram basketbola entuziastam vai datu analītiķim.
