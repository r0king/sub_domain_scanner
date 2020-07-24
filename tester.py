
import json





with open("details.json", 'r') as json_details_loc:
    details_content_dict = json.load(json_details_loc)
    with open(str(details_content_dict['Detail of sessoin'][-1]["json_loc"]), 'r') as json_details:
        details_content_dict = json.load(json_details)
    for num,line in details_content_dict.items():
        print(num,line)

    print("{}".format("{}, {} \n".format(num,line) for num,line in details_content_dict.items() ))