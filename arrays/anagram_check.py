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
  pass