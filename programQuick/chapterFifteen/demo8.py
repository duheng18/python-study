import threading

print('Cats', 'Dogs', 'Frogs', sep=' & ')
threadObj = threading.Thread(target=print, args=['Cats', 'Dogs', 'Frogs'], kwargs={'sep': ' & '})
threadObj.start()
