# The Eye API

## Story

You work in an organization that has multiple applications serving websites, but it's super hard to analyze user behavior in those, because you have no data.

In order to be able to analyze user behavior (pages that are being accessed, buttons that are being clicked, forms that are being submitted, etc..), your team realized you need a service that aggregates that data.

You're building "The Eye", a service that will collect those events from these applications, to help your org making better data-driven decisions.

## How to run
>**Note**: you should have docker-compose previously installed on your machine, [if you don't follow this tutorial](https://docs.docker.com/compose/install/).

Open a terminal inside the project folder and run the following command:

 - `docker-compose build` -- Only necessary when you need a new build, like the first time you are running
 - `docker-compose up`
 - `docker-compose exec app flask db upgrade head` -- Only necessary first time running or if you a new is launch migration. 

## Folder Structure
Following is the main folder and files structure and their function:
```
the_eye/
|
└───scripts/ -> Group project scripts
└───the_eye/ -> Where the api code is located
│   └───controller/ -> Controller of the API routes
│   └───migration/  -> Migration related files
│   └───models/     -> Python database definition models
│   └───schemas/    -> Input/Output validation schemas
│   └───setting/    -> App configuration files
│   └───views/      -> API routes definition
│   └───decorators.py -> Define decorators
│   └───app.py -> Main file, runs de application
│   └───Dockerfile -> Docker difinitions
│   └───requirements.txt -> Project requirements definition 
└─── docker-compose.yml -> Docker compose definitions
└─── README.md -> This file
```

## Authentication Process

On The Eye API, we receive events from other applications, in order to validate if the applications have access to the eye. Each application has its API token (UUID4) that validates them as a partner of the eye. This token should be sent on the authentication header field for each request. 

## Schemas Validations
The application works with a large volume of data to be analyzed for a data team in the future. Since the main point that the application must guarantee is the consistency of the data, I developed a rigorous scheme validation the events to be inserted.

To validate the events I used the Pydantic library to help define schemas input and output validations, that are executed in the route decorator and are centralized in the `the_eye/the_eye/schemas/` folder.

The input templates limit all string fields to the size, to avoid errors during database insertion and oversized JSON columns. I also defined validation for fields that I saw necessary as you can see in the code.

The most complex validation was the event validation since each event has a category, each category has linked names and each category name has a different data field structure. Given that, I first defined an enum called `EventCategory` that stores all the enums accepted by the application and is used to validate the `category` field of the events.
 
Then I created an enum of names for each category present in the `EventCategory` that will be imported to execute the `name` field validation of an event, so it must follow a strict name pattern, which I defined as follows:
*"\<category in camel case\>" + "NamesEnum"*
Example:
*PageInteractionNamesEnum*

And finally, I defined a Model Class that is imported when validating the `data` field, which follows the following pattern:
"\<category in camel case\>" + "\<name in camel case\>" + "Data"*
Example:
*PageInteractionCtaClickData*

### How to add a new event:

 1. Add the event category on the `EventCategory` enum -- at `schemas/enums.py`
 2. Create a new name's enum following the naming pattern explained above and add all names possible for the category to which they belong, -- at `schemas/enums.py`
 3. Create a model class for data validation following the naming pattern explained above

## Database Definitions
To make the application possible I have defined two tables. The first one is the **Partner** table that keeps all the partner information and the second one is the **Event** table that keeps all events.
  
For keeping track of the modifications made to the database structure I am using migrations. 
### Partner Table
The Partner table is a table that saves the name and the API token of each partner The Eye API has. This table has one index column that is the API token in order to find the partner faster during the authentication process.

| id | name | api_token|
|----|------|----------|
|Integer|String|UUID|

### Event table
 The Event saves all events sent to The Eye API, on their structure we have all the fields of the events and an extra column the `partner_id` a Partner table foreign key that saves which partner added that event. We have defined three indexes for this table, the `category`, `name`, and `session_id` for the data team to query the information faster.
 
| id | session_id | category | name | data | timestamp | partner_id
|----|-------------|------------|-------|-------|--------------|---
|Integer|UUID|String|String|Json|Datetime|Integer -- ForeignKey of Partner Id

### Migration
We are using Flask-Migrate to manage our migrations. If you need to make a new migration after altering the model inside `the_eye/the_eye/models` just run the project via docker-compose, open a terminal at the project root and run the following commands:

```bash
docker-compose exec app flask db migrate -m '<MENSAGEM DA MIGRACAO>'
docker-compose exec app flask db upgrade head
```

