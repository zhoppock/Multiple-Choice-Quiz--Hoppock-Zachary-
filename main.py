score = 0
print(">>>> The Marvel Movie Character Quiz! <<<<")
print("\n")
print("=== When entering in answers, please use capital letters. ===")
print("\n")

print("Question 1: Who was the first Marvel Superhero to have a movie set in the Marvel Cinematic Universe (MCU)?")
print(" A. The Hulk","\n","B. Thor", "\n", "C. Iron Man", "\n", "D. Captain America")
print("\n")
answer1 = ""

while answer1 != "A" and answer1 != "B" and answer1 != "C" and answer1 != "D":
  answer1 = input("What is the correct answer? ")
  if answer1 == "A":
    print(" Incorrect.")
  elif answer1 == "B":
    print(" Incorrect.")
  elif answer1 == "C":
    print(" Correct!  \'Iron Man\' was the first recognized movie in the MCU.")
    score = score + 1
  elif answer1 == "D":
    print(" Incorrect.")
  else:
    print(" Invalid answer.  Please try again.")

print("\n")

print("Question 2: Which character is the love interest of superhero Iron Man?")
print(" A. Wanda Maximoff","\n","B. Pepper Potts", "\n", "C. Natasha Romanoff", "\n", "D. Bruce Banner")
print("\n")
answer2 = ""

while answer2 != "A" and answer2 != "B" and answer2 != "C" and answer2 != "D":
  answer2 = input("What is the correct answer? ")
  if answer2 == "A":
    print(" Incorrect.")
  elif answer2 == "B":
    print(" Correct!  Starting out as Iron Man/Tony Stark's secretary, Pepper Potts soon begins going out with him.")
    score = score + 1
  elif answer2 == "C":
    print(" Incorrect.")
  elif answer2 == "D":
    print(" Incorrect.")
  else:
    print(" Invalid answer.  Please try again.")

print("\n")

print("Question 3: In which of the 21st Century X-Men films so far has Wolverine not made an apperance?")
print(" A. X-Men: First Class","\n","B. Dark Phoenix", "\n", "C. Logan", "\n", "D. X-Men: The Last Stand")
print("\n")
answer3 = ""

while answer3 != "A" and answer3 != "B" and answer3 != "C" and answer3 != "D":
  answer3 = input("What is the correct answer? ")
  if answer3 == "A":
    print(" Incorrect.")
  elif answer3 == "B":
    print(" Correct!  Dark Phoenix marks the first X-Men movie not to have an appearance by Wolverine.")
    score = score + 1
  elif answer3 == "C":
    print(" Incorrect.")
  elif answer3 == "D":
    print(" Incorrect.")
  else:
    print(" Invalid answer.  Try again.")

print("\n")

print("Question 4: Which character from the 2005 \'Fantastic Four\' movie had their actor/actress reprised as a different Marvel Superhero around the last decade?")
print(" A. Mr. Fantastic","\n","B. The Invisible Woman", "\n", "C. The Thing", "\n", "D. The Human Torch")
print("\n")
answer4 = ""

while answer4 != "A" and answer4 != "B" and answer4 != "C" and answer4 != "D":
  answer4 = input("What is the correct answer? ")
  if answer4 == "A":
    print(" Incorrect.")
  elif answer4 == "B":
    print(" Incorrect.")
  elif answer4 == "C":
    print(" Incorrect.")
  elif answer4 == "D":
    print(" Correct!  The Human Torch was played by Chris Evans, who is more famously notable nowadays as Captain America.")
    score = score + 1
  else:
    print(" Invalid answer.  Try again.")

print("\n")

print("Question 5: Which Guardian of the Galaxy character originates from a planet called \'Terra\'?")
print(" A. Star Lord","\n","B. Groot", "\n", "C. Drax", "\n", "D. Gamora")
print("\n")
answer5 = ""

while answer5 != "A" and answer5 != "B" and answer5 != "C" and answer5 != "D":
  answer5 = input("What is the correct answer? ")
  if answer5 == "A":
    print(" Correct!  Star Lord, better known as Peter Quill, comes from the planet \'Terra\', better known as Earth.")
    score = score + 1
  elif answer5 == "B":
    print(" Incorrect.")
  elif answer5 == "C":
    print(" Incorrect.")
  elif answer5 == "D":
    print(" Incorrect.")
  else:
    print(" Invalid answer.  Try again.")

print("\n")
print("Your score is", str(score), "out of 5.")
print("Thank you for participating!")
