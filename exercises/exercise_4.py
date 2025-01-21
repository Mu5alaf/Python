# This app Calcalute average of passengers per car

cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90

cars_not_driven = cars - drivers
cars_driven = drivers

carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

#now we will print our Calculation

print('There are',cars)
print('There are only',drivers,'drivers avalibel')
print('there will be',cars_not_driven, 'empty cars today')
print('we can transport', carpool_capacity,'pepole today')
print('we have',passengers, 'to carpool today')
print('we need to put about', average_passengers_per_car,'in each car')