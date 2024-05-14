responses = {
    'exit': 'Ok, good bye',
    'default': 'Sorry, please elaborate...',
    'greeting': 'How may I help you today? '
}

exit_keys = ('exit','quit','q')


if __name__ == '__main__':
    print("Hello there, I am a chat bot built by Robert Godlewski.")
    info = input(responses['greeting'])
    while True:
        if info in exit_keys:
            print(responses['exit'])
            break
        elif info in responses:
            print(responses[info])
        else:
            print(responses['default'])
        info = input("Respond with q to exit or type query here: ")
