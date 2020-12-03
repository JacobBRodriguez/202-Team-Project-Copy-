
Team 5

Members:

Chanip Chong </br>
Parshwa Gandhi </br>
Jacob Rodriguez </br>

### Design Decisions:
#### Day 1 Design:
- Initial design idea is to do a React-Django REST-Framework to allow for decoupled work between the frontend and backend teams
- This will allow for minimal stalled progress since communication between the two sides can be accomplished via AJAX requests
- We will look into Firebase as a potential database option for our backend

#### First Sprint Design:
- Decided to go with MongoDB as our backend database. Will be using the *Djongo* connector in order to make use the of the Django ORM
- Rest of design decisions remain as is.

#### Second Sprint Design:
- Will no longer be doing a Django REST-Framework with React
- Instead will be serving up html files as Django templates within the Django app itself
- Will need to restructure base code so that all files are under the *djangoBackend* folder now

### Diagrams:
#### Overall Dependency of Components
![Component](https://github.com/gopinathsjsu/fa20-cmpe-202-sec-03-team-project-team-5/blob/master/design_images/Dependency%20Diagram.png?raw=true)

#### UML Class Diagram
![Class](https://github.com/gopinathsjsu/fa20-cmpe-202-sec-03-team-project-team-5/blob/master/design_images/graph.png?raw=true)

### Feature Set of Website:
- Register new users/login existing users
- Admin can remove users as needed
- Search current listings based on certain criteria
- Save a listing to favorites
- Realtor and Homeowner can sell a home (can list details in listing)
- Buyer can submit offer to seller
- Realtor and Homeowner/Landlord(same) can rent out a home/room
- Renter/Buyer(same) can submit offer for a rental
- All parties can view offers they sent or received
- Recieved offers also are sent to registered email account

### Project URLs
GitHub Repo
https://github.com/gopinathsjsu/fa20-cmpe-202-sec-03-team-project-team-5

Project Board
https://github.com/gopinathsjsu/fa20-cmpe-202-sec-03-team-project-team-5/projects/1

Project Journal
https://github.com/gopinathsjsu/fa20-cmpe-202-sec-03-team-project-team-5/blob/master/Project%20Journal

Google Sprint Task Sheet & burndown chart
https://docs.google.com/spreadsheets/d/1hmaxy0rC4w1bO9iUSOJgVA3cTYgKkh3Lv9J3Y84oYuU/edit#gid=1401709108

Clearer pictures of diagrams
https://github.com/gopinathsjsu/fa20-cmpe-202-sec-03-team-project-team-5/tree/master/Diagrams

