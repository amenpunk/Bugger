import time
import random
import requests
import urllib.parse
import os

URL = str(os.getenv('FORM'))


departamentos = {
    1 : "Contabilidad", 2 : "contabilidad", 3 : "presupuestos", 4 : "estadística", 5 : "estadistica",
    6 : "", 7 : "ventas", 8 : ".", 9 : "rrhh", 10 : "recuros humanos", 11 : "IT", 12 : 'it', 13 : 'informatica',
    12 : "IT",13 : 'papeles', 14 : 'general', 15 : 'actas', 16 : 'permisos', 17 : 'gestiones', 18 : "gerencia",
    19 : 'administracion', 20 : 'compras', 21 : 'planificacion', 22 : "cobros", 23 : 'finanzas publicas', 24 : "presupuestos",
    25 : 'informática', 26 : 'pedidos', 27 : "no se", 28 : 'niguno', 29 : "backoffice"
}

multiple = {
    1 : "Sí",
    2 : "No"
}

dispositivo = {
    1 :  "Teléfono móvil",
    2 :  "Computador"
}

motivos = {
    1 : "No tengo conocimiento", 2 : "El proceso", 3 : "No ha pasado", 4 : "No se le ha puesto el interes debido", 19 : 'factor economico',
    5 : "", 6 : ".", 7 : "Información", 8 : "informacion", 9 : 'desconocimiento', 10 : 'Desconocimiento del Tema' , 11 : 'no estoy familiarizado',
    12 : 'el sistema que se utiliza', 13 : "Desconocimiento" , 14 : 'oportunidades', 15 : 'factor economico', 17 : 'presupuesto', 18 : 'motivos monetarios'
}

delay = [30]
#delay = [300,1,1800,180,900,660,1380,240,900,480,780,960, 340, 1440]

def send_request(raw):
    r = requests.post(URL,
            headers = {
                "authority": "docs.google.com",
                "accept": "*/*",
                "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.128 Safari/537.36",
                "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
                "accept-language": "en-US,en;q=0.9",
                "dnt": '1',
                "origin": "https://google-form-submitter.herokuapp.com",
                "sec-fetch-site": "cross-site",
                "sec-fetch-mode": "cors",
                "sec-fetch-dest": "empty",
                "referer": "https://google-form-submitter.herokuapp.com/",
            },
            data=raw
        )
    print(r)


def void():
    while(True):
        snorlax = delay[random.randint(0,len(delay) - 1) ]
        print('delay => {}'.format(snorlax))
        time.sleep(snorlax)

        i_d = random.randint(1, len(departamentos))
        i_m = random.randint(1, len(motivos))
        binary = random.randint(1,2)

        raw = {
            'entry.1393319388' :  departamentos[i_d],
            'entry.1788585374' :  motivos[i_m],
            'entry.19933933' :  multiple[binary],
            'entry.227994073' :  multiple[binary],
            'entry.573181048' :  multiple[binary],
            'entry.1905983253' :  multiple[binary],
            'entry.1259259080' :  multiple[binary],
            'entry.1099100354' :  multiple[binary],
            'entry.1969660512' :  multiple[binary],
            'entry.1229628029' :  dispositivo[binary],
        }

        raw = urllib.parse.urlencode(raw)
        send_request(raw)
        #time.sleep(100)
        #print (i_d, departamentos[i_d] )


void();
#send_request()

