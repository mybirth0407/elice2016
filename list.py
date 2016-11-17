def exercise(my_language):
    # 1
    programming_languages = ["C#", "Javascript", "Java",
                             "Python", "Matlab", 'R']
    # 2
    del programming_languages[programming_languages.index("Javascript")]
    # 3
    programming_languages.append("C++")
    
    is_my_language = False
    if my_language in programming_languages:
        # 4
        is_my_language = True

    return is_my_language

print(exercise('R'))
