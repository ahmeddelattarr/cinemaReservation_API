# Ticket Reservation System API

This is a Django REST framework (DRF)-based API for managing guests, movies, and reservations. The API includes both Function-Based Views (FBVs) and Viewsets.


## API Endpoints

The following endpoints are available in this API:

### Function-Based Views (FBVs)

1. **Guest List & Create**  
   - `GET /rest/fbv/`: Get a list of all guests.
   - `POST /rest/fbv/`: Create a new guest.

2. **Guest Detail, Update & Delete**  
   - `GET /rest/pk/<int:pk>`: Get details of a specific guest by their `pk` (primary key).
   - `PUT /rest/pk/<int:pk>`: Update details of a specific guest by their `pk`.
   - `DELETE /rest/pk/<int:pk>`: Delete a specific guest by their `pk`.

### Viewset-Based Views

These are registered with the DRF router for automatic URL routing.

1. **Guests Viewset**
   - `GET /rest/guests/`: Get a list of all guests.
   - `POST /rest/guests/`: Create a new guest.
   - `GET /rest/guests/<int:pk>/`: Get details of a specific guest.
   - `PUT /rest/guests/<int:pk>/`: Update a specific guest.
   - `DELETE /rest/guests/<int:pk>/`: Delete a specific guest.

2. **Movies Viewset**
   - `GET /rest/movies/`: Get a list of all movies.
   - `POST /rest/movies/`: Create a new movie.
   - `GET /rest/movies/<int:pk>/`: Get details of a specific movie.
   - `PUT /rest/movies/<int:pk>/`: Update a specific movie.
   - `DELETE /rest/movies/<int:pk>/`: Delete a specific movie.
   - **Search**: You can search movies by title using the query parameter `?search=<movie_name>`.

3. **Reservations Viewset**
   - `GET /rest/reservations/`: Get a list of all reservations.
   - `POST /rest/reservations/`: Create a new reservation.
   - `GET /rest/reservations/<int:pk>/`: Get details of a specific reservation.
   - `PUT /rest/reservations/<int:pk>/`: Update a specific reservation.
   - `DELETE /rest/reservations/<int:pk>/`: Delete a specific reservation.

