import json

data =[]

with open("schedule.json", "r") as read_file:
    schedule_dict = json.load(read_file)
for element in schedule_dict:
    data_set = {"title": element['summary'], "start": element['start'], "end": element['end']}
    print(data_set)
    data.append(data_set)
    with open("parsed_schedule.json", "w") as write_file:
        json.dump(data, write_file)
