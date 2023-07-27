#!/usr/bin/env python3
import requests
url = "https://opentdb.com/api.php?amount=10&category=20&difficulty"

url_responce = requests.get(url)
data = url_responce.json()
num = 0
for num in range(1,9):
    correct = 0
    incorrect = 0
    question = data['results'][num]['question']
    answer = data['results'][num]["correct_answer"]
    version = data['results'][num]["type"]
    if version == "multiple":
        choice0 = data['results'][num]["incorrect_answers"][0]
        choice1 = data['results'][num]["incorrect_answers"][1]
        choice2 = data['results'][num]["incorrect_answers"][2]
        print(question)
        trivia = input(f"is it {choice0}, {choice2}, {answer}, or {choice1}:\n")
        if trivia.lower() == answer:
            print("correct")
            correct += 1
        elif trivia.lower() == choice0 or choice1 or choice2:
            print("that is incorrect")
            incorrect += 1
    if version == "boolean":
        choice0 = data['results'][num]["incorrect_answers"][0]
        print(question)
        trivia = input(f"is it {choice0} or {answer}:\n")
        if trivia.lower() == answer:
            print("correct")
            correct += 1
        elif triva.lower() == choice0:
            print("that is incorrect")
            incorrect += 1
   
