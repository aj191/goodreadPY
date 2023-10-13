###AH 10/13/23 this is an AIless Star geneRATING system for book lovers on Good Reads. NO MORE all the same reviews
def main():
    # Initialize the score
    score = 0

    # Define a list of questions, where each question is a dictionary
    questions = [
        {
            "question": "1) How did you feel as soon as you had finished the book?",
            "answers": [
                {"index": 1, "displayed_option": "Wowed and sad it's over", "score": 5},
                {"index": 2, "displayed_option": "Emotional", "score": 4},
                {"index": 3, "displayed_option": "Content", "score": 3},
                {"index": 4, "displayed_option": "Meh", "score": 2},
                {"index": 5, "displayed_option": "Thankfully it's over", "score": 1}
            ]
        },
        {
            "question": "2) Would you recommend?",
            "answers": [
                {"index": 1, "displayed_option": "Very likely (Yelling from rooftops)", "score": 5},
                {"index": 2, "displayed_option": "Likely (sure for the right person)", "score": 4},
                {"index": 3, "displayed_option": "Neither likely nor unlikely (I don't even remember this book I just read)", "score": 3},
                {"index": 4, "displayed_option": "Unlikely except for that one friend", "score": 2},
                {"index": 5, "displayed_option": "Never ever", "score": 1}
            ]
        },
        {
            "question": "3) Plot: I NEEDED TO find out what happened next? Was it too predictable??",
            "answers": [
                {"index": 1, "displayed_option": "Stayed up late, turning pages", "score": 5},
                {"index": 2, "displayed_option": "Average", "score": 3},
                {"index": 3, "displayed_option": "Predictable", "score": 1}
            ]

        },
        {
            "question": "4) How engaged were you in the story?",
            "answers": [
                {"index": 1, "displayed_option": "Extremely Engaged", "score": 5},
                {"index": 2, "displayed_option": "Very Engaged", "score": 4},
                {"index": 3, "displayed_option": "Somewhat Engaged", "score": 3},
                {"index": 4, "displayed_option": "Not So Engaged", "score": 2},
                {"index": 5, "displayed_option": "ZERO engagement, tell me when it's over zzz", "score": 1}
            ]
        },
        {
            "question": "5) Did you feel an extreme emotion? I.e., excited? Shocked? Moved? Appropriately Angered?",
            "answers": [
                {"index": 1, "displayed_option": "A great deal of emotion", "score": 5},
                {"index": 2, "displayed_option": "A lot more emotional than the average book", "score": 4},
                {"index": 3, "displayed_option": "Normal emotional commitment","score": 3},
                {"index": 4, "displayed_option": "Less than normal emotion", "score": 2},
                {"index": 5, "displayed_option": "I felt nothing", "score": 1}
            ]
        },
        {
            "question": "6) Characters...",
            "answers": [
                {"index": 1, "displayed_option": "Exceeded expectations (deep and unique)", "score": 5},
                {"index": 2, "displayed_option": "Average characters found in novels", "score": 3},
                {"index": 3, "displayed_option": "Below expectations (one note, boring, no depth)", "score": 1}
            ]

        },
        {
            "question": "7) Grammar, sentence structure?",
            "answers": [
                {"index": 1, "displayed_option": "Very high quality, I will quote and remember such beautifully written sentences", "score": 5},
                {"index": 2, "displayed_option": "High quality, compared to other books", "score": 4},
                {"index": 3, "displayed_option": "Average", "score": 3},
                {"index": 4, "displayed_option": "Less than average", "score": 2},
                {"index": 5, "displayed_option": "Who wrote this crap?", "score": 1}
            ]
        },
        {
            "question": "8) Would you reread?.",
            "answers": [
                {"index": 1, "displayed_option": "Yes", "score": 5},
                {"index": 2, "displayed_option": "Probably not! Not because it was bad, just so many other books out there", "score": 3},
                {"index": 3, "displayed_option": "No EVER EVER AGAIN", "score": 1}
            ]

        }
    ]

    # Iterate through the list of questions (NERD ALERT)
    for question_data in questions:
        question = question_data["question"]
        answers = question_data["answers"]

        while True:
            print(question)
            for answer in answers:
                print(f"{answer['index']}. {answer['displayed_option']}")

            user_choice = input("Enter the number corresponding to your answer: ")

            try:
                user_choice = int(user_choice)
                if 1 <= user_choice <= len(answers):
                    score += answers[user_choice - 1]["score"]
                    print("*" * 40)
                    print("\n")
                    break
                else:
                    print("!!" * 10)
                    print("ERROR!!!!Invalid choice. Please choose a valid option. TRY AGAIN")
                    print("!!" * 10)
            except ValueError:
                print("#" * 10)
                print("ERROR####Invalid input. Please enter a number.")
                print("#" * 10)


    #print("-" * 40)
    # Display the final score
    #print("Your score is:", score)
    #score= (score/40)*100
    print (score)
    if score <= 20:
        print("*")
        print ("Nerdy generator says..GIVE IT 1 Star! *, you really did not like this book")
        print("*")
    elif score > 20 and score <= 40:
        print("**")
        print ("Nerdy generator says..2 STARS **, below average")
        print("**")
    elif score > 40 and score <= 60:
        print("***")
        print ("Nerdy generator says..3 STARS ***, your average book")
        print("***")
    elif score > 60 and score <= 80:
        print("****")
        print ("Nerdy generator says..4 STARS ****, you liked this book!")
        print("****")
    elif score > 80 and score <= 100:
        print("*****")
        print("Nerdy generator says..5 STARS *****, YOU LOVED this book")
        print("*****")
    else:
        print ("opps i am broken!")
    quit()


if __name__ == "__main__":
    main()

