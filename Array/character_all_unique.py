# Check that all characters of a string are unique
# We can assume that the characters are all lowercase.
# Notice that we can keep track of all char values in an array of
# size 26, or with a more efficient bit vector.

def char_all_unique_array(string):
   is_found = [0] * 26
   for c in string:
      index = ord(c) - ord('a')
      if is_found[index]:
         return False
      else:
         is_found[index] = 1
   return True

def char_all_unique_bit_vector(string):
   mask = 0
   for c in string:
      index = ord(c) - ord('a')
      if (1 << index) & mask != 0:
         return False
      else:
         mask = mask | (1 << index)
   return True

if __name__ == "__main__":
   values = ["abc", "des", "aba"]
   is_unique = [True, True, False]
   for x in xrange(len(values)):
      assert char_all_unique_bit_vector(values[x]) == is_unique[x]
      assert char_all_unique_array(values[x]) == is_unique[x]
