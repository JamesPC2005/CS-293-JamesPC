import random

#declare universals
max_k = 14
max_b = 4
sample_size = 10000


class user:
    def __init__(self,name):
        self.delay = 0                      #keeps track of when to next attempt a send.
        self.window = 1                     #range of time that the user will increase before trying to send again
        self.time = 0                       #tracks the passed time
        self.sending = 0                    #true/false if message sending 0=false, 1=true
        self.name = name                    #assigns a number to each user, techanically can also assign names
                                            #just found out you can use tab to make comments look neat, this is sick, reduces clutter by a lot
    
    def step(self,current_time):
        if self.delay == current_time:      #sends packet if self.time 
            self.sending = 1
        else: self.sending = 0

    def fail_send(self, max_b):             #executes exponential backoff max time growth and new random time selection capped to 2**5
        if self.window < 2**max_b:          #increases window of time to a cap of 32
            self.window = 2*self.window
        self.delay += random.randint(1, self.window) #the time never resets, if self delay doenst continue to increase then the max cap might be passed before a solution is found

def run_trial(k, xb):                       #resolves a single test of the ethernet simulation
    userbase = create_user(k)               #creates desired number of k  
    time = 0

    while True:                             #continue until results found
        sum = 0
        for user in userbase:               #make sure commands affect all of the userbase
            user.step(time)                 #progress time
            sum += user.sending             #if this number is ==1 then there is only one sender and a packet gets sent.
        time +=1

        if sum == 1:                        #check for sent packet
            return int(time) 
        else:
            for user in userbase:           #reset random timers for next itteration
                if user.sending == 1:
                    user.fail_send(xb)
        if time == 100000:                  #quit if time becomes unreasonably large
            return 100000

def create_user(k):                         #creates a single new simulated ethernet user in a databdatabase
    database=[]
    for i in range(k):
        database.append(user(i))
    return database                         #return list of all users, as far as i understand this should be an array with pointers to all of the users? it works though so i wont worry about the details to much

def ev_oneOK(k,xb):
    
    results=[]                              #create empty array to store results
    
    if k == 1:
        return 1

    for i in range (sample_size):           #repeat for number of desired tests
        results.append(run_trial(k,xb))     #run a single test with number of desired users
    total = 0                               #count total time for averageing later
    for i in range(len(results)):           #sum for the average
        total+=results[i]
    avg_time = total/sample_size            #calculate average
    
    return(avg_time)                        #returns the average time

def main():
    print("max_k= "+str(max_k)+"max_b= "+str(max_b)+"sample_size="+str(sample_size))
    print("==============================")
    for k in range(max_k+1):
        for xb in [max_b-1, max_b]:
            avg = ev_oneOK(k+1, xb)
            print("k= "+str(k+1)+" xb= "+str(xb)+" ev_oneOK= "+str(avg))

main()  