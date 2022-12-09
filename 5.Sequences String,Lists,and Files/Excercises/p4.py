def fun_acronym():

    word = input("Enter the Sentence ").split()

    acronym = ''
    for i in range(len(word)):
        acronym += word[i][:1].capitalize()

    print(f" Your input acroynm is: {acronym}")


fun_acronym()
