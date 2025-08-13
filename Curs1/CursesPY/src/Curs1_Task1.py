morse_string = input()
def count_morse_characters(morse_string):
    dots = 0
    dash = 0
    for i in range(len(morse_string)):
      if morse_string[i] == '.':
        dots += 1
      if morse_string[i] == '-':
                 dash += 1
      print(dots)
      print(dash)
    return dots+dash

print(count_morse_characters(morse_string))
