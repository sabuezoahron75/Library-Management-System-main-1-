# Task 1.05 -- Sketch the Classes with CRC Cards

**Project:** Smart Parking Lot System (SPLS)\
**Deliverable:** Class--Responsibility--Collaborator (CRC) Cards

## 1. Introduction

This document summarizes the main domain classes and application modules
in the Smart Parking Lot System. Each CRC card identifies the class or
module, its primary responsibility, and the components it collaborates
with.

## 2. CRC Cards

  -----------------------------------------------------------------------
  Class Name              Responsibilities        Collaborators
  ----------------------- ----------------------- -----------------------
  **User (Abstract        Stores shared user      Driver; Administrator;
  Class)**                information and         Attendant; Server.
                          provides common account 
                          and authentication      
                          behavior.               

  **Driver**              Finds compatible        User; Vehicle;
                          parking spaces, makes   ParkingLot;
                          reservations, checks    ParkingSpace;
                          in, monitors parking    Reservation;
                          sessions, and pays      ParkingSession;
                          parking fees.           Payment.

  **Administrator**       Manages parking         User; ParkingLot;
                          operations, reviews     ParkingSpace;
                          incidents, updates      ParkingSession;
                          parking-space statuses, Reservation; Incident;
                          and adjusts facility    Server.
                          settings.               

  **Attendant**           Provides on-site        User; Driver;
                          assistance when         ParkingSpace;
                          automated parking       ParkingSession;
                          operations fail or      Administrator;
                          drivers need help.      Incident.

  **Vehicle**             Stores vehicle          Driver; ParkingLot;
                          information, including  ParkingSpace;
                          its identifier and      ParkingSession;
                          type, and determines    Reservation.
                          compatibility with a    
                          parking space.          

  **ParkingLot**          Manages the parking     ParkingSpace; Vehicle;
                          facility, including its Driver; Reservation;
                          levels, spaces,         ParkingSession;
                          availability, and       Administrator.
                          capacity.               

  **ParkingSpace**        Maintains an individual ParkingLot; Vehicle;
                          space's identifier,     Driver; Reservation;
                          type, availability      ParkingSession;
                          status, and current     Administrator.
                          assignment.             

  **Reservation**         Manages a booking,      Driver; Vehicle;
                          including the assigned  ParkingLot;
                          space, driver details,  ParkingSpace;
                          arrival time,           ParkingSession;
                          expiration,             Incident.
                          cancellation, and       
                          check-in status.        

  **ParkingSession**      Tracks an active        Driver; Vehicle;
                          parking session,        ParkingSpace;
                          including the vehicle,  Reservation; Rate;
                          assigned space, start   Payment.
                          time, duration, and     
                          checkout.               

  **Rate**                Calculates parking fees Vehicle;
                          using configured rates  ParkingSession;
                          and parking duration.   Payment; Administrator.

  **Payment**             Records payment amount, Driver; ParkingSession;
                          method, transaction     Rate; Incident;
                          status, and receipt     Administrator.
                          details.                

  **Incident**            Records parking-related Administrator;
                          problems, failed        ParkingLot;
                          payments, reservation   ParkingSpace;
                          exceptions, and other   Reservation;
                          operational issues.     ParkingSession;
                                                  Payment.

  **Server (Java)**       Hosts the web           auth.js; Administrator;
                          application, handles    Login Page; Admin
                          HTTP requests, manages  Dashboard.
                          administrator           
                          authentication          
                          sessions, and serves    
                          application files.      

  **driver.js (Driver     Handles the driver's    Vehicle; ParkingSpace;
  Module)**               interface, space        Reservation;
                          filtering,              ParkingSession;
                          reservations, check-in, Payment; Rate;
                          fee calculations,       localStorage.
                          checkout, and simulated 
                          payments.               

  **auth.js               Handles administrator   Server; Administrator;
  (Authentication         login, session          Login Page; Admin
  Module)**               verification,           Dashboard.
                          authentication errors,  
                          and logout requests.    

  **Admin Dashboard       Displays parking        Administrator;
  Module (admin.html)**   statistics and provides ParkingLot;
                          management controls for ParkingSpace;
                          spaces, reservations,   Reservation;
                          sessions, payments,     ParkingSession;
                          incidents, and facility Payment; Incident;
                          settings.               Rate; localStorage.
  -----------------------------------------------------------------------

## 3. Collaboration Overview

A typical parking workflow involves the following components:

1.  **Driver / Administrator** -- Interacts with the system and manages
    parking operations.
2.  **ParkingLot** -- Represents the facility, its capacity, and space
    availability.
3.  **Vehicle + ParkingSpace** -- Support vehicle classification,
    compatibility checks, and space assignment.
4.  **Reservation + ParkingSession** -- Manage bookings, check-in,
    parking duration, and checkout.
5.  **Rate + Payment** -- Calculate the parking fee and record the
    transaction.
6.  **Incident** -- Records operational exceptions for administrator
    review.

## 4. Design Considerations

-   **Encapsulation:** Each class is responsible for managing its own
    information and operations.
-   **Inheritance:** Driver, Administrator, and a possible Attendant
    role can share common User properties.
-   **Polymorphism:** Different vehicle and parking-space types can
    support different compatibility behaviors.
-   **Abstraction:** Reservation, parking, and payment operations are
    separated from their implementation details.
-   **Modularity:** Each class or module focuses on a specific
    responsibility.

## 5. Conclusion and Implementation Note

The CRC cards describe the responsibilities and relationships of the
Smart Parking Lot System's main components. They provide a clear
overview of how the system's classes and modules work together.

**Implementation note:** The implementation described for this
deliverable uses JavaScript functions and browser `localStorage` for
many parking operations, while `Server.java` handles HTTP serving and
administrator authentication. The domain classes shown in this design
are not all separately implemented Java classes. Payment processing is
currently simulated. `Attendant` is a proposed design role, not a
separate implemented class.
