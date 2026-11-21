"""Demo of Python sets."""

empty_set = set()
numbers1 = { 1, 2, 3, 4, 5 }
numbers2 = { 4, 5, 6, 7, 8 }

numbers1.add(6)                # adds 6 to the set
numbers1.remove(2)             # removes 2 from the set
# numbers1.remove(10)          # raises KeyError if 10 is not in the set
numbers1.discard(10)           # removes 10 from the set if it exists


# set operations
union = numbers1 | numbers2                     # ένωση των δύο συνόλων
intersection = numbers1 & numbers2              # τομή των δύο συνόλων
difference = numbers1 - numbers2                # διαφορά των δύο συνόλων
symmetric_difference = numbers1 ^ numbers2      # συμμετρική διαφορά των δύο συνόλων