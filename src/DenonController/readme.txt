## - reset inputs

- - - All Zone - - -
000 - Power off all zones

- - - Main Zone - - -
XX# - Example: 42# - set the volume
100 - Turn on main zone
101 - Turn off main zone
105 - Mute on/off zone 2

- - - Zone 2 - - -
200 - Turn on zone 2
201 - Turn off zone 2
205 - Mute on/off zone 2




- - - - - - - - - - - - - - - - - - - - - - - - - 
- - - - - - - - Add more commands - - - - - - - - 
- - - - - - - - - - - - - - - - - - - - - - - - - 
To add more commands: 
1. Create a new command named <YOUR_COMMAND>.py
2. <YOUR_COMMAND>.py have to be a class and implement 2 methods:
	- def CanExecute(self, input):
		Have to return either True or False.
		It should return True when the string 'input' is equal to the wanted input combination you want your command to have. 
		If the string 'input' is not the wanted combination, the method should return False
	
	- def Execute(self, input):
		Implement the actual execution of the command, this can be as complex as you want

3. Add your new command to Start.py in the method GetCommands(...)
4. That is it, you are finished. 

Made by: 
Jens 'JWolf' Larsen

