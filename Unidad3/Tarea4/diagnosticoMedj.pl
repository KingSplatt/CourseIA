evaluar :-
    writeln("=== Sistema Experto de Diagnóstico Médico ==="),
    writeln("Responde con 'si.' o 'no.'"),
    nl,
    encontrar_enfermedades(Lista),
    (Lista = [] ->
        writeln("No se pudo determinar una enfermedad con los síntomas proporcionados.")
    ;
        mostrar_lista_diagnosticos(Lista)
    ),
    deshacer.

encontrar_enfermedades(Lista) :-
    findall(Enfermedad, hipotesis(Enfermedad), Lista).

mostrar_lista_diagnosticos([]).
mostrar_lista_diagnosticos([E | Resto]) :-
    mostrar_info(E),
    nl,
    mostrar_lista_diagnosticos(Resto).


hipotesis(gripe) :- gripe.
hipotesis(gastritis) :- gastritis.
hipotesis(faringitis) :- faringitis.
hipotesis(migraña) :- migraña.
hipotesis(dermatitis) :- dermatitis.
hipotesis(resfriado) :- resfriado.
hipotesis(cistitis) :- cistitis.
hipotesis(lumbalgia) :- lumbalgia.
hipotesis(conjuntivitis) :- conjuntivitis.

% Reglas de síntomas
gripe :-
    verificar(fiebre),
    verificar(dolor_muscular),
    verificar(congestion_nasal),
    verificar(tos_seca).

gastritis :-
    verificar(dolor_abdominal),
    verificar(acidez),
    verificar(nauseas).

faringitis :-
    gripe,
    verificar(dolor_de_garganta),
    verificar(dificultad_al_tragar),
    verificar(fiebre).

migraña :-
    verificar(dolor_de_cabeza_intenso),
    verificar(nauseas),
    verificar(sensibilidad_luz).

dermatitis :-
    verificar(picazon_intensa),
    verificar(piel_seca),
    verificar(enrojecimiento).

resfriado :-
    verificar(estornudos),
    verificar(tos_leve),
    verificar(dolor_de_garganta).

cistitis :-
    verificar(dolor_al_orinar),
    verificar(orina_turbia),
    verificar(frecuencia_urinaria).

lumbalgia :-
    verificar(dolor_lumbar),
    verificar(rigidez),
    verificar(limitacion_movimiento).

conjuntivitis :-
    verificar(enrojecimiento_ocular),
    verificar(picazon),
    verificar(secrecion),
    verificar(lagrimeo),
    verificar(sensacion_cuerpo_extraño).

% Mostrar información según enfermedad
mostrar_info(gripe) :-
    writeln("Diagnóstico probable: Gripe (Influenza)"),
    writeln("Sistema afectado: Respiratorio"),
    writeln("Causa: Infección viral (virus influenza)"),
    writeln("Diagnóstico: Clínico por síntomas, prueba rápida de influenza"),
    writeln("Tratamiento: Reposo, líquidos, antipiréticos, antivirales en casos graves"),
    writeln("Edad común: Todas las edades, más frecuente en niños y adultos mayores").

mostrar_info(gastritis) :-
    writeln("Diagnóstico probable: Gastritis"),
    writeln("Sistema afectado: Digestivo"),
    writeln("Causa: Irritación gástrica por estrés, alcohol, medicamentos o H. pylori"),
    writeln("Diagnóstico: Clínico, endoscopia si persiste"),
    writeln("Tratamiento: Antiácidos, IBPs, erradicación de H. pylori"),
    writeln("Edad común: Adultos jóvenes y mayores").

mostrar_info(faringitis) :-
    writeln("Diagnóstico probable: Faringitis"),
    writeln("Sistema afectado: Garganta / Respiratorio"),
    writeln("Causa: Infección viral o bacteriana"),
    writeln("Diagnóstico: Clínico, prueba rápida si es bacteriana"),
    writeln("Tratamiento: Analgésicos, antibióticos si es bacteriana"),
    writeln("Edad común: Niños y adultos jóvenes").

mostrar_info(migraña) :-
    writeln("Diagnóstico probable: Migraña"),
    writeln("Sistema afectado: Neurológico"),
    writeln("Causa: Desconocida (genética, hormonal, ambiental)"),
    writeln("Diagnóstico: Clínico por historia médica"),
    writeln("Tratamiento: Analgésicos, triptanes, prevención"),
    writeln("Edad común: Adolescentes y adultos jóvenes").

mostrar_info(dermatitis) :-
    writeln("Diagnóstico probable: Dermatitis"),
    writeln("Sistema afectado: Piel"),
    writeln("Causa: Transtorno inflamatorio crónico"),
    writeln("Diagnóstico: Clínico por evaluación de síntomas"),
    writeln("Tratamiento: Hidratación de la piel, corticoides tópicos, antihistamínicos").

mostrar_info(resfriado) :-
    writeln("Diagnóstico probable: Resfriado Común"),
    writeln("Sistema afectado: Respiratorio"),
    writeln("Causa: Infección viral (rinovirus, coronavirus)"),
    writeln("Diagnóstico: Clínico por síntomas"),
    writeln("Tratamiento: Reposo, hidratación, sintomáticos"),
    writeln("Edad común: Todas las edades").

mostrar_info(cistitis) :-
    writeln("Diagnóstico probable: Cistitis"),
    writeln("Sistema afectado: Urinario"),
    writeln("Causa: Infección bacteriana (E. coli)"),
    writeln("Diagnóstico: Uroanálisis y urocultivo"),
    writeln("Tratamiento: Antibióticos, abundante hidratación"),
    writeln("Edad común: Adultos, más frecuente en mujeres").

mostrar_info(lumbalgia) :-
    writeln("Diagnóstico probable: Lumbalgia"),
    writeln("Sistema afectado: Musculoesquelético"),
    writeln("Causa: Sobrecarga, postura, degeneración discal"),
    writeln("Diagnóstico: Clínico, imagen si persiste"),
    writeln("Tratamiento: Reposo, analgésicos, fisioterapia"),
    writeln("Edad común: Adultos jóvenes y mayores").

mostrar_info(conjuntivitis) :-
    writeln("Diagnóstico probable: Conjuntivitis"),
    writeln("Sistema afectado: Ocular"),
    writeln("Causa: Infección viral, bacteriana o alergias"),
    writeln("Diagnóstico: Clínico por examen ocular"),
    writeln("Tratamiento: Higiene ocular, colirios antibióticos o antihistamínicos según causa"),
    writeln("Edad común: Todas las edades").

% Entrada de datos
preguntar(Sintoma) :-
    write('¿Tienes el síntoma: '),
    write(Sintoma),
    write('? (si/no) '),
    read(Respuesta),
    nl,
    ((Respuesta == si) -> assert(si(Sintoma)) ;
     assert(no(Sintoma)), fail).

% Memoria dinámica
:- dynamic si/1, no/1.

verificar(S) :-
    (si(S) -> true ;
     no(S) -> fail ;
     preguntar(S)).

deshacer :- retract(si(_)), fail.
deshacer :- retract(no(_)), fail.
deshacer.
