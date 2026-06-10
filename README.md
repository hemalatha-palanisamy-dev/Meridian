# Purpose of Meridian:

    - Keeping all the items to be done in our head will feel overwhelmed by nature. 
    - Meridian will help us to take off everything from our head into a consolidated, well structured place which will be then fit into our ideal routine schedule.
    - Appropriate notifications will keep us reminded about the need of the hour task alone; not the entire day plan which makes us dizzy

# Meridian construction plan:

    - Meridian API will focus on collecting user's ideal schedule and their task list using Fast API routers and CRUD endpoints.
    - SQLAlchemy(async) will be used to design the PostgreSQL data models and Pydantic schemas will be used to validate and serialize the data for the user.
    - Then it will identify best possible mapping of given tasks against the schedule for any given day and will be scheduled in the user's Google calendar.
    - Celery workers combined with Redis will asynchronously check for the schedule to trigger appropriate notification to the user.

Schedule Example:
Weekday schedule template: 
        7:00 AM - 11:30 AM - Office meetings & off-shore co-ordiantion calls
        12:00 PM - 3:00 PM - Onshore meetings and core work
        4:00 PM - 5:00 PM - End of the day closures
        5:00 PM - 6:30 PM - Family time
        6:30 PM - 8:00 PM - Health time
        9:00 PM - 9:30 PM - Kids time
Note: Weekend schedule template would contain extra blocks for Finance and Social life.

# Meridian API Architecture:

Layered Architecture; each layer is separated to handle its own role alone.

Router - Handles CRUD endpoints
Schemas - Request validation and Response serialization
Services - Business logic, DB operations, Redis operations
Models - Table definitions and constraints
Celery - Asynchronous task handler

Flow of a ideal request:
========================
User -> FastAPI router -> Schemas -> Services -> Models(SQLAlchemy) -> PostgreSQL -> Schemas -> Router -> User