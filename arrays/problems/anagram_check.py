# Given two strings check to see if they are anagrams

# Reminder: An anagram is when the two strings can be written using the exact same letters (different order of words or phrase)

# Example:

  # - "Public relations" -> "Crap built on lies"
  # - "Clint eastwood" -> "old west action"

# Ignore spaces and capitalization

# The way I would solve this is would we by doing the following:
  # make the strings lists because in python strings are imutable and therefore can't reassign an index for sorting. 
  # remove spaces and also convert to lowercase
  # sort the two strings, once sorted return s1 == s2 which will be false or true if they are true anagrams

def anagram(s1, s2):
  s1 = list(s1.lower().replace(" ",""))
  s2 = list(s2.lower().replace(" ",""))

  # own sort algorithm
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

  return s1 == s2

# Testing anagrams and random strings
print(anagram("Public relations","Crap built on lies"))
print(anagram("Clint eastwood","old west action"))
print(anagram("Clint eastwood","old west actionn"))