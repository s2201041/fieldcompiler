import json
import csv

def load_csv(filename,opponent,turns,turnSeconds,first,id):

    #CSV読み込み

    f = open(filename+".csv")

    reader = csv.reader(f)
    building = [row for row in reader]

    m_size = len(building)

    masons = [[0] * m_size] * m_size
    masons = [[0] * m_size for i in range(m_size)]

    masons[1][1] = 1


    m_count = 0
    a = 1
    b = -1
    for x, w in enumerate(building):
        for y, field in enumerate(w):
            if field == "a":
                building[x][y] = 0
                masons[x][y] = a
                a+=1

                m_count+=1
            elif field == "b":
                building[x][y] = 0
                masons[x][y] = b
                b-=1

                m_count+=1
            else :
                building[x][y] = int(field)


    for i in building:
        print(i)

    print("")

    for i in masons:
        print(i)

    print("")

    #Json書き出し  
    json_load = open('matches.json' , "r")
    matches = json.load(json_load)

    matches["matches"][0]["id"] = id
    matches["matches"][0]["opponent"] = opponent
    matches["matches"][0]["turns"] = turns 
    matches["matches"][0]["turnSeconds"] = turnSeconds
    matches["matches"][0]["turnSeconds"] = turnSeconds
    matches["matches"][0]["first"] = first
    matches["matches"][0]["board"]["mason"] = m_count
    matches["matches"][0]["board"]["structures"] = building
    matches["matches"][0]["board"]["masons"] = masons 

    save_json = open("./matches/"+filename+".json","w")
    json.dump(matches,save_json,indent=2)

#magic numbers
m_first = [True,False]
m_type = ["A","B","C"]
m_size = ["11","13","15","17","21","25"]

filename = "A11" 
opponent = "test"
turns = 10
turnSeconds = 10
id = 0
first = True

#for first in m_first:
for type in m_type:
    for size in m_size:
        load_csv(type+size,opponent,turns,turnSeconds,first,id)