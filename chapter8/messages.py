messages = ['first message', 'second_message', 'third message']


def show_messages(list_messages):
    for message in list_messages:
        print(message)

show_messages(messages[:])
