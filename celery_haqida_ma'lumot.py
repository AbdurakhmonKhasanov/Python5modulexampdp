# #Celery
#
# Celerydan foydalanish va qo'lash oson bo'lib va u konfiguratsiya fayllariga muhtoj emas.
#
# U orqali  bir qancha emailarga bir vaqtning o'zida  bitta ma'lumotni jo'nata olamiz '.
#
# Celery ishlatilgan bir misolni keltirmoqchiman:
#
# import celery
#
# ilova = celery('salom', broker='amqp://guest@localhost//')
#
# def salom():
#     return "Hello World!"
#
#
# Bitta Celery  jarayoni bir daqiqada millionlab vazifalarni bajarishi mumkin, bunda millisekunddan past bo'lgan aylanish kechikishi (RabitMQ, librabbitmq va optimallashtirilgan sozlamalar yordamida).

