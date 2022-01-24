#The function calculates mortality rating each hurricane
def mortality_rating(dict):
    #mortality_scale: 0: 0,
    #               1: 100,
     #              2: 500,
      #             3: 1000,
       #            4: 10000
    
    calculated_rating = {0:[], 1:[], 2:[], 3:[], 4:[]}
    
    for key, value in dict.items():
        if value["deaths"] < 100:
            calculated_rating[0].append(key)
        elif value["deaths"] >= 100 and value["deaths"] < 500:
            calculated_rating[1].append(key)
        elif value["deaths"] >= 500 and value["deaths"] < 1000:
            calculated_rating[2].append(key)
        elif value["deaths"] >= 1000 and value["deaths"] < 10000:
            calculated_rating[3].append(key)
        elif value["deaths"] >= 10000:
            calculated_rating[4].append(key)
    
    return calculated_rating

#The function calculates the deadliest hurricane
def the_deadliest_hurricane(dict):

    possible_value = []
    how_much_it_happened = 0

    for key, value in dict.items():
        if value["deaths"] > how_much_it_happened:
            how_much_it_happened = value["deaths"]
            possible_value = key
    
    the_result = {}
    the_result[possible_value] = how_much_it_happened

    return the_result

#This function finds the most affected area
def the_most_affected_area(area):

    how_much_it_happened = 0
    possible_area = []
    for item in area:
        if len(item) > how_much_it_happened:
            how_much_it_happened = len(item)
            possible_area = item
    
    the_result = {}
    the_result[how_much_it_happened] = possible_area
    
    return the_result

#This function returns a list with information how much area
#has been affected by hurricane
def how_often_is(area):
    
    new_dict = {}

    for item in area:
        for subitem in item:
            #If we already have the are we'll add one
            if subitem in new_dict:
                new_dict[subitem] = 1 + new_dict[subitem]
                continue
            #If we don't have we'll set the default value
            new_dict[subitem] = 1
    
    return new_dict

#This function is supposed to return information 
#about hurricane occurred in the year 
#that has been given as parameter
def the_hurricanes_by_year(dict, year):

    new_list = []
    #With parameter 'year' we're searching for a match 
    # through provided dictionary then we add it into new_list 
    for key, value in dict.items():
        if value["year"] == year:
            new_list.append(dict[key])
    
    return new_list

#This function makes a dictionary from all lists we have
def construct_a_dictionary(names, month, year, max_sustained_wind, 
                           area_affected, damage, death):

    hurricane_dictionary = {}
    
    #each hurricane have information such as month and year it appeared, 
    #damage caused and so one
    for index in range(0, len(names)):
        hurricane_dictionary[names[index]] = {
        "name": names[index],
        "month": month[index], 
        "year": year[index], 
        "max sustained wind": max_sustained_wind[index], 
        "affected area": area_affected[index], 
        "damage": damage[index], 
        "deaths": death[index]
        }

    return hurricane_dictionary

#This function returns new list with float numbers
def list_of_updated_damages(list_to_change):
    
    updated_list = []

    for value in list_to_change:
        #when we find known value we have to delete shortening the value have (M or B), changed value we save in this variable
        value_to_convert = 0
        #we find known values by determining whether value has shortening B (billions) or M (millions)
        if 'B' in value:
            value_to_convert = float(value[:-1])
            value_to_convert *= 1000000000
            updated_list.append(value_to_convert)
            continue
        elif 'M' in value:
            value_to_convert = float(value[:-1])
            value_to_convert *= 1000000
            updated_list.append(value_to_convert)
            continue
        #unknown values will be also assigned in new list
        updated_list.append(value)

    return updated_list
        

names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

updated_list_of_damages = list_of_updated_damages(damages)

the_hurricane_dictionary = construct_a_dictionary(names, months, years, max_sustained_winds, areas_affected, updated_list_of_damages, deaths)

search_for_year = the_hurricanes_by_year(the_hurricane_dictionary, 1932)

how_much__are_was_affected = how_often_is(areas_affected)

unlucky_area = the_most_affected_area(areas_affected)

deadliest_hurricane = the_deadliest_hurricane(the_hurricane_dictionary)

mortality_rating_of_hucalculated_rating = mortality_rating(the_hurricane_dictionary)

