from PIL import Image
class Hangman:

    def __init__(self, word):
        self.word = word.lower()
        self.count = 10
        self.game()

    def game(self):
        index = 0
        lstword = list(self.word)
        letterdict = {}
        for x in lstword:
            if x not in letterdict:
                letterdict[x] = [index]
                index += 1
            else:
                letterdict[x] += [index]
                index += 1

        construct_word = (['_ '] * len(self.word)) #word that will be built up with each letter representing an element in a list
        for letter in lstword: #input spaces in between multiple words
            if letter == ' ':
                key = letterdict[letter]
                for x in key:
                    construct_word[x] = '  ' 
        print(''.join(construct_word))
        final_word = "" #word that will be built up as a string and compared to the original word
        while self.count > 0 and final_word != self.word:
            letter = input("Enter a letter ")
            if letter == self.word or final_word == self.word:
                break
            elif letter in self.word:
                key = letterdict[letter] #get index(es) of specific letter in original word
                for x in key:
                    construct_word[x] = letter #insert letter into correct index position in the construct word
                final_word = ''.join(construct_word) #convert construct word which is a list to a string final word
                print(final_word)
            else:
                print("That letter is not in the word!")
                self.count -= 1

        if final_word == self.word:
            print("Congrats, you correctly guessed the word '", self.word, "' and won!")
        else:
            print("Sorry, the correct word was", self.word)
