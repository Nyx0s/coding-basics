import threading
#import _thread

#Aktuellen Thread ausgeben, der den Programmcode der Funktion durchläuft
# ID + Name
import time


def myFunction(id):
    """
    Ich schaue welcher Thread gerade die FUnktion myFUnction durchläuft
    :param id: eindeutige ID
    :return: None
    """
    print(f'{threading.current_thread().name} ist gestartet\n')
    time.sleep(3)
    print(f'\nFunktionsaufruf durch Thread {id}\n')
    print(f'{threading.current_thread().name} ist beendet\n')

threadList = []

for id in range(1,6):
    t = threading.Thread(name=f'Thread {id}', target=myFunction, args=(id,))
    print(t, type(t))

    #Thread starten
    t.start()
    threadList.append(t)

print(f'\nAktiven Threads: {threading.active_count()}')

#Jeder Thread braucht unterschiedlich lange (je nach Resourcen)

#Zusammenwarten bis alle Threads beendet sind
for thread in threadList:
    thread.join()

#wird erst nach beendigung aller Threads ausgeführt
print('ENDE')
