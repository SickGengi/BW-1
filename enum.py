import requests
import re

def extract_csrf_token(response_content):
    # Modifica questa espressione regolare in base alla struttura della risposta
    csrf_pattern = re.compile(r'csrf_token": "(.*?)"')
    match = csrf_pattern.search(response_content)
    if match:
        csrf_token = match.group(1)
        return csrf_token
    else:
        return None

def enumerate_http_services(target_url):
    try:
        # Esempio di richiesta GET
        response_get = requests.get(target_url)
        response_get.raise_for_status()
        print("\nMetodo GET Abilitato \nStatus code:", response_get.status_code)
        # Ottenere il token CSRF della richiesta (se presente)
        token_get = extract_csrf_token(response_get.text)
        print("\nToken CSRF:", token_get)
        # Chiede gli header della richiesta
        response_get.headers
        # Stampa gli header su linee separate
        print("\nHeaders:")
        for header, value in response_get.headers.items():
         print(f"{header}: {value}")
        
        print("\n******************************************************************************")
        

        # Esempio di richiesta POST
        data = {"key": "value"}
        response_post = requests.post(target_url, data=data)
        response_post.raise_for_status()
        print("\nMetodo POST Abilitato \nStatus code:", response_post.status_code)
        # Ottenere il token CSRF della richiesta
        token_post = extract_csrf_token(response_post.text)
        print("\nToken CSRF:", token_post)
        # Chiede gli header della richiesta
        response_post.headers
        # Stampa gli header su linee separate
        print("\nHeaders:")
        for header, value in response_post.headers.items():
         print(f"{header}: {value}")
         
        
        print("\n******************************************************************************")
        

        # Esempio di richiesta DELETE
        data = {"key": "value"}
        response_delete = requests.delete(target_url, data=data)
        response_delete.raise_for_status()
        print("\nMetodo DELETE Abilitato \nstatus code:", response_delete.status_code)
        token_delete = extract_csrf_token(response_delete.text)
        print("\nToken CSRF:", token_delete)
        # Chiede gli header della richiesta
        response_delete.headers
        # Stampa gli header su linee separate
        print("\nHeaders:")
        for header, value in response_delete.headers.items():
         print(f"{header}: {value}")
        
        print("\n******************************************************************************")
        

        # Esempio di richiesta PUT
        data = {"key": "value"}
        response_put = requests.put(target_url, data=data)
        response_put.raise_for_status()
        print("\nMetodo PUT Abilitato \nStatus code:", response_put.status_code)
        # Ottenere il token CSRF della richiesta (se presente)
        token_put = extract_csrf_token(response_put.text)
        print("\nToken CSRF:", token_put)
        # Chiede gli header della richiesta
        response_put.headers
        # Stampa gli header su linee separate
        print("\nHeaders:")
        for header, value in response_put.headers.items():
         print(f"{header}: {value}")
        
        print("\n******************************************************************************")
        

        # Esempio di richiesta HEAD
        data = {"key": "value"}
        response_head = requests.head(target_url, data=data)
        response_head.raise_for_status()
        print("\nMetodo HEAD Abilitato \nStatus code:", response_head.status_code)
        # Ottenere il token CSRF della richiesta (se presente)
        token_head = extract_csrf_token(response_head.text)
        print("\nToken CSRF:", token_head)
        # Chiede gli header della richiesta
        response_head.headers
        # Stampa gli header su linee separate
        print("\nHeaders:")
        for header, value in response_head.headers.items():
         print(f"{header}: {value}")
        
        print("\n******************************************************************************")
        

        # Esempio di richiesta OPTION
        data = {"key": "value"}
        response_options = requests.options(target_url, data=data)
        response_options.raise_for_status()
        print("\nMetodo OPTIONS Abilitato \nStatus code:", response_options.status_code)
        # Ottenere il token CSRF della richiesta (se presente)
        token_options = extract_csrf_token(response_options.text)
        print("\nToken CSRF:", token_options)
        # Chiede gli header della richiesta
        response_options.headers
        # Stampa gli header su linee separate
        print("\nHeaders:")
        for header, value in response_options.headers.items():
         print(f"{header}: {value}")
        
        print("\n******************************************************************************")
        

        

    except requests.exceptions.RequestException as e:
        print(f"Errore durante la connessione a {target_url}: {e}")
        return




if __name__ == "__main__":
    # Chiedi all'utente di inserire l'URL
    target_url = input("Inserisci l'URL del sito: ").strip()

    # Verifica se l'utente ha fornito un'URL valido
    if not target_url.startswith(('http://', 'https://')):
        target_url = 'http://' + target_url

    enumerate_http_services(target_url)
