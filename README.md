 Elevvo - Expense Tracker & Inventory System

Python CLI based projects for Elevvo Internship Task 1.

This repository contains two separate Python projects built using Object Oriented Programming (OOP).

---

1. Expense Tracker - `expense_tracker.py`

A simple CLI tool to manage daily expenses.

 Features
- Add new expense (Food, Transport, Shopping, etc.)
- View all expenses
- View total spending
- Data saved automatically

 How To Run
python expense_tracker.py

---

 2. Inventory Management System - `inventory_system.py`

A Python OOP based system to manage products, stock and low-stock alerts.

 Features
- Add and remove stock with validation
- Price and stock cannot be negative (using @property)
- Low stock alert system
- Perishable products with expiry date support
- Clean product display using __str__ method

 Classes Used

1. Product Class**
Main class for all products.
- Attributes: name, price, stock, low_stock_threshold
- Methods: add_stock(), remove_stock(), is_low_stock()

2. PerishableProduct Class (Inheritance)**
Inherits from Product class.
- Extra Attribute: expiry_date
- Example: Milk, Fruits, Medicines

How To Run
python inventory_system.py

 Demo Example
Product: Laptop | Price: $1200.00 | Stock: 10
Product: Milk | Price: $2.50 | Stock: 4 | Expiry Date: 2026-05-10

---

 Concepts Covered
- Object Oriented Programming (OOP)
- Inheritance
- Property Decorator & Validation
- Error Handling

 Tech Used
Python

 Made By
Maham - Data Analytics Student | Elevvo Intern
