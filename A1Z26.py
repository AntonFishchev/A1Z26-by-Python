alfavit = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж',
           'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о',
           'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц',
           'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю',
           'я']

def StartMesseng():
    print("Программа кодирования/декодирования текста шифром A1Z26\n")
    print("Выберите действие:")
    print("1. Зашифровать\n2. Расшифровать ")

def RegisterLower(text):
    originalString = list(text)
    for i in range(0, len(text)):
        if originalString[i].isupper():
            originalString[i] = originalString[i].lower()
    return originalString

def CoderText(text):
    text = RegisterLower(text)
    string = list(text)
    encodedText = ""

    for i in range(0, len(text) - 1):
        if (string[i] in alfavit):
            if (string[i + 1] in alfavit):
                encodedText += str(alfavit.index(string[i]) + 1) + "-"
            else:
                encodedText += str(alfavit.index(string[i]) + 1)
        else:
            encodedText += string[i]

    if (string[len(text) - 1] in alfavit):
        encodedText += str(alfavit.index(string[len(text) - 1]) + 1)
    else:
        encodedText += string[len(text) - 1]

    return encodedText

def DecoderText(text):
    string = list(text + " ")
    num = ""
    decodedText = ""

    for i in range(0, len(text) + 1):
        if (string[i].isdigit()):
            num += str(string[i])
        else:
            if num != "":
                decodedText += alfavit[int(num) - 1]
            if (string[i] != "-"):
                decodedText += string[i]
            num = ""

    return decodedText

#ПРОГРАММА
StartMesseng()
vote = int(0)
while vote == 0:
    vote = int(input())
    if vote == 1:
        print("Введите текст")
        originalText = str(input())
        encodedText = CoderText(originalText)
        print(encodedText, "\n")
    if vote == 2:
        print("Введите текст")
        encodedText = str(input())
        originalText = DecoderText(encodedText)
        print(originalText, "\n")
    vote = 0
    print("Выберите номер пункта из списка")
    print("1. Зашифровать\n2. Расшифровать ")
