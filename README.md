# Cinematica


### Cinematica is a project that allows users to browse and book movie tickets for various cinemas. Users can choose their preferred cinema, select a movie, pick a seat, and place their order seamlessly. Additionally, users can view available movies based on their showtimes.
### Admin users have full control over the system and can perform CRUD (Create, Read, Update, Delete) operations on cinemas, movies, showtimes, rooms, seats, and orders.


## Technologies Used
- Django: a high-level Python web framework
- Django Rest Framework (DRF): a powerful toolkit for building Web APIs in Django


## Features
- User-friendly interface for browsing cinemas, movies, showtimes, and seats
- Secure authentication and authorization system for users and admins
- Seamless ticket booking process with options to choose seats and confirm orders
- Comprehensive admin dashboard for managing cinemas, movies, showtimes, rooms, seats, and orders
- RESTful API endpoints for interacting with the system programmatically


### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/dnazirzhanov/Neobis_Cinematica.git
    ```

2. Navigate to the project directory:

    ```bash
    cd cinematica
    ```

3. Create a virtual environment (optional but recommended):

    ```bash
    python -m venv venv
    ```

4. Activate the virtual environment:

    - On Windows:

        ```bash
        .\venv\Scripts\activate
        ```

    - On macOS/Linux:

        ```bash
        source venv/bin/activate
        ```

5. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```


6. Apply database migrations:

    ```bash
    python manage.py migrate
    ```

7. Run the development server:

    ```bash
    python manage.py runserver
    ```


