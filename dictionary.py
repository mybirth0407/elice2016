def exercise(my_language):
    # 1
    programming_languages_popularity = {"Java": 24.0, "Python": 13.2,
                                        "PHP": 10.4, "C#": 9.0}
    # 2
    del programming_languages_popularity["PHP"]
    programming_languages_popularity["Javascript"] = 7.6
    programming_languages_popularity["C++"] = 7.0
    # 3
    my_language_popularity = programming_languages_popularity[my_language]

    return my_language_popularity

print(exercise('Python'))
