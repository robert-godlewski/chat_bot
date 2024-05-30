import json


exit_keys = ('exit','quit','q')


if __name__ == '__main__':
    print("Hello there, I am a chat bot built by Robert Godlewski.")
    try:
        data = open('responses.json').read()
        responses = json.loads(data)
        print(responses['greeting'])
    except:
        print("responses are not properly loaded")
        responses = None
    info = None
    while responses:
        info = input("> ")
        print("Respond with q to exit.")
        if info in exit_keys:
            print(responses['exit'])
            break
        elif info == 'hello' or info == '2':
            print(responses['greeting'])
        elif info in responses:
            print(responses[info])
        else:
            i = 0
            while i < len(responses['confused']):
                print(responses['confused'][i])
                i += 1
