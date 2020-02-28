# Given two strings check to see if they are anagrams

# Reminder: An anagram is when the two strings can be written using the exact same letters (different order of words or phrase)

# Example:

  # - "Public relations" -> "Crap built on lies"
  # - "Clint eastwood" -> "old west action"

# Ignore spaces and capitalization

# The way I would solve this is would we by doing the following:
  # - Check the lenght of the string s1 against s2
  # - if pass, store the charactters with its repetitions on a sorted list within a list = [[a,2], [b,3]...]
  # - check if both lists are equal

def anagram(s1, s2):
  s1 = list(s1.lower().replace(" ",""))
  s2 = list(s2.lower().replace(" ",""))

  if len(s1) != len(s2):
    print("This aren't anagrams, not the same length")
    return

  print(s1)
  print(s2)
  
  print("---------------------------------------------------------------------------")

  # own sort algorithms
  for i in range(len(s1)-1):
    for j in range(len(s1)-1):
      if s1[j] > s1[j+1]:
        temp = s1[j]
        s1[j] = s1[j+1]
        s1[j+1] = temp

      if s2[j] > s2[j+1]:
        temp = s2[j]
        s2[j] = s2[j+1]
        s2[j+1] = temp

  print(s1)
  print(s2)

  if s1 == s1:
    print("These strings are anagrams")
    return

  # print(s1, s2)


anagram("Crap built on lies","Public relations")