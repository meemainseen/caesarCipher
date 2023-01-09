from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

End = False

print(logo)


def code(direction, text, shift):
  # Generates a list based on index value for each letter from alphabet list. Ignores non alphabet characters.
  plain_index = []
  for letter in text:
    if letter in alphabet:
      for i, e in enumerate(alphabet):
        if e == letter:
          plain_index.append(i)
    else: plain_index.append(letter)
  #print(f"Plain Index: {plain_index}")   

  # Generates a new list based on shifted values for code or encode. Keeps non alphabet characters as is.
  cipher_index = []
  cipher_text = []
  for x in plain_index:
    if type(x) is int:
      if direction == "encode":
        cipher_index.append(x + shift)
      elif direction == "decode":
        cipher_index.append(x - shift)
    else:
      cipher_index.append(x)
  #print(f"Cipher Index: {cypher_index}")

  # Ensures the value is within range of alphabet list
  for x in cipher_index:
    if type(x) is int:
      if x > 23:
        cipher_text.append(alphabet[x-26])
      elif x < 0:
        cipher_text.append(alphabet[x+26])
      else:
        cipher_text.append(alphabet[x])
    else:
      cipher_text.append(x)

  # Prints the coded or decoded list as string
  print(f"Your {direction}d message is: {''.join(cipher_text)}")

while not End:
# Input direction for coding or decoding the message. Takes only code or decode as valid input. 
  while True:
    try:
      direction = (input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")).lower().strip() 
      if direction == "encode" or direction == "decode":
        break;
      else:
        print("The input value should be code or encode")      
    except ValueError:
      print("Provide correct value...")
      continue
  
  # Input message for the cypher
  text = input("Type your message:\n").lower()
  
  # Input number by which the alphabet should be shifted forward or backwards. Takes a valued bewteen 1 - 25 as valid input. 
  while True:
    try:
      shift = int(input("Type the shift number between 1 - 25:\n"))
      if shift >= 1 and shift <=25:
        break;
      else:
        print("The value should be between 1 - 25")      
    except ValueError:
      print("Pleae provide correct value")
      continue

  # Call to code function
  code(direction, text, shift)

  next = (input("Type Y if you want to go again otherwise type N: ")).lower().strip()
  if next == 'y':
    End = False
  elif next == 'n':
    print("Goodbye!")
    End = True
  

