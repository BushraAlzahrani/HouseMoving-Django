
# Project Name: Houses Moving-out System

## Idea:
A system to manage moving out/in house's bleongings like furntiure, kitchenware even personal stuff such as clothes if the owner desires so.

## Inspiration:
Facilitating the Moving out/in process wither it is between houses in the same city or to a diffrent city. Also, keeping track of the house bleongings and mangaing those who will pack and move it.
 
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

### House Owner

- Add House.
- Edit house information.
- Delete House.
- Reserve appointment.
- View their information.
- Edit their information.

### Packers

- Get the house information.
- Get the house owner information.
- view appointments.
- Add house blenggings.
- Edit house blenggings.
- Delete house blenggings.

### Drivers

- Get the house information.
- Get the house owner information.
- Get the car/truck inforamtion.


------------


#### Models


##### House:
- Previous_Address
- New_Address
- City
- Owner

#### Apointment:
- House
- User
- Date/time

##### Belongings:
- House
- Name (couch, wardrobe, silverware...)
- Type(furniture, kitchenware, clothes, toys, or other can be written )
- Room (living room, kitchen, bedroom, kids room)


##### PackingSupplies:
- Material (cardboard, bubble wrap, tissue paper)
- Quantity

##### Car/Truck:
- Name
- Size
- House
- Driver
