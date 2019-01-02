# Simple use case

as a administrator of the system, I want to be able to create a lesson, with a set of nodes (questions). Each question may contain a picture and leads to an other node/question. Eventually, the result page is reached, where to path followed is displayed, along the correct path.


# Data

Lesson
  - Chosen number
  - description

Question
  - Parent Lesson
  - Question text
  - Choices
  - [error committed on last choice ??]

Choice
  - Choice text
  - target question
