import json

with open("candidates.json", "r") as read_file:
    data = json.load(read_file)
def load_candidates_from_json(file):
    print(file)
def get_candidate(candidate_id):
    pass

def get_candidates_by_name(candidate_name):
    pass

def get_candidates_by_skill(skill_name):
    pass

load_candidates_from_json(data)
