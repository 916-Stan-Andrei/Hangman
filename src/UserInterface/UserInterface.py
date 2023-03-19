from src.Controller.Service import SentencesService
from src.Tests.SentenceException import SentenceException


class UserInterface:
    def __init__(self):
        self.__service = SentencesService()

    def ui_add_sentence(self):
        sentence = input("Please write a sentence. A valid sentence should have words with at least 3 letters!\n")
        sentence = sentence.strip()
        try:
            self.__service.add_sentence(sentence)
            print("Sentence successfully added to the repo!")
        except SentenceException as e:
            print(e)

    def ui_play(self):
        hangman_goal = "hangman"
        hangman_start = ""
        k = 0
        random_sentence = self.__service.random_sentence().strip()
        string = self.__service.hangman_style(random_sentence)[0]
        counter = self.__service.hangman_style(random_sentence)[1]
        past_letters = self.__service.hangman_style(random_sentence)[2]
        string = string.strip()

        while counter > 0 and hangman_start != hangman_goal:
            print(f"{string} ==> {hangman_start}")
            letter = input("Please choose a letter:")
            while len(letter) > 1:
                print("A LETTER MEANS ONLY ONE CHARACTER!!!")
                letter = input("Please choose a letter:")
            if letter not in random_sentence or letter in past_letters:
                k += 1
                hangman_start = hangman_goal[0:k]
            else:
                past_letters.append(letter)
                new_string = ""
                for i in range(len(random_sentence)):
                    if letter == random_sentence[i]:
                        new_string += letter
                        counter -= 1
                    else:
                        new_string += string[i]
                string = new_string

        if hangman_start == hangman_goal:
            print(f"{string} ==> {hangman_start}")
            print("You lost!")

        if counter == 0:
            print(f"{string} ==> {hangman_start}")
            print("You won!")

        print("\n")

    def print_menu(self):
        print("Hangman")
        print("add => add a sentence to the repo")
        print("play => play")
        print("exit => quit the menu.")
        print()

    def run_menu(self):
        self.print_menu()
        while True:
            opt = input("Choose an option from the menu:")
            opt = opt.strip()
            if opt == "add":
                self.ui_add_sentence()
            elif opt == "play":
                self.ui_play()
            elif opt == "exit":
                return
