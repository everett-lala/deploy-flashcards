from django.shortcuts import render, redirect
from random import randint
import random
from .models import State, List, Word, WordFive, WordSix, WordSeven, WordEight
from flash_card_login_app.models import User
from django.contrib import messages


################################ DASHBOARD #############################################

def home(request):
    context = {
        'user' : User.objects.all(),
    }
    return render(request, 'home.html', context)


################################ WORD SCRAMBLE FOUR LETTERS #############################################

def word_scramble(request):
    if not "incorrect_guesses" in request.session:
        request.session['incorrect_guesses'] = []
    if request.method == "GET":
        many_words = Word.objects.all()
        
        #PICKING THE WORD AND SCRAMBLE
        pick_a_word = random.choice(many_words)
        #SCRAMBLE THE WORD
        pick_a_word_str = str(pick_a_word)
        convert_wrd_lst = list(pick_a_word_str)
        
        random.shuffle(convert_wrd_lst)
        
        shuffled_word = ''
        for letter in convert_wrd_lst:
            shuffled_word += letter

        # SEND INFO TO HTML PAGE
        context = {
            'shuffled_word' : shuffled_word,
            'answer': pick_a_word,
        }
        return render(request, 'wordscramble/word_scramble.html', context)   
    else:
        request.session['ws_answer'] = request.POST['wordscramble_answer']
        request.session['old_shuffled_word'] = request.POST['old_shuffled_word']
        request.session['answer'] = request.POST['answer']
        request.session['current_user'] = request.POST['current_user']

        # Error handling if no form fillout
        if not request.session['ws_answer']:
            request.session['my_answer'] = "Please provide an answer before submitting."
            request.session['color'] = "primary"
            context = {
                'shuffled_word': request.session['old_shuffled_word'],
                'answer': request.session['answer'],
                'my_answer': request.session['my_answer'],
                'color' : request.session['color'],
    }
            return render(request, 'wordscramble/word_scramble.html', context)

        # CORRECT ANSWER
        if request.session['ws_answer'] == request.session['answer']:
            request.session['my_answer'] = request.session['ws_answer'] 
            request.session['color'] = "success"
            context = {
                'my_answer': request.session['my_answer'],
                'color' : request.session['color'],}
            
            # increase username word_scram_count
            update_word_scram_count = User.objects.get(username = request.session['username'])
            update_word_scram_count.word_scram_count += 1
            update_word_scram_count.save()

            # CLEARING OUT incorrect_guesses SESSIONS
            request.session['incorrect_guesses'].clear()
            return render(request, 'wordscramble/correct_word_scramble.html', context)
        else:
            # INCORRECT ANSWER
            request.session['my_answer'] = f"Incorrect! Your guess {request.session['ws_answer']}, did not match."
            request.session['color'] = "danger"

            request.session['incorrect_guesses'].append(request.session['ws_answer'])
            return redirect('word-scramble-incorrect')
        return redirect('word-scramble')

def word_scramble_incorrect(request):
    context = {
        'shuffled_word': request.session['old_shuffled_word'],
        'answer': request.session['answer'],
        'my_answer': request.session['my_answer'],
        'color' : request.session['color'],
        "incorrect_guesses": request.session['incorrect_guesses']
    }
    return render(request, 'wordscramble/word_scramble.html', context)

def word_scramble_mercy(request):
    request.session['answer'] = request.POST['answer']
    my_answer =  request.session['answer']
    color = "warning"
    context = {
        'my_answer': my_answer,
        'color' : color,
        }
    # CLEARING OUT incorrect_guesses SESSIONS
    request.session['incorrect_guesses'].clear()
    return render(request, 'wordscramble/word_scramble_mercy.html', context)

################################ WORD SCRAMBLE FIVE LETTERS #############################################

def word_scramble_five(request):
    if not "incorrect_guesses" in request.session:
        request.session['incorrect_guesses'] = []
    if request.method == "GET":
        many_words = WordFive.objects.all()
        #PICKING THE WORD AND SCRAMBLE
        pick_a_word = random.choice(many_words)
        #SCRAMBLE THE WORD
        pick_a_word_str = str(pick_a_word)
        convert_wrd_lst = list(pick_a_word_str)
        random.shuffle(convert_wrd_lst)
        shuffled_word = ''
        for letter in convert_wrd_lst:
            shuffled_word += letter

        # SEND INFO TO HTML PAGE
        context = {
            'shuffled_word' : shuffled_word,
            'answer': pick_a_word,
        }
        return render(request, 'wordscramble/word_scramble_five.html', context)   
    else:
        request.session['ws_answer'] = request.POST['wordscramble_answer']
        request.session['old_shuffled_word'] = request.POST['old_shuffled_word']
        request.session['answer'] = request.POST['answer']
        request.session['current_user'] = request.POST['current_user']

        # Error handling if no form fillout
        if not request.session['ws_answer']:
            request.session['my_answer'] = "Please provide an answer before submitting."
            request.session['color'] = "primary"
            context = {
                'shuffled_word': request.session['old_shuffled_word'],
                'answer': request.session['answer'],
                'my_answer': request.session['my_answer'],
                'color' : request.session['color'],
    }
            return render(request, 'wordscramble/word_scramble_five.html', context)
        # CORRECT ANSWER
        if request.session['ws_answer'] == request.session['answer']:
            request.session['my_answer'] = request.session['ws_answer'] 
            request.session['color'] = "success"
            context = {
                'my_answer': request.session['my_answer'],
                'color' : request.session['color'],}
            
            # increase username word_scram_count
            update_word_scram_count = User.objects.get(username = request.session['username'])
            update_word_scram_count.word_scram_count += 1
            update_word_scram_count.save()
            #CLEARING OUT incorrect_guesses SESSIONS
            request.session['incorrect_guesses'].clear()
            return render(request, 'wordscramble/correct_word_scramble_five.html', context)
        else:
            # INCORRECT ANSWER
            request.session['my_answer'] = f"Incorrect! Your guess {request.session['ws_answer']}, did not match."
            request.session['color'] = "danger"
            request.session['incorrect_guesses'].append(request.session['ws_answer'])
            return redirect('word-scramble-incorrect-five')
        return redirect('word-scramble-five')

def word_scramble_incorrect_five(request):
    context = {
        'shuffled_word': request.session['old_shuffled_word'],
        'answer': request.session['answer'],
        'my_answer': request.session['my_answer'],
        'color' : request.session['color'],
        "incorrect_guesses": request.session['incorrect_guesses']
    }
    return render(request, 'wordscramble/word_scramble_five.html', context)

def word_scramble_mercyfive(request):
    request.session['answer'] = request.POST['answer']
    my_answer =  request.session['answer']
    color = "warning"
    context = {
        'my_answer': my_answer,
        'color' : color,
        }
    # CLEARING OUT incorrect_guesses SESSIONS
    request.session['incorrect_guesses'].clear()
    return render(request, 'wordscramble/word_scramble_mercyfive.html', context)

################################ WORD SCRAMBLE SIX LETTERS #############################################

def word_scramble_six(request):
    if not "incorrect_guesses" in request.session:
        request.session['incorrect_guesses'] = []
    if request.method == "GET":
        many_words = WordSix.objects.all()
        
        #PICKING THE WORD AND SCRAMBLE
        pick_a_word = random.choice(many_words)

        #SCRAMBLE THE WORD
        pick_a_word_str = str(pick_a_word)
        convert_wrd_lst = list(pick_a_word_str)
        random.shuffle(convert_wrd_lst)
        shuffled_word = ''
        for letter in convert_wrd_lst:
            shuffled_word += letter

        # SEND INFO TO HTML PAGE
        context = {
            'shuffled_word' : shuffled_word,
            'answer': pick_a_word,
        }
        return render(request, 'wordscramble/word_scramble_six.html', context)   
    else:
        request.session['ws_answer'] = request.POST['wordscramble_answer']
        request.session['old_shuffled_word'] = request.POST['old_shuffled_word']
        request.session['answer'] = request.POST['answer']
        request.session['current_user'] = request.POST['current_user']

        # Error handling if no form fillout
        if not request.session['ws_answer']:
            request.session['my_answer'] = "Please provide an answer before submitting."
            request.session['color'] = "primary"
            context = {
                'shuffled_word': request.session['old_shuffled_word'],
                'answer': request.session['answer'],
                'my_answer': request.session['my_answer'],
                'color' : request.session['color'],
    }
            return render(request, 'wordscramble/word_scramble_six.html', context)

        # CORRECT ANSWER
        if request.session['ws_answer'] == request.session['answer']:
            request.session['my_answer'] = request.session['ws_answer'] 
            request.session['color'] = "success"
            context = {
                'my_answer': request.session['my_answer'],
                'color' : request.session['color'],}

            # increase username word_scram_count
            update_word_scram_count = User.objects.get(username = request.session['username'])
            update_word_scram_count.word_scram_count += 1
            update_word_scram_count.save()

            # CLEARING OUT incorrect_guesses SESSIONS
            request.session['incorrect_guesses'].clear()
            return render(request, 'wordscramble/correct_word_scramble_six.html', context)
        else:
            # INCORRECT ANSWER
            request.session['my_answer'] = f"Incorrect! Your guess {request.session['ws_answer']}, did not match."
            request.session['color'] = "danger"

            request.session['incorrect_guesses'].append(request.session['ws_answer'])
            return redirect('word-scramble-incorrect-six')
        return redirect('word-scramble-six')

def word_scramble_incorrect_six(request):
    context = {
        'shuffled_word': request.session['old_shuffled_word'],
        'answer': request.session['answer'],
        'my_answer': request.session['my_answer'],
        'color' : request.session['color'],
        "incorrect_guesses": request.session['incorrect_guesses']
    }
    return render(request, 'wordscramble/word_scramble_six.html', context)

def word_scramble_mercysix(request):
    request.session['answer'] = request.POST['answer']
    my_answer =  request.session['answer']
    color = "warning"
    context = {
        'my_answer': my_answer,
        'color' : color,
        }
    # CLEARING OUT incorrect_guesses SESSIONS
    request.session['incorrect_guesses'].clear()
    return render(request, 'wordscramble/word_scramble_mercysix.html', context)


################################ WORD SCRAMBLE SEVEN LETTERS #############################################

def word_scramble_seven(request):
    if not "incorrect_guesses" in request.session:
        request.session['incorrect_guesses'] = []
    if request.method == "GET":
        many_words = WordSeven.objects.all()
        
        #PICKING THE WORD AND SCRAMBLE
        pick_a_word = random.choice(many_words)

        #SCRAMBLE THE WORD
        pick_a_word_str = str(pick_a_word)
        convert_wrd_lst = list(pick_a_word_str)
        random.shuffle(convert_wrd_lst)
        shuffled_word = ''
        for letter in convert_wrd_lst:
            shuffled_word += letter

        # SEND INFO TO HTML PAGE
        context = {
            'shuffled_word' : shuffled_word,
            'answer': pick_a_word,
        }
        return render(request, 'wordscramble/word_scramble_seven.html', context)   
    else:
        request.session['ws_answer'] = request.POST['wordscramble_answer']
        request.session['old_shuffled_word'] = request.POST['old_shuffled_word']
        request.session['answer'] = request.POST['answer']
        request.session['current_user'] = request.POST['current_user']

        # Error handling if no form fillout
        if not request.session['ws_answer']:
            request.session['my_answer'] = "Please provide an answer before submitting."
            request.session['color'] = "primary"
            context = {
                'shuffled_word': request.session['old_shuffled_word'],
                'answer': request.session['answer'],
                'my_answer': request.session['my_answer'],
                'color' : request.session['color'],
    }
            return render(request, 'wordscramble/word_scramble_seven.html', context)

        # CORRECT ANSWER
        if request.session['ws_answer'] == request.session['answer']:
            request.session['my_answer'] = request.session['ws_answer'] 
            request.session['color'] = "success"
            context = {
                'my_answer': request.session['my_answer'],
                'color' : request.session['color'],}

            # increase username word_scram_count
            update_word_scram_count = User.objects.get(username = request.session['username'])
            update_word_scram_count.word_scram_count += 1
            update_word_scram_count.save()

            # CLEARING OUT incorrect_guesses SESSIONS
            request.session['incorrect_guesses'].clear()
            return render(request, 'wordscramble/correct_word_scramble_seven.html', context)
        else:
            # INCORRECT ANSWER
            request.session['my_answer'] = f"Incorrect! Your guess {request.session['ws_answer']}, did not match."
            request.session['color'] = "danger"

            request.session['incorrect_guesses'].append(request.session['ws_answer'])
            return redirect('word-scramble-incorrect-seven')

        return redirect('word-scramble-seven')

def word_scramble_incorrect_seven(request):
    context = {
        'shuffled_word': request.session['old_shuffled_word'],
        'answer': request.session['answer'],
        'my_answer': request.session['my_answer'],
        'color' : request.session['color'],
        "incorrect_guesses": request.session['incorrect_guesses']
    }
    return render(request, 'wordscramble/word_scramble_seven.html', context)

def word_scramble_mercyseven(request):
    request.session['answer'] = request.POST['answer']
    my_answer =  request.session['answer']
    color = "warning"
    context = {
        'my_answer': my_answer,
        'color' : color,
        }
    # CLEARING OUT incorrect_guesses SESSIONS
    request.session['incorrect_guesses'].clear()
    return render(request, 'wordscramble/word_scramble_mercyseven.html', context)


################################ WORD SCRAMBLE EIGHT LETTERS #############################################

def word_scramble_eight(request):
    if not "incorrect_guesses" in request.session:
        request.session['incorrect_guesses'] = []
    if request.method == "GET":
        many_words = WordEight.objects.all()
        
        #PICKING THE WORD AND SCRAMBLE
        pick_a_word = random.choice(many_words)

        #SCRAMBLE THE WORD
        pick_a_word_str = str(pick_a_word)
        convert_wrd_lst = list(pick_a_word_str)
        random.shuffle(convert_wrd_lst)
        shuffled_word = ''
        for letter in convert_wrd_lst:
            shuffled_word += letter

        # SEND INFO TO HTML PAGE
        context = {
            'shuffled_word' : shuffled_word,
            'answer': pick_a_word,
        }
        return render(request, 'wordscramble/word_scramble_eight.html', context)   
    else:
        request.session['ws_answer'] = request.POST['wordscramble_answer']
        request.session['old_shuffled_word'] = request.POST['old_shuffled_word']
        request.session['answer'] = request.POST['answer']
        request.session['current_user'] = request.POST['current_user']

        # Error handling if no form fillout
        if not request.session['ws_answer']:
            request.session['my_answer'] = "Please provide an answer before submitting."
            request.session['color'] = "primary"
            context = {
                'shuffled_word': request.session['old_shuffled_word'],
                'answer': request.session['answer'],
                'my_answer': request.session['my_answer'],
                'color' : request.session['color'],
    }
            return render(request, 'wordscramble/word_scramble_eight.html', context)

        # CORRECT ANSWER
        if request.session['ws_answer'] == request.session['answer']:
            request.session['my_answer'] = request.session['ws_answer'] 
            request.session['color'] = "success"
            context = {
                'my_answer': request.session['my_answer'],
                'color' : request.session['color'],}
            
            # increase username word_scram_count
            update_word_scram_count = User.objects.get(username = request.session['username'])
            update_word_scram_count.word_scram_count += 1
            update_word_scram_count.save()

            # CLEARING OUT incorrect_guesses SESSIONS
            request.session['incorrect_guesses'].clear()
            return render(request, 'wordscramble/correct_word_scramble_eight.html', context)
        else:
            # INCORRECT ANSWER
            request.session['my_answer'] = f"Incorrect! Your guess {request.session['ws_answer']}, did not match."
            request.session['color'] = "danger"

            request.session['incorrect_guesses'].append(request.session['ws_answer'])
            return redirect('word-scramble-incorrect-eight')

        return redirect('word-scramble-eight')

def word_scramble_incorrect_eight(request):
    context = {
        'shuffled_word': request.session['old_shuffled_word'],
        'answer': request.session['answer'],
        'my_answer': request.session['my_answer'],
        'color' : request.session['color'],
        "incorrect_guesses": request.session['incorrect_guesses']
    }
    return render(request, 'wordscramble/word_scramble_eight.html', context)

def word_scramble_mercyeight(request):
    request.session['answer'] = request.POST['answer']
    my_answer =  request.session['answer']
    color = "warning"
    context = {
        'my_answer': my_answer,
        'color' : color,
        }
    # CLEARING OUT incorrect_guesses SESSIONS
    request.session['incorrect_guesses'].clear()
    return render(request, 'wordscramble/word_scramble_mercyeight.html', context)


################################ TODO List #############################################
def to_do(request):
    context = {
        'list' : List.objects.all().order_by('priority'),
    }
    return render(request, 'todo/todo.html', context)

def todo_delete(request, list_id):
    if request.method == "POST":
        item = List.objects.get(pk=list_id)
        item.delete()
        messages.success(request, ("To Do Item has been Deleted!"))
        return redirect('to-do')
    return redirect('to-do')

def done(request, list_id):
    if request.method == "POST":
        item = List.objects.get(pk=list_id)
        item.completed = True
        item.save()
        return redirect('to-do')
    return redirect('to-do')

def not_completed(request, list_id):
    if request.method == "POST":
        item = List.objects.get(pk=list_id)
        item.completed = False
        item.save()
        return redirect('to-do')
    return redirect('to-do')


################################ STATE CAPITALS #############################################

def statecapitals(request):
    if request.method == "POST":
        sc_answer = request.POST['statecapitals_answer']
        old_state = request.POST['old_state']
        state_capital = request.POST['state_capital']
        current_user = request.POST['current_user']
        
        # Error handling if no form fillout
        if not sc_answer:
            my_answer = "Please provide an answer before submitting."
            color = "primary"
            r_state_id = randint(1,51)
            random_state = State.objects.get(id=r_state_id)
            # shape = random_state.shape

            return render(request, 'us_states/statecapitals.html', {
                'state': random_state,
                'my_answer': my_answer,
                'color' : color,})

        if sc_answer == state_capital:
            my_answer = f"Correct! {sc_answer} is the capital of {old_state} " 
            color = "success"

            # increase username capital_count
            update_capital_count = User.objects.get(username = request.session['username'])
            update_capital_count.capital_count += 1
            update_capital_count.save()

            r_state_id = randint(1,51)
            random_state = State.objects.get(id=r_state_id)
            capital = random_state.capital

        else:
            my_answer = f"Incorrect!  {state_capital} is the capital of {old_state}, not {sc_answer} "
            color = "danger"

            # decrease username capital_count
            update_capital_count = User.objects.get(username = request.session['username'])
            update_capital_count.capital_count -= 1
            update_capital_count.save()

            r_state_id = randint(1,51)
            random_state = State.objects.get(id=r_state_id)
            capital = random_state.capital

        return render(request, 'us_states/statecapitals.html', {
        'sc_answer': sc_answer,
        'my_answer': my_answer,
        "state": random_state,
        "capital": random_state.capital,
        'color' : color,
        # 'state' : old_state,
        } )

    else:
        r_state_id = randint(1,51)
        random_state = State.objects.get(id=r_state_id)
        capital = random_state.capital

        return render(request, 'us_states/statecapitals.html', {
            "state": random_state,
            "capital": random_state.capital,
        })
        


################################ STATE SHAPE #############################################
def stateshape(request):
    if request.method == "POST":
        ss_answer = request.POST['stateshape_answer']
        old_shape = request.POST['old_shape']
        state_name = request.POST['state_name']
        current_user = request.POST['current_user']

        # Error handling if no form fillout
        if not ss_answer:
            my_answer = "Please provide an answer before submitting."
            color = "primary"
            r_state_id = randint(1,51)
            random_state = State.objects.get(id=r_state_id)
            shape = random_state.shape

            return render(request, 'us_states/stateshape.html', {
                "state": random_state,
                'shape': shape,
                'my_answer': my_answer,
                'color' : color,})
        
        if ss_answer == state_name:
            my_answer = f"Correct! {ss_answer} is the correct state" 
            color = "success"

            # increase username shape_count
            update_shape_count = User.objects.get(username = request.session['username'])
            update_shape_count.shape_count += 1
            update_shape_count.save()

            r_state_id = randint(1,51)
            random_state = State.objects.get(id=r_state_id)
            shape = random_state.shape
        else:
            my_answer = f"Incorrect!  The shape was {state_name}, not {ss_answer} "
            color = "danger"

            # decrease username shape_count
            update_shape_count = User.objects.get(username = request.session['username'])
            update_shape_count.shape_count -= 1
            update_shape_count.save()

            r_state_id = randint(1,51)
            random_state = State.objects.get(id=r_state_id)
            shape = random_state.shape

        return render(request, 'us_states/stateshape.html', {
        'ss_answer': ss_answer,
        'my_answer': my_answer,
        "state": random_state,
        "shape": random_state.shape,
        'color' : color,
        } )

    else:
        r_state_id = randint(1,51)
        random_state = State.objects.get(id=r_state_id)
        shape = random_state.shape
        return render(request, 'us_states/stateshape.html', {
            "state": random_state,
            "shape": random_state.shape,
        })


################################ STATE FLAG #############################################
def stateflag(request):
    if request.method == "POST":
        sf_answer = request.POST['stateflag_answer']
        old_flag = request.POST['old_flag']
        state_name = request.POST['state_name']
        current_user = request.POST['current_user']

        # Error handling if no form fillout
        if not sf_answer:
            my_answer = "Please provide an answer before submitting."
            color = "primary"
            r_state_id = randint(1,51)
            random_state = State.objects.get(id=r_state_id)
            flag = random_state.flag

            return render(request, 'us_states/stateflag.html', {
                "state": random_state,
                'flag': flag,
                'my_answer': my_answer,
                'color' : color,})
        if sf_answer == state_name:
            my_answer = f"Correct! {sf_answer} is the correct state" 
            color = "success"

            # increase username flag_count
            update_flag_count = User.objects.get(username = request.session['username'])
            update_flag_count.flag_count += 1
            update_flag_count.save()

            r_state_id = randint(1,51)
            random_state = State.objects.get(id=r_state_id)
            flag = random_state.flag
        
        else:
            my_answer = f"Incorrect!  The flag was for {state_name}, not {sf_answer} "
            color = "danger"

            # decrease username flag_count
            update_flag_count = User.objects.get(username = request.session['username'])
            update_flag_count.flag_count -= 1
            update_flag_count.save()

            r_state_id = randint(1,51)
            random_state = State.objects.get(id=r_state_id)
            flag = random_state.flag
        
        return render(request, 'us_states/stateflag.html', {
        'sf_answer': sf_answer,
        'my_answer': my_answer,
        "state": random_state,
        "flag": random_state.flag,
        'color' : color,
        } )

        
    else:
        r_state_id = randint(1,51)
        random_state = State.objects.get(id=r_state_id)
        flag = random_state.flag
        return render(request, 'us_states/stateflag.html', {
            "state": random_state,
            "flag": random_state.flag,
        })



################################ STATE STUDY #############################################
# displays all states in order of statehood
def statestudy(request):
    context = {
        'state': State.objects.all().order_by('order_statehood'),
        }
    return render(request, 'us_states/statestudy.html', context)

# displays all states in order of thier name
def statestudy_byname(request):
    context = {
        'state': State.objects.all().order_by('name'),
        }
    return render(request, 'us_states/statestudy.html', context)

# displays all states in a random order
def statestudy_random(request):
    context = {
        'state': State.objects.all().order_by('?'),
        }
    return render(request, 'us_states/statestudy.html', context)


################################ ADDITION #############################################
def addition(request):
    add_num_1 = randint(0,9)
    add_num_2 = randint(0,9)

    if request.method == "POST":
        add_answer = request.POST['addition_answer']
        old_add_num_1 = request.POST['old_add_num_1']
        old_add_num_2 = request.POST['old_add_num_2']
        current_user = request.POST['current_user']

        # Error handling if no form fillout
        if not add_answer:
            my_answer = "Please provide an answer before submitting."
            color = "primary"

            return render(request, 'math/addition.html', {
        'add_num_1': add_num_1,
        'add_num_2': add_num_2,
        'my_answer': my_answer,
        'color' : color,
    })

        correct_answer = int(old_add_num_1) + int(old_add_num_2)
        if int(add_answer) == correct_answer:
            my_answer = "Correct!  " + old_add_num_1 + " + " + old_add_num_2 + " = " +  add_answer
            color = "success"

            # increase username add_count
            update_add_count = User.objects.get(username = request.session['username'])
            update_add_count.add_count += 1
            update_add_count.save()

        else:
            my_answer = "Incorrect!  " + old_add_num_1 + " + " + old_add_num_2 + " = "  +  str(correct_answer) + " not " + add_answer
            color = "danger"

            # decrease username add_count
            update_add_count = User.objects.get(username = request.session['username'])
            update_add_count.add_count -= 1
            update_add_count.save()

        return render(request, 'math/addition.html', {
            'add_answer': add_answer,
            'my_answer': my_answer,
            'add_num_1': add_num_1,
            'add_num_2': add_num_2,
            'color' : color,
            } )


    return render(request, 'math/addition.html', {
        'add_num_1': add_num_1,
        'add_num_2': add_num_2,
    })


################################ ADDITION LEVEL TWO #############################################
def addition_lvl_two(request):
    add_num_1 = randint(10,99)
    add_num_2 = randint(10,99)

    if request.method == "POST":
        add_answer = request.POST['addition_answer']
        old_add_num_1 = request.POST['old_add_num_1']
        old_add_num_2 = request.POST['old_add_num_2']
        current_user = request.POST['current_user']

        # Error handling if no form fillout
        if not add_answer:
            my_answer = "Please provide an answer before submitting."
            color = "primary"

            return render(request, 'math/addition_lvl_two.html', {
        'add_num_1': add_num_1,
        'add_num_2': add_num_2,
        'my_answer': my_answer,
        'color' : color,
    })

        correct_answer = int(old_add_num_1) + int(old_add_num_2)
        if int(add_answer) == correct_answer:
            my_answer = "Correct!  " + old_add_num_1 + " + " + old_add_num_2 + " = " +  add_answer
            color = "success"

            # increase username add_count
            update_add_count = User.objects.get(username = request.session['username'])
            update_add_count.add_count += 1
            update_add_count.save()

        else:
            my_answer = "Incorrect!  " + old_add_num_1 + " + " + old_add_num_2 + " = "  +  str(correct_answer) + " not " + add_answer
            color = "danger"

            # decrease username add_count
            update_add_count = User.objects.get(username = request.session['username'])
            update_add_count.add_count -= 1
            update_add_count.save()

        return render(request, 'math/addition_lvl_two.html', {
            'add_answer': add_answer,
            'my_answer': my_answer,
            'add_num_1': add_num_1,
            'add_num_2': add_num_2,
            'color' : color,
            } )


    return render(request, 'math/addition_lvl_two.html', {
        'add_num_1': add_num_1,
        'add_num_2': add_num_2,
    })


################################ ADDITION LEVEL THREE #############################################
def addition_lvl_three(request):
    add_num_1 = randint(100,999)
    add_num_2 = randint(100,999)

    if request.method == "POST":
        add_answer = request.POST['addition_answer']
        old_add_num_1 = request.POST['old_add_num_1']
        old_add_num_2 = request.POST['old_add_num_2']
        current_user = request.POST['current_user']

        # Error handling if no form fillout
        if not add_answer:
            my_answer = "Please provide an answer before submitting."
            color = "primary"

            return render(request, 'math/addition_lvl_three.html', {
        'add_num_1': add_num_1,
        'add_num_2': add_num_2,
        'my_answer': my_answer,
        'color' : color,
    })

        correct_answer = int(old_add_num_1) + int(old_add_num_2)
        if int(add_answer) == correct_answer:
            my_answer = "Correct!  " + old_add_num_1 + " + " + old_add_num_2 + " = " +  add_answer
            color = "success"

            # increase username add_count
            update_add_count = User.objects.get(username = request.session['username'])
            update_add_count.add_count += 1
            update_add_count.save()

        else:
            my_answer = "Incorrect!  " + old_add_num_1 + " + " + old_add_num_2 + " = "  +  str(correct_answer) + " not " + add_answer
            color = "danger"

            # decrease username add_count
            update_add_count = User.objects.get(username = request.session['username'])
            update_add_count.add_count -= 1
            update_add_count.save()

        return render(request, 'math/addition_lvl_three.html', {
            'add_answer': add_answer,
            'my_answer': my_answer,
            'add_num_1': add_num_1,
            'add_num_2': add_num_2,
            'color' : color,
            } )


    return render(request, 'math/addition_lvl_three.html', {
        'add_num_1': add_num_1,
        'add_num_2': add_num_2,
    })


################################ ADDITION LEVEL FOUR #############################################
def addition_lvl_four(request):
    add_num_1 = randint(1000,9999)
    add_num_2 = randint(1000,9999)

    if request.method == "POST":
        add_answer = request.POST['addition_answer']
        old_add_num_1 = request.POST['old_add_num_1']
        old_add_num_2 = request.POST['old_add_num_2']
        current_user = request.POST['current_user']

        # Error handling if no form fillout
        if not add_answer:
            my_answer = "Please provide an answer before submitting."
            color = "primary"

            return render(request, 'math/addition_lvl_four.html', {
        'add_num_1': add_num_1,
        'add_num_2': add_num_2,
        'my_answer': my_answer,
        'color' : color,
    })

        correct_answer = int(old_add_num_1) + int(old_add_num_2)
        if int(add_answer) == correct_answer:
            my_answer = "Correct!  " + old_add_num_1 + " + " + old_add_num_2 + " = " +  add_answer
            color = "success"

            # increase username add_count
            update_add_count = User.objects.get(username = request.session['username'])
            update_add_count.add_count += 1
            update_add_count.save()

        else:
            my_answer = "Incorrect!  " + old_add_num_1 + " + " + old_add_num_2 + " = "  +  str(correct_answer) + " not " + add_answer
            color = "danger"

            # decrease username add_count
            update_add_count = User.objects.get(username = request.session['username'])
            update_add_count.add_count -= 1
            update_add_count.save()

        return render(request, 'math/addition_lvl_four.html', {
            'add_answer': add_answer,
            'my_answer': my_answer,
            'add_num_1': add_num_1,
            'add_num_2': add_num_2,
            'color' : color,
            } )


    return render(request, 'math/addition_lvl_four.html', {
        'add_num_1': add_num_1,
        'add_num_2': add_num_2,
    })


################################ MULTIPLICATION #############################################
def multiplication(request):
    mltp_num_1 = randint(0,9)
    mltp_num_2 = randint(0,9)

    if request.method == "POST":
        multiply_answer = request.POST['multiplication_answer']
        old_mltp_num_1 = request.POST['old_mltp_num_1']
        old_mltp_num_2 = request.POST['old_mltp_num_2']
        current_user = request.POST['current_user']

        # Error handling if no form fillout
        if not multiply_answer:
            my_answer = "Please provide an answer before submitting."
            color = "primary"

            return render(request, 'math/multiplication.html', {
        'mltp_num_1': mltp_num_1,
        'mltp_num_2': mltp_num_2,
        'my_answer': my_answer,
        'color' : color,
    })

        correct_answer = int(old_mltp_num_1) * int(old_mltp_num_2)

        if int(multiply_answer) == correct_answer:
            my_answer = "Correct!  " + old_mltp_num_1 + " * " + old_mltp_num_2 + " = " +  multiply_answer
            color = "success"

            # increase username multi_count
            update_multi_count = User.objects.get(username = request.session['username'])
            update_multi_count.multi_count += 1
            update_multi_count.save()

        else:
            my_answer = "Incorrect!  " + old_mltp_num_1 + " + " + old_mltp_num_2 + " = "  +  str(correct_answer) + " not " + multiply_answer
            color = "danger"

            # decrease username multi_count
            update_multi_count = User.objects.get(username = request.session['username'])
            update_multi_count.multi_count -= 1
            update_multi_count.save()


        return render(request, 'math/multiplication.html', {
            'multiply_answer':multiply_answer,
            'my_answer': my_answer,
            'mltp_num_1': mltp_num_1,
            'mltp_num_2': mltp_num_2,
            'color' : color,
            } )


    return render(request, 'math/multiplication.html', {
        'mltp_num_1': mltp_num_1,
        'mltp_num_2': mltp_num_2,
    })


################################ MULTIPLICATION LEVEL TWO #############################################
def multiplication_lvl_two(request):
    mltp_num_1 = randint(10,99)
    mltp_num_2 = randint(10,99)

    if request.method == "POST":
        multiply_answer = request.POST['multiplication_answer']
        old_mltp_num_1 = request.POST['old_mltp_num_1']
        old_mltp_num_2 = request.POST['old_mltp_num_2']
        current_user = request.POST['current_user']

        # Error handling if no form fillout
        if not multiply_answer:
            my_answer = "Please provide an answer before submitting."
            color = "primary"

            return render(request, 'math/multiplication_lvl_two.html', {
        'mltp_num_1': mltp_num_1,
        'mltp_num_2': mltp_num_2,
        'my_answer': my_answer,
        'color' : color,
    })

        correct_answer = int(old_mltp_num_1) * int(old_mltp_num_2)

        if int(multiply_answer) == correct_answer:
            my_answer = "Correct!  " + old_mltp_num_1 + " * " + old_mltp_num_2 + " = " +  multiply_answer
            color = "success"

            # increase username multi_count
            update_multi_count = User.objects.get(username = request.session['username'])
            update_multi_count.multi_count += 1
            update_multi_count.save()

        else:
            my_answer = "Incorrect!  " + old_mltp_num_1 + " + " + old_mltp_num_2 + " = "  +  str(correct_answer) + " not " + multiply_answer
            color = "danger"

            # decrease username multi_count
            update_multi_count = User.objects.get(username = request.session['username'])
            update_multi_count.multi_count -= 1
            update_multi_count.save()


        return render(request, 'math/multiplication_lvl_two.html', {
            'multiply_answer':multiply_answer,
            'my_answer': my_answer,
            'mltp_num_1': mltp_num_1,
            'mltp_num_2': mltp_num_2,
            'color' : color,
            } )


    return render(request, 'math/multiplication_lvl_two.html', {
        'mltp_num_1': mltp_num_1,
        'mltp_num_2': mltp_num_2,
    })


################################ MULTIPLICATION LEVEL THREE #############################################
def multiplication_lvl_three(request):
    mltp_num_1 = randint(100,999)
    mltp_num_2 = randint(100,999)

    if request.method == "POST":
        multiply_answer = request.POST['multiplication_answer']
        old_mltp_num_1 = request.POST['old_mltp_num_1']
        old_mltp_num_2 = request.POST['old_mltp_num_2']
        current_user = request.POST['current_user']

        # Error handling if no form fillout
        if not multiply_answer:
            my_answer = "Please provide an answer before submitting."
            color = "primary"

            return render(request, 'math/multiplication_lvl_three.html', {
        'mltp_num_1': mltp_num_1,
        'mltp_num_2': mltp_num_2,
        'my_answer': my_answer,
        'color' : color,
    })

        correct_answer = int(old_mltp_num_1) * int(old_mltp_num_2)

        if int(multiply_answer) == correct_answer:
            my_answer = "Correct!  " + old_mltp_num_1 + " * " + old_mltp_num_2 + " = " +  multiply_answer
            color = "success"

            # increase username multi_count
            update_multi_count = User.objects.get(username = request.session['username'])
            update_multi_count.multi_count += 1
            update_multi_count.save()

        else:
            my_answer = "Incorrect!  " + old_mltp_num_1 + " + " + old_mltp_num_2 + " = "  +  str(correct_answer) + " not " + multiply_answer
            color = "danger"

            # decrease username multi_count
            update_multi_count = User.objects.get(username = request.session['username'])
            update_multi_count.multi_count -= 1
            update_multi_count.save()


        return render(request, 'math/multiplication_lvl_three.html', {
            'multiply_answer':multiply_answer,
            'my_answer': my_answer,
            'mltp_num_1': mltp_num_1,
            'mltp_num_2': mltp_num_2,
            'color' : color,
            } )


    return render(request, 'math/multiplication_lvl_three.html', {
        'mltp_num_1': mltp_num_1,
        'mltp_num_2': mltp_num_2,
    })


################################ MULTIPLICATION LEVEL FOUR #############################################
def multiplication_lvl_four(request):
    mltp_num_1 = randint(1000,9999)
    mltp_num_2 = randint(1000,9999)

    if request.method == "POST":
        multiply_answer = request.POST['multiplication_answer']
        old_mltp_num_1 = request.POST['old_mltp_num_1']
        old_mltp_num_2 = request.POST['old_mltp_num_2']
        current_user = request.POST['current_user']

        # Error handling if no form fillout
        if not multiply_answer:
            my_answer = "Please provide an answer before submitting."
            color = "primary"

            return render(request, 'math/multiplication_lvl_four.html', {
        'mltp_num_1': mltp_num_1,
        'mltp_num_2': mltp_num_2,
        'my_answer': my_answer,
        'color' : color,
    })

        correct_answer = int(old_mltp_num_1) * int(old_mltp_num_2)

        if int(multiply_answer) == correct_answer:
            my_answer = "Correct!  " + old_mltp_num_1 + " * " + old_mltp_num_2 + " = " +  multiply_answer
            color = "success"

            # increase username multi_count
            update_multi_count = User.objects.get(username = request.session['username'])
            update_multi_count.multi_count += 1
            update_multi_count.save()

        else:
            my_answer = "Incorrect!  " + old_mltp_num_1 + " + " + old_mltp_num_2 + " = "  +  str(correct_answer) + " not " + multiply_answer
            color = "danger"

            # decrease username multi_count
            update_multi_count = User.objects.get(username = request.session['username'])
            update_multi_count.multi_count -= 1
            update_multi_count.save()


        return render(request, 'math/multiplication_lvl_four.html', {
            'multiply_answer':multiply_answer,
            'my_answer': my_answer,
            'mltp_num_1': mltp_num_1,
            'mltp_num_2': mltp_num_2,
            'color' : color,
            } )


    return render(request, 'math/multiplication_lvl_four.html', {
        'mltp_num_1': mltp_num_1,
        'mltp_num_2': mltp_num_2,
    })


################################ SUBTRACTION #############################################
def subtraction(request):
    ran_num_1 = randint(0,9)
    ran_num_2 = randint(0,9)
    if ran_num_1 > ran_num_2:
        sub_num_1 = ran_num_1
        sub_num_2 = ran_num_2
    else:
        sub_num_1 = ran_num_2
        sub_num_2 = ran_num_1

    if request.method == "POST":
        sub_answer = request.POST['subtraction_answer']
        old_sub_num_1 = request.POST['old_sub_num_1']
        old_sub_num_2 = request.POST['old_sub_num_2']
        current_user = request.POST['current_user']

        # Error handling if no form fillout
        if not sub_answer:
            my_answer = "Please provide an answer before submitting."
            color = "primary"

            return render(request, 'math/subtraction.html', {
        'sub_num_1': sub_num_1,
        'sub_num_2': sub_num_2,
        'my_answer': my_answer,
        'color' : color,
    })

        correct_answer = int(old_sub_num_1) - int(old_sub_num_2)

        if int(sub_answer) == correct_answer:
            my_answer = "Correct!  " + old_sub_num_1 + " - " + old_sub_num_2 + " = " +  sub_answer
            color = "success"

            # increase username sub_count
            update_sub_count = User.objects.get(username = request.session['username'])
            update_sub_count.sub_count += 1
            update_sub_count.save()

        else:
            my_answer = "Incorrect!  " + old_sub_num_1 + " - " + old_sub_num_2 + " = "  +  str(correct_answer) + " not " + sub_answer
            color = "danger"

            # decrease username sub_count
            update_sub_count = User.objects.get(username = request.session['username'])
            update_sub_count.sub_count -= 1
            update_sub_count.save()

        return render(request, 'math/subtraction.html', {
            'sub_answer': sub_answer,
            'my_answer': my_answer,
            'sub_num_1': sub_num_1,
            'sub_num_2': sub_num_2,
            'color' : color,
            } )

    return render(request, 'math/subtraction.html', {
        'sub_num_1': sub_num_1,
        'sub_num_2': sub_num_2,
    })


################################ SUBTRACTION LEVEL TWO #############################################
def subtraction_lvl_two(request):
    ran_num_1 = randint(10,99)
    ran_num_2 = randint(10,99)
    if ran_num_1 > ran_num_2:
        sub_num_1 = ran_num_1
        sub_num_2 = ran_num_2
    else:
        sub_num_1 = ran_num_2
        sub_num_2 = ran_num_1

    if request.method == "POST":
        sub_answer = request.POST['subtraction_answer']
        old_sub_num_1 = request.POST['old_sub_num_1']
        old_sub_num_2 = request.POST['old_sub_num_2']
        current_user = request.POST['current_user']

        # Error handling if no form fillout
        if not sub_answer:
            my_answer = "Please provide an answer before submitting."
            color = "primary"

            return render(request, 'math/subtraction_lvl_two.html', {
        'sub_num_1': sub_num_1,
        'sub_num_2': sub_num_2,
        'my_answer': my_answer,
        'color' : color,
    })

        correct_answer = int(old_sub_num_1) - int(old_sub_num_2)

        if int(sub_answer) == correct_answer:
            my_answer = "Correct!  " + old_sub_num_1 + " - " + old_sub_num_2 + " = " +  sub_answer
            color = "success"

            # increase username sub_count
            update_sub_count = User.objects.get(username = request.session['username'])
            update_sub_count.sub_count += 1
            update_sub_count.save()

        else:
            my_answer = "Incorrect!  " + old_sub_num_1 + " - " + old_sub_num_2 + " = "  +  str(correct_answer) + " not " + sub_answer
            color = "danger"

            # decrease username sub_count
            update_sub_count = User.objects.get(username = request.session['username'])
            update_sub_count.sub_count -= 1
            update_sub_count.save()

        return render(request, 'math/subtraction_lvl_two.html', {
            'sub_answer': sub_answer,
            'my_answer': my_answer,
            'sub_num_1': sub_num_1,
            'sub_num_2': sub_num_2,
            'color' : color,
            } )

    return render(request, 'math/subtraction_lvl_two.html', {
        'sub_num_1': sub_num_1,
        'sub_num_2': sub_num_2,
    })


################################ SUBTRACTION LEVEL THREE #############################################
def subtraction_lvl_three(request):
    sub_num_1 = randint(100,999)
    sub_num_2 = randint(100,999)

    if request.method == "POST":
        sub_answer = request.POST['subtraction_answer']
        old_sub_num_1 = request.POST['old_sub_num_1']
        old_sub_num_2 = request.POST['old_sub_num_2']
        current_user = request.POST['current_user']

        # Error handling if no form fillout
        if not sub_answer:
            my_answer = "Please provide an answer before submitting."
            color = "primary"

            return render(request, 'math/subtraction_lvl_three.html', {
        'sub_num_1': sub_num_1,
        'sub_num_2': sub_num_2,
        'my_answer': my_answer,
        'color' : color,
    })

        correct_answer = int(old_sub_num_1) - int(old_sub_num_2)

        if int(sub_answer) == correct_answer:
            my_answer = "Correct!  " + old_sub_num_1 + " - " + old_sub_num_2 + " = " +  sub_answer
            color = "success"

            # increase username sub_count
            update_sub_count = User.objects.get(username = request.session['username'])
            update_sub_count.sub_count += 1
            update_sub_count.save()

        else:
            my_answer = "Incorrect!  " + old_sub_num_1 + " - " + old_sub_num_2 + " = "  +  str(correct_answer) + " not " + sub_answer
            color = "danger"

            # decrease username sub_count
            update_sub_count = User.objects.get(username = request.session['username'])
            update_sub_count.sub_count -= 1
            update_sub_count.save()

        return render(request, 'math/subtraction_lvl_three.html', {
            'sub_answer': sub_answer,
            'my_answer': my_answer,
            'sub_num_1': sub_num_1,
            'sub_num_2': sub_num_2,
            'color' : color,
            } )

    return render(request, 'math/subtraction_lvl_three.html', {
        'sub_num_1': sub_num_1,
        'sub_num_2': sub_num_2,
    })


################################ SUBTRACTION LEVEL FOUR #############################################
def subtraction_lvl_four(request):
    sub_num_1 = randint(1000,9999)
    sub_num_2 = randint(1000,9999)

    if request.method == "POST":
        sub_answer = request.POST['subtraction_answer']
        old_sub_num_1 = request.POST['old_sub_num_1']
        old_sub_num_2 = request.POST['old_sub_num_2']
        current_user = request.POST['current_user']

        # Error handling if no form fillout
        if not sub_answer:
            my_answer = "Please provide an answer before submitting."
            color = "primary"

            return render(request, 'math/subtraction_lvl_four.html', {
        'sub_num_1': sub_num_1,
        'sub_num_2': sub_num_2,
        'my_answer': my_answer,
        'color' : color,
    })

        correct_answer = int(old_sub_num_1) - int(old_sub_num_2)

        if int(sub_answer) == correct_answer:
            my_answer = "Correct!  " + old_sub_num_1 + " - " + old_sub_num_2 + " = " +  sub_answer
            color = "success"

            # increase username sub_count
            update_sub_count = User.objects.get(username = request.session['username'])
            update_sub_count.sub_count += 1
            update_sub_count.save()

        else:
            my_answer = "Incorrect!  " + old_sub_num_1 + " - " + old_sub_num_2 + " = "  +  str(correct_answer) + " not " + sub_answer
            color = "danger"

            # decrease username sub_count
            update_sub_count = User.objects.get(username = request.session['username'])
            update_sub_count.sub_count -= 1
            update_sub_count.save()

        return render(request, 'math/subtraction_lvl_four.html', {
            'sub_answer': sub_answer,
            'my_answer': my_answer,
            'sub_num_1': sub_num_1,
            'sub_num_2': sub_num_2,
            'color' : color,
            } )

    return render(request, 'math/subtraction_lvl_four.html', {
        'sub_num_1': sub_num_1,
        'sub_num_2': sub_num_2,
    })


################################ DIVISION #############################################
def division(request):
    ran_num_1 = randint(1,9)
    ran_num_2 = randint(1,9)
    if ran_num_1 > ran_num_2:
        div_num_1 = ran_num_1
        div_num_2 = ran_num_2
    else:
        div_num_1 = ran_num_2
        div_num_2 = ran_num_1

    if request.method == "POST":
        div_answer = request.POST['division_answer']
        old_div_num_1 = request.POST['old_div_num_1']
        old_div_num_2 = request.POST['old_div_num_2']
        current_user = request.POST['current_user']

        # Error handling if no form fillout
        if not div_answer:
            my_answer = "Please provide an answer before submitting."
            color = "primary"

            return render(request, 'math/division.html', {
        'div_num_1': div_num_1,
        'div_num_2': div_num_2,
        'my_answer': my_answer,
        'color' : color,
    })
        # divide the numbers to get the answer
        answer = int(old_div_num_1) / int(old_div_num_2)
        #then rouned the answer to 2 decimal places.
        correct_answer = round(answer, 2)

        if float(div_answer) == correct_answer:
            my_answer = "Correct!  " + old_div_num_1 + " / " + old_div_num_2 + " = " +  div_answer
            color = "success"

            # increase username div_count
            update_div_count = User.objects.get(username = request.session['username'])
            update_div_count.div_count += 1
            update_div_count.save()

        else:
            my_answer = "Incorrect!  " + old_div_num_1 + " / " + old_div_num_2 + " = "  +  str(correct_answer) + " not " + div_answer
            color = "danger"

            # decrease username div_count
            update_div_count = User.objects.get(username = request.session['username'])
            update_div_count.div_count -= 1
            update_div_count.save()

        return render(request, 'math/division.html', {
            'div_answer': div_answer,
            'my_answer': my_answer,
            'div_num_1': div_num_1,
            'div_num_2': div_num_2,
            'color' : color,
            } )

    return render(request, 'math/division.html', {
        'div_num_1': div_num_1,
        'div_num_2': div_num_2,
    })


################################ DIVISION LEVEL TWO #############################################
def division_lvl_two(request):
    ran_num_1 = randint(10,99)
    ran_num_2 = randint(10,99)
    if ran_num_1 > ran_num_2:
        div_num_1 = ran_num_1
        div_num_2 = ran_num_2
    else:
        div_num_1 = ran_num_2
        div_num_2 = ran_num_1

    if request.method == "POST":
        div_answer = request.POST['division_answer']
        old_div_num_1 = request.POST['old_div_num_1']
        old_div_num_2 = request.POST['old_div_num_2']
        current_user = request.POST['current_user']

        # Error handling if no form fillout
        if not div_answer:
            my_answer = "Please provide an answer before submitting."
            color = "primary"

            return render(request, 'math/division_lvl_two.html', {
        'div_num_1': div_num_1,
        'div_num_2': div_num_2,
        'my_answer': my_answer,
        'color' : color,
    })
        # divide the numbers to get the answer
        answer = int(old_div_num_1) / int(old_div_num_2)
        #then rouned the answer to 2 decimal places.
        correct_answer = round(answer, 2)

        if float(div_answer) == correct_answer:
            my_answer = "Correct!  " + old_div_num_1 + " / " + old_div_num_2 + " = " +  div_answer
            color = "success"

            # increase username div_count
            update_div_count = User.objects.get(username = request.session['username'])
            update_div_count.div_count += 1
            update_div_count.save()

        else:
            my_answer = "Incorrect!  " + old_div_num_1 + " / " + old_div_num_2 + " = "  +  str(correct_answer) + " not " + div_answer
            color = "danger"

            # decrease username div_count
            update_div_count = User.objects.get(username = request.session['username'])
            update_div_count.div_count -= 1
            update_div_count.save()

        return render(request, 'math/division_lvl_two.html', {
            'div_answer': div_answer,
            'my_answer': my_answer,
            'div_num_1': div_num_1,
            'div_num_2': div_num_2,
            'color' : color,
            } )

    return render(request, 'math/division_lvl_two.html', {
        'div_num_1': div_num_1,
        'div_num_2': div_num_2,
    })


################################ DIVISION LEVEL THREE #############################################
def division_lvl_three(request):
    ran_num_1 = randint(100,999)
    ran_num_2 = randint(100,999)
    if ran_num_1 > ran_num_2:
        div_num_1 = ran_num_1
        div_num_2 = ran_num_2
    else:
        div_num_1 = ran_num_2
        div_num_2 = ran_num_1

    if request.method == "POST":
        div_answer = request.POST['division_answer']
        old_div_num_1 = request.POST['old_div_num_1']
        old_div_num_2 = request.POST['old_div_num_2']
        current_user = request.POST['current_user']

        # Error handling if no form fillout
        if not div_answer:
            my_answer = "Please provide an answer before submitting."
            color = "primary"

            return render(request, 'math/division_lvl_three.html', {
        'div_num_1': div_num_1,
        'div_num_2': div_num_2,
        'my_answer': my_answer,
        'color' : color,
    })
        # divide the numbers to get the answer
        answer = int(old_div_num_1) / int(old_div_num_2)
        #then rouned the answer to 2 decimal places.
        correct_answer = round(answer, 2)

        if float(div_answer) == correct_answer:
            my_answer = "Correct!  " + old_div_num_1 + " / " + old_div_num_2 + " = " +  div_answer
            color = "success"

            # increase username div_count
            update_div_count = User.objects.get(username = request.session['username'])
            update_div_count.div_count += 1
            update_div_count.save()

        else:
            my_answer = "Incorrect!  " + old_div_num_1 + " / " + old_div_num_2 + " = "  +  str(correct_answer) + " not " + div_answer
            color = "danger"

            # decrease username div_count
            update_div_count = User.objects.get(username = request.session['username'])
            update_div_count.div_count -= 1
            update_div_count.save()

        return render(request, 'math/division_lvl_three.html', {
            'div_answer': div_answer,
            'my_answer': my_answer,
            'div_num_1': div_num_1,
            'div_num_2': div_num_2,
            'color' : color,
            } )

    return render(request, 'math/division_lvl_three.html', {
        'div_num_1': div_num_1,
        'div_num_2': div_num_2,
    })


################################ DIVISION LEVEL FOUR #############################################
def division_lvl_four(request):
    ran_num_1 = randint(1000,9999)
    ran_num_2 = randint(1000,9999)
    if ran_num_1 > ran_num_2:
        div_num_1 = ran_num_1
        div_num_2 = ran_num_2
    else:
        div_num_1 = ran_num_2
        div_num_2 = ran_num_1

    if request.method == "POST":
        div_answer = request.POST['division_answer']
        old_div_num_1 = request.POST['old_div_num_1']
        old_div_num_2 = request.POST['old_div_num_2']
        current_user = request.POST['current_user']

        # Error handling if no form fillout
        if not div_answer:
            my_answer = "Please provide an answer before submitting."
            color = "primary"

            return render(request, 'math/division_lvl_four.html', {
        'div_num_1': div_num_1,
        'div_num_2': div_num_2,
        'my_answer': my_answer,
        'color' : color,
    })
        # divide the numbers to get the answer
        answer = int(old_div_num_1) / int(old_div_num_2)
        #then rouned the answer to 2 decimal places.
        correct_answer = round(answer, 2)

        if float(div_answer) == correct_answer:
            my_answer = "Correct!  " + old_div_num_1 + " / " + old_div_num_2 + " = " +  div_answer
            color = "success"

            # increase username div_count
            update_div_count = User.objects.get(username = request.session['username'])
            update_div_count.div_count += 1
            update_div_count.save()

        else:
            my_answer = "Incorrect!  " + old_div_num_1 + " / " + old_div_num_2 + " = "  +  str(correct_answer) + " not " + div_answer
            color = "danger"

            # decrease username div_count
            update_div_count = User.objects.get(username = request.session['username'])
            update_div_count.div_count -= 1
            update_div_count.save()

        return render(request, 'math/division_lvl_four.html', {
            'div_answer': div_answer,
            'my_answer': my_answer,
            'div_num_1': div_num_1,
            'div_num_2': div_num_2,
            'color' : color,
            } )

    return render(request, 'math/division_lvl_four.html', {
        'div_num_1': div_num_1,
        'div_num_2': div_num_2,
    })

################################ LOG OUT #############################################
def logout(request):
    request.session.flush()
    return redirect('/')