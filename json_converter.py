import json

with open('input.json') as data:
    json_input = json.load(data)
    result = {}
    for k, v in json_input['maker_response']['video2d']['data']['annotations'][0]['frames'].items():
        result_data = {}
        frame_label = k
        result_data['_id'] = v['_id']
        result_data['type'] = v['type']
        result_data['label'] = v['label']
        result_data['point_x'] = v['points']['p1']['x']
        result_data['point_y'] = v['points']['p1']['y']
        result_data['point_label'] = v['points']['p1']['label']
        result_data['waering_mask'] = v['attributes']['waering_mask']['value']
        result_data['wearing_shirt'] = v['attributes']['wearing_shirt']['value']
        result_data['selfie_validity'] = v['attributes']['selfie_validity']['value']
        result_data['rider_id'] = json_input['rider_info'][k]['rider_id']
        result_data['tracker_id'] = json_input['maker_response']['video2d']['data']['annotations'][0]['_id']
        result[k] = [result_data]
    output = {'export_data': {}}
    output['export_data']['annotations'] = {}
    output['export_data']['annotations']['frames'] = result
    output['export_data']['number of annotations'] = len(result)

# Saving the result
with open('result_json.json', 'w') as f:
    json.dump(output, f, indent=2)
