from django.shortcuts import render, HttpResponse

import random

max_guesses = 5

def index(request):
    secret_number = random.randint(1, 100)
    print(secret_number)
    request.session['secret_number'] = secret_number
    request.session['number_of_guesses'] = 0
    request.session['guesses'] = [] 
    request.session['guess'] = 0
    context = {
                "guesses_remaining": max_guesses
    }
    return render(request, 'index.html', context)

def game(request):
    return render(request, 'index.html')

def check_guess(request):
    guess = int(request.POST['guess'])
    number_of_guesses = request.session.get('number_of_guesses')
    secret_number = request.session.get('secret_number')
    guesses = request.session.get('guesses')
    guesses.append(guess)
    guess_list = ', '.join(map(str, guesses))
    while number_of_guesses < max_guesses-1:
        number_of_guesses += 1
        if guess < secret_number:
            request.session['number_of_guesses'] = number_of_guesses
            context = {
                "response": "Too Low!",
                "guesses_remaining": max_guesses-number_of_guesses,
                "correct": False,
                "color": "red",
                "guesses": guess_list
            }
            return render(request, 'index.html', context)
        elif guess > secret_number:
            request.session['number_of_guesses'] = number_of_guesses
            context = {
                "response": "Too High!",
                "guesses_remaining": max_guesses-number_of_guesses,
                "correct": False,
                "color": "red",
                "guesses": guess_list
            }
            return render(request, 'index.html', context)
        elif guess == secret_number:
            context = {
                "response": f"CORRECT!! {secret_number} was the number!",
                "guesses_remaining": max_guesses-number_of_guesses,
                "correct": True,
                "color": "green",
                "guesses": guess_list
            }
            return render(request, 'index.html', context)
    number_of_guesses +=1
    context = {
        "response": f"Sorry, {secret_number} was the right answer!",
        "guesses_remaining": max_guesses-number_of_guesses,
        "correct": False,
        "color": "red",
        "guesses": guess_list
    }
    return render(request, 'index.html', context)
