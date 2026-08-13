# RECALL

### Keeping Every Commitment Within Reach

> A desktop application designed to organize orders, monitor delivery deadlines, recognize customers, manage discounts, collect feedback, and turn stored records into useful insights.

---

## THE IDEA

Every order starts with a commitment.

A customer places an order.  
A delivery date is set.  
A customer may return.  
Feedback arrives.  
And over time, keeping track of everything can become difficult.

**Recall brings these details together in one focused desktop application.**

It helps keep orders organized, deadlines visible, customer history recognizable, discounts manageable, and feedback meaningful.

---

## WHAT RECALL DOES

### ORDER ENTRY

Recall provides a structured space for recording orders.

The user enters:

- Customer Name
- Username / Page ID
- Product Name
- Order Date
- Delivery Date

But Order Entry does more than collect information.

While entering an order, Recall also:

- Checks whether the customer is new or returning
- Calculates the remaining delivery days
- Checks discount eligibility
- Displays the applicable discount
- Saves the completed order

---

### DELIVERY AWARENESS

Recall interprets the delivery date instead of simply storing it.

Depending on the remaining time, an order can be shown as:

- Due Today
- Due Tomorrow
- Due Soon
- Upcoming Delivery
- Scheduled

The dashboard also contains an **Attention Indicator**.

Orders with **0–3 days remaining** are marked as needing attention.

---

### CUSTOMER RECOGNITION

When a username is entered, Recall searches the existing order records.

It identifies the customer as:

- **New Customer**
- **Returning Customer**

This information is also used by the discount system.

---

### DISCOUNT MANAGEMENT

Discounts can be controlled from the Settings section.

The user can:

- Enable or disable discounts
- Enter a discount percentage
- Apply discounts to new customers
- Apply discounts to returning customers
- Apply discounts to both customer types

The Order Entry page automatically checks these settings and displays the applicable discount.

---

### CUSTOMER FEEDBACK

Recall allows customer feedback to be recorded through a dedicated Feedback section.

It stores:

- Customer Name
- Username / Page ID
- Appreciated Area
- Improvement Needed

The feedback is later analyzed to identify common patterns.

---

### INSIGHTS

Recall turns stored records into simple business insights.

It shows:

- Total Orders
- New Customers
- Returning Customers
- Most Ordered Product
- Most Appreciated Area
- Common Improvement
- Monthly Order Activity
- Highest Order Month

The purpose is not only to store information, but to make that information easier to understand.

---

# HOW RECALL WORKS

```text
                         ┌─────────────┐
                         │   RECALL    │
                         └──────┬──────┘
                                │
                                ▼
                     ┌──────────────────┐
                     │    ORDER ENTRY   │
                     └────────┬─────────┘
                              │
             ┌────────────────┼────────────────┐
             ▼                ▼                ▼
      ┌────────────┐   ┌────────────┐   ┌────────────┐
      │  CUSTOMER  │   │ DELIVERY   │   │  DISCOUNT  │
      │   CHECK    │   │ CALCULATION│   │   CHECK    │
      └────────────┘   └────────────┘   └────────────┘
             │                │                │
             └────────────────┼────────────────┘
                              ▼
                     ┌──────────────────┐
                     │   SAVE THE ORDER │
                     └────────┬─────────┘
                              │
                              ▼
                     ┌──────────────────┐
                     │   JSON STORAGE   │
                     └────────┬─────────┘
                              │
                              ▼
                ┌──────────────────────────┐
                │     RECALL PROCESSES     │
                └────────────┬─────────────┘
                             │
              ┌──────────────┼──────────────┐
              ▼              ▼              ▼
        ┌──────────┐   ┌──────────┐   ┌──────────┐
        │  ALERTS  │   │ FEEDBACK │   │ INSIGHTS │
        └──────────┘   └──────────┘   └──────────┘
ORDER ENTRY FLOW
                         ORDER ENTRY
                              │
             ┌────────────────┼────────────────┐
             ▼                ▼                ▼
      Customer Check    Delivery Check    Discount Check
             │                │                │
             ▼                ▼                ▼
       New / Returning   Days Remaining    Eligible / Not
             │                │                │
             └────────────────┼────────────────┘
                              ▼
                         Save Order
                              │
                              ▼
                        orders.json
Customer Check

Recall compares the entered username with existing order records.

If the username already exists:

Returning Customer

Otherwise:

New Customer

Delivery Calculation

Recall compares the entered delivery date with today's date and calculates the remaining days.

Discount Check

Recall reads settings.json and checks:

Is the discount enabled?
What percentage is set?
Which customer type is eligible?

The result is displayed directly in Order Entry.

Save Order

After the required information is entered, the order is stored in orders.json.

DELIVERY ALERT FLOW
Delivery Date
      │
      ▼
Compare With Today's Date
      │
      ▼
Calculate Remaining Days
      │
      ├── 0 days ───────► Due Today
      │
      ├── 1 day ────────► Due Tomorrow
      │
      ├── 2–3 days ─────► Due Soon
      │
      ├── 4–7 days ─────► Upcoming Delivery
      │
      └── 8+ days ──────► Scheduled

The Attention Indicator focuses on the most urgent orders.

0–3 days remaining
       │
       ▼
⚠ Need Attention

If there are no urgent orders:

✓ All Orders on Track

If there are no orders at all:

No Orders for Attention
CUSTOMER AND DISCOUNT FLOW
                    Username Entered
                           │
                           ▼
                    Search Orders
                           │
                  ┌────────┴────────┐
                  ▼                 ▼
           New Customer      Returning Customer
                  │                 │
                  └────────┬────────┘
                           ▼
                    Check Settings
                           │
                           ▼
                  Discount Enabled?
                    │          │
                   Yes         No
                    │          │
                    ▼          ▼
              Check Type    No Discount
                    │
                    ▼
              Show Discount
FEEDBACK FLOW
Customer Feedback
        │
        ▼
┌──────────────────────┐
│ Appreciated Area     │
│ Improvement Needed   │
└──────────┬───────────┘
           │
           ▼
     feedback.json
           │
           ▼
    Feedback Analysis
           │
      ┌────┴────┐
      ▼         ▼
Most Appreciated   Common
     Area        Improvement
INSIGHTS FLOW
                 Stored Records
                       │
             ┌─────────┴─────────┐
             ▼                   ▼
        orders.json        feedback.json
             │                   │
             ▼                   ▼
       Order Analysis      Feedback Analysis
             │                   │
             └─────────┬─────────┘
                       ▼
                    INSIGHTS
                       │
        ┌──────────────┼──────────────┐
        ▼              ▼              ▼
     Orders        Customers       Feedback
        │              │              │
        ▼              ▼              ▼
   Monthly Data   New/Returning   Common Patterns
APPLICATION STRUCTURE

Recall follows a simple three-layer structure:

┌─────────────────────────────────────┐
│             INTERFACE               │
│             Tkinter GUI             │
└──────────────────┬──────────────────┘
                   │
                   ▼
┌─────────────────────────────────────┐
│              LOGIC                  │
│          Python Functions            │
│                                     │
│ Validation • Calculations •         │
│ Customer Checking • Analysis        │
└──────────────────┬──────────────────┘
                   │
                   ▼
┌─────────────────────────────────────┐
│             STORAGE                 │
│             JSON Files              │
│                                     │
│ orders.json                         │
│ feedback.json                       │
│ settings.json                       │
└─────────────────────────────────────┘
TECHNOLOGY USED
Technology	Purpose
Python	Main programming language and application logic
Tkinter	Graphical User Interface
JSON	Local data storage
datetime	Date and delivery calculations
os	File and folder path management
try-except	Error handling
DATABASE

No database is used in Recall.

The application uses JSON files as local storage.

It does not use:

MySQL
SQLite
MongoDB
PostgreSQL
Any external database system

This keeps the project lightweight and simple to run.

DATA STORAGE

The project uses three JSON files:

data/
├── orders.json
├── feedback.json
└── settings.json
orders.json

Stores order records such as:

Customer name
Username
Product name
Order date
Delivery date
Customer status
feedback.json

Stores:

Customer name
Username
Appreciated area
Improvement suggestion
settings.json

Stores application settings such as:

Discount enabled / disabled
Discount percentage
Eligible customer type
DATA STRUCTURES

Recall mainly uses lists and dictionaries.

One Order → Dictionary
order = {
    "customer_name": "Example Customer",
    "username": "example_user",
    "product_name": "Example Product",
    "order_date": "10-08-26",
    "delivery_date": "15-08-26"
}

A dictionary stores information using:

key → value

For example:

"customer_name" → "Example Customer"
Multiple Orders → List of Dictionaries
orders = [
    order1,
    order2,
    order3
]

So the basic structure is:

List
 │
 ├── Dictionary → Order 1
 ├── Dictionary → Order 2
 └── Dictionary → Order 3
HOW JSON AND PYTHON WORK TOGETHER

Recall uses:

json.load()

Converts data from a JSON file into Python data.

JSON
  ↓
json.load()
  ↓
Python
json.dump()

Converts Python data and saves it into a JSON file.

Python
  ↓
json.dump()
  ↓
JSON

The complete cycle is:

JSON FILE
    │
    │ json.load()
    ▼
PYTHON DATA
    │
    ├── Lists
    ├── Dictionaries
    ├── Calculations
    ├── Searching
    └── Analysis
    │
    │ json.dump()
    ▼
JSON FILE
IMPORTANT PYTHON CONCEPTS USED

The project demonstrates:

Variables
Functions
Lists
Dictionaries
Loops
Conditional statements
File handling
JSON handling
Exception handling
Date and time processing
GUI programming
Basic data analysis
IMPORTANT FUNCTIONS AND MODULES
Function / Module	Purpose
json.load()	Reads JSON data into Python
json.dump()	Writes Python data into JSON
datetime	Handles dates
datetime.strptime()	Converts text into a date
datetime.today()	Gets today's date
os.path.join()	Creates file paths safely
os.makedirs()	Creates the data folder if needed
try-except	Prevents the program from crashing on expected errors
mainloop()	Keeps the Tkinter application running
PROJECT STRUCTURE
Recall/
│
├── main.py
│
├── data/
│   ├── orders.json
│   ├── feedback.json
│   └── settings.json
│
└── README.md
main.py

Contains the main application:

GUI
Navigation
Order Entry
Delivery Alerts
Feedback
Insights
Settings
Calculations
File handling
data/

Contains the application's local data.

README.md

Contains project documentation.

ERROR HANDLING

Recall uses try-except blocks when working with files and dates.

For example:

try:
    with open(file_path, "r") as file:
        data = json.load(file)

except FileNotFoundError:
    data = []

This prevents the application from crashing when a file does not exist or contains invalid JSON.

The program can then continue with an appropriate default value.

FILE PATH HANDLING

Recall uses Python's os module to create paths based on the application's location.

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")

This helps the application find its data folder correctly even when the project is moved to another location.

RUNNING THE PROJECT
Requirements
Python 3.x
Tkinter
Run
python main.py

The Recall desktop application will open through Tkinter.

WHY JSON INSTEAD OF A DATABASE?

JSON was selected because Recall is a lightweight local desktop application.

It allows the project to:

Store structured data
Read and update records easily
Work without a database server
Keep the project simple
Make the stored data easy to inspect

For a larger multi-user system, a database would be more suitable.

PROJECT HIGHLIGHTS

Order Management
Record and organize customer orders.

Delivery Tracking
Calculate remaining delivery days and highlight urgent orders.

Customer Recognition
Identify new and returning customers automatically.

Discount Management
Control discount availability and eligibility.

Feedback Collection
Capture customer appreciation and improvement suggestions.

Insights
Turn stored order and feedback data into meaningful summaries.

Local Storage
Keep application data organized through JSON files.

Desktop GUI
Provide the complete experience through Tkinter.

RECALL IN ONE VIEW
┌──────────────────────────────────────────┐
│                  RECALL                  │
│                                          │
│            ORDER ENTRY                   │
│                 │                        │
│      ┌──────────┼──────────┐             │
│      ▼          ▼          ▼             │
│  CUSTOMER    DELIVERY   DISCOUNT         │
│   CHECK      CHECK       CHECK           │
│      └──────────┼──────────┘             │
│                 ▼                        │
│            SAVE ORDER                    │
│                 │                        │
│                 ▼                        │
│            JSON STORAGE                  │
│                 │                        │
│       ┌─────────┼─────────┐              │
│       ▼         ▼         ▼              │
│     ALERTS   FEEDBACK   INSIGHTS         │
│       │         │         │              │
│       └─────────┼─────────┘              │
│                 ▼                        │
│          BETTER DECISIONS                │
└──────────────────────────────────────────┘
THE CORE IDEA

Recall is not simply about storing information.

It is about making stored information useful.

Orders
   ↓
Records
   ↓
Calculations
   ↓
Alerts & Recognition
   ↓
Feedback & Analysis
   ↓
Insights

Orders become records.
Dates become alerts.
Customer history becomes recognition.
Feedback becomes patterns.
Records become insights.

FINAL THOUGHT

Recall was built around one simple principle:

Important commitments should never be forgotten.

From the first order entry to the final insight, Recall keeps the information connected, visible, and within reach.

AUTHOR

Maria Tasnim

RECALL

Every order remembered. Every commitment within reach.

I told you to give me in one go so i can copy paste
# RECALL

### Keeping Every Commitment Within Reach

Recall is a Python-based desktop application designed to organize customer orders, track delivery deadlines, manage customer feedback, and turn stored information into useful business insights.

Instead of keeping order details scattered across notes or files, Recall brings everything together in one simple interface.

## What Recall Does

Recall helps manage the complete order journey:

Customer information
→ Order entry
→ Customer recognition
→ Discount checking
→ Delivery tracking
→ Due alerts
→ Feedback collection
→ Business insights

## Core Features

### Order Entry

Users can enter:

- Customer name
- Username / Page ID
- Product name
- Order date
- Delivery date

Recall automatically:

- Detects whether the customer is new or returning
- Calculates the remaining delivery days
- Checks whether a discount is available
- Applies the discount settings configured by the user
- Saves the order information for future use

### Delivery Tracking

Recall calculates the time remaining until delivery.

Orders can appear as:

- Due Today
- Due Tomorrow
- Due Soon
- Upcoming Delivery
- Scheduled Delivery

A delivery progress indicator also shows how close an order is to its delivery date.

### Attention Indicator

The dashboard automatically checks upcoming deliveries.

If an order has 0–3 days remaining:

⚠ Order Needs Attention

If no order requires attention:

✓ All Orders on Track

If there are no orders:

No Orders for Attention

### Discount System

Discounts can be configured from Settings.

The user can:

- Enable or disable discounts
- Enter a discount percentage
- Choose New Customers
- Choose Returning Customers
- Choose Both

The discount information is then shown during order entry.

### Customer Recognition

Recall checks the username against previous order records.

If the username already exists:

Returning Customer

If the username is not found:

New Customer

### Feedback

The Feedback section allows users to record:

- Customer name
- Username / Page ID
- Appreciated area
- Improvement feedback

Recall also checks whether the customer exists in the order records before saving feedback.

### Insights

The Insights section turns stored order and feedback data into a simple business summary.

It shows:

- Total orders
- New customers
- Returning customers
- Most ordered product
- Most appreciated area
- Common improvement
- Recent monthly order activity
- Month with the highest number of orders

This allows the user to understand customer behavior and order patterns without manually counting the records.

## Application Flow

```text
                    RECALL
                       |
                       v
                 Order Entry
                       |
        +--------------+--------------+
        |              |              |
        v              v              v
 Customer Check   Delivery Check   Discount Check
        |              |              |
        +--------------+--------------+
                       |
                       v
                 Save Order
                       |
                       v
                orders.json
                       |
          +------------+------------+
          |                         |
          v                         v
      Due Alerts                 Insights
          |                         |
          v                         v
 Delivery Status          Business Information
          |
          v
      Attention
       Indicator


Feedback Entry
      |
      v
Customer Verification
      |
      v
feedback.json
      |
      v
Insights


Settings
      |
      v
settings.json
      |
      v
Discount Configuration
How Data Is Stored

Recall does not use a database.

Instead, it uses JSON files for lightweight local data storage.

Recall/
│
├── main.py
│
├── data/
│   ├── orders.json
│   ├── feedback.json
│   └── settings.json
│
└── README.md
orders.json

Stores customer order information.

One order is stored as a Python dictionary.

Multiple orders are stored as a list of dictionaries.

Example structure:

[
    {
        "customer_name": "Example Customer",
        "username": "example_user",
        "product_name": "Example Product",
        "order_date": "10-08-26",
        "delivery_date": "15-08-26",
        "customer_status": "New Customer"
    }
]
feedback.json

Stores customer feedback such as appreciated areas and improvement suggestions.

settings.json

Stores application settings such as:

{
    "discount_active": true,
    "discount_percentage": 20,
    "customer_type": "new"
}
Technologies Used
Component	Technology
Programming Language	Python
GUI	Tkinter
Data Storage	JSON
Database	Not used
Date Handling	datetime
File Management	os
Error Handling	try-except
Python Concepts Used

Recall demonstrates several fundamental Python concepts:

Variables
Functions
Lists
Dictionaries
Loops
Conditional statements
try-except
File handling
JSON handling
Lambda functions
Tkinter widgets
Event handling
Date calculations
String formatting
Important Python Functions
json.load()

Reads JSON data from a file and converts it into Python data.

orders = json.load(file)

JSON → Python

json.dump()

Converts Python data into JSON and saves it to a file.

json.dump(data, file, indent=4)

Python → JSON

datetime

Used for calculating delivery dates and remaining days.

os

Used to create reliable file and folder paths.

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")

This allows the application to find its data folder even when the project is moved to another location.

try-except

Used to prevent the application from crashing when a file is missing or contains invalid data.

Why JSON Instead of a Database?

JSON was chosen because Recall is a small desktop application with relatively simple data.

Using JSON makes the project:

Lightweight
Easy to understand
Easy to transfer
Easy to inspect
Suitable for a small amount of local data
Simple to implement using Python's built-in libraries

A database would be more suitable for a larger application with many users, large amounts of data, or advanced querying requirements.

Project Structure
Recall
│
├── main.py
│
├── data
│   ├── orders.json
│   ├── feedback.json
│   └── settings.json
│
└── README.md
main.py

Contains the main application logic, GUI, functions, calculations, file handling, and navigation.

data/

Contains the JSON files used to store application information.

How Recall Works Internally
User Input
    |
    v
Tkinter GUI
    |
    v
Python Functions
    |
    +---- Customer Checking
    |
    +---- Delivery Calculation
    |
    +---- Discount Checking
    |
    +---- Feedback Validation
    |
    +---- Insight Calculation
    |
    v
JSON Files
    |
    +---- orders.json
    +---- feedback.json
    +---- settings.json
Design

Recall uses a warm, minimal interface inspired by paper and coffee tones.

The interface contains:

Welcome screen
Dashboard
Sidebar navigation
Order Entry
Due Alerts
Insights
Feedback
Settings

The design focuses on keeping the application simple while making important information easy to notice.

Author

Maria Tasnim

Project Purpose

Recall was created as a practical Python desktop application that demonstrates how a simple application can combine GUI design, file handling, data structures, JSON storage, date calculations, customer recognition, feedback analysis, and business insights in one system.

The main idea behind Recall is simple:

Remember the order.
Track the commitment.
Understand the customer.
Improve the next one.
how do i cpy pste all this in one go?

Yes. The easiest way:

Click inside the big code box above.
Press Ctrl + A — this selects everything inside the box.
Press Ctrl + C — copies it.
Go to your GitHub repository.
Open README.md → click the pencil/Edit button.
Press Ctrl + A to remove the existing README content.
Press Ctrl + V to paste everything.
Click Commit changes.

Important: Copy only the content inside the large box, starting from:

# RECALL

and ending with:

Improve the next one.

Don't copy the markdown at the top or at the bottom.
