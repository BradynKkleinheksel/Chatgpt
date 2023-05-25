import random





#def adjective():


def actorslistandindex():
    actorlist = [ 'The Rock', 'Leonardo DiCaprio', 'Jennifer Lawrence', 'Scarlett Johansson', 'LeBron James', 'Tom Brady', 'Kylie Jenner', 'Drake', 'Barrack Obama', 'Bill Gates', 'Eminem', 'Juice Wrld', ]
    rng_list_index = random.randint(range(len(actorlist)))
    returnactor(actorlist, rng_list_index)


def returnactor(actorlist, rng_list_index):
    i = rng_list_index
    for i in range(len(actorlist)):
        userprompt(i)

def callfunction(actor, adjective):
    if actor and adjective:
        userprompt()

def userprompt(actor, adjective):
    print(f'Write me a story from the perspective of a ask reddit user answering a prompt about meeting a celebirty, suggesting {actor} was {adjective}.')


