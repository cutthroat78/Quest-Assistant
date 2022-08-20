# -*- coding: utf-8 -*-
import random
HP = "none"
AP = "none"
inventory = []
def Character():
    global CharacterParagraph
    CharacterParagraph = "Hello, my name is " + CharacterName + " " + CharacterPronouns + ". I'm " + CharacterAge + " years old and stand " + CharacterHeight + " tall. I’m the party’s " + CharacterRole + ". When people see me, they first notice my " + CharacterDistinctiveFeature1 + ", " + CharacterDistinctiveFeature2 + ", " + "and " + CharacterDistinctiveFeature3 + ". I wear " + CharacterClothingItem1 + ", " + CharacterClothingItem2 + ", and move with " + CharacterMovementStyle + ". I’m from " + CharacterPlace + ", where my people are known for " + CharacterCommunityFeature + ". I believe in " + CharacterIdeal + ", but my " + CharacterFlaw + " side can get in my way. I dream of " + CharacterDream + ". I carry\n"
while True:
    option = input("Main Menu:\nUse Dice\nCharacter\nInventory\nHP\nAP\nExit\n")
    if option == "Use Dice":
        result = random.randint(1,20)
        print("You rolled a " + str(result) + "!")
        if result == 1:
            print("Catastrophe:\nOh no. You automatically fail, and you may suffer a severe setback.")
        elif result in range(2, 5):
            print("Failure:\nYou fail your intended action and face a setback of the Guide’s choice. You might lose equipment, take damage from an enemy counterattack, or face some other misfortune.")
        elif result in range(5, 11):
            print("Tough Choice:\nYou succeed in your action, but there’s a cost. The Guide will give you a choice between two setbacks.")
        elif result in range(10, 20):
            print("Success:\nYou accomplish what you were trying to do without any compromises. If you’re dealing damage, you deal the standard amount.")
        elif result == 20:
            print("Triumph:\nThis is an exciting moment. You automatically succeed at what you were trying to do, and you may even find added fortune. If you’re dealing damage, double it.")
    if option == "Character":
        while True:
            characteroption = input("Character Creation Menu:\nCreate Character\nChange Something\nView Character\nExit\n")
            if characteroption == "Create Character":
                CharacterName = input("What is the Character's Name?\n")
                CharacterPronouns = input("What are the " + CharacterName + "'s Pronouns?\n")
                CharacterAge = input("What is the " + CharacterName + "'s Age?\n")
                CharacterHeight = input("What is the " + CharacterName + "'s Height?\n")
                CharacterRole = input("What is the " + CharacterName + "'s role in the party?\n")
                CharacterDistinctiveFeature1 = input("What is the first distinctive feature of " + CharacterName + "?\n")
                CharacterDistinctiveFeature2 = input("What is the second distinctive feature of " + CharacterName + "?\n")
                CharacterDistinctiveFeature3 = input("What is the third distinctive feature of " + CharacterName + "?\n")
                CharacterClothingItem1 = input("What is the first clothing item " + CharacterName + " wears?\n")
                CharacterClothingItem2 = input("What is the second clothing item " + CharacterName + " wears?\n")
                CharacterMovementStyle = input("How does " + CharacterName + " move?\n")
                CharacterPlace = input("Where is " + CharacterName + " from?\n")
                CharacterCommunityFeature = input("What is a community feature of " + CharacterPlace + " that " + CharacterName + " is from?\n")
                CharacterIdeal = input("What is a belief of " + CharacterName + "?\n")
                CharacterFlaw = input("What is a flaw of " + CharacterName + "?\n")
                CharacterDream = input("What is a dream " + CharacterName + " has?\n")
                Character()
                print(CharacterParagraph)
                print(inventory)
            elif characteroption == "Change Something":
                while True:
                    Character()
                    print(CharacterParagraph)
                    print(inventory)
                    CharacterChangeOption = input("What do you wanna change?\nName\nPronouns\nAge\nHeight\nRole\nFirst Distinctive Feature\nSecond Distinctive Feature\nThird Distinctive Feature\nFirst Clothing Item\nSecond Clothing Item\nMovement Style\nLocation\nCommunity Feature\nBelief\nFlaw\nDream\nExit\n")
                    if CharacterChangeOption == "Name":
                        CharacterName = input("What is the Character's Name?\n")
                    elif CharacterChangeOption == "Pronouns":
                        CharacterPronouns = input("What are the " + CharacterName + "'s Pronouns?\n")
                    elif CharacterChangeOption == "Age":
                        CharacterAge = input("What is the " + CharacterName + "'s Age?\n")
                    elif CharacterChangeOption == "Height":
                        CharacterHeight = input("What is the " + CharacterName + "'s Height?\n")
                    elif CharacterChangeOption == "Role":
                        CharacterRole = input("What is the " + CharacterName + "'s role in the party?\n")
                    elif CharacterChangeOption == "First Distinctive Feature":
                        CharacterDistinctiveFeature1 = input("What is the first distinctive feature of " + CharacterName + "?\n")
                    elif CharacterChangeOption == "Second Distinctive Feature":
                        CharacterDistinctiveFeature2 = input("What is the second distinctive feature of " + CharacterName + "?\n")
                    elif CharacterChangeOption == "Third Distinctive Feature":
                        CharacterDistinctiveFeature3 = input("What is the third distinctive feature of " + CharacterName + "?\n")
                    elif CharacterChangeOption == "First Clothing Item":
                        CharacterClothingItem1 = input("What is the first clothing item " + CharacterName + " wears?\n")
                    elif CharacterChangeOption == "Second Clothing Item":
                        CharacterClothingItem2 = input("What is the second clothing item " + CharacterName + " wears?\n")
                    elif CharacterChangeOption == "Movement Style":
                        CharacterMovementStyle = input("How does " + CharacterName + " move?\n")
                    elif CharacterChangeOption == "Location":
                        CharacterPlace = input("Where is " + CharacterName + " from?\n")
                    elif CharacterChangeOption == "Community Feature":
                        CharacterCommunityFeature = input("What is a community feature of " + CharacterPlace + " that " + CharacterName + " is from?\n")
                    elif CharacterChangeOption == "Belief":
                        CharacterIdeal = input("What is a belief of " + CharacterName + "?\n")
                    elif CharacterChangeOption == "Flaw":
                        CharacterFlaw = input("What is a flaw of " + CharacterName + "?\n")
                    elif CharacterChangeOption == "Dream":
                        CharacterDream = input("What is a dream " + CharacterName + " has?\n")
                    elif CharacterChangeOption == "Exit":
                        break
                    else:
                        print("That is not a valid answer")
            elif characteroption == "View Character":
                if "CharacterParagraph" in globals():
                    print(CharacterParagraph)
                    print(inventory)
                else:
                    print("Character has not been created yet!")
            elif characteroption == "Exit":
                break
            else:
                print("That is not a valid answer")
    elif option == "Inventory":
        finishedwithinventory = "none"
        if not inventory:
            inventoryOption = input("Your inventory is currently empty\nWould you like to add something? (yes/no)")
            if inventoryOption == "yes":
                inventory.append(input("Type what you wanna add!\n"))
                finishedwithinventory = input("Would you like to add something else? (yes/no)")
                while True:
                    if finishedwithinventory == "yes":
                        inventory.append(input("Type what you wanna add!\n"))
                        finishedwithinventory = input("Would you like to add anything else? (yes/no)")
                    elif finishedwithinventory == "no":
                        break
                    else:
                        print("That is not a valid answer. Type yes or no\n")
            elif inventoryOption == "no":
                continue
            else:
                print("That is not a valid answer. Type yes or no\n") 
        else:
            print("In your inventory is")
            print(*inventory, sep='\n')
            inventoryOption = input("Would you like to add something? (yes/no)\n")
            if inventoryOption == "yes":
                inventory.append(input("Type what you wanna add!\n"))
                finishedwithinventory = input("Would you like to add anything else? (yes/no)\n")
                while True:
                    if finishedwithinventory == "yes":
                        inventory.append(input("Type what you wanna add!\n"))
                        finishedwithinventory = input("Would you like to add anything else? (yes/no)\n")
                    elif finishedwithinventory == "no":
                        inventoryOption = "no"
                        break
                    else:
                        print("That is not a valid answer. Type yes or no\n")
            elif inventoryOption == "no":
                break
            else:
                print("That is not a valid answer. Type yes or no\n") 
    elif option == "HP":
        while True:
            if HP != "none":
                HPOption = input("Your current HP is " + str(HP) + "!\nDo you want to change your HP? (yes/no)\n")
                if HPOption == "yes":
                    while True:
                        print("Your current HP is " + str(HP) + "!")
                        HPOption = input("What do you wanna do?\nChange\nAdd\nSubtract\nExit\n")
                        if HPOption == "Change":
                            HP = input("What is your current HP?\n") 
                        elif HPOption == "Add":
                            HPadd = input("How much HP did you gain?\n")
                            HP = int(HP) + int(HPadd)
                        elif HPOption == "Subtract":
                            HPsubtract = input("How much HP did you lose?\n")
                            HP = int(HP) - int(HPsubtract)
                        elif HPOption == "Exit":
                            break
                        else:
                            print("That is not a valid answer")
                elif HPOption == "no":
                    break
                else:
                    print("That is not a valid answer. Type yes or no\n") 
            else:
                HP = input("What is your current HP?\n")   
    elif option == "AP":
        while True:
            if AP != "none":
                APOption = input("Your current AP is " + str(AP) + "!\nDo you want to change your AP? (yes/no)\n")
                if APOption == "yes":
                    while True:
                        print("Your current AP is " + str(AP) + "!")
                        APOption = input("What do you wanna do?\nChange\nAdd\nSubtract\nExit\n")
                        if APOption == "Change":
                            AP = input("What is your current AP?\n") 
                        elif APOption == "Add":
                            APadd = input("How much AP did you gain?\n")
                            AP = int(AP) + int(APadd)
                        elif APOption == "Subtract":
                            APsubtract = input("How much AP did you lose?\n")
                            AP = int(AP) - int(APsubtract)
                        elif APOption == "Exit":
                            break
                        else:
                            print("That is not a valid answer")
                elif APOption == "no":
                    break
                else:
                    print("That is not a valid answer. Type yes or no\n") 
            else:
                AP = input("What is your current AP? (You start with 10 AP)\n")  
    elif option == "Exit":
        break
    else:
        print("Feature is not ready or doesn't exist!")