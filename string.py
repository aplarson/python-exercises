def num_to_string(num, base):
    digits = [
      "0",
      "1",
      "2",
      "3",
      "4",
      "5",
      "6",
      "7",
      "8",
      "9",
      "A",
      "B",
      "C",
      "D",
      "E",
      "F"
    ]
    result = ""
    while num > 0:
        result = digits[num % base] + result
        num = num // base
    return result

def caesar_cipher(message, offset):
    letters = "abcdefghijklmnopqrstuvwxyz"
    result = ""
    for i in range(0, len(message)):
        result += letters[(letters.find(message[i]) + offset) % 26]
    return result

def reverse(string):
    result = ""
    length = len(string)
    for i in range(0, len(string)):
        result += string[-(i + 1)]
    return result

print(reverse("helloworld"))
