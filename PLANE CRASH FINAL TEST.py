import time
import sys


def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)


###### EVERYTHING ABOVE MAKE THE TXT APEAR ONE CHARACTER AT THE TIME ######
###########################################################################

#################################################################################################
############################ CAVE TO - JEFF BEZOS PATH BELOW  !!!!! #############################
#################################################################################################


def game():
    def start_game():
        print("""
        ██████  ██       █████  ███    ██ ███████     
        ██   ██ ██      ██   ██ ████   ██ ██          
        ██████  ██      ███████ ██ ██  ██ █████       
        ██      ██      ██   ██ ██  ██ ██ ██          
        ██      ███████ ██   ██ ██   ████ ███████     
                                                    
                                                    
        ██████   ██████    █████   ███████ ██   ██       
        ██       ██   ██  ██   ██  ██      ██   ██       
        ██       ██████   ███████  ███████ ███████       
        ██       ██   ██  ██   ██       ██ ██   ██       
        ██████   ██   ██  ██   ██  ███████ ██   ██  
                """)
        answer=input("Would you like to play the game? (Y)es \ (N)o :  ").lower()
        if answer == "yes".lower().strip() or answer == "y".lower().strip():
            print("Ok lets play")
            character_set()
        elif answer=="no".lower() or answer== "n".lower():
            print("Ok! see you next time !")
            exit()
        else:
            print("I didn't understand that, please try again.")
            start_game()
    

    def character_set():
        global sex_1
        global name
        sex_1 = 0
        name =(input("What is your name ? "))
        sex = (input(f"Ok {name} are you 'male' or 'female' ? ")).lower().strip()
        
        if sex == "female":
            sex_1 += 1   
        elif sex == "male":
            sex_1 += 2
        else:
            print("Didn't got that, please try again!")
            character_set()
            
        intro()
            
    def intro():
        print()
        print()
        delay_print("""
        After five months of constantly working, you finally get some days off you. You decide that you're going on a long awaited holiday...
        While on the plane flying to your destination, a fire starts in one of the plane engines ... 
        Your plane start to fall, people start to panic, someone opens the evacuation door 
        and immediately got pulled outside by the air pressure... 
        Everything starts to fly around and you get hit by someones luggage!!
        Your vision blurs and sounds gradually become distant... 
        You wake up and realise that the plane crashed at the base of a huge cliff partly covered by dense jungle,
        It seems that someone else survived but thought that you were dead! so they left you behind with the dead bodies 
        You see a suitcase with your name on it... 
        You come closer, open it and pick some sandwiches that you packed before you left
        After you had eaten, you calm down and realize that if you want to survive you have to move on 

        """)
        print()
        arive_island()

    def arive_island():

        answer_1 = input("You can try to climb down the 'CLIFF' or go into the 'JUNGLE', what you want to do ? ").lower().strip()
        if answer_1 == "cliff":
            print()
            delay_print("""
            Climbing down one of the stones that you step on slipped...
            You tried your best to reach another one but you lose your balance and fall 
                       
            """)
            game_over()


        elif answer_1 == "jungle":
            delay_print("""
            You make your way through overgrown jungles
            Suddenly you come across an old rope bridge
            """)
            print()
            jungle()
        else:
            print("Please enter your choice again")
            arive_island()

##############################################################################################################
#### BELOW PATH SPLITS IN HERE IN TO (JEFF BEZOS/SEA_BOAT) - "BRIDGE"| AND HANGAR_AIRCRAFT - "CONTINUE" ###### 
##############################################################################################################


    def jungle():

            answer_2 =input("Do you want to risk it and try to go across 'BRIDGE' or do you 'CONTINUE' walking through the jungle ? ").lower().strip()
            if answer_2 == "bridge":
                    bridge()
            elif answer_2 == "continue":
                    print("Nice")
                    savvanah()
            else:
                print("Please enter your choice again")
                jungle()

##############################################################################################################    
####################### PATH SPLITS IN HERE IN TO JEFF BEZOS/ SEA_BOAT/ HANGAR_AIRCRAFT ###################### 
##############################################################################################################
################################### CAVE TO - JEFF BEZOS PATH BELOW !!!!! ####################################
##############################################################################################################

    def bridge():

        delay_print("""
            The bridge was making strange noises but you made it..
            You walk the path that was on the other side of the bridge
            The road splits, and you see that path ahead is used more often and leads to a 'CAVE'
            While the path to the right seems to lead to huge 'THICKETS'
        """)

        print()
        answer_3 = input("What do you do? Do you go to 'CAVE' or you chose path that lead to 'THICKETS'? ").lower().strip()
        if answer_3 == "cave":
            cave()
        elif answer_3 =="thickets":
            swamp()
        else:
            print("Please enter your choice again")
            bridge() 
            
    def cave():
        
        print()
        delay_print("""
            You slowly approach the cave...
            When you start to get closer, you notice a strange smell in the air.
            You enter the cave. Suddenly you hear a dreadful sound behind you,
            You turn around and there is a huge brown bear that runs at you !!
        """)
        print()

        answer_4 = input("What are you doing, run 'DEEPER' into cave or try to run 'OUTSIDE'? ").lower().strip()

        if answer_4 == "deeper":
            print()
            delay_print("""
            In the depths of the cave you found a little gap that bear could not reach
            The bear finally gives up, but you terrified and dont want to leave a gap
            After a long time you fall asleep from exhaustion....
            ...ZzzzZzzzzZZZzzzzzzZZzzzzZZZZzzzzzZZzzzz...
            ...zzzZZZZzzzZZzzzzzZZZzzZZZzzzzzZZZZZzZ..
            """)
            
            underground_lake()

        elif answer_4 == "outside":
            
            print()
            print()
            delay_print("""
            You try to run out of the cave, but a massive ferocious brown bear blocked your way!
            It knocks you to the ground with a mighty blow of the paw and begins to devour you!!

            """)
            game_over()
            


        else:
            print("Please enter your choice again")
            cave()            

    def underground_lake():

        delay_print("""
            You wake up, and remind your self of the horror of last night
            You start to look around for way out and realise that theres path leading even deeper in to the cave
            You go inside and find that theres an underground lake inside the second cave
            A faint light seems to be coming out of the water...
        """)
        print()

        answer_5 = input("What do you do?, try to 'DIVE' and see where light come from or go 'BACK'? ").lower().strip()
        if answer_5 == "back":
            print()
            print()
            delay_print("""
            You make your way back to the first cave
            You slipped through the gap that last night saved you life
            And keep going towards the exit
            Just before you reach the exit you run into the same massive brown bear, this time with two cubs
            The mama bear immediately jumps on you and starts to tear you apart!!

            """)
            print()
            game_over()


        elif answer_5 == "dive":
            print()
            delay_print("""
            You decide to go into water, and realise that its really cold
            You dive and try to find out where the light coming from
            You find a little gap in corner under water
            By the time you get to it you start run out of air
            You swim directly above the gap and tried again
            This time you made it! You follow the light and you rise from under a waterfall..
            You left the water frozen but happy to be alive !!
            """)

            abandoned_camp()
        else:
            print("Please enter your choice again")
            underground_lake()


    def abandoned_camp():
        
        delay_print("""
            You came across an abandoned camp.
            There is a fire thats still seems to be warm.
            If you would find dry wood you may be able to spark fire

            """)
        answer_9 = input("""Do you want to look for 'WOOD' to start fire or 'MOVE' on ? """).lower().strip()
        
        if answer_9 == "wood":
            delay_print("""
            You find some dry wood and was able to spark a fire with it.
            While you was looking for wood you found a rabbit hole.
            You wait outside to see is there any rabbits inside. 
            Luckily to you! your and ambush seems to work, you got one rabbit.
            You came back to campfire, you dried your self and baked a rabbit.
            You are no longer hungry and freezing so you decide to move on.
            """)
            jeff_bezos()
            
        elif answer_9 == "move":
            delay_print("""
            After spending all night in cave and diving in freezing mountain water you freezing...
            Lack of energy caused by not having any meal for long time dont help either...
            But you still decide to continue walking through the jungle...
            As darkness falls it begins to get really cold...
            You feel sleepy... and pass out.....
            You died of hypothermia...
            """)
            game_over()
        else:
            print("Please enter your choice again")
            abandoned_camp()          
    
    def jeff_bezos():
        global sex_1
        global name
        delay_print(f"""
            You keep walking through the jungle
            You came across a huge villa in the middle of the jungle
            You though it strange
            Someone walks towards you before you can hide, as he get close you realised that its Jeff Bezos.
            he welcome you saying 'Hello {name}!', you thought it a bit strange he knows your name but 
            you are very hungry and he invites you for dinner....
        """)
        if sex_1 == 1: 
            delay_print("""
            Dinner went really nice, he was surprised with your story and enchanted by your grace.
            After the dinner both of you went to bedroom.
            Nine months later you gave birth to his first child.
            He arranges your marriage on the island and live together long and happy!!!!

            """)
            print("""
                      ██    ██  ██████  ██    ██     ██     ██  ██████  ███    ██ 
                       ██  ██  ██    ██ ██    ██     ██     ██ ██    ██ ████   ██ 
                        ████   ██    ██ ██    ██     ██  █  ██ ██    ██ ██ ██  ██ 
                         ██    ██    ██ ██    ██     ██ ███ ██ ██    ██ ██  ██ ██ 
                         ██     ██████   ██████       ███ ███   ██████  ██   ████ 
            """)
            print("""
                                                mMm  _[_]_
                                               /(")\  (")
                                              //)^(\)//:]]
                                             /(/&@&\)/|~|/
                                            / /-~`~-\ |||
                                            `/       \|||
                                            `----------'--
            """)
            print("""
            
            """)

        elif sex_1 == 2:
            delay_print("""
            After the dinner Jeff invites you to his "man cave"
            Both of you climb into a big hospital elevator.
            As the doors open a room full of cameras appears.
            You remind your self that he already knew your name when you meet.
            You want to ask questions but at that moment, the door to the elevator opens behind you 
            And couple of well build guys step out and grab you.
            They pull you into a room built of glass with a bed with straps in the middle.
            They put you down to the bed and a person who looks like a doctor comes and injects you with something
            Jeff comes next to you and explain that for the good of mankind he need to test hes new vaccine on you
            and that one day you will be a remembered as hero!
            The blood in your veins start to BURN, screaming in agony you lose you consciousness!!!.
            """)

            game_over()

#################################################################################################
############################# CAVE TO - JEFF BEZOS PATH ABOVE !!!!! #############################
#################################################################################################



#################################################################################################
################## THICKETS/SWAMP (CODE LINE 148) TO - BOAT AND SEA PATH BELOW !!!!! ############
#################################################################################################


    def swamp():

        print()
        delay_print("""
            After a dozen or so minutes of tearing through the thickets you reach something that looks like swamp
            The swamp doesn't seem too deep as trees grow all over the place..
            But you cant see what underneath the surface...
            You see that you could try to cross over the swampy terrain by climbing dense trees
            But the noise above your head indicates that there has to be some kinds of insect living in those trees 
            You might as well try to walk through the swamp.

        """)
        print()
        print()
        answer_6= input("What do you do? Try to cross it by 'TREES' or 'WALK'? ").lower().strip()
        
        if answer_6 == "walk":
            print()
            delay_print("""
            You slowly make your way through the swamp
            You start to see familiar thickets on the other side
            You see that something moving beneath the surface around those thickets
            Suddenly you realise that huge anaconda is approaching your way
            You try to run back but anaconda seems to be much faster in water
            Half way back the wild animal has caught you...
            It covers your body and starts to grind you bones!!!!
            Before you know its already start to swallow you!!!

            """)
            game_over()

            
        elif answer_6 == "trees":
            print()
            delay_print("""
            While climbing a tree you  were stung by a next of murder hornets
            Sore and tired, you managed to get to the other side by walking old branches.
            """)
            print()
            trees()
        else:
            print("Please enter your choice again")
            swamp()


    def trees():
        global sex_1
        delay_print("""
            As you manage to get through the thickets on the other side you leave the swamp behind you
            Hungry, sore and tired you see that there is a small village not far from you,
            From a distance its looks like someone is living in the village,
            In the other direction you see seagulls flying in the distance
            """)
        print()
        answer_sea=input("Do you want to go to 'VILLAGE' or follow the sea 'SEAGULLS'? ").lower().strip()
        
        if answer_sea=="seagulls": 
            delay_print("""
            You follow the sea gulls for about an hour, finally the sea appears on horizon
            From a distance you can see that there is something on beach
            You keep walking toward the strange shape you have seen from far away
            Once you get closer you realised its a boat full of food and water.
            You take the boat and cheer, now you can escape the island!!

            """)
            print("""
                      ██    ██  ██████  ██    ██     ██     ██  ██████  ███    ██ 
                       ██  ██  ██    ██ ██    ██     ██     ██ ██    ██ ████   ██ 
                        ████   ██    ██ ██    ██     ██  █  ██ ██    ██ ██ ██  ██ 
                         ██    ██    ██ ██    ██     ██ ███ ██ ██    ██ ██  ██ ██ 
                         ██     ██████   ██████       ███ ███   ██████  ██   ████ 
            """)
            print("""
                                                  ~;
                                                 ,/|\,
                                               ,/' |\ \,
                                             ,/'   | |  ]
                                           ,/'     | |   |
                                         ,/'       |/    |
                                       ,/__________|-----' ,
                                      ___.....-----''-----/
                                      \                  /
                ~~-~^~^~`~^~`~^^~^~-^~^~^~-~^~^~~-~^~^~`~^~`~^^~^~-^~^~^~-~^~^~^^~^~-^
                    ~-^~^-`~^~-^~^`^~^-^~^`^~^-~^~-^~^-`~^~-^~^`^~^-^~^`^~^-~^~-^~^-`~^~-^
                ~^-`~^~-^~^`^~^-^~^`^~^-~^`^~^-^~^`^~^-~^~^`^~^-~^~-^~^-`~^~-^~^`^~^-^~^`^~^`^~
                """)

        elif answer_sea=="village":
            delay_print("""
            You go to the village cautiously, people who live there seems to be a natives
            Everyone looks at you strange and then start to encircle you
            Suddenly from one of the tents came out a man with a lion skin on him
            He invites you to his tent for a meal, it seems a bit suspicious but you are so hungry! you eat whats on offer.
            Slowly your vision starts to go blurry.
            Loud noises wake you up, you realise that you are tied to a pole in the centre of firepit
            The same man with the lion skin sets the fire 
            You spend your last minutes in agony while a tribe of cannibals shouts and dance around you.
            """)
            game_over()
        else:
            print("Please enter your choice again")
            trees()


#################################################################################################
############################ THICKETS TO - BOAT AND SEA ABOVE !!!!! #############################
#################################################################################################



#################################################################################################
################# "CONTINUE" IN JUNGLE (CODE LINE 119) TO - BOAT AND SEA BELOW !!!!! ############
#################################################################################################



    def savvanah():
        delay_print("""
            You keep walking through the jungle and as you break through the dense bushes,
            A huge desert appears in front of your eyes
            Its empty flat terrain and you can see a pack of lions resting not far away in front of you
            You hide back into the bushes and start to observe them and try to figure out what to do
        """)
        print()
        savvanah_answer = input("Do you want to 'WAIT' in bushes or you want try to 'SNEAK' past them ? ").lower().strip()

        if savvanah_answer=="wait":
            delay_print("""
            You feel like trying to pass a pride of lions would be too risky so you stay in the bushes and wait
            After few hours you realise that pride have all fallen asleep 
            You crawl out of bushes and sneak past them without them noticing you... 
            """)
            oasis()

        elif savvanah_answer=="sneak":
            delay_print("""
            You keep yourself low and start to walk slowly around the lions
            Every so often you look above grass to see that none of the lions follow you
            Suddenly a strong wind begins to blow blasting away the grass that you are using for cover
            One of the lions noticed you. Whats even worse is that the wind blows towards the pride, 
            and now the rest of the lions can smell your scent.
            The lions begin to hunt, you try to run but it didn't take long for them to get to their victim 
            """)
            game_over()

        else:
            print("Please enter your choice again")
            savvanah()


    def oasis():
        global sex_1
        delay_print("""
            The sun is hot you been keep walking for several hours and got really firstly luckily 
            suddenly you see an "OASIS" on left side of horizon
            at same time small "HANGAR" appears on right side of horizon
            """)
        print()

        oasis_answer = input("Do you want to go to 'OASIS' or check 'HANGAR' ? ").lower().strip()

        if oasis_answer=="oasis":
            delay_print("""
            You keep walking for several hours, but you cant seem to get to the oasis
            You finally realised that its you mind that playing tricks with you 
            and theres no Oasis at all. It was just a mirage!!...
            You try to walk back but you exerted all your energy
            You fall to the ground, exhausted. 
            """)
            game_over()


        elif oasis_answer =="hangar":
            delay_print("""
            You keep walking for about an hour and finally get close to the Hanger
            Hoping that you can find some food and water and hide from a sun in shadow
            You open the old steel doors and can't believe what you got in front of your eyes!
            There a boxes full of food and water, barrels full of fuel and a light aircraft
            You eat and pack food and water into aircraft, you pour the fuel into the aircraft.
            You manage to find a way to open main big doors and you start the plane engine.
            
            Ready for takeoff!""")

            print("""
                      ██    ██  ██████  ██    ██     ██     ██  ██████  ███    ██ 
                       ██  ██  ██    ██ ██    ██     ██     ██ ██    ██ ████   ██ 
                        ████   ██    ██ ██    ██     ██  █  ██ ██    ██ ██ ██  ██ 
                         ██    ██    ██ ██    ██     ██ ███ ██ ██    ██ ██  ██ ██ 
                         ██     ██████   ██████       ███ ███   ██████  ██   ████ 
                    """)
            print("""
                                                  |                                             
                                                  |                                             
                    ______________________________|_______________________________              
                                        ----\--||___||--/----                                   
                                             \ :==^==: /                                        
                                              \|  o  |/                                         
                                               \_____/                                          
                                               /  |  \                                          
                                             ^/   ^   \^                                        
                                             U    U    U                               
                                                                    
                """)
        else:
            print("Please enter your choice again")
            oasis()


    def game_over():
            print("YOU DIED!!!!!")
            print("""
            ┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
            ┼┼┼██┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼██┼┼┼┼┼┼┼┼┼███▀▀▀██┼███▀▀▀███┼███▀█▄█▀███┼██▀▀▀┼
            ┼████▄┼┼┼▄▄▄▄▄▄▄┼┼┼▄████┼┼┼┼┼┼┼██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼█┼┼┼██┼██┼┼┼┼
            ┼┼┼┼▀▀█▄█████████▄█▀▀┼┼┼┼┼┼┼┼┼┼██┼┼┼▄▄▄┼██▄▄▄▄▄██┼██┼┼┼▀┼┼┼██┼██▀▀▀┼
            ┼┼┼┼┼┼█████████████┼┼┼┼┼┼┼┼┼┼┼┼██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██┼┼┼┼
            ┼┼┼┼┼┼██▀▀▀███▀▀▀██┼┼┼┼┼┼┼┼┼┼┼┼███▄▄▄██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██▄▄▄┼
            ┼┼┼┼┼┼██┼┼┼███┼┼┼██┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
            ┼┼┼┼┼┼█████▀▄▀█████┼┼┼┼┼┼┼┼┼┼┼┼███▀▀▀███┼▀███┼┼██▀┼██▀▀▀┼██▀▀▀▀██▄┼┼
            ┼┼┼┼┼┼┼███████████┼┼┼┼┼┼┼┼┼┼┼┼┼██┼┼┼┼┼██┼┼┼██┼┼██┼┼██┼┼┼┼██┼┼┼┼┼██┼┼
            ┼┼┼▄▄▄██┼┼█▀█▀█┼┼██▄▄▄┼┼┼┼┼┼┼┼┼██┼┼┼┼┼██┼┼┼██┼┼██┼┼██▀▀▀┼██▄▄▄▄▄▀▀┼┼
            ┼┼┼▀▀██┼┼┼┼┼┼┼┼┼┼┼██▀▀┼┼┼┼┼┼┼┼┼██┼┼┼┼┼██┼┼┼██┼┼█▀┼┼██┼┼┼┼██┼┼┼┼┼██┼┼
            ┼┼┼┼┼▀▀┼┼┼┼┼┼┼┼┼┼┼▀▀┼┼┼┼┼┼┼┼┼┼┼███▄▄▄███┼┼┼─▀█▀┼┼─┼██▄▄▄┼██┼┼┼┼┼██▄┼
            ┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
            """) 

    start_game()
game()
