to_send_messages = ['first_message', 'second_message', 'third_message']
sent_messages = []

def send_messages(to_send_list):
    while to_send_list:
        sent_messages.append(to_send_list.pop())

send_messages(to_send_messages[:])
print(to_send_messages)
print(sent_messages)