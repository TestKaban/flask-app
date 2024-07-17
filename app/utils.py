import json
strings = ['id','name','picture','position','gender','age','skills']
with open("candidates.json", "r") as read_file:
    data = json.load(read_file)
def load_candidates_from_json(file):
    for i in range(len(file)):
        print("######################")
        for x in range(len(strings)):
            print(file[i][strings[x]])
def get_candidate(file):
    id = str(input("Enter candidate id: "))
    for i in range(len(file)):
        if(id == str(file[i]['id'])):
            print("######################")
            for x in range(len(strings)):
                print(file[i][strings[x]])

def get_candidates_by_name(file):
    name = str(input("Enter candidate name: "))
    for i in range(len(file)):
        if (name == str(file[i]['name'])):
            print("######################")
            for x in range(len(strings)):
                print(file[i][strings[x]])

def get_candidates_by_skill(file):
    skill = str(input("Enter candidate skill: "))
    for i in range(len(file)):
        if (skill in str(file[i]['skills'].lower())):
            print("######################")
            for x in range(len(strings)):
                print(file[i][strings[x]])

# load_candidates_from_json(data)
get_candidate(data)
get_candidates_by_name(data)
get_candidates_by_skill(data)