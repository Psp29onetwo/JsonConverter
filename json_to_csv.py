# Json to csv

import csv
import json

with open('input.json') as data:
    json_input = json.load(data)
    result = []
    for k, v in json_input['maker_response']['video2d']['data']['annotations'][0]['frames'].items():
        result_data = {'frame_label': k,
                       'label': v['label'],
                       'tracker_id': json_input['maker_response']['video2d']['data']['annotations'][0]['_id']}

        # Renaming keys
        result_data['frame_id'] = result_data.pop('frame_label')
        result_data['tracking_id'] = result_data.pop('tracker_id')
        result.append(result_data)

# field names
fields = ['frame_id', 'tracking_id', 'label']
# name of csv file
filename = "result_csv.csv"

# writing to csv file
with open(filename, 'w') as csvfile:
    # creating a csv dict writer object
    writer = csv.DictWriter(csvfile, fieldnames=fields)

    # writing headers (field names)
    writer.writeheader()

    # writing data rows
    writer.writerows(result)