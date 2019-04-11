import random

def who_are_you():
    messages = ['I am Charlie, your lovely personal assistant.',
                 'Charlie, didnt I tell you before?',
                'You ask that so many times! I am Charlie']
    return random.choice(messages)


def toss_coin():
    outcomes = ['heads', 'tails']
    return('I just flipped a coin. It shows ' + random.choice(outcomes))


def how_am_i():
    replies = [
        'You are coolest gangsta!',
        'You  look like a pirate.',
        'You are sexy!',
        'You look like the kindest person that I have met.']
    return random.choice(replies)


def who_am_i(name):
    return ('You are ' + name)


def where_born():
    return 'I was created in the middle of a storm. Nobody can drag me down!'


def how_are_you():
    return 'I am fine, thank you.'


def are_you_up():
    return 'Charlie Reporting!'


def love_you():
    replies = [
               'I love you too.',
               'You are looking for love in the wrong place.'
              ]
    return random.choice(replies)

def bye():
    replies = ['bye sir!','Charlie signing out', 'bye bye tata ']
    return random.choice(replies)


#def undefined():
    #return 'Can you repeat again!'
