from functions import *

# WORKING

swimmers_list = []
input_text = ''
while True:
    searched_swimmer = input('Provide swimmers LASTNAME FIRSTNAME: ')
    if searched_swimmer == 'F':
        break
    swimmers_list_df = get_page_source(searched_swimmer)
    print(swimmers_list_df.to_string(index=False))
    swimmer_params = get_specific_swimmer(swimmers_list_df)
    link_swimmer = swimmer_params[0]
    swimmer = swimmer_params[1]
    swimmers_list.append((link_swimmer, swimmer))

print(swimmers_list)
