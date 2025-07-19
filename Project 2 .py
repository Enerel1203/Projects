message = input("Type your message: ")

uppercase_message = message.upper()
undercase_message = message.lower()

if message == undercase_message:
    print("Your message in uppercase is:", uppercase_message)
else:
    print("Your message in undercase is:", undercase_message)