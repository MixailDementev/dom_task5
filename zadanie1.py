# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
text = 'абв Ура, питон крутой абвязык , очень интересные семинарабвы ДЗ! абв'
print(' '.join(list(filter(lambda x: 'абв' not in x, text.replace('абв', '').split()))))