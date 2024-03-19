import socket
from ip2geotools.databases.noncommercial import DbIpCity
from termcolor import colored
import requests
from pytube import YouTube
from gtts import gTTS
import os 
import pyshorteners
import requests
from bs4 import BeautifulSoup
import re
import random
import string
from ascii import menu
from ascii import logo_imprime
from ascii import display_contact_info




def search_ip_whit_url():
    url_info = """
                                        Rastreador de dirección Ip mediante la URL del lugar



    """
    print(colored(url_info, 'green'))

    url = input(colored("Inserte una URL: ", 'green'))
    ip = socket.gethostbyname(url)
    response = DbIpCity.get(ip, api_key="free")

    print(colored(f"IP: {ip}", 'green'))
    print(colored(f"City: {response.city}", 'green'))
    print(colored(f"Regíon: {response.region}", 'green'))
    print(colored(f"Country: {response.country}", 'green'))
#termina clase search ip whit url
    
def subdomain_scarnner():
    scanner = '''
       
                                                        Subdomain Scanner


    '''
    print(colored(scanner, 'green'))

    domain = input(colored("Ingresa el dominio: ", 'green'))
    file = open('wordlist.txt', 'r')
    content = file.read()

    subdomains = content.splitlines()

    for subdomain in subdomains:
        url1 = f"http://{subdomain}.{domain}"
        url2 = f"https://{subdomain}.{domain}"
        try:
            requests.get(url1)
            print(colored(f"Discovered URl: {url1}", 'green'))
            requests.get(url2)
            print(colored(f"Discovered URl: {url2}" ,'green'))
        except requests.ConnectionError:
            pass

#Fin de la clase subdomain scanner
        
def youtube_downloader_video():
    downloader_video = '''
                                                    YouTube downloader video


'''
    print(colored(downloader_video, 'green'))

    link = input(colored("Ingrese el link de youtube: ", 'green'))
    yt = YouTube(link)

    video = yt.streams.get_highest_resolution()
    video.download()
    print(colored("Done! ", 'green'))

#termina la clase youtube_downloader_video
    
def text_to_speech():
    name_speech = '''
                                                    Text to speech in python


'''
    print(colored(name_speech, 'green'))

    text = str(input(colored("Ingrese el texto deseado: ", 'green')))
    language = 'es'
    speech = gTTS(text = text, lang = language, slow = False)
    speech.save("text.mp3")
    os.system("open text.mp3")

#termina la clase text to speech
    
def short_url():
    name_short_url = '''
                                                            Shorter URL


'''

    print(colored(name_short_url, 'green'))


    url = input(colored("Enter the URL: ", 'green'))

    def shortenurl(url):
        s = pyshorteners.Shortener()
        print("\n")
        print(colored(s.tinyurl.short(url),'green'))

    shortenurl(url)
#termina la clase shorter url

def screping_web():
    name_screping_web='''
                                                            Screping web
'''

    print(colored(name_screping_web, 'green'))


    url = input(colored("Ingrese la url que deseea consultar: ", 'green'))

    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')


    for element in soup.find_all('a'):  
        print(element.get('href'))

#fin de la clase screping web
        
def python_ofuscate():
    name_python_ofuscate = '''
                                                    Python ofuscate
'''

    print(colored(name_python_ofuscate, 'green'))


    def ofuscar_codigo(codigo):
        variables = re.findall(r'\b[a-zA-Z_][a-zA-Z0-9_]*\b', codigo)
        variables_unicas = set(variables) - set(['for', 'in', 'if', 'else', 'print', 'def', 'import', 'from', 'as'])  

        mapa_ofuscacion = {}

        for var in variables_unicas:
            nuevo_nombre = ''.join(random.choices(string.ascii_letters, k=8))  
            mapa_ofuscacion[var] = nuevo_nombre

        for original, nuevo in mapa_ofuscacion.items():
            codigo = re.sub(r'\b' + original + r'\b', nuevo, codigo)

        return codigo

    print(colored("Por favor, ingresa tu código Python. Escribe 'FIN' en una nueva línea para terminar la entrada.", 'green'))
    codigo_ingresado = []
    while True:
        linea = input()
        if linea == "FIN":
            break
        codigo_ingresado.append(linea)

    codigo_ingresado = "\n".join(codigo_ingresado)
    codigo_ofuscado = ofuscar_codigo(codigo_ingresado)

    print(colored("\nCódigo Ofuscado:\n", 'green'))
    print(colored(codigo_ofuscado, 'green'))




def display_menu():
    menu()
    while True:
        try:
            option = int(input(colored("Ingresa tu opción: ", 'green')))
            if option == 1:
                logo_imprime()
                display_contact_info()
            elif option == 2:
                logo_imprime()
                search_ip_whit_url()
            elif option == 3:
                logo_imprime()
                subdomain_scarnner()
            elif option == 4:
                logo_imprime()
                youtube_downloader_video()
            elif option == 5:
                logo_imprime()
                text_to_speech()
            elif option == 6:
                logo_imprime()
                short_url()
            elif option==7:
                logo_imprime()
                screping_web()
            elif option==8:
                logo_imprime()
                python_ofuscate()
            break
        except ValueError:
            print(colored("Por favor ingresa un número valido.", 'green'))

if __name__ == "__main__":
    while True:
        display_menu()
        print("\n")
        exit_option = input(colored("Deseas salir? (si/no): ", 'green')).lower()
        if exit_option == 'si':
            break
