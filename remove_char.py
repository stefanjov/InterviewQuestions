try:
    string = input('>>>')
    text = string.split(' ')[0]
    character = string.split(' ')[1]
    print(text.replace(character, ''))
except:
    print("Input form: text character")