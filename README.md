# Final project for 'INF 305- Database Management Systems 2' course - **Hotel booking system in Kazakhstan** 2022 Spring

## About project
The project is a hotel booking system.  
It consists of 30 Hotels in Kazakhstan 
User can search a city (**autocomplete** supported) and can sort through the search results. 

### Features overview
 - Responsive design
 - Search bar with autocomplete support
 - Dynamic elements
 - Pagination
 - Material design

#### 4 sorting methods are supported:
 - Rating (Ascending)
 - Price (Ascending)
 - Rating (Descending)
 - Price (Descending) 

User can Signup or book a hotel without signup(track number)
While Viewing a Hotel , user can view info, pictures, highlights, price, rating.  
When booking a hotel , user can select checkin date and checkout date and other details.  
Price for booking is created at front end and also at backend after submitting booking details

#### Details included for booking
 - Checkin date
 - Checkout date
 - Number of rooms
 - Number of kids
 - Number of Adults

#### Dynamic changes in booking details
 - Price changes dynamically as user select other fields.
 - Disabling of dates is also applied.
 - Checkout date can't be after checkin date.
 - Default checkout date is after one day of checkin date.
 - Maximum date of booking is one year in future.

### models.py 
this file contain models for user hotel booking 
info about the models are as following

 1. User model  
   this is the base auth model inherited from AbstractUser class.  
   additional info about users are phone (IntegerField) & avatar - image url for users (CharField).  
 2. Hotel model   
   this is to store hotels . it contains following fields.  
    - city (city of hotel)
    - name (name of the hotel)
    - overview (description for hotel)
    - highlight (general highlights for hotel)
    - room_types (luxury or regural) 
    - rating (stars)  
    - price (base price)
    - imgurls (image urls)
 3. Booking model   
   this is to store a booking. it contains following fields.  
    - hotel (hotel object)
    - user (user object)
    - tracking_id (unique tracking ID)
    - first_name (users first name)
    - last_name (users last name)
    - email (email address of user)
    - phone (phone number of user)
    - room (no of rooms booked)
    - adult (no of adults booked)
    - child (no of children booked)
    - checkin_date (check in date)
    - checkout_date (check in date)
    
 4. Add_hotels
    this is to store archive data
    -hotel
    -tracking id
    -first_name
    -last_name
    -email
    -phone
    -room
    -adult
    -child
    -checkin_date
    -checkout_date
    -booking_date
    -price
    -user
    
  5. UserArchive
   -user_id
   -username
   -first_name
   -last_name
   -phone


### urls.py  
this file contains url routes for the app
 - login
 - logout
 - register
 - cities (return JsonResponse of all cities)
 - search (search hotels)
 - popular (popular hotels)
 - profile (user profile )
 - book (booking page)
 - success (after a booking is successful)
 - track (track the booking with tracking_id)
 - add_hotel(only for admins)

  
### views.py  
function based views.   
 - index (basic homepage with few popular hotels) 
 - cities (return list of cities, for autocomplete inputs) 
 - search_hotels (for search and sort functionality pagination enabled)
 - popular hotels (high rated hotels , pagination enabled)
 - hotel_view (single hotel page)
 - create_price (generate price by hotel_id,room, no of adults,child,days)
 - book_hotel (POST request only ,book a hote withl)
 - successful (POST only, booking succesful page ,create a booking)
 - callback
 - track_booking
 - profile
 - login,logout view
 - register
 - add_hotels
