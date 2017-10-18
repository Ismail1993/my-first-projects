from sys import exit
from random import randint

class Scene(object):

    def enter(self):
      print "This scene is not yet configured. Subclass it and implement enter()."
      exit(1)

class Engine(object):

# initialise new object, 'self'.
  def __init__(self,scene_map):
    self.scene_map = scene_map

  def play(self):
# Gets the first scene, Central Corridor. Current_scene becomes object from the 'Scene' class.
    current_scene = self.scene_map.opening_scene()
# Gets the next scene(s)
    while True:
        if current_scene != None:
            print "\n"
            print "-" * 20
# Launch the scene and then store the string of the next scene to be played.
            next_scene_name = current_scene.enter()
# Get the next scene and store it into current_scene.
            current_scene = self.scene_map.next_scene(next_scene_name)
        else:
            break




class Death(Scene):

    quips = ["Your death brings shame to all of humanity.",
            "Gothons target and strike the planet below, which happens to be Earth.",
            "Your mission failed"]



    def enter(self):
        print Death.quips[randint(0, len(self.quips) - 1)]
        exit(1)



class CentralCorridor(Scene):

  def enter(self):
    print "Welcome Hero!"
    print "-" * 20
    print "You walk along the central corridor heading toward the weapon armory room."
    print 'This is where you are and has a Gothon already standing'
    print "there."
    print '-' * 20
    print "do you fight the Gothon head on? \n"


    while True:
        print "(Y for Yes and N for No.)"
        reply = raw_input("> ")
        if reply == 'Y':
            print 'You confront the Gothon by moving closer.'
            print 'Gothon looks at you menacingly and grabs for the gun.'
            print '\tGothon strikes and hits you on the chest.'
            return 'Death'
        elif reply == 'N':
            print 'You avoid the situation and flee to the nearest room.'
            return 'Escapepod'
        else:
            print 'what do you mean?'

class Escapepod(Scene):

    def enter(self):
        print "You find three pods to escape into and they seem to be colour"
        print "coded"
        print "You see green, blue and purple."
        print "Which one do you escape into?\n"

        reply = raw_input(">")

        if reply == "blue" or reply == "Blue":
            print "You decide to escape into the blue one."
            print "There is a button on the entry door that you think reads,"
            print "\'Gjsjsffns sshskdsidks\'"
            print "This is Gothon script, which puzzles you. In the midst"
            print "of all the confusion you hear lots of Gothons trampling nearby"
            print "like a pack of wild buffaloes."
            print "You hesitate..."
            print "press the button and sound the alarm."
            print "its soundless..\n"
            print "\t3 Gothons appear and pull their guns out."
            return 'Death'
        elif reply == "green" or reply == "Green":
            print "You decide to escape into the green one."
            print "There is a button on the entry door that you think reads,"
            print "\'Odfdjsj ss fjsi sfjsfusu ss ifis ss.\'"
            print "This is Gothon script, which puzzles you. In the midst"
            print "of all the confusion you hear lots of Gothons trampling nearby"
            print "like a pack of wild buffaloes."
            print "You hesitate..."
            print "press the button and..\n"
            print "nothing happens."
            print "The sounds from the Gothon hyperactivity remains the same.."
            print "You see what looks like a screen."
            print "You press on it..\n"
            print "nothing happens."
            print "You then try speaking into it."
            print "nothing happens."
            print "You hear a Gothon appear, he must've overheard you speaking."
            print "What do you do?\n"

            reply_2 = raw_input("> ")
            taunt = False
            while True:
# Begin taunting the Gothon.
                if reply_2 == "taunt gothon" and taunt == False:
                    print "You taunt it.\n"
                    print "He gets very annoyed.."
                    taunt = True
# Type in the next move.
                    reply_2 = raw_input("> ")
# Taunt him again.
                elif reply_2 == "taunt gothon" and taunt == True:
                    print "You taunt him again."
                    print "You've really annoyed him now..\n"
                    print "He shouts and screams \'shdshdsk hfhsfjssfh!\'"
                    print "The green escape pod opens!"
                    print "\tYou pull your gun out and shoot at the Gothon and"
                    print "\tkill him. You manage to escape before more Gothons arrive.."
                    return 'Finished'
# Shoot the Gothon.
                elif reply_2 == "draw gun" or reply_2 == "shoot him":
                    print "The Gothon notices your move.."
                    print "He manages to draw his first and shoot you the head.."
                    print "The Gothon repeatedly shoots your face and then eats you up.."
                    return 'Death'
# Taunt him and then do something else.
                elif reply_2 != "taunt gothon" and taunt == True:
                    print "The Gothon is still mad crazy... are you sure?"
                    print "Well here goes nothing.\n"
                    print "\tYou fail miserably........"
                    print "\tMore Gothons arrive on the scene and you quickly become outnumbered."
                    return 'Death'
                else:
                    print "what do you mean?\n"
                    print "Hint: taunt gothon or shoot him/draw gun"
                    reply_2 = raw_input("> ")

        elif reply == 'purple' or 'Purple':
            print "You decide to escape into the purple one."
            print "There is a button on the entry door that you think reads,"
            print "\'opsdjfjs sifj isd.\'"
            print "This is Gothon script, which puzzles you. In the midst"
            print "of all the confusion you hear lots of Gothons trampling nearby"
            print "like a pack of wild buffaloes."
            print "You hesitate..."
            print "press the button and..\n"
            print "Door opens and you go in.."
            print "Door shuts itself and a bomb begins to detonate."

            for i in range (1,11):
                print "\n"
                print str(i) + "!"

            print "BOOOOOOM!\n"
            print "\tThe whole ship explodes."
            return 'Death'


class Finished(Scene):

    def enter(self):
        print "You managed to escape! You breathe a huge sigh of relief..."
        print "-" * 20
        print "CONGRATULATIONS.. THE END!"
        exit(1)

class Map(object):
# Store all the scenes into a dictionary.
  scenes = {'central_corridor':CentralCorridor(), 'Death':Death(),
  'Escapepod':Escapepod(), 'Finished':Finished()
  }

  def __init__(self, start_scene):
    self.start_scene = start_scene
# Function for grabbing a scene from the dictionary, returns a scene.
  def next_scene(self, scene_name):
    return Map.scenes.get(scene_name)
# Start at a scene and call next_scene to grab it.
  def opening_scene(self):
    return self.next_scene(self.start_scene)

# Set a_map to an object belonging to Map, carrying parameters (self & central_corridor)
a_map = Map('central_corridor')
# Set a_game to an object belonging to Engine, carrying parameters (self, a_map)
a_game = Engine(a_map)
a_game.play()
