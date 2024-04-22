## Flask Application Design for Holiday Home Portal

### HTML Files

- **index.html**: The primary page of the application that displays search options for holiday rentals.
- **owner_dashboard.html**: A private portal for owners to publish and manage their properties.
- **property_details.html**: Page to showcase and book a specific holiday rental.
- **user_dashboard.html**: A private portal for users to manage their bookings and view their trip details.

### Routes

- **Home Page (GET)**:
   - `/`
   - Displays the search interface and allows users to search for properties.
- **Owner Login (GET, POST)**:
   - `/owner/login`
   - Authenticates and logs in property owners.
- **Property Listing (GET, POST)**:
   - `/owner/properties`
   - Used by owners to publish and manage their rental properties.
- **Property Details (GET)**:
   - `/properties/<property_id>`
   - Displays詳細なページ for a specific holiday rental, including availability and booking options.
- **User Login (GET, POST)**:
   - `/user/login`
   - Authenticates and logs in potential renters.
- **User Dashboard (GET)**:
   - `/user/dashboard`
   - Allows users to manage their bookings and view trip details.
- **Booking Management (GET, POST)**:
   - `/bookings`
   - Enables users to make and cancel bookings, as well as view their booking history.