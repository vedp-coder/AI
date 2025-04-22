email = "Your account has been compromised! You must take action immediately! Otherwise you might face severe consequences!"

#tokenize this email
token = email.split()
print("Tokens: ", token)
dangerous = ["compromised", "immediately", "consequences"]

for word in token:
  if word.lower() in dangerous:
    print(f"Security word: {word}")



