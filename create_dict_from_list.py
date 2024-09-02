names = ["Stefan Banica", "Horia Brenciu", "Mihaela Radulescu", "Teo Trandafir"]
names_dictionary = {}

for name in names:
  splitted_name = name.split()
  print(splitted_name)
  names_dictionary[splitted_name[1]] = splitted_name[0]

print(names_dictionary)