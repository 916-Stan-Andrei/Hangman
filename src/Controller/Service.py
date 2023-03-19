import random

from src.Repository.RepoTextFile import RepoTextFile
from src.Tests.SentenceException import SentenceException


class SentencesService:
    def __init__(self):
        self.__repo = RepoTextFile("./Hangman.txt")

    def add_sentence(self, sentence):
        for i in range(len(self.__repo.get_all())):
            if sentence.strip() == self.__repo.get_entity(i).strip():
                raise SentenceException("The sentence is already in the repository!")

        counter = 0
        for i in range(len(sentence)):
            if sentence[i].isalpha() is False and sentence[i] != " ":
                raise SentenceException("Just letters in your sentence!!!")
            elif sentence[i].isalpha():
                counter += 1
            elif sentence[i] == " " and counter < 3:
                raise SentenceException("A word in the sentence has not enough letters!")
            elif sentence[i] == " " and counter >= 3:
                counter = 0

        if counter < 3:
            raise SentenceException("The last word in the sentence has not enough letters!")

        self.__repo.repo_add(sentence)

    def hangman_style(self, sentence):
        hangman_sentence = [sentence[0]]
        for i in range(1, len(sentence)):
            if sentence[i] == " ":
                hangman_sentence.append(sentence[i-1])
                hangman_sentence.append(sentence[i+1])
        hangman_sentence.append(sentence[-1])
        hangman_sentence.append(" ")

        string = ""
        counter = 0
        for i in range(len(sentence)):
            if sentence[i] in hangman_sentence:
                string += sentence[i]
            else:
                string += "_"
                counter += 1

        return string, counter, hangman_sentence

    def random_sentence(self):
        return self.__repo.get_entity(random.randint(0, len(self.__repo.get_all()) - 1))



