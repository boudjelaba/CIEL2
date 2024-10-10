import http.server as http
import asyncio
import websockets
import socketserver
import multiprocessing
import cv2
import sys
from datetime import datetime as dt
import threading
import imutils
import beepy as beep
import time

# Garder une trace des processus
PROCESSES = []

def log(message):
    print("[LOG] " + str(dt.now()) + " - " + message)

def camera(man):
    log("Démarrage de la caméra")
    vc = cv2.VideoCapture(0)

    if vc.isOpened():
        r, f = vc.read()
    else:
        r = False

    while r:
        cv2.waitKey(20)
        r, f = vc.read()
        f = cv2.resize(f, (640, 480))
        encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 65]
        man[0] = cv2.imencode('.jpg', f, encode_param)[1]
        ##################################################
        f = cv2.cvtColor(f, cv2.COLOR_BGR2GRAY)
        f = cv2.GaussianBlur(f, (21,21), 0)
        alarm_counter = 0
        while True:
            #alarm_counter = 0
            ##################################################
            alarm = False
            alarm_mode = False

            def beep_alarm():
                global alarm
                for _ in range(3):
                    if not alarm_mode:
                        break
                    print("Objet en mouvement")
                    beep.beep(1)
                alarm = False
            ##################################################
            _, frame = vc.read()
            frame = cv2.resize(frame, (640, 480))

            frame_bw = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            frame_bw = cv2.GaussianBlur(frame_bw, (5,5), 0)
            difference = cv2.absdiff(frame_bw, f)
            threshold = cv2.threshold(difference, 25, 255, cv2.THRESH_BINARY)[1]            

            if threshold.sum() > 10000:
                f = frame_bw
                alarm_counter += 1
                alarm_mode = True
                man[0] = cv2.imencode('.jpg', threshold, encode_param)[1]
            else:
                if alarm_counter > 0:
                    f = f
                    alarm_counter -= 1
                else:
                    f = f
                    alarm_mode = False
                    man[0] = cv2.imencode('.jpg', frame, encode_param)[1]

            if alarm_counter > 20:
                if not alarm:
                    alarm = True
                    threading.Thread(target=beep_alarm).start()
        ##################################################

# Gestionnaire de serveur HTTP
def server():
    server_address = ('127.0.0.1', 8000) # http://127.0.0.1:8000
    if sys.version_info[1] < 7:
        class ThreadingHTTPServer(socketserver.ThreadingMixIn, http.HTTPServer):
            pass
        httpd = ThreadingHTTPServer(server_address, http.SimpleHTTPRequestHandler)
    else:
        httpd = http.ThreadingHTTPServer(server_address, http.SimpleHTTPRequestHandler)
    log("Serveur démarré")
    httpd.serve_forever()

def socket(man):
    # Gérer les connexions Websocket
    async def handler(websocket, path):
        log("Socket ouvert")
        try:
            while True:
                await asyncio.sleep(0.033) # 30 fps
                await websocket.send(man[0].tobytes())
        except websockets.exceptions.ConnectionClosed:
            log("Socket fermé")

    log("Démarrage du gestionnaire de socket")
    # Créer l'objet
    start_server = websockets.serve(ws_handler=handler, host='127.0.0.1', port=8585) # http://127.0.0.1:8585
    # Démarrer le serveur, son ajout à la boucle d'événements
    asyncio.get_event_loop().run_until_complete(start_server)
    # Enregistrer le gestionnaire de connexion Websocket, exécutant ainsi la boucle d'événements
    asyncio.get_event_loop().run_forever()


def main():
    # queue = multiprocessing.Queue()
    manager = multiprocessing.Manager()
    lst = manager.list()
    lst.append(None)
    # Héberger la page, créer le serveur
    http_server = multiprocessing.Process(target=server)
    # Configurer le gestionnaire Websocket
    socket_handler = multiprocessing.Process(target=socket, args=(lst,))
    # Configurer la caméra
    camera_handler = multiprocessing.Process(target=camera, args=(lst,))
    # Ajoutez-les à la liste
    PROCESSES.append(camera_handler)
    PROCESSES.append(http_server)
    PROCESSES.append(socket_handler)
    for p in PROCESSES:
        p.start()
    # Attente
    while True:
        pass

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        for p in PROCESSES:
            p.terminate()