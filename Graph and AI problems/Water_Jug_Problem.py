# You are given two jugs of 4, 3 litre capacity respectively (initialy empty), a tap of unlimited supply, and a ground. You have to fill the jug of 4 litre capacity upto 2 litres.
#Solution is calculated using BFS algorithm with each step calculating all possible cases that can be generated from it.
def water_jug(initial_state):
    history = set()
    queue = [initial_state]
    history.add(initial_state)
    cost = 0
    while(len(queue)):
        length = len(queue)
        print(queue)
        for i in range(0,length):
            curr_state = queue.pop(0)
            print("current state is: {}".format(curr_state))
            if(curr_state[0]==2):
                print("End reached")
                return cost
            if(curr_state[0]<4 and (4,curr_state[1]) not in history):
                queue.append((4,curr_state[1]))
                history.add((4,curr_state[1]))
            if(curr_state[1]<3 and (curr_state[0],3) not in history):
                queue.append((curr_state[0],3))
                history.add((curr_state[0],3))
            if(curr_state[0]>0 and (0,curr_state[1]) not in history):
                queue.append((0,curr_state[1]))
                history.add((0,curr_state[1]))
            if(curr_state[1]>0 and (curr_state[0],0) not in history):
                queue.append((curr_state[0],0))
                history.add((curr_state[0],0))
            if(curr_state[0]+curr_state[1]>0 and curr_state[0]+curr_state[1]>=4 and curr_state[1]>0 and  (4,curr_state[1]-4+curr_state[0]) not in history):
                history.add((4,curr_state[1]-4+curr_state[0]))
                queue.append((4,curr_state[1]-4+curr_state[0]))
            if(curr_state[0]+curr_state[1]>0 and curr_state[0]+curr_state[1]>=3 and curr_state[0]>0 and (4 - (3- curr_state[1]), 3) not in history):
                history.add((4 - (3- curr_state[1]), 3))
                queue.append((4 - (3- curr_state[1]), 3))
            if(curr_state[0]+curr_state[1]>0 and curr_state[0]+curr_state[1]<=4 and curr_state[1]>=0 and (curr_state[0]+curr_state[1],0) not in history):
                history.add((curr_state[0]+curr_state[1],0))
                queue.append((curr_state[0]+curr_state[1],0))
            if(curr_state[0]+curr_state[1]>0 and curr_state[0]+curr_state[1]<=3 and curr_state[0]>=0 and (0,curr_state[0]+curr_state[1]) not in history):
                history.add((0,curr_state[0]+curr_state[1]))
                queue.append((0,curr_state[0]+curr_state[1]))
        cost+=1
    print("Impossible to reach desired state")
initial_state = (0,0)
print(water_jug(initial_state))