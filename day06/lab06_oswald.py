# TODO: write code to answer the following questions: 
# 1) which of these embassies is closest to the White House in meters? 
# how far is it, and what is the address?
# 2) if I wanted to hold a morning meeting there, which cafe would you suggest?
# 3) if I wanted to hold an evening meeting there, which bar would you suggest? 

####Question 1

import imp
imported_items = imp.load_source('mylab', '/Users/oswaldcodjoe/OneDrive - Washington University in St. Louis/Summer 19/Python/SecretAPIFolder/googleAPI/start_google_oswald.py')
gmaps = imported_items.client

whitehouse = '1600 Pennsylvania Avenue, Washington, DC'
location=gmaps.geocode(whitehouse)
location[0].keys()    #note: location is a list and the first item in that list is a
                      #dictionary. And it's the keys of this dictionary that we want. 
                      
location[0]["geometry"].keys()  #this is the keys of geometry, which is itself a key
                                #of the first item in location (a list)
location[0]['geometry']['location']

latlong=location[0]['geometry']['location'] #this gives us latitude and longitude of
                                            #whitehouse/the address we specified. 

destination = gmaps.reverse_geocode(latlong) #this takes latlong and gives us location
                                             #which is gmaps.geocode(whitehouse). It's 
                                             #like reverse. 

#Now I want to use the matrix function and the latlong of whitehouse as well as the
#latlong of the embassies below to find the distance. So I can know which is near. 

embassies = [[38.917228,-77.0522365], 
	[38.9076502, -77.0370427], 
	[38.916944, -77.048739] ] 

embassy1_latlong = {'lat':38.917228, 'lng':-77.0522365}
embassy2_latlong = {'lat':38.9076502, 'lng':-77.0370427}
embassy3_latlong = {'lat':38.916944, 'lng':-77.048739}

#Note: I got an error massage because latlong is a dictionary but I made just a list
#for latlong of the embassies so the matrix function didn't know how to proceed. Hence
#why I create a dictionary above. 

distance_1 = gmaps.distance_matrix(latlong, embassy1_latlong)
distance_2 = gmaps.distance_matrix(latlong, embassy2_latlong)
distance_3 = gmaps.distance_matrix(latlong, embassy3_latlong)

print(distance_1['rows'][0]['elements'][0]['distance']['text'])
print(distance_2['rows'][0]['elements'][0]['distance']['text'])
print(distance_3['rows'][0]['elements'][0]['distance']['text'])

#This code above selects/subsets the distance from a bunch info and prints it. 

#So the nearest is embassy2 with a distance of 1.9km. 

#Also note, if you don't know what a function does, you can look up documentation
#about it online. 

####Question 2

#For the cafe, my criterion is proximity. So I have to find the cafe's and 
#then their distance. So I can write a function that finds near by
#cafes. Or that takes cafes and uses code in question 1 to return
#their distance. Or if my criteria is price, I can write a function
#that takes in or looks for nearby cafes and returns their prices. cont. here. 


############This is just to get and change my current working dirctory so I can write a path.
import os
os.getcwd()
os.chdir('/Users/oswaldcodjoe/OneDrive - Washington University in St. Louis/Summer 19/Python/ocodjoePythonCourse2019/day06') 
###################
#####################
dir(imported_items)
####################
dir(gmaps)

type(location)

whitehouse