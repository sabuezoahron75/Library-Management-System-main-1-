# SMART PARKING LOT --- CRC CARDS

**Task 1.05 -- Sketch the Classes with CRC Cards**\
**Class • Responsibility • Collaborator**

## 1. Purpose

CRC cards identify the main classes in the Smart Parking Lot system,
define one focused responsibility for each class, and show the classes
it collaborates with. The cards follow the project proposal and existing
class diagram. Service classes suggested in the proposal are included as
coordination classes so that business workflows do not become the job of
one large class.

## 2. CRC Cards

### 1. User (abstract)

-   **Class:** `User`
-   **Responsibility:** Stores shared account information and provides
    the common sign-in behavior for system users.
-   **Collaborators:** `Driver`, `Attendant`, `Administrator`, `Server`
-   **Extension point:** Shared identity/authentication fields and
    behavior belong here. Role-specific actions belong in subclasses.

### 2. Driver

-   **Class:** `Driver`
-   **Responsibility:** Allows a driver to select a vehicle, find
    compatible spaces, reserve a space, check in, and pay for a parking
    session.
-   **Collaborators:** `User`, `Vehicle`, `ParkingLot`,
    `ReservationService`, `ParkingSession`, `PaymentService`
-   **Extension point:** Add new driver-facing actions here without
    placing administrator duties in this class.

### 3. Attendant (optional role)

-   **Class:** `Attendant`
-   **Responsibility:** Provides on-site assistance when an automated
    parking operation fails or a driver needs help.
-   **Collaborators:** `User`, `Driver`, `ParkingSpace`,
    `ParkingSession`, `Incident`, `Administrator`
-   **Extension point:** Optional in the proposal. Include only if the
    team decides to implement attendant accounts and permissions.

### 4. Administrator

-   **Class:** `Administrator`
-   **Responsibility:** Reviews incidents and performs authorized manual
    corrections to parking spaces, assignments, and session records.
-   **Collaborators:** `User`, `Incident`, `ParkingLot`, `ParkingSpace`,
    `ParkingSession`, `ParkingService`
-   **Extension point:** Manual override and resolution rules should be
    added here or delegated to a dedicated policy/service---not to
    `Driver`.

### 5. Vehicle

-   **Class:** `Vehicle`
-   **Responsibility:** Stores vehicle identification and type, and
    determines whether a parking space is compatible with the vehicle.
-   **Collaborators:** `Driver`, `ParkingSpace`, `ParkingLot`,
    `ParkingSession`, `Reservation`
-   **Extension point:** New vehicle categories and compatibility
    criteria plug into `VehicleType` and the compatibility rule.

### 6. ParkingLot

-   **Class:** `ParkingLot`
-   **Responsibility:** Represents the facility and provides the
    collection of spaces from which availability and assignments are
    determined.
-   **Collaborators:** `ParkingSpace`, `Vehicle`, `ParkingService`,
    `ReservationService`
-   **Extension point:** New zones, levels, or facility-capacity rules
    can be added here. The initial scope is one facility.

### 7. ParkingSpace

-   **Class:** `ParkingSpace`
-   **Responsibility:** Maintains one parking space's identifier, type,
    status, and current reservation or occupancy assignment.
-   **Collaborators:** `ParkingLot`, `Vehicle`, `Reservation`,
    `ParkingSession`, `Administrator`, `ParkingService`
-   **Extension point:** Space status transitions (available, reserved,
    occupied, out of service) must be controlled here.

### 8. Reservation

-   **Class:** `Reservation`
-   **Responsibility:** Records a driver's reservation, including the
    selected space, arrival time window, and reservation status.
-   **Collaborators:** `Driver`, `Vehicle`, `ParkingSpace`,
    `ReservationService`, `ParkingSession`
-   **Extension point:** Cancellation, expiration, late-arrival, and
    grace-period rules plug into reservation status and
    `ReservationService`.

### 9. ParkingSession

-   **Class:** `ParkingSession`
-   **Responsibility:** Records one parking stay from entry to exit,
    including timestamps, status, duration, and calculated fee.
-   **Collaborators:** `Vehicle`, `ParkingSpace`, `Reservation`, `Rate`,
    `Payment`, `ParkingService`, `PaymentService`
-   **Extension point:** Time limits, reminders, and session status
    transitions belong with session rules/service logic.

### 10. Rate

-   **Class:** `Rate`
-   **Responsibility:** Stores the applicable parking pricing rule and
    calculates the charge for a parking duration.
-   **Collaborators:** `ParkingSession`, `PaymentService`, `Vehicle`
-   **Extension point:** New pricing models (hourly, flat,
    vehicle-specific, or peak rates) plug into rate
    configuration/calculation.

### 11. Payment

-   **Class:** `Payment`
-   **Responsibility:** Stores a payment attempt/result, amount, method,
    transaction reference, and receipt information.
-   **Collaborators:** `Driver`, `ParkingSession`, `Rate`,
    `PaymentService`, `Server`
-   **Extension point:** New payment methods and provider integrations
    plug into `PaymentMethod`/provider adapters. Current outcomes are
    simulated.

### 12. Incident

-   **Class:** `Incident`
-   **Responsibility:** Records a parking-rule issue or operational
    exception, its details, status, and resolution.
-   **Collaborators:** `Administrator`, `Attendant`, `ParkingSpace`,
    `Reservation`, `ParkingSession`, `ParkingService`
-   **Extension point:** New incident categories, severity levels,
    escalation, and resolution rules plug into incident
    classification/workflow.

### 13. Server (Java)

-   **Class:** `Server`
-   **Responsibility:** Handles HTTP requests, serves allowed web files,
    and manages administrator login sessions and access checks.
-   **Collaborators:** `Administrator`, `auth.js`, `admin.html`,
    `login.html`
-   **Extension point:** Authentication/session behavior is implemented
    in `Server.java`. Keep parking-domain rules out of HTTP request
    handling.

### 14. ReservationService (proposed)

-   **Class:** `ReservationService`
-   **Responsibility:** Coordinates reservation creation, compatibility
    and availability checks, assignment, cancellation, and expiry.
-   **Collaborators:** `Driver`, `Vehicle`, `ParkingLot`,
    `ParkingSpace`, `Reservation`, `Incident`
-   **Extension point:** Main insertion point for reservation policies
    such as duplicate-booking prevention, grace periods, and expiry.

### 15. ParkingService (proposed)

-   **Class:** `ParkingService`
-   **Responsibility:** Coordinates check-in/check-out, space assignment
    and release, occupancy updates, session tracking, and exception
    handling.
-   **Collaborators:** `ParkingLot`, `ParkingSpace`, `Vehicle`,
    `Reservation`, `ParkingSession`, `Rate`, `Incident`, `Administrator`
-   **Extension point:** Main insertion point for entry/exit event
    sources, occupancy rules, time limits, and future sensor/gate
    integration.

### 16. PaymentService (proposed)

-   **Class:** `PaymentService`
-   **Responsibility:** Coordinates fee calculation, payment
    processing/result recording, and receipt generation.
-   **Collaborators:** `ParkingSession`, `Rate`, `Payment`, `Driver`
-   **Extension point:** Main insertion point for real payment-provider
    integration, retries, refunds, and payment validation.

## 3. Where New Types and Rules Plug In

The following types are values/enumerations or configurable rules used
by the classes above. They do not need to become separate CRC cards
unless the implementation later gives them their own behavior.

  -------------------------------------------------------------------------
  New type / rule         Primary class or service Purpose / insertion
                                                   point
  ----------------------- ------------------------ ------------------------
  `VehicleType`           `Vehicle`;               Car, motorcycle, EV,
                          `ParkingSpace`;          etc.; used to filter and
                          `ReservationService`     validate compatible
                                                   spaces.

  `SpaceType` /           `ParkingSpace`           Defines space category
  `SpaceStatus`                                    and lifecycle states
                                                   such as available,
                                                   reserved, occupied, and
                                                   out of service.

  `ReservationStatus`     `Reservation`;           Controls pending,
                          `ReservationService`     confirmed, cancelled,
                                                   checked-in, and expired
                                                   reservation states.

  `SessionStatus`         `ParkingSession`;        Controls active,
                          `ParkingService`         completed/closed, and
                                                   other session states.

  `PaymentMethod` /       `Payment`;               Supports Maya, PayPal,
  `PaymentStatus`         `PaymentService`         GCash, GoMo, cash, or
                                                   another method, plus
                                                   pending/success/failed
                                                   results.

  `IncidentStatus` /      `Incident`;              Tracks open, under
  incident category       `Administrator`          review, resolved, or
                                                   escalated exceptions.

  Rates and time limits   `Rate`;                  Configurable pricing,
                          `ParkingSession`;        maximum duration, and
                          `ParkingService`         reminder thresholds.

  Grace period and        `ReservationService`     Defines how long a
  reservation expiry                               reserved space is held
                                                   and what happens after
                                                   late arrival.

  Compatibility policy    `Vehicle`;               Single place to add
                          `ReservationService`;    future restrictions such
                          `ParkingService`         as accessible spaces or
                                                   vehicle dimensions.

  Payment provider        `PaymentService`;        Replace simulated
  adapter                 `Payment`                payment outcomes with a
                                                   real provider
                                                   integration in a future
                                                   version.

  Entry/exit event source `ParkingService`         Connect future IoT
  (sensor or gate)                                 hardware without
                                                   changing the core
                                                   session and space
                                                   responsibilities.

  Persistent storage      Repository/data-access   Replace browser
                          layer (future)           `localStorage` for
                                                   parking records with a
                                                   shared database; keep
                                                   storage separate from
                                                   domain classes.
  -------------------------------------------------------------------------

## 4. Collaboration Overview

**Main workflow:**

`Driver → Vehicle → ParkingLot/ParkingSpace → ReservationService → Reservation → ParkingService → ParkingSession → Rate → PaymentService → Payment`

The `Administrator` reviews `Incident` records and uses `ParkingService`
to correct exceptional space or session states. `Server` protects
administrator pages and API endpoints.

**Inheritance:** `Driver`, `Attendant`, and `Administrator` extend
`User`.

**Associations:** - `ParkingLot` contains `ParkingSpace` objects. -
`Vehicle` and `Driver` participate in reservations and sessions. - A
`ParkingSession` uses a `Rate` and may be settled by a `Payment`.

## 5. Alignment with the Current Project

The project guide and class diagram define the domain model above. The
current prototype does not yet implement every domain class as a Java
class: parking records are stored in browser `localStorage` and driver
workflows are handled by JavaScript (`driver.js`). The Java `Server`
currently serves files and manages administrator authentication/session
state. Payment and parking entry/exit outcomes are simulated.
`ReservationService`, `ParkingService`, and `PaymentService` are
proposed design classes from the project guide, not existing implemented
source classes.

## 6. Acceptance Criteria Check

-   [x] A CRC card exists for each class in the proposed design,
    including the classes in the project guide and the Java Server
    component shown in the class diagram.
-   [x] Each class has one focused responsibility; workflow coordination
    is assigned to the proposed service classes.
-   [x] New types and rules are explicitly marked in Section 3 as
    extension points.

------------------------------------------------------------------------

**End of Task 1.05**
