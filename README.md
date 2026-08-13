# RECALL

### Keeping Every Commitment Within Reach

> A desktop application designed to organize orders, monitor delivery deadlines, understand customer feedback, manage discounts, and turn everyday records into useful insights.

---

## ✦ THE STORY

Every order starts with a promise.

A customer places an order.  
A delivery date is set.  
A customer may return.  
Feedback arrives.  
And over time, all of those details become difficult to keep track of.

**Recall was created around one simple idea:**

**Important commitments should not be forgotten.**

Instead of keeping order information, delivery dates, customer history, feedback, and discount settings scattered around, Recall brings them together into one focused desktop application.

---

## ✦ WHAT RECALL DOES

### ORDER ENTRY

Recall provides a structured space for recording every order.

The user enters:

- Customer name
- Username / Page ID
- Product name
- Order date
- Delivery date

But Order Entry does more than collect information.

While entering an order, Recall also:

- Checks whether the customer is new or returning
- Calculates the remaining delivery days
- Checks discount eligibility
- Shows the available discount
- Saves the completed order to the order records

---

### DELIVERY AWARENESS

Recall doesn't simply store a delivery date.

It interprets it.

Depending on how close the delivery is, an order can appear as:

**Due Today**  
**Due Tomorrow**  
**Due Soon**  
**Upcoming Delivery**  
**Scheduled**

The dashboard also provides an **Attention Indicator** so approaching deliveries are immediately noticeable.

Orders with **0–3 days remaining** are considered to need attention.

---

### CUSTOMER FEEDBACK

A customer's experience should not disappear after an order is completed.

Recall records:

- Customer name
- Username / Page ID
- Appreciated area
- Improvement suggestions

The collected feedback can then be analyzed to discover recurring patterns.

---

### DISCOUNT CONTROL

Discounts can be managed directly from the Settings section.

The user can:

- Enable or disable discounts
- Enter a discount percentage
- Select new customers
- Select returning customers
- Apply discounts to both customer types

The Order Entry page then checks the saved settings and displays the applicable discount.

---

### INSIGHTS

Stored information becomes more useful when it tells a story.

Recall summarizes the collected data into:

- Total orders
- New customers
- Returning customers
- Most ordered product
- Most appreciated area
- Common improvement suggestion
- Monthly order activity

The goal is not just to store records.

**The goal is to understand them.**

---

# ✦ HOW RECALL WORKS

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

✦ THE DATA

Recall uses local JSON files instead of a database.

The data is stored inside a dedicated data folder:

data/
├── orders.json
├── feedback.json
└── settings.json
orders.json

Stores customer and order records.

feedback.json

Stores customer feedback and improvement suggestions.

settings.json

Stores application settings, including discount preferences.
