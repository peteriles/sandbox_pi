# Exercises 8-9 .. 8-11: Messages

print('Exercises 8-9..8-11')

text_messages = ['hey there', "what's up", "going out?", "OMG!"]
sent_messages = []
print(f'text_messages = {text_messages}')
print(f'sent_messages = {sent_messages}')

def show_messages(text_messages):
    """Print all messages in a list"""
    for text_message in text_messages:
        print(f'Message is: {text_message}')

def send_messages(text_messages, sent_messages2):
    """Send all messages in a list"""
    while text_messages:
        # Get current message (and remove it from the list)
        text_message = text_messages.pop()
        
        print(f'Message is: {text_message}')

        # Move message to sent list
        sent_messages2.append(text_message)



#show_messages(text_messages)

# Send messages with the list (text_messages) itself
# Note: Python always passes variables by reference, so we can adjust the value of the 
# original variable in the function. Only when we're working with immutable objects 
# (e.g. strings, numbers) does it look like we're passing by value. This is because when
# we change the value of an e.g. string, we aren't modifying the original string, we are
# re-assigning the string to a new value.
send_messages(text_messages, sent_messages) 

# Send messages with a copy of the list
# send_messages(text_messages[:], sent_messages) 

print(f'text_messages = {text_messages}')
print(f'sent_messages = {sent_messages}')

#print(locals())
#print(globals())

print('\n')
