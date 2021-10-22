from functions import *

swimmers_to_compare = []
input_text = ''
while True:
    searched_swimmer = input('Provide swimmers LASTNAME FIRSTNAME: ')
    if searched_swimmer == 'F':
        break
    swimmers_list = get_page_source(searched_swimmer)
    print(swimmers_list.to_string(index=False))
    swimmer_params = get_specific_swimmer(swimmers_list)
    link_swimmer = swimmer_params[0]
    swimmer = swimmer_params[1]
    swimmer_distances = get_swimmer_distances(link_swimmer)['Code']
    swimmers_to_compare.append((link_swimmer, swimmer, set(swimmer_distances)))

common_distances = get_common_distances(swimmers_to_compare)
print('\n\n')
print(common_distances.to_string(index=False))
distance_str = input('Select distance to compare. Provide distance code: ')
distance_params = get_distances_to_compare(distance_str)[0]
distance_label = get_distances_to_compare(distance_str)[1][0]

results_all = []
swimmers_labels = []
for swimmer in swimmers_to_compare:
    link_swimmer = swimmer[0]
    swimmer_label = swimmer[1]
    link_distance_details = link_swimmer + '&styleId='
    results = get_results(distance_params, link_distance_details, 'one-dist')
    results_all.append(results)
    swimmers_labels.append(swimmer_label)

draw_plots(results_all, swimmers_labels, distance_label)
