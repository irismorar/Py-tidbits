def count_enemies(enemy_names):
  enemies_dict = {}
  count = 1
  for enemy_name in enemy_names:
    if enemy_name in enemies_dict:
      count += 1
    enemies_dict[enemy_name] = count
  return enemies_dict


enemy_names = ['jackal', 'kobold', 'jackal', 'iris', "jackal"]
print (count_enemies(enemy_names))
