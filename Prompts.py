import random


#Can probobly make a fucntion for indexing values


def Adjective():
    adjectivlist = ['aggressive', 'obnoxious', 'Down to Earth', 'Humble', 'uptight', 'creepy', 'Sad', 'Concerned']
    rng_list_index = random.randint(0,(len(adjectivlist)-1))
    return adjectivlist[rng_list_index]
    

def Actors():
    actorlist = [ 'The Rock', 'Leonardo DiCaprio', 'Jennifer Lawrence', 'Scarlett Johansson', 'LeBron James', 'Tom Brady', 'Kylie Jenner', 'Drake', 'Barrack Obama', 'Bill Gates', 'Eminem', 'Juice Wrld', ]   #Look in to libraries that have Celebrity  
    rng_list_index = random.randint(0, (len(actorlist)-1))
    return actorlist[rng_list_index]



# Most likely scrap and redo with OOP.





def prompt(actor, adjective):
    return (f'Write me a story from the perspective of a ask reddit user answering a prompt about meeting a celebirty, suggesting {actor} was {adjective}, about a noun that makes sense given the context.')

