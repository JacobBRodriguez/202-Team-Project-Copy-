
Team 5

Members:

Chanip Chong
Parshwa Gandhi
Jacob Rodriguez

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
- (TODO: Add to)
