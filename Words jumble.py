import sys
import random
score = 0
def input_words():
        sentence_input = input("Please, input your sentence: ")
        return [sentence_input.split(), sentence_input]
def play_again():
    play_again=input("Do you want to play again (Yes/No): ").upper()
    if (play_again.upper()=="YES"):
        main()
    else:
        False
def main():
    global score
    function = input_words()
    originalInput = function[1]
    sentence_list = function[0]
    print(originalInput)
    sentence_list.reverse()
    for i in range (0, len(sentence_list)):
        tmp = sentence_list[i];
        swapWith = random.randrange(0, len(sentence_list)-1)
        sentence_list[i] = sentence_list[swapWith]
        sentence_list[swapWith] = tmp
    print(sentence_list)
    guess=input("Insert your answer: ")
    if (guess==originalInput):
        score = score+1
        print("Your Answer Is Correct!! Congratuliations! You win one point!")
        print("Your current score is " +str(score))
        play_again()
    else:
        score = score-1
        print(":( Sorry, Your Answer Was Wrong.. You lose one point!")
        print("Your current score is " +str(score))
        play_again()
main()
