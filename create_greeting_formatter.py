# Create a function that returns a new function to format greeting messages

def create_greeting_formatter(formatter):
  def greeting(name):
    formatted_message = formatter(name)
    return formatted_message
  return greeting

def daily_greeting(name):
  return f"Have a great day, {name}!"

def too_much_greeting(name):
  return f"I appreciate you more than you know, my darling - {name}!"

def diabetical_greeting(name):
  return f"My life wouldn't be so bright if i wouldn't meet those magical lights of your eyes, {name}!"

first_example = create_greeting_formatter(daily_greeting)
print (first_example("Paul"))

second_example = create_greeting_formatter(too_much_greeting)
print (second_example("Pupu Mare"))

third_example = create_greeting_formatter(diabetical_greeting)
print (third_example("MFHP (= My Favorite Human Pupuloi"))