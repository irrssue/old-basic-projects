import imp
from traceback import print_tb
from question_model import Question

from data import question_data
from quiz_brain import quiz_brain


question_bank = []
for question in question_data:
  question_text = question["text"]
  question_answer = question["answer"]

  new_question = Question(q_text=question_text, q_answer=question_answer)

  question_bank.append(new_question)


quiz = quiz_brain(question_bank)

while quiz.still_have_questions():
  quiz.next_question()


print("The end of challenge")
print(f"The final score is: {quiz.score}/{quiz.question_number}")
print("\n")

