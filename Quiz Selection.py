def user_menu(username):
    print("Welcome,", username)
    print("Select a quiz category:")
    for i, category in enumerate(quiz_categories.keys()):
        print(f"{i+1}. {category}")
    choice = int(input("Enter your choice: "))
    selected_category = list(quiz_categories.keys())[choice - 1]
    selected_questions = quiz_categories[selected_category]
    run_quiz(selected_questions)
