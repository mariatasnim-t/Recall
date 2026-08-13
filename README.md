# RECALL

### Keeping Every Commitment Within Reach

Recall is a Python-based desktop application designed to bring customer orders, delivery tracking, discounts, feedback, and business insights into one organized workspace.

It turns everyday order records into a simple story of what was ordered, what needs attention, what customers liked, and what can be improved.

## What Recall Does

### ➜Order Entry

The starting point of every order.

Customer name, username, product, order date, and delivery date are entered and stored. Recall also identifies whether the customer is new or returning, checks available discounts, and calculates the delivery status.

### ➜Delivery Tracking

Recall calculates the remaining days until each delivery and displays the current delivery progress.

### ➜Attention Indicator

Orders with 0–3 days remaining are automatically highlighted so important deliveries are easy to notice.

### ➜Discount System

Discounts can be enabled from Settings and assigned to new customers, returning customers, or both.

### ➜Customer Recognition

Recall compares the entered username with previous orders to identify returning customers.

### ➜Feedback

Customer feedback is recorded and later used to identify the most appreciated areas and common improvement suggestions.

### ➜Insights

Stored order and feedback data are transformed into a simple overview of customer activity, popular products, and monthly order patterns.

## Application Flow

```text
                         RECALL
                           |
          +----------------+----------------+
          |                |                |
          v                v                v
     ORDER ENTRY      DUE ALERTS       FEEDBACK
          |                |                |
          v                v                v
   Customer Check     Delivery Check   Customer Check
   Discount Check     Attention        Save Feedback
   Delivery Check          |                |
          |                |                |
          v                v                v
     orders.json      Attention       feedback.json
                           |
                           +--------+
                                    |
                                    v
                               INSIGHTS
                                    |
                                    v
                          Business Overview
```

## ➜ How Order Entry Works

```text
User enters order
        |
        v
Customer username checked
        |
        +------> New Customer
        |
        +------> Returning Customer
        |
        v
Discount settings checked
        |
        v
Delivery date calculated
        |
        v
Order saved
        |
        v
orders.json
```

## ➜ How Due Alerts Work

```text
Delivery Date
      |
      v
Calculate Remaining Days
      |
      +---- 0 days ----> Due Today
      |
      +---- 1 day -----> Due Tomorrow
      |
      +---- 2–3 days --> Due Soon
      |
      +---- 4–7 days --> Upcoming
      |
      +---- 8+ days ---> Scheduled
      |
      v
Attention Indicator Updated
```

## ➜ How Feedback Works

```text
Customer enters feedback
          |
          v
Customer verified
          |
          v
Feedback saved
          |
          v
feedback.json
          |
          v
Insights
          |
          +---- Most Appreciated Area
          |
          +---- Common Improvement
```

## ➜ How Insights Work

```text
orders.json
     |
     +---- Total Orders
     +---- New Customers
     +---- Returning Customers
     +---- Most Ordered Product
     +---- Monthly Orders
     |
     v
Business Overview


feedback.json
     |
     +---- Appreciated Areas
     +---- Improvement Suggestions
     |
     v
Customer Diary
```

## Data Storage

Recall uses lightweight JSON files instead of a database.

```text
Recall
 |
 +-- main.py
 |
 +-- data
      |
      +-- orders.json
      +-- feedback.json
      +-- settings.json
```

▪ orders.json stores order and customer information.

▪ feedback.json stores customer feedback.

▪ settings.json stores discount preferences and application settings.

## Technologies

```text
┌──────────────────┬─────────────────────────────────────────────┐
│ Python           │ Core programming language and logic         │
├──────────────────┼─────────────────────────────────────────────┤
│ Tkinter          │ Desktop GUI and application interface      │
├──────────────────┼─────────────────────────────────────────────┤
│ JSON             │ Local data storage                          │
├──────────────────┼─────────────────────────────────────────────┤
│ datetime         │ Date, delivery and progress calculations   │
├──────────────────┼─────────────────────────────────────────────┤
│ os               │ File and folder path management             │
├──────────────────┼─────────────────────────────────────────────┤
│ Lists & Dicts    │ Organizing orders, feedback and settings   │
├──────────────────┼─────────────────────────────────────────────┤
│ File Handling    │ Reading and writing JSON data               │
├──────────────────┼─────────────────────────────────────────────┤
│ try-except       │ Error handling and input protection         │
└──────────────────┴─────────────────────────────────────────────┘
```

## Design

Recall was intentionally designed not to feel like a typical business dashboard.

▪ Instead of a sharp, complex, data-heavy interface, the goal was to create something cozy, calm, and personal — almost like opening a warm little workspace where everything is already in its place.
The mood board focused on warmth, simplicity, paper, coffee, and earthy tones. Soft cream, coffee brown, khaki, and muted beige create a comfortable visual atmosphere while keeping the information easy to read.
Every element was kept clean and purposeful so that managing orders, deliveries, feedback, and insights feels organized without feeling overwhelming.

## Project Purpose

Recall was created from a simple observation: running a small business page can become surprisingly difficult when everything has to be handled at once.

▪ Orders come through messages, delivery dates have to be remembered, customers need to be recognized, discounts need to be managed, and feedback can easily get lost.
Over time, this can become messy, overwhelming, and easy to forget.
Recall was designed to bring these scattered responsibilities into one calm and organized space.
The vision was not to build another complicated business system, but to create a simple digital workspace that remembers the details, brings attention to what matters, and helps the seller understand their customers.

**Recall remembers the commitments, so the seller doesn't have to remember everything alone.**

## AUTHOR

### Maria Tasnim
