N = int(input())
rooms = input().split(' ')
total_reading = 0
central_meter = int(input())
meter_dict = {'J':'A','I':'B','H':'C','G':'C','F':'E'}
while(len(rooms)>0):
    curr_room = rooms.pop(0)
    room_reading = ''
    for i in range(0,len(curr_room)):
        if(curr_room[i] in meter_dict and i<len(curr_room)-1 and curr_room[i+1]==meter_dict[curr_room[i]]):
            room_reading = room_reading + str(ord(meter_dict[curr_room[i]]) - ord('A'))
        else:
            room_reading = room_reading + str(ord(curr_room[i]) - ord('A'))
    
    if(room_reading!=''):
        total_reading+=int(room_reading)

if(total_reading>central_meter):
    print("GREEDY")
    print(total_reading-central_meter)
else:
    print("INNOCENT")