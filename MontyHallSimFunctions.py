#Author: Tara Yoo - Monty Hall simulation

#Randomly assign a car to one of the doors: 1, 2, 3
import random
car_door = random.randint(1,3)

#Get user to choose door
def choose_door():
	door_chosen_by_user = random.randint(1,3)
	return door_chosen_by_user

#Randomly pick a remaining door with a goat

def open_a_door(door_chosen_by_user,door_with_car):
	options = [1,2,3]
	if door_chosen_by_user == door_with_car:
		options.remove(door_chosen_by_user)
	if door_chosen_by_user != door_with_car:
		options.remove(door_chosen_by_user)
		options.remove(door_with_car)
	if len(options) > 1:		
		return options[random.randint(0,1)]
	else:
		return options[0]

#User randomly chooses to switch or not to switch - output second chosen door
def switch(door_chosen_by_user,door_chosen_by_host):
	options = [1,2,3]
	options.remove(door_chosen_by_host)
	options.remove(door_chosen_by_user)
	door_chosen_by_user = options[0]
	return door_chosen_by_user		
	
def Simulate_Monty_Hall_if_user_switches():
	runs = int(input("How many runs? "))
	got_car = 0
	for i in range(runs):
		first_door = choose_door()
		opened_dud_door = open_a_door(first_door,car_door)
		second_door = switch(first_door,opened_dud_door)
		if second_door == car_door:
			got_car += 1
	print(got_car / runs)

def Simulate_Monty_Hall_if_user_stays():
	runs = int(input("How many runs? "))
	got_car = 0
	for i in range(runs):
		first_door = choose_door()
		opened_dud_door = open_a_door(first_door,car_door)
		if first_door == car_door:
			got_car += 1
	print (got_car / runs)

Simulate_Monty_Hall_if_user_switches()
Simulate_Monty_Hall_if_user_stays()
