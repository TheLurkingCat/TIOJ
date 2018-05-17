num_to_string = {0:'Monday',1:'Tuesday',2:'Wednesday',3:'Thursday',4:'Friday',5:'Saturday',6:'Sunday'}
string_to_num = dict(zip(num_to_string.values(), num_to_string.keys()))
a = string_to_num[input()]
b = int(input())
c = (a + b) % 7
print(num_to_string[c])