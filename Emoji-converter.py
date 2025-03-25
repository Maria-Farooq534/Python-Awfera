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

# using Function


def emoji_converter(message):
    splitted_words = message.split(" ")
    emoji = {
    ":)" : "😊",
    ":(" : "😒"
}
    display_output = ''
    for each_word in splitted_words:
        display_output = display_output + emoji.get(each_word , each_word) + " "
    return display_output

message = input("> ")
print(emoji_converter(message))
        