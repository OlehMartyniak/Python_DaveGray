# try / except are used to catch errors

#print(x) # NameError: name 'x' is not defined

# в даному випадку якщо виникне проблема ми (try) ми виведемо конкретно заготовлене повідомелння (except)
try:
    print(x)
except:
    print("There is an error")

# наприклад якщо ми знаємо конкретно яку помилку потрібно виділити:
# помилка з діленням на 0:
x = 2
try:
    print (x / 0)
except ZeroDivisionError:
    print("Please, do not divide by zero")
else: # else виконається якщо не буде знайдено зазначених помилок
    print("No errors")
finally: # finally спрацює в будь-якому випадку
    print("Finally prints whether or not there is an error")

# Exception as an error
# можна здійснити перевірку на тип даних, наприклад якщо дані не string тоді вивести помилку

try:
    if not type(x) is str:
        raise TypeError("Only strings are allowed")
except Exception as error:
    print(error)

