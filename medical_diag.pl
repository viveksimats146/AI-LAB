% ---- Symptoms for each disease ----
disease(cold) :-
    symptom(cough),
    symptom(sneezing).

disease(flu) :-
    symptom(fever),
    symptom(body_ache).

disease(malaria) :-
    symptom(fever),
    symptom(chills).

% ---- Ask symptoms from user ----
start :-
    retractall(symptom(_)),
    ask(cough),
    ask(sneezing),
    ask(fever),
    ask(body_ache),
    ask(chills),
    diagnose.

% ---- Ask question ----
ask(S) :-
    format("Do you have ~w? (yes/no): ", [S]),
    read(Reply),
    (Reply == yes -> assertz(symptom(S)); true).

% ---- Diagnosis ----
diagnose :-
    ( disease(D) ->
        format("You may have: ~w~n", [D])
    ; writeln("No disease matched your symptoms.")
    ).
