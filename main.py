import random
name = "nicholas"
attempts = 0
max_attempt = 3
email = "nicholas@nicholas"
PIN = 12345678
energy = 50
HP = 100
Coins = 100

bagList = [ "banana", 'bandage']
sword_damage = 15
fireball_damage = 20
ice_damage= 10
goblin_health = 50
goblin_damage = 20

while attempts < max_attempt:
    email_input = input("Masukkan email: ")
    PIN_input = int(input("Masukkan PIN: "))
    
    if email_input == email:
        if PIN_input == PIN:
            print("email atau PIN benar")
            # break
            print("----------")
            print("RUN FROM DRAGON")
            while True:
            	print("1.Profil")
            	print("2. Main")
            	question = input("Pilih 1 atau 2 ?: ")
            	if question == "1":
            		print("name:" , name)
            		print("energy: ", energy)
            		print("Health:", HP)
            		print("Bag List:", bagList)
            		questionp = input("Would you like to edit your name? (YES/NO)")
            		if questionp == "YES":
            			questionpp = input("type your new name")
            			name = questionpp
            			print("Name has been changed to", name)
            			input("click enter to go back")

            	elif question == "2":
                    if energy >= 50:
                        question1 = input("Dragon chasing you, go to Mountain or cave: ")
                        print(" ")
                        if question1 == "cave":
                            print("you fall into a hole and die")
                        elif question1 == "Mountain":
                            print("You hike the mountain and see an apple tree full of apples")
                            # energy = energy - 10
                            # print("Energy: ", energy)
                            question2 = input("Eat or ignore")
                            if question2 == "Eat":
                            print("You lose health because of poison")
                            print("Health:", HP - 15)
                            print("You hike more and you see an old woman inviting you to her house, go in or ignore")
                            print(" ")
                            question3 = input("Go or ignore: ")
                            if question3 == "ignore":
                            print("You have no place to rest and eat food and eventually die")
                            elif question3 == "Go":
                            print(" ")
                            print("You rest at the house")
                            energy = energy + 20
                            bagList.append("Bread")
                            print("Energy :", energy)
                            print("You have been given bread")
                            print("Bag List:", bagList)
                            question4 = input("Eat the bread or no ?")
                            if question4 == "Eat":
                            energy = energy + 10
                            print("Energy:", energy)
                            print("The woman gives you 2 Treasure Chests")
                            question5 = input("Chest 1 or Chest 2")
                            if question5 == "Chest 1":
                            print("It was Cursed.You die")
                            elif question5 == "Chest 2":
                            bagList.append("Coins")
                            Coins = Coins + 500
                            print(bagList)
                            print("Coins:", Coins)

                            print("You see a goblin")
                            print(" ")
                            print("Choice: Sword/Fireball/Ice")
                            print(" ")

                            question6 = input("Slash with sword/ Use Fireball/ Use Ice")

                            print("-----")

                            hit_chance = random.randint(0,1)
                            if question6 == "Sword":
                            if hit_chance == 1:

                            print("Goblin takes damage:",sword_damage)
                            goblin_health= goblin_health - sword_damage
                            print("Goblin health:",goblin_health)
                            elif hit_chance == 0:
                            print("You missed")
                            elif question6 == "Fireball":
                            if hit_chance == 1:

                            print("Goblin takes damage:",fireball_damage)
                            goblin_health =  goblin_health - fireball_damage
                            print("Goblin health:", goblin_health)
                            elif hit_chance == 0:
                            print("You missed")
                            elif question6 == "Ice":
                            if hit_chance == 1:

                            print("Goblin takes damage:", ice_damage)
                            goblin_health = goblin_health - ice_damage
                            print("Goblin health:", goblin_health)
                            elif hit_chance == 0:
                            print("You missed")
                            hit_chance = random.randint(0,1)

                            print("----")
                            print("Goblin attacks you")
                            if hit_chance == 1:

                            HP = HP - goblin_damage
                            print("You take damage, your health is:", HP)
                            else:
                            print("Goblin Missed")
                            while goblin_health > 0:
                            question7 = input("Heal or Attack:")
                            if question7 == "Heal":
                            while "bandage" in bagList:

                            print("Used bandage")

                            HP += 15
                            print("Healed 15 HP")
                            bagList.remove("bandage")
                            break
                            else:
                            print("no bandage, can't heal")

                            elif question7 == "Attack":
                            hit_chance = random.randint(0,1)
                            print("Choice : Sword/Fireball/Ice")
                            question8= input("Slash with sword/ Use Fireball/ Use Ice")
                            if question8 == "Sword":
                            if hit_chance == 1:

                            print("Goblin takes damage:",sword_damage)
                            goblin_health= goblin_health - sword_damage
                            print("Goblin health:",goblin_health)
                            elif hit_chance == 0:
                            print("You missed")
                            elif question8 == "Fireball":
                            if hit_chance == 1:

                            print("Goblin takes damage:",fireball_damage)
                            goblin_health =  goblin_health - fireball_damage
                            print("Goblin health:", goblin_health)
                            elif hit_chance == 0:
                            print("You missed")
                            elif question8 == "Ice":
                            if hit_chance == 1:

                            print("Goblin takes damage:", ice_damage)
                            goblin_health = goblin_health - ice_damage
                            print("Goblin health:", goblin_health)
                            elif hit_chance == 0:
                            print("You missed")
                            hit_chance = random.randint(0,1)

                            print("----")
                            print("Goblin attacks you")
                            if hit_chance == 1:

                            HP = HP - goblin_damage
                            print("You take damage, your health is:", HP)
                            else:
                            print("Goblin Missed")
			                    
			                    
			            elif question2 == "ignore":
			                print("You hike more and you see an old woman inviting you to her house, go in or ignore")
			                print(" ")
			                question3 = input("Go or ignore: ")
			                if question3 == "ignore":
			                    print("You have no place to rest and eat food and eventually die")
			                elif question3 == "Go":
			                    print(" ")
			                    print("You rest at the house")
			                    energy = energy + 20
			                    bagList.append("Bread")
			                    print(" ")
			                    print("Energy :", energy)
			                    print("You have been given bread")
			                    print("Bag List:", bagList)
			                    question4 = input("Eat the bread or no ?")
			                    if question4 == "Eat":
			                        energy = energy + 10
			                        
			                        print("Energy:", energy)
			                        
			                        bagList.remove("Bread")
			                        print("You have eaten the bread")
			                        print(bagList)
			                        print(" ")
			                    print("The woman gives you 2 Treasure Chests")
			                    question5 = input("Chest 1 or Chest 2")
			                    if question5 == "Chest 1":
			                        print("It was Cursed.You die")
			                    elif question5 == "Chest 2":
			                        bagList.append("Coins")
			                        Coins = Coins + 500
			                        print(bagList)
			                        print("Coins:", Coins)
			                        
			                        # print("You see a goblin")
			                        # question6 = input("Slash with sword/ Use Fireball/ Use Ice")
			                        # print("Choice: Sword/Fireball/Ice")
			                        # if question6 == "Sword":
			                        #     print("Goblin takes damage:", sword_damage)
			                
			        			
							# question4 = input("Chest 1 or Chest 2:)
							# if question4 == "Chest 1":
							# 	print("It was cursed. You die")
							# elif question4 == "Chest 2":
							# 	print("You get money and win")
					
			    
			    
			    # question1 = input("Mountain or cave")
			    # if question1 == "cave":
			    #     print("you fall into a hole and die")
			    # elif question1 == "Mountain":
			    #     print("You hike the mountain and see an apple tree full of apples")
			        
			    #     question2 = input("Eat or ignore?")
			    #     if question2 == "Eat":
			    #         print("You die because of poison")
			    #     elif question2 == "ignore":
			    #         print("You hike more and you see an old woman invites you to her house, go in or ignore?")
			            
			    #         question3 = input("Go or ignore")
			    #         if question3== "ignore":
			    #             print("You have no place to rest and eat food and eventually die")
			    #         elif question3 == "Go":
			    #             print("You rest at the house and the woman gives you 2 treasure chests")
			                
			    #             question4 = input("Chest 1 or Chest 2?")
			    #             if question4 == "Chest 1":
			    #                 print ("It was cursed. You die")
			    #             elif question4 =="Chest 2":
			    #             print("You get money and win")
	                
        else:
	        # attempts += 1
	        attempts = attempts + 1
	        # print("Attempts : ", attempts)
	        print(f"attempts: {attempts}")
	        
	        print("email atau PIN salah")
                       
    else:
        print("email atau PIN salah")
        attempts = attempts + 1
        print(f"attempts : {attempts}")
else:
    print("Account locked, too many attempts")
attempts = 0
max_attempt = 3
email = "nicholas@nicholas"
PIN = 12345678
energy = 50
HP = 100
Coins = 100
bagList = [ "banana", 'energy ball', 'revive card']
sword_damage = 15
fireball_damage = 20
ice_damage= 10
goblin_health = 50

while attempts < max_attempt:
    email_input = input("Masukkan email: ")
    PIN_input = int(input("Masukkan PIN: "))
    
    if email_input == email:
        if PIN_input == PIN:
            print("email atau PIN benar")
            # break
            print("----------")
            
            print("RUN FROM DRAGON")
            
         
            print("1.Profil")
            print("2. Main")
        
            
            question = input("Pilih 1 atau 2 ?: ")
            if question == "1":
                print("nama:nicholas")
                print("energy: ", energy)
                print("Health:", HP)
                print("Bag List:", bagList)
            elif question == "2":
                if energy >= 50:
                    question1 = input("Mountain or cave: ")
                    print(" ")
                    if question1 == "cave":
                    	print("you fall into a hole and die")
                    elif question1 == "Mountain":
                        print("You hike the mountain and see an apple tree full of apples")
                        # energy = energy - 10
                        # print("Energy: ", energy)
                        question2 = input("Eat or ignore")
                        if question2 == "Eat":
                            print("You lose health because of poison")
                            print("Health:", HP - 15)
                            print("You hike more and you see an old woman inviting you to her house, go in or ignore")
                            print(" ")
                            question3 = input("Go or ignore: ")
                            if question3 == "ignore":
                                print("You have no place to rest and eat food and eventually die")
                            elif question3 == "Go":
                                print(" ")
                                print("You rest at the house")
                                energy = energy + 20
                                bagList.append("Bread")
                                print("Energy :", energy)
                                print("You have been given bread")
                                print("Bag List:", bagList)
                                question4 = input("Eat the bread or no ?")
                                if question4 == "Eat":
                                    energy = energy + 10
                                    print("Energy:", energy)
                                print("The woman gives you 2 Treasure Chests")
                                question5 = input("Chest 1 or Chest 2")
                                if question5 == "Chest 1":
                                    print("It was Cursed.You die")
                                elif question5 == "Chest 2":
                                    bagList.append("Coins")
                                    Coins = Coins + 500
                                    print(bagList)
                                    print("Coins:", Coins)
                                    
                                    print("You see a goblin")
                                    print("Choice: Sword/Fireball/Ice")
                                    question6 = input("Slash with sword/ Use Fireball/ Use Ice")
                                    print("-----")
                                    
                                    if question6 == "Sword":
                                        print("Goblin takes damage:", goblin_health - sword_damage)
                                        goblin_health= goblin_health - sword_damage
                                        print("Goblin health:",goblin_health)
                                    if question6 == "Fireball":
                                        print("Goblin takes damage:", goblin_health - fireball_damage)
                                        goblin_health =  goblin_health - fireball_damage
                                        print("Goblin health:", goblin_health)
                                    if question6 == "Ice":
                                        print("Goblin takes damage:", goblin_health - sword_damage)
                                        goblin_health = goblin_health - ice_damage
                                        print("Goblin health:", goblin_health)
                                    
                                
                        elif question2 == "ignore":
                            print("You hike more and you see an old woman inviting you to her house, go in or ignore")
                            print(" ")
                            question3 = input("Go or ignore: ")
                            if question3 == "ignore":
                                print("You have no place to rest and eat food and eventually die")
                            elif question3 == "Go":
                                print(" ")
                                print("You rest at the house")
                                energy = energy + 20
                                bagList.append("Bread")
                                print(" ")
                                print("Energy :", energy)
                                print("You have been given bread")
                                print("Bag List:", bagList)
                                question4 = input("Eat the bread or no ?")
                                if question4 == "Eat":
                                    energy = energy + 10
                                    
                                    print("Energy:", energy)
                                    
                                    bagList.remove("Bread")
                                    print("You have eaten the bread")
                                    print(bagList)
                                    print(" ")
                                print("The woman gives you 2 Treasure Chests")
                                question5 = input("Chest 1 or Chest 2")
                                if question5 == "Chest 1":
                                    print("It was Cursed.You die")
                                elif question5 == "Chest 2":
                                    bagList.append("Coins")
                                    Coins = Coins + 500
                                    print(bagList)
                                    print("Coins:", Coins)
                                    
                                    print("You see a goblin")
                                    question6 = input("Slash with sword/ Use Fireball/ Use Ice")
                                    print("Choice: Sword/Fireball/Ice")
                                    if question6 == "Sword":
                                        print("Goblin takes damage:", sword_damage)
                            
                    			
        					# question4 = input("Chest 1 or Chest 2:)
        					# if question4 == "Chest 1":
        					# 	print("It was cursed. You die")
        					# elif question4 == "Chest 2":
        					# 	print("You get money and win")
    				
                
                
                # question1 = input("Mountain or cave")
                # if question1 == "cave":
                #     print("you fall into a hole and die")
                # elif question1 == "Mountain":
                #     print("You hike the mountain and see an apple tree full of apples")
                    
                #     question2 = input("Eat or ignore?")
                #     if question2 == "Eat":
                #         print("You die because of poison")
                #     elif question2 == "ignore":
                #         print("You hike more and you see an old woman invites you to her house, go in or ignore?")
                        
                #         question3 = input("Go or ignore")
                #         if question3== "ignore":
                #             print("You have no place to rest and eat food and eventually die")
                #         elif question3 == "Go":
                #             print("You rest at the house and the woman gives you 2 treasure chests")
                            
                #             question4 = input("Chest 1 or Chest 2?")
                #             if question4 == "Chest 1":
                #                 print ("It was cursed. You die")
                #             elif question4 =="Chest 2":
                #             print("You get money and win")
                
        else:
	        # attempts += 1
	        attempts = attempts + 1
	        # print("Attempts : ", attempts)
	        print(f"attempts: {attempts}")
	        
	        print("email atau PIN salah")
                       
    else:
        print("email atau PIN salah")
        attempts = attempts + 1
        print(f"attempts : {attempts}")
else:
    print("Account locked, too many attempts")




               
       
    

            
    

    





