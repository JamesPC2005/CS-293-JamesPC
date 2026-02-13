import random

#declare universals
current_time = 0

class user:
    def __init__(self,name):
        self.delay = 0 #keeps track of when to next attempt a send.
        self.window = 1 #range of time that the user will increase before trying to send again
        self.time = 0 #origonally kept track of time, i decided to move this feature to a function
        self.sending = 0 #true/false if message sending 0=false, 1=true
        self.name = name #assigns a number to each user, techanically can also assign names
    def step(self,current_time):
        if self.time == current_time: #sends packet if self.time 
            self.sending = 1
        else: self.sending = 0

    def fail_send(self):#executes exponential backoff max time growth and new random time selection capped to 2**5
        if self.window < 32: #increases window of time to a cap of 32
            self.window = 2*self.window

        self.delay = self.delay + random.randint(0 - self.window) #the time never resets, if self delay doenst continue to increase then the max cap might be passed before a solution is found



def test_ethernet(agents): #resolves a single test of the ethernet simulation
    userbase = create_agents(agents) #creates desired number of agents
    time = 0
    while None == False: #continue until results found
        sum = 0
        for i in len(userbase): #make sure commands affect all of the userbase
            userbase[i].step() #progress time
            sum += userbase[i].sending #if this number is ==1 then there is only one sender and a packet gets sent.
        time +=1
        if sum == 1: #check for sent packet
            return int(time) 
        else:
            for i in len(userbase): #reset random timers for next itteration
                userbase[i].fail_send()

def create_agents(agents): #creates a single new simulated ethernet user in a databdatabase
    database=[]
    for i in range(agents):
        database.append(user(i))
    return database #return list of all users




def main():
    print("please put how many simoultanious users you would like to simulate, and how many trials you would like to simulate")
    user_input=[None,None]
    user_input[0]=input("Number of users : ") #how many simulated users
    user_input[1]=input("Number of tests : ") #ask how many tests to preform
    
    results=[] #create empty array to store results
    
    for i in range (int(user_input[1])): #repeat for number of desired tests
        results.append(test_ethernet(int(user_input[0]))) #run a single test with number of desired users
    
    total = 0 #count total time for averageing later
    
    for i in range(len(results)): #sum for the average
        total+=results[i]
    avg_time = total/user_input[1] #calculate average
    
    #print(str(results)) #use to print out full dataset if you want to check it
    
    print("the average time to first send is:" + str(avg_time))

    
main()