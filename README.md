# 💻 Calcolatrice a Riga di Comando (CLI Calculator)

## 🎯 Obiettivo del Progetto

Questo progetto è stato sviluppato come esercizio per consolidare le basi di **Python**, concentrandosi sui seguenti obiettivi di apprendimento:

1.  **Modularità del Codice:** Separare la logica di calcolo (matematica) dalla logica di gestione dell'input (interazione utente).
2.  **Validazione dell'Input:** Implementare cicli robusti per garantire che l'utente inserisca i tipi di dati corretti (numeri e operatori validi).
3.  **Uso dei Dizionari:** Utilizzare un dizionario per mappare i simboli degli operatori (valori) ai nomi delle funzioni (chiavi) e viceversa.

---

## 🏗️ Struttura del Codice

Il progetto è composto da due file Python principali che comunicano tra loro:

### 1. `operations.py`

Questo modulo contiene tutte le **funzioni matematiche pure**. Non contiene logica di input/output, rendendolo un modulo *stand-alone* e riutilizzabile.

| Funzione | Descrizione |
| :---: | :---: |
| `sum(a, b)` | Esegue l'addizione. |
| `subctract(a, b)` | Esegue la sottrazione. |
| `multiply(a, b)` | Esegue la moltiplicazione. |
| `divide(a, b)` | Esegue la divisione. |
| `square(a, b)` | Esegue l'elevamento a potenza. |
| `module(a, b)` | Calcola il modulo (resto della divisione). |

### 2. `calculator.py`

Questo è il modulo principale che gestisce il flusso dell'applicazione e l'interazione con l'utente.

* **Dizionario `operations`**: Definisce la mappatura tra i nomi delle operazioni e i simboli accettati (es. `"sum": "+" `).
* **`get_number(prompt)`**: Richiede l'input numerico all'utente, utilizzando un ciclo `while` e un blocco `try-except` per forzare l'inserimento di un valore di tipo `float`.
* **`get_operation(prompt)`**: Richiede l'input dell'operatore, utilizzando un ciclo `while` per convalidare che il simbolo sia tra quelli definiti nel dizionario `operations`.
* **`calculator(num1, num2, operation)`**: Funzione principale che prende l'operatore e, tramite un blocco di `if/elif`, chiama la funzione corrispondente dal modulo `operations.py`.
* **Logica di Output**: Utilizza un ciclo `for` iterando su `operations.items()` per trovare il nome completo dell'operazione (la chiave) dato il simbolo (il valore) inserito dall'utente.

---

## ▶️ Istruzioni per l'Esecuzione

1.  Assicurati che i file `calculator.py` e `operations.py` siano salvati nella stessa directory.
2.  Apri il tuo terminale e naviga nella directory del progetto.
3.  Esegui lo script principale:

    ```bash
    python calculator.py
    ```

Il programma richiederà, in sequenza, il primo numero, il secondo numero e l'operatore.

---
