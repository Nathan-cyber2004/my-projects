from game_logic import GameLogic

game_logic = GameLogic()

def get_geography_question():
    geography_question, geography_choices, geography_answer = game_logic.get_question_answer(game_logic.geography_questions, game_logic.geography_choices, game_logic.geography_answers)
    game_logic.geography_questions.remove(geography_question), game_logic.geography_choices.remove(geography_choices), game_logic.geography_answers.remove(geography_answer)
    if len(game_logic.geography_questions) == 0:
      return False
    else:
      return geography_question, geography_choices, geography_answer

def get_history_question():
    history_question, history_choices, history_answer = game_logic.get_question_answer(game_logic.history_questions, game_logic.history_choices, game_logic.history_answers)
    game_logic.history_questions.remove(history_question), game_logic.history_choices.remove(history_choices), game_logic.history_answers.remove(history_answer)
    return history_question, history_choices, history_answer

def get_science_question():
    science_question, science_choices, science_answer = game_logic.get_question_answer(game_logic.science_questions, game_logic.science_choices, game_logic.science_answers)
    game_logic.science_questions.remove(science_question), game_logic.science_choices.remove(science_choices), game_logic.science_answers.remove(science_answer)
    return science_question, science_choices, science_answer

def get_language_question():
    language_question, language_choices, language_answer = game_logic.get_question_answer(game_logic.language_questions, game_logic.language_choices, game_logic.language_answers)
    game_logic.language_questions.remove(language_question), game_logic.language_choices.remove(language_choices), game_logic.language_answers.remove(language_answer)
    return language_question, language_choices, language_answer

def get_culture_question():
    culture_question, culture_choices, culture_answer = game_logic.get_question_answer(game_logic.culture_questions, game_logic.culture_choices, game_logic.culture_answers)
    game_logic.culture_questions.remove(culture_question), game_logic.culture_choices.remove(culture_choices), game_logic.culture_answers.remove(culture_answer)
    return culture_question, culture_choices, culture_answer

def get_nature_question():
    nature_question, nature_choices, nature_answer = game_logic.get_question_answer(game_logic.nature_questions, game_logic.nature_choices, game_logic.nature_answers)
    game_logic.nature_questions.remove(nature_question), game_logic.nature_choices.remove(nature_choices), game_logic.nature_answers.remove(nature_answer)
    return nature_question, nature_choices, nature_answer

def get_space_question():
    space_question, space_choices, space_answer = game_logic.get_question_answer(game_logic.space_questions, game_logic.space_choices, game_logic.space_answers)
    game_logic.space_questions.remove(space_question), game_logic.space_choices.remove(space_choices), game_logic.space_answers.remove(space_answer)
    return space_question, space_choices, space_answer

def get_riddle_question():
    riddle_question, riddle_choices, riddle_answer = game_logic.get_question_answer(game_logic.riddles_questions, game_logic.riddles_choices, game_logic.riddles_answers)
    game_logic.riddles_questions.remove(riddle_question), game_logic.riddles_choices.remove(riddle_choices), game_logic.riddles_answers.remove(riddle_answer)
    return riddle_question, riddle_choices, riddle_answer

def get_fun_facts_question():
    fun_facts_question, fun_facts_choices, fun_facts_answer = game_logic.get_question_answer(game_logic.fun_facts_questions, game_logic.fun_facts_choices, game_logic.fun_facts_answers)
    game_logic.fun_facts_questions.remove(fun_facts_question), game_logic.fun_facts_choices.remove(fun_facts_choices), game_logic.fun_facts_answers.remove(fun_facts_answer)
    return fun_facts_question, fun_facts_choices, fun_facts_answer