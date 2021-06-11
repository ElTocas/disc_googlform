# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 11:20:28 2021

@author: marti
"""
import numpy as np

def disc_help(D):
    sez = []
    sez.append(calcola(D["Sezione 1"], ["Analitico","Impulsivo","Tollerante","Sistematico"],[10,1,1,10]))
    sez.append(calcola(D["Sezione 2"], ["Idealista","Ottimista","Riflessivo","Saggio"],[10,10,1,1]))
    sez.append(calcola(D["Sezione 3"], ["Accomodante","Risoluto","Accogliente","Decisivo"],[1,10,1,10]))
    sez.append(calcola(D["Sezione 4"], ["Attivo","Controllato","Progressista","Costante"],[1,10,1,10]))
    sez.append(calcola(D["Sezione 5"], ["Prudente","Spontaneo","Meticoloso","Libero"],[10,1,10,1]))
    sez.append(calcola(D["Sezione 6"], ["Distaccato","Esilarante","Prevedibile","Ispiratore"],[1,10,1,10]))
    sez.append(calcola(D["Sezione 7"], ["Collaborativo","Obbediente","Deciso","Impaziente"],[1,1,10,10]))
    sez.append(calcola(D["Sezione 8"], ["Diretto","Giudizioso","Riservato","Vigile"],[1,10,10,1]))

    sez.append(calcola(D["Sezione 9"], ["Veloce","Calcolatore","Contemplativo","Incondizionato"],[1,10,10,1]))
    sez.append(calcola(D["Sezione 10"], ["Silenzioso","Entusiasta","Passionale","Procedurale"],[1,10,10,1]))
    sez.append(calcola(D["Sezione 11"], ["Ambizioso","Conservativo","Stabile","Assertivo"],[10,1,1,10]))
    sez.append(calcola(D["Sezione 12"], ["Energico","Flessibile","Paziente","Affabile"],[1,1,10,10]))
    sez.append(calcola(D["Sezione 13"], ["Logico","Metodico","Disinibito","Loquace"],[10,10,1,1]))
    sez.append(calcola(D["Sezione 14"], ["Calmo","Convincente","Attento","Persuasore"],[1,10,1,10]))
    sez.append(calcola(D["Sezione 15"], ["Garbato","Sicuro di sè","Premuroso","Determinato"],[1,10,1,10]))
    sez.append(calcola(D["Sezione 16"], ["Coerente","Istintivo","Esigente","Ascoltatore"],[10,1,1,10]))

    sez.append(calcola(D["Sezione 17"], ["Minuzioso","Emancipato","Formale","Sciolto"],[10,1,10,1]))
    sez.append(calcola(D["Sezione 18"], ["Preciso","Amichevole","Realistico","Socievole"],[1,10,1,10]))
    sez.append(calcola(D["Sezione 19"], ["Motivato","Competitivo","Armonioso","Gentile"],[10,10,1,1]))
    sez.append(calcola(D["Sezione 20"], ["Affidabile","Leale","Esplicito","Senza riserve"],[10,10,1,1]))
    sez.append(calcola(D["Sezione 21"], ["Innovatore","Sapiente","Pioniere","Indagatore"],[1,10,1,10]))
    sez.append(calcola(D["Sezione 22"], ["Alla mano","Pratico","Pragmatico","Sensibile"],[10,1,1,10]))
    sez.append(calcola(D["Sezione 23"], ["Accurato","Perfezionista","Problem solver","Intuitivo"],[1,1,10,10]))
    sez.append(calcola(D["Sezione 24"], ["Perseverante","Dinamico","Confortante","Spregiudicato"],[10,1,10,1]))        
    
    return sez


def calcola(risp_eff,risp_poss,val_poss):
    s1 = np.array(risp_poss)
    s1_value = np.array(val_poss)
    temp = np.array(risp_eff.split(", "))
    valore = np.sum(s1_value[np.where(np.in1d(s1,temp))])
    return valore


def informazioni_colori():
    a = []
    a.append("È orientato al risultato, amante delle sfide. Prende decisioni rapide e si sente a proprio agio nell’assumere il controllo di un gruppo e nell’accollarsi i rischi. L’impressione generale è che i Rossi siano dei leader naturali. Sono tanto determinati che riescono nell’intento nonostante gli ostacoli. Amano la competizione, spesso amministratori delegati o presidenti sono Rossi. La competizione è presente in tutto ciò che fanno, anche quando il premio non è così importante, l’obiettivo è vincere, sempre!")
    a.append("Il suo atteggiamento è sempre positivo, intrattengono gli altri, fanno sorridere, e attorno a loro succede sempre qualcosa di divertente. Sanno catturare l’attenzione degli altri, e conservarla. Ci fanno sentire importanti. Sono anche molto sensibili, come i Rossi, i Gialli amano prendere decisioni rapide, ma raramente riescono a spiegarle razionalmente. Di solito le giustificano dicendo “ho sentito che era la cosa giusta”.")
    a.append("I Verdi non si mettono in mostra come gli altri, e per questo conferiscono una buona dose di serenità a una situazione. Se avete un amico Verde non dimenticherà mai il vostro compleanno. Non sarà geloso dei vostri successi, non cercherà di mettervi in ombra raccontando le proprie gesta. Non vorrà primeggiare a tutti i costi, né mettervi sotto torchio o tormentarvi con richieste sempre più assurde. Non vi vedrà come un concorrente se doveste trovarvi in una situazione simile. Non prenderà il comando a meno che qualcuno non lo incarichi di farlo.")
    a.append("I Blu hanno tutte le risposte, dietro le quinte non fa che analizzare, classificare, valutare e giudicare. È anche un pessimista, anzi, un realista. Sa valutare gli errori e i rischi. È anche un malinconico che vede il bicchiere mezzo vuoto. Lui sa tutto, non si dà delle arie, ma il suo modo di presentare i fatti impedisce di metterli in dubbio. Ricorda benissimo dove ha trovato le informazioni e può anche recuperare la fonte per dimostrarvi che ha ragione. Di solito conoscono perfettamente il fatto loro prima di aprire bocca.")
    return a