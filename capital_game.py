import random

# a mini array of state dictionaries
# states = [
# {
#     "name": "Arkansas",
#     "capital": "Little Rock"
# }, {
#     "name": "California",
#     "capital": "Sacramento"
# }, {
#     "name": "Colorado",
#     "capital": "Denver"
# }, {
#     "name": "Hawaii",
#     "capital": "Honolulu"
# }, {
#     "name": "Kansas",
#     "capital": "Topeka"
# }, {
#     "name": "Wyoming",
#     "capital": "Cheyenne"
# }]

from capitals import states

def ready(opt_one, opt_two):
    """Ask player if they are ready to play"""
    print('Are you ready to guess some capitals? ', opt_one + ' or ' + opt_two)
    ready_to_play = input()
    if ready_to_play == opt_one:
        print('lets go')
    else:
        print('why not')
        ready(opt_one,opt_two)

def print_list(list):
    """Print all the states"""
    for i in range(0, len(list)):
        print(list[i])

def add_key_value_pairs(list):
    for i in range(0, len(list)):
        list[i].update({'correct' : 0})
        list[i].update({'incorrect' : 0})

def ask_for_cap(obj, key, key_2, key_3, key_4):
    print('Whats the capital of: ', obj[key])
    guess = input()
    if guess == obj[key_2]:
        obj[key_3] += 1
        print('You are correct, Sir!')
    else:
        obj[key_4] += 1
        print('Not even close, try again.')
        ask_for_cap(obj, key, key_2, key_3, key_4)



ready('yes', 'no')
random.shuffle(states)
add_key_value_pairs(states)
for i in range(0, len(states)):
    ask_for_cap(states[i], 'name', 'capital', 'correct', 'incorrect')
    

score = 0
for i in range(0, len(states)):
    score += states[i]['correct']
    score -= states[i]['incorrect']

print('Final Score: ', score)

    


