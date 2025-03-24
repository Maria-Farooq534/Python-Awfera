# Emoji Converter
user_input = input("> ")
words = user_input.split(" ")
emojis = {
    ":)" : "😊",
    ":(" : "😒"
}
output = ""
for word in words:
    output += emojis.get(word , word)  + " "
print(output)