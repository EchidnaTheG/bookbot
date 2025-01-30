import string
chars={}


def countwords(file):
    words= file.split()
    count=len(words)
    return count 

def countchars(words):
    for i in words:
        if i in chars:
            chars[i]+= 1
        else:
            chars[i]= 1
    return chars

def printreport(chars, book, wordcount):
    print(f"--- Begin report of {book} ---")
    print(f"{wordcount} words found in the document")
    
    for i in chars:
        if i in string.ascii_lowercase:
            print(f"The '{i}' character was found {chars[i]} times")

    print("--- End report ---")


def main():
    book="books/frankenstein.txt"
    with open(book) as f:
        file_contents = f.read()
        wordslowered= file_contents.lower()
        x=countwords(wordslowered)
        y=countchars(wordslowered)
        printreport(y, book, x)

main()