import spacy

nlp = spacy.load("en_core_web_sm")

def extract_user_info(dialogue_history):
  """Extracts user information from a dialogue history.

  Args:
    dialogue_history: The dialogue history.

  Returns:
    A dictionary containing the user information.
  """

  # Tokenize the dialogue history.
  tokens = []
  for sentence in dialogue_history:
    tokens.extend(nlp(sentence))

  # Extract the user name.
  user_name = None
  for token in tokens:
    if token.pos_ == "NOUN" and token.text.startswith("My"):
      user_name = token.text[2:]
      break

  # Extract the user age.
  user_age = None
  for token in tokens:
    if token.pos_ == "NUM" and token.text.isdigit():
      user_age = int(token.text)
      break

  # Extract the user hobbies.
  user_hobbies = []
  for token in tokens:
    if token.pos_ == "NOUN" and token.text not in ["My", "name", "age", "hobbies"]:
      user_hobbies.append(token.text)

  # Extract the user interests.
  user_interests = []
  for token in tokens:
    if token.pos_ == "NOUN" and token.text not in ["My", "name", "age", "hobbies", "interests"]:
      user_interests.append(token.text)

  # Extract the user favorite sport.
  user_favorite_sport = None
  for token in tokens:
    if token.pos_ == "NOUN" and token.text.startswith("My") and token.text.endswith("sport"):
      user_favorite_sport = token.text[2:-5]
      break

  # Extract the user favorite food.
  user_favorite_food = None
  for token in tokens:
    if token.pos_ == "NOUN" and token.text.startswith("My") and token.text.endswith("food"):
      user_favorite_food = token.text[2:-4]
      break

  # Return the user information.
  return {
    "name": user_name,
    "age": user_age,
    "hobbies": user_hobbies,
    "interests": user_interests,
    "favorite_sport": user_favorite_sport,
    "favorite_food": user_favorite_food,
  }
dialogue_history = ["My name is John Doe. I am 30 years old. I like to play basketball and watch movies. My favorite food is pizza.", "I also like to play tennis."]

user_info = extract_user_info(dialogue_history)

print(user_info)
