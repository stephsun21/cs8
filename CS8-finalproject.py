# Final project for CS8 - Summer 2020, Professor Jeff Moehlis (Prof J-Mo)

import random


def setParameter(paramStr,defaultValue):

    '''This function takes as input a string paramStr and a float or 
    int defaultValue.  If paramStr is the empty string, the function 
    returns the value of defaultValue.  If paramStr is not the empty
    string, the function returns the float or integer associated with 
    the string, according to the type of defaultValue.

    param paramStr: a string
    param defaultValue: can be either a float or an int
    '''

    if paramStr == "":
        return defaultValue
    else:
        if type(defaultValue) == int:
            return int(paramStr)
        else:            
            return float(paramStr)



def runTrial(beta,kappa,S0,Z0,survivors):

    ''' This function simulates a single trial, where a trial is a
    simulation of the zombie model which starts with S0 susceptibles
    and Z_0 zombies, and proceeds until either the humans win (Z=0) or
    the zombies win (S=0).  The input parameters S0, Z0, beta, and kappa 
    are model parameters.  The input parameter survivors is a list 
    containing the number of human survivors for all trials so far for 
    which there is a positive number.  If the zombies win, the function 
    returns the string "zombies".  If the humans win, the function returns 
    the string "humans"

    param beta: a float giving the rate of zombie infection
    param kappa: a float giving the rate at which zombies are killed
    param S0: an integer giving the initial number of humans
    param Z0: an integer giving the initial number of zombies
    param survivors: a list of integers containing the number of human
     survivors for all trials so far for which there is a positive
     number; note that this is mutable
    '''
    # set the value of dt and R0
    dt = 0.001
    R0 = 0

    # while there're still human and zombie survive, bite and kill will continue 
    while S0 != 0 and Z0 != 0:
        r = random.random() #set the value of r 

        # calculate the chance of a bite and a kill
        bite_constant = beta*S0*Z0*dt
        kill_constant = kappa*S0*Z0*dt

        if r < bite_constant:
        # a human gets bite by zombies,
        # survivers decreased by one and zombie increased by one
            S0 = S0 - 1
            Z0 = Z0 + 1
        elif r > (1-kill_constant):
        # a zombie gets killed by humans,
        # zombies decreased by one and survivers remain the same
        # the removed group increased by one
            S0 = S0
            Z0 = Z0 - 1
            R0 = R0 + 1
        else:
        # nothing happen
            S0 = S0
            Z0 = Z0

    # while one side loses
    if Z0 == 0: # humans win
        survivors.append(S0) #add the # of survivers of the trial to the survivors list
        return "humans"
    if S0 == 0: #zombies win
        return "zombies"

    

    
# Dictionary which contains default values for the model parameters
default = {
    "beta":0.01,
    "kappa":0.008,
    "S0":190,
    "Z0":10,
    "numtrials":100
}


# Main Program

# prompt the user to either choose to enter their own values or
# use the default values for the parameters 

ans = input("Would you like to use the default values for model parameters? (y or n): ")

if ans == 'y':   # use default values for model parameters;

    # assign the parameters with their default values
    beta = default["beta"]
    kappa = default["kappa"]
    S0 = default["S0"]
    Z0 = default["Z0"]
    numtrials = default["numtrials"]

else: #use user-entered value for model parameters
    
    # prompt the user to enter their values for each parameter
    # the user can still choose to use the default value
    # then assign the parameters with the user-entered values using the setParameter function

    beta_str = input("Enter value for beta (Press return for beta = {}): "\
                     .format(default["beta"]))
    beta = setParameter(beta_str, default["beta"])
    
    kappa_str = input("Enter value for kappa (Press return for kappa = {}): "\
                     .format(default["kappa"]))
    kappa = setParameter(kappa_str, default["kappa"])
    
    S0_str = input("Enter value for S0 (Press return for S0 = {}): "\
                     .format(default["S0"]))
    S0 = setParameter(S0_str, default["S0"])

    Z0_str = input("Enter value for Z0 (Press return for Z0 = {}): "\
                     .format(default["Z0"]))
    Z0 = setParameter(Z0_str, default["Z0"])

    numtrials_str = input("Enter value for numtrials (Press return for numtrials = {}): "\
                     .format(default["numtrials"]))
    numtrials = setParameter(numtrials_str, default["numtrials"])



# numtrials simulations of the zombie apocalypse
# call the runTrial function numtrials times using the while loop

i = 0 # initialize the i value to 0
survivors = [] # initialize the list survivors 

while i < numtrials:
    print(runTrial(beta,kappa,S0,Z0,survivors))
    i += 1
print()

# calculate and print the percent chance that the humans win

count = len(survivors) # counts the number of trails in which the humans survive
chance_human_win = (count/numtrials)*100

print('Chance that humans survive is {:.2f}%'.format(chance_human_win))

# print tha appropriate statement that corresponds with the percent chance that the humans win

if chance_human_win == 0:
    print("Yikes!")
elif chance_human_win < 10:
    print("Sorry, doesn't look good for the humans!")
elif chance_human_win <= 60 and chance_human_win >= 40:
    print("It's a toss-up!")
elif chance_human_win > 90:
    print("Looks good for the humans!")

# initializing the num_of_survivors variable, which counts the total # of survivors
num_of_survivors = 0

# counts the total number of survivors 
for i in range(len(survivors)):
    num_of_survivors = num_of_survivors + survivors[i]


# If there was at least one trial for which at least one human survived, the program
# prints the average number of suvivors in the format given in the problem statment

count = len(survivors) # counts the number of trails in which the humans survive

if count > 0:
    avg_survivors = (num_of_survivors/(S0*len(survivors)))*S0
    print(
    'If humans survive, the average number of survivors is {:.2f} out of {}.'.format(avg_survivors, S0))



