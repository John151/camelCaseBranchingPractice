def camelcase(sentence):
    """convert sentence to camelCase"""
    title_case = sentence.title()
    upper_camel_cased = title_case.replace(' ', '')
    return upper_camel_cased[0:1].lower() + upper_camel_cased[1:]

def banner():
    """display welcome banner"""
    message = 'CAMELCASE PROGRAM'
    stars = '*' * len(message)
    print(f'{stars}\n{message}\n{stars}')

def main():
    banner()
    sentence = input('Enter your sentence: ')
    output = camelcase(sentence)
    print(output)

if __name__ == '__main__':
    main()
