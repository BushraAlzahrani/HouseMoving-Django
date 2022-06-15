
# Project Name: Houses Moving-out System

## Idea:
A system to manage moving out/in house's bleongings like furntiure, kitchenware even personal stuff such as clothes if the owner desires so.

## Inspiration:
Facilitating the Moving out/in process between houses. Also, keeping track of the house bleongings and mangaing those who will pack and move it.
 
## List of Services / Features:

- Manage the houses.
- Manage the appointments.
- Manage the house's belongings.
- Manage the house owner.
- Manage the packers.
- Manage the drivers

## User Stories
- Type of users: Admin, House Owner, Packers, and Drivers.

### Admin

- Create, Read, Update, Delete House Owner.
- Create, Read, Update, Delete Packers.
- Create, Read, Update, Delete Drivers.
- Create, Read, Update, Delete Moving Trucks.

### House Owner

- Add House.
- Edit house information.
- Delete house.
- Reserve appointment.
- view appointment.
- edit appointment.
- delete appointment.

### Packers

- Get the house information.
- Get the house owner information.
- view appointments.
- Add house belongings.
- Edit house belongings.
- Delete house belongings.

### Drivers

- Get the house information.
- Get the house owner information.
- Get the moving truck inforamtion.


------------

## Deployment

https://housemoving.herokuapp.com/

#### Models


##### House:
- Name
- Previous_Address
- New_Address
- Owner

#### Apointment:
- House
- User
- Reservation_date

##### Belongings:
- House
- Name (couch, wardrobe, silverware...)
- Type_belonging(choices= furniture, kitchenware, clothes, toys)
- Room (choices= living room, kitchen, bedroom, kids room)
- Quantity

##### Moving Truck:
- Size
- House
- Driver
