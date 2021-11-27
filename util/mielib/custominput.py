from .responseoption import ResponseOption, option, optionList


def bool_input(output, default=None, abrv=True):
    '''A function to get a user's response to a question that has a yes or no
    (True or False) answer.
    
    Keyword arguments:
        default -- This is the default response if the user does not input
    anything. This parameter can be either True, False, or None. If set to None,
    the function will not accept an empty answer. It will require one of the
    given responses. (Defaults to None)
        abrv -- Uses the abbreviated response. (Defaults to True)'''
    true_answers = ["y", "yes"]
    false_answers = ["n", "no"]
    used_index = 0 if abrv else 1
    ammendment = ""
    valid_answers = []
    if default is None:
        ammendment = "[{}/{}]".format(true_answers[used_index],
                                      false_answers[used_index])
        valid_answers = true_answers + false_answers
    elif default:
        ammendment = "[{}/{}]".format(true_answers[used_index].upper(),
                                      false_answers[used_index])
        valid_answers = true_answers + false_answers + [""]
    else:
        ammendment = "[{}/{}]".format(true_answers[used_index],
                                      false_answers[used_index].upper())
        valid_answers = true_answers + false_answers + [""]

    message = "{} {} ".format(output, ammendment)
    valid_input = False

    while (not valid_input):
        user_response = input(message)

        if user_response.lower() in true_answers:
            return True
        elif user_response.lower() in false_answers:
            return False
        elif user_response.lower() in valid_answers:
            return default

        print("I'm sorry, I didn't understand that input.")

def choice_input(output, options, default=None, abrv=True):
    ''''''
    option_list = optionList(options, default, abrv)
    message = "{} {} ".format(output, option_list)
    valid_input = False

    while (not valid_input):
        user_input = input(message)
        possible_option = option(options, user_input)

        if user_input is "" and default.response is not None:
            return default.response
        elif possible_option is None:
            print("I'm sorry, I didn't understand that input.")
        else:
            return possible_option.response