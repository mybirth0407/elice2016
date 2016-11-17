def exercise(my_language):
    # 1
    programming_languages = ("C#", "Javascript", "Java",
                             "Python", "Matlab", 'R')
    # 2
    programming_languages = programming_languages[2:5]
    # 3
    new_programming_languages = ("Swift", "Go")
    # 4
    programming_languages += new_programming_languages
    # 5
    is_my_language = False
    if my_language in programming_languages:
        is_my_language = True

    return is_my_language

print(exercise('R'))
