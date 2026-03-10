from util import get_card_values
from util import ascii_card


print(get_card_values(['a-c', '10-h']))
print(get_card_values(['k-c', 'a-c', 'a-h']))

print(ascii_card("10-h"))
print(ascii_card("9-h"))