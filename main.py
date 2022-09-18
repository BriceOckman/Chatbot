import random

def chatbot_responses(input):
  responses = [
    "Wow!",
    "How about that?",
    "Darn.",
    "Have fun!",
  ]
  return random.choice(responses)

def chat():
  leave = 'l'
  us_input = input("Hi friend! How is your day going? \n")

  while us_input != leave:

    us_input = input(chatbot_responses(input) + "\n")
  print("Have a fine day! Good bye.")
if __name__ == "__main__":
  chat()
print("x")