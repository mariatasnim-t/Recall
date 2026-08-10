import tkinter as tk
import json
from tkinter import messagebox
from datetime import datetime
entries = []
status_label = None


def get_attention_count():

    file_path = "data/orders.json"

    try:

        with open(file_path, "r") as file:
            orders = json.load(file)

    except (
        FileNotFoundError,
        json.JSONDecodeError
    ):

        return 0

    # No orders at all
    if not orders:
        return 0

    today = datetime.today().date()

    attention_count = 0

    for order in orders:

        try:

            delivery_date = datetime.strptime(
                order["delivery_date"].strip(),
                "%d-%m-%y"
            ).date()

        except (
            KeyError,
            ValueError
        ):

            continue

        remaining_days = (
            delivery_date - today
        ).days

        # Orders needing attention:
        # 0, 1, 2 or 3 days remaining
        if 0 <= remaining_days <= 3:

            attention_count += 1

    return attention_count
def update_attention_message():

    try:
        with open("data/orders.json", "r") as file:
            orders = json.load(file)

    except (FileNotFoundError, json.JSONDecodeError):
        orders = []

    # No orders exist
    if not orders:
        attention_text = "No orders for attention"

    else:
        today = datetime.today().date()
        count = 0

        for order in orders:

            try:
                delivery_date = datetime.strptime(
                    order["delivery_date"].strip(),
                    "%d-%m-%y"
                ).date()

            except (KeyError, ValueError):
                continue

            remaining_days = (
                delivery_date - today
            ).days

            # 3 days or less remaining
            if 0 <= remaining_days <= 3:
                count += 1

        if count == 0:

            attention_text = "✓ All Orders on Track"

        elif count == 1:

            attention_text = "⚠ 1 Order Need Attention"

        else:

            attention_text = (
                f"⚠ {count} Orders Need Attention"
            )

    attention.config(text=attention_text)
# main clrs
COCONUT_MILK = "#F0EDE5"
COFFEE_WITH_MILK = "#645A4E"
KHAKI = "#BEB9A9"
DARK_EARTH = "#5c4939"
PASTEL_GREY= "#D4CABC"
LIGHT_PAPER = "#FFF8E7"\

# main window
root = tk.Tk()
root.title("Recall")
root.geometry("1000x650")
root.configure(bg=COCONUT_MILK)

#welcome page
welcome_frame = tk.Frame(
    root,
    bg=COCONUT_MILK
)
welcome_frame.pack(fill="both", expand=True)
title = tk.Label(
    welcome_frame,
    text="R E C A L L",
    font=("Anton", 90, "bold"),
    fg=DARK_EARTH,
    bg=COCONUT_MILK
)
title.place(
    relx=0.5,
    rely=0.25,
    anchor="center"
)
tagline = tk.Label(
    welcome_frame,
    text='"KEEPING EVERY COMMITMENT WITHIN REACH"',
    font=("Canva Sans", 22,),
    fg=DARK_EARTH,
    bg=COCONUT_MILK
)
tagline.place(
    relx=0.5,
    rely=0.35,
    anchor="center"
)
welcome_label = tk.Label(
    welcome_frame,
    text="Welcome",
    font=("Segoe Script", 42),
    fg=DARK_EARTH,
    bg=COCONUT_MILK
)
welcome_label.place(
    relx=0.5,
    rely=0.52,
    anchor="center"
)
# dashboard
dashboard_frame = tk.Frame(
    root,
    bg=COCONUT_MILK
)
def open_recall():
    welcome_frame.pack_forget()
    dashboard_frame.pack(fill="both", expand=True)

open_button = tk.Button(
    welcome_frame,
    text="Click to Open",
    font=("Canva Sans", 12, "bold"),
    fg=COCONUT_MILK,
    bg=DARK_EARTH,
    activebackground=KHAKI,
    activeforeground=DARK_EARTH,
    relief="flat",
    padx=35,
    pady=10,
    cursor="hand2",
    command=open_recall
)
open_button.place(
    relx=0.5,
    rely=0.62,
    anchor="center"
)
heart = tk.Label(
    welcome_frame,
    text="♥",
    font=("Arial", 35),
    fg="#B8A69A",
    bg=COCONUT_MILK
)
heart.place(
    relx=0.5,
    rely=0.76,
    anchor="center"
)
# dash top

top_bar = tk.Frame(
    dashboard_frame,
    bg=COCONUT_MILK
)

top_bar.pack(
    fill="x",
    padx=30,
    pady=20
)
app_name = tk.Label(
    top_bar,
    text="Recall",
    font=("Georgia", 22, "bold"),
    fg=DARK_EARTH,
    bg=COCONUT_MILK
)

app_name.pack(side="left")

# Attention indicator

try:
    with open("data/orders.json", "r") as file:
        orders = json.load(file)

except (FileNotFoundError, json.JSONDecodeError):
    orders = []

today = datetime.today().date()

attention_count = 0

for order in orders:

    try:
        delivery_date = datetime.strptime(
            order["delivery_date"].strip(),
            "%d-%m-%y"
        ).date()

    except (KeyError, ValueError):
        continue

    remaining_days = (
        delivery_date - today
    ).days

    # 0, 1, 2 or 3 days remaining = attention
    if 0 <= remaining_days <= 3:
        attention_count += 1


if len(orders) == 0:

    attention_text = "No orders for attention"

elif attention_count > 0:

    attention_text = f"⚠ {attention_count} Order"

    if attention_count > 1:
        attention_text += "s"

    attention_text += " Need Attention"

else:

    attention_text = "✓ All Orders on Track"


attention = tk.Label(
    top_bar,
    text=attention_text,
    font=("Georgia", 12),
    fg=DARK_EARTH,
    bg=COCONUT_MILK,
    cursor="hand2"
)

attention.pack(
    side="right",
    padx=15
)

update_attention_message()

#body

body = tk.Frame(
    dashboard_frame,
    bg=COCONUT_MILK
)

body.pack(
    fill="both",
    expand=True,
    padx=30
)
# sidebar

sidebar = tk.Frame(
    body,
    bg=DARK_EARTH,
    width=220
)
sidebar.pack(
    side="left",
    fill="y",
    padx=(0,20)
)
# content

content_area = tk.Frame(
    body,
    bg=LIGHT_PAPER
)

content_area.pack(
    side="right",
    fill="both",
    expand=True
)
content_heart = tk.Label(
    content_area,
    text="♥",
    font=("Arial", 40),
    fg="#B8A69A",
    bg=LIGHT_PAPER
)

content_heart.place(
    relx=0.5,
    rely=0.5,
    anchor="center"
)
# page switch

def save_order():

    for entry in entries:
        if entry.get().strip() == "":
            messagebox.showwarning(
                "Missing Information",
                "Please fill all fields before saving."
            )
            return

    order = {}

    order["customer_name"] = entries[0].get()
    order["username"] = entries[1].get()
    order["product_name"] = entries[2].get()
    order["order_date"] = entries[3].get()
    order["delivery_date"] = entries[4].get()
    order["customer_status"] = status_label.cget("text")

    file_path = "data/orders.json"

    with open(file_path, "r") as file:
        data = json.load(file)

    data.append(order)

    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)

    messagebox.showinfo(
        "Success",
        "Order saved successfully!"
    )

    update_attention_message()

    # Clear fields for next order
    for entry in entries:
        entry.delete(0, tk.END)

    status_label.config(
        text="Customer Status: Checking..."
    )

    delivery_status_label.config(
        text="Delivery Status: Waiting..."
    )

    entries[0].focus()

def check_customer(username):

    file_path = "data/orders.json"

    with open(file_path, "r") as file:
        data = json.load(file)

    for order in data:
        if order["username"] == username:
            return "Returning Customer"

    return "New Customer"
def get_customer_discount_message(username):

    settings_file = "data/settings.json"

    try:

        with open(settings_file, "r") as file:
            settings = json.load(file)

    except (FileNotFoundError, json.JSONDecodeError):

        return "No discount available"

    # Discount system is disabled

    if not settings.get("discount_active", False):

        return "No discount available"


    # Get discount percentage

    try:

        discount = float(
            settings.get(
                "discount_percentage",
                0
            )
        )

    except (ValueError, TypeError):

        discount = 0
    # No actual discount

    if discount <= 0:

        return "No discount available"


    customer_status = check_customer(username)

    customer_type = settings.get(
        "customer_type",
        "all"
    )

    # New customers only

    if customer_type == "new":

        if customer_status == "New Customer":

            return f"{discount:g}% discount available for new customer"

        return "No discount available"

    # Returning customers only

    elif customer_type == "returning":

        if customer_status == "Returning Customer":

            return f"{discount:g}% discount available for returning customer"

        return "No discount available"

    # Both customers

    elif customer_type == "all":

        return f"{discount:g}% discount available for all customers"


    return "No discount available"

def calculate_progress(order_date, delivery_date):
    try:
        delivery = datetime.strptime(
            delivery_date.strip(),
            "%d-%m-%y"
        ).date()

        today = datetime.today().date()

        remaining_days = (delivery - today).days

        # Delivery is today
        if remaining_days <= 0:
            return 100

        # 20 or more days remaining = 0%
        if remaining_days >= 20:
            return 0

        # Closer delivery = higher progress
        progress = ((20 - remaining_days) / 20) * 100

        return round(progress)

    except Exception as e:
        print("Progress Error:", e)
        return 0
    # all your Due Alerts code here

def show_due_alerts():

    alert_card = tk.Frame(
        content_area,
        bg=PASTEL_GREY,
        padx=30,
        pady=15
    )

    alert_card.pack(
        pady=15,
        padx=15,
        fill="both",
        expand=True
    )

    title = tk.Label(
        alert_card,
        text="Due Alerts",
        font=("Georgia", 26, "bold"),
        fg=COCONUT_MILK,
        bg=COFFEE_WITH_MILK
    )

    title.pack(
        pady=15,
        fill="x"
    )

    # scroll area

    canvas_frame = tk.Frame(
        alert_card,
        bg=PASTEL_GREY
    )

    canvas_frame.pack(
        fill="both",
        expand=True
    )

    canvas = tk.Canvas(
        canvas_frame,
        bg=PASTEL_GREY,
        highlightthickness=0
    )

    canvas.pack(
        side="left",
        fill="both",
        expand=True
    )
    scrollbar = tk.Scrollbar(
        canvas_frame,
        orient="vertical",
        command=canvas.yview
    )
    scrollbar.pack(
        side="right",
        fill="y"
    )
    canvas.configure(
        yscrollcommand=scrollbar.set
    )
    order_container = tk.Frame(
        canvas,
        bg=PASTEL_GREY
    )
    canvas.create_window(
        (0, 0),
        window=order_container,
        anchor="nw"
    )
    order_container.bind(
        "<Configure>",
        lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")
        )
    )

    #load order
    file_path = "data/orders.json"

    try:
        with open(file_path, "r") as file:
            orders = json.load(file)

    except:
        orders = []

    today = datetime.today().date()

    active_orders = []

    # check active ordr

    for order in orders:

        try:
            delivery_date = datetime.strptime(
                order["delivery_date"].strip(),
                "%d-%m-%y"
            ).date()

        except:continue
        # Only show orders that have not passed
        if delivery_date >= today:

            remaining_days = (
                delivery_date - today
            ).days

            #urgency

            if remaining_days == 0:

                status_text = "⚠ Due Today"

            elif remaining_days == 1:

                status_text = "⚠ Due Tomorrow"

            elif remaining_days <= 3:

                status_text = (
                    f"⚠ Due Soon — "
                    f"{remaining_days} days remaining"
                )

            elif remaining_days <= 7:

                status_text = (
                    f"Upcoming Delivery — "
                    f"{remaining_days} days remaining"
                )

            else:

                status_text = (
                    f"Scheduled — "
                    f"{remaining_days} days remaining"
                )

            active_orders.append(
                (
                    order,
                    remaining_days,
                    status_text
                )
            )
    # sort urgent ordr frst

    active_orders.sort(
        key=lambda x: x[1]
    )

    if not active_orders:

        empty = tk.Label(
            order_container,
            text="No upcoming deliveries",
            font=("Georgia", 14, "italic"),
            fg=COCONUT_MILK,
            bg=COFFEE_WITH_MILK
        )
        empty.pack(
            pady=40
        )

        return
    # show ordr

    for order, remaining_days, status_text in active_orders:

        order_box = tk.Frame(
            order_container,
            bg=LIGHT_PAPER,
            padx=20,
            pady=15,
            relief="flat"
        )

        order_box.pack(
            fill="x",
            padx=10,
            pady=8
        )
        # Customer name
        customer_label = tk.Label(
            order_box,
            text=order["customer_name"],
            font=("Georgia", 16, "bold"),
            fg=DARK_EARTH,
            bg=LIGHT_PAPER
        )

        customer_label.pack(
            anchor="w",
            pady=(0, 5)
        )

        # Product name
        product_label = tk.Label(
            order_box,
            text=f"Product: {order['product_name']}",
            font=("Georgia", 11),
            fg=DARK_EARTH,
            bg=LIGHT_PAPER
        )

        product_label.pack(
            anchor="w",
            pady=2
        )

        # Username
        username_label = tk.Label(
            order_box,
            text=f"Username: {order['username']}",
            font=("Georgia", 11),
            fg=DARK_EARTH,
            bg=LIGHT_PAPER
        )

        username_label.pack(
            anchor="w",
            pady=2
        )

        # Delivery date
        delivery_label = tk.Label(
            order_box,
            text=f"Delivery Date: {order['delivery_date']}",
            font=("Georgia", 11),
            fg=DARK_EARTH,
            bg=LIGHT_PAPER
        )

        delivery_label.pack(
            anchor="w",
            pady=2
        )

        # Urgency status
        status_label = tk.Label(
            order_box,
            text=status_text,
            font=("Georgia", 11, "italic"),
            fg=DARK_EARTH,
            bg=LIGHT_PAPER
        )

        status_label.pack(
            anchor="w",
            pady=5
        )
        progress_percentage = calculate_progress(
            order["order_date"],
            order["delivery_date"]
        )

        progress = round(progress_percentage / 5)

        progress_text = tk.Label(
            order_box,
            text=f"Delivery Progress: {progress_percentage}%",
            font=("Georgia", 11, "italic"),
            fg=DARK_EARTH,
            bg=LIGHT_PAPER
        )

        progress_text.pack(
            anchor="w",
            pady=3
        )

        # Progress bar
        progress_bar = tk.Label(
            order_box,
            text="█" * progress + "░" * (20 - progress),
            font=("Georgia", 12),
            fg=DARK_EARTH,
            bg=LIGHT_PAPER
        )

        progress_bar.pack(
            anchor="w",
            pady=5
        )
def show_feedback_entry():

    feedback_card = tk.Frame(
        content_area,
        bg=PASTEL_GREY,
        padx=30,
        pady=15
    )

    feedback_card.pack(
        pady=15
    )

    title = tk.Label(
        feedback_card,
        text="Feedback Entry",
        font=("Georgia", 26, "bold"),
        fg=COCONUT_MILK,
        bg=COFFEE_WITH_MILK
    )

    title.pack(
        pady=15
    )

    fields = [
        "Customer Name",
        "Username / Page ID",
        "Appreciated Area"
    ]

    feedback_entries = []

    for field in fields:

        label = tk.Label(
            feedback_card,
            text=field,
            font=("Georgia", 12),
            fg=COCONUT_MILK,
            bg=COFFEE_WITH_MILK
        )

        label.pack(
            anchor="w",
            pady=(8, 2)
        )

        entry = tk.Entry(
            feedback_card,
            font=("Georgia", 12),
            width=35,
            bg=LIGHT_PAPER,
            relief="flat"
        )

        entry.pack(
            pady=5
        )

        feedback_entries.append(entry)

    # Improvement box
    label = tk.Label(
        feedback_card,
        text="Improvement Needed",
        font=("Georgia", 12),
        fg=COCONUT_MILK,
        bg=COFFEE_WITH_MILK
    )

    label.pack(
        anchor="w",
        pady=(8, 2)
    )

    improvement_box = tk.Text(
        feedback_card,
        font=("Georgia", 12),
        width=35,
        height=4,
        bg=LIGHT_PAPER,
        relief="flat"
    )

    improvement_box.pack(
        pady=5
    )

    # Save feedback
    def save_feedback():

        # Check if all fields are filled
        if any(
            entry.get().strip() == ""
            for entry in feedback_entries
        ):

            messagebox.showwarning(
                "Missing Information",
                "Please fill all fields before saving."
            )

            return

        # Get username
        username = feedback_entries[1].get().strip()

        # Check whether customer exists
        orders_file = "data/orders.json"

        try:

            with open(orders_file, "r") as file:
                orders = json.load(file)

        except (
            FileNotFoundError,
            json.JSONDecodeError
        ):

            orders = []

        customer_exists = any(
            order.get("username", "").strip() == username
            for order in orders
        )

        # Customer does not exist
        if not customer_exists:

            messagebox.showwarning(
                "Customer Not Found",
                "This customer does not exist in the order records."
            )

            return

        # Check improvement feedback
        if improvement_box.get(
            "1.0",
            tk.END
        ).strip() == "":

            messagebox.showwarning(
                "Missing Information",
                "Please write improvement feedback."
            )

            return

        # Create feedback
        feedback = {

            "customer_name":
                feedback_entries[0].get().strip(),

            "username":
                username,

            "appreciated_area":
                feedback_entries[2].get().strip(),

            "improvement":
                improvement_box.get(
                    "1.0",
                    tk.END
                ).strip()

        }

        # Feedback file
        feedback_file = "data/feedback.json"

        try:

            with open(feedback_file, "r") as file:
                data = json.load(file)

        except (
            FileNotFoundError,
            json.JSONDecodeError
        ):

            data = []

        # Save feedback
        data.append(feedback)

        with open(feedback_file, "w") as file:

            json.dump(
                data,
                file,
                indent=4
            )

        messagebox.showinfo(
            "Success",
            "Feedback saved successfully!"
        )

        # Clear fields
        for entry in feedback_entries:

            entry.delete(
                0,
                tk.END
            )

        improvement_box.delete(
            "1.0",
            tk.END
        )

        feedback_entries[0].focus()

    # Move from Appreciated Area to Improvement box
    def move_to_improvement(event):

        improvement_box.focus_set()

        return "break"

    feedback_entries[2].bind(
        "<Return>",
        move_to_improvement
    )

    # Enter key navigation
    feedback_entries[0].bind(
        "<Return>",
        lambda event: feedback_entries[1].focus()
    )

    feedback_entries[1].bind(
        "<Return>",
        lambda event: feedback_entries[2].focus()
    )

    # Save Feedback button
    save_button = tk.Button(
        feedback_card,
        text="Save Feedback",
        font=("Georgia", 12, "bold"),
        fg=COCONUT_MILK,
        bg=DARK_EARTH,
        relief="flat",
        padx=30,
        pady=8,
        cursor="hand2",
        command=save_feedback
    )

    save_button.pack(
        pady=15
    )

def get_order_insights():

    file_path = "data/orders.json"

    try:
        with open(file_path, "r") as file:
            orders = json.load(file)

    except:
        orders = []


    total_orders = len(orders)

    returning_customers = 0
    new_customers = 0

    product_count = {}

    monthly_orders = {}

    for order in orders:

        # Customer status count
        if "Returning" in order.get("customer_status", ""):
            returning_customers += 1

        else:
            new_customers += 1


        # Most ordered product
        product = order.get(
            "product_name",
            "Unknown"
        )

        product_count[product] = product_count.get(
            product,
            0
        ) + 1


        # Monthly growth
        try:
            date = datetime.strptime(
                order["order_date"].strip(),
                "%d-%m-%y"
            )

            month = date.strftime("%B")

            monthly_orders[month] = monthly_orders.get(
                month,
                0
            ) + 1

        except:
            pass



    # Most ordered product
    if product_count:

        most_ordered_product = max(
            product_count,
            key=product_count.get
        )
        most_ordered_count = product_count[
            most_ordered_product
        ]

    else:

        most_ordered_product = "No Data"
        most_ordered_count = 0

    # Highest month from January to current month
    if monthly_orders:

        highest_month = max(
            monthly_orders,
            key=monthly_orders.get
        )

        highest_month_count = monthly_orders[
            highest_month
        ]

    else:

        highest_month = "No Data"
        highest_month_count = 0

    return {

        "total_orders": total_orders,

        "returning_customers": returning_customers,

        "new_customers": new_customers,

        "most_ordered_product": most_ordered_product,

        "most_ordered_count": most_ordered_count,

        "monthly_orders": monthly_orders,

        "highest_month": highest_month,

        "highest_month_count": highest_month_count

    }
def get_feedback_insights():

    file_path = "data/feedback.json"

    try:
        with open(file_path, "r") as file:
            feedbacks = json.load(file)

    except:
        feedbacks = []


    appreciated_count = {}
    improvement_count = {}

    for feedback in feedbacks:

        # Appreciated area count
        area = feedback.get(
            "appreciated_area",
            "Unknown"
        )

        appreciated_count[area] = appreciated_count.get(
            area,
            0
        ) + 1
        # Improvement count
        improvement = feedback.get(
            "improvement",
            "No suggestion"
        )

        improvement_count[improvement] = improvement_count.get(
            improvement,
            0
        ) + 1

    # Most appreciated area
    if appreciated_count:

        most_appreciated = max(
            appreciated_count,
            key=appreciated_count.get
        )

        appreciated_number = appreciated_count[
            most_appreciated
        ]

    else:

        most_appreciated = "No Data"
        appreciated_number = 0

    # Common improvement
    if improvement_count:

        common_improvement = max(
            improvement_count,
            key=improvement_count.get
        )

    else:

        common_improvement = "No Data"
    return {

        "most_appreciated": most_appreciated,

        "appreciated_number": appreciated_number,

        "common_improvement": common_improvement

    }
def get_growth_insights():

    order_data = get_order_insights()

    monthly_orders = order_data["monthly_orders"]


    month_names = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]
    current_month = datetime.today().month

    # Last 3 available months
    available_months = []

    for month_number in range(current_month):

        month = month_names[month_number]

        if month in monthly_orders:
            available_months.append(
                (
                    month,
                    monthly_orders[month]
                )
            )
    last_three = available_months[-3:]


    # Highest order growth from January to current month
    highest_month = "No Data"
    highest_count = 0

    for month_number in range(current_month):

        month = month_names[month_number]

        count = monthly_orders.get(
            month,
            0
        )

        if count > highest_count:
            highest_count = count
            highest_month = month

    return {
        "last_three": last_three,
        "highest_month": highest_month,
        "highest_count": highest_count
    }
def show_insights():

    insight_page = tk.Frame(
        content_area,
        bg=LIGHT_PAPER
    )

    insight_page.pack(
        fill="both",
        expand=True
    )
    title = tk.Label(
        insight_page,
        text="Your business story, remembered",
        font=("Georgia", 20, "bold"),
        fg=DARK_EARTH,
        bg=LIGHT_PAPER
    )

    title.pack(
        pady=(30,20)
    )

    top_frame = tk.Frame(
        insight_page,
        bg=LIGHT_PAPER
    )

    top_frame.pack(
        pady=10
    )

    # business overview
    overview_card = tk.Frame(
        top_frame,
        bg=PASTEL_GREY,
        width=330,
        height=220
    )
    overview_card.pack(
        side="left",
        padx=15
    )
    overview_card.pack_propagate(False)

    overview_title = tk.Label(
        overview_card,
        text="Business Overview",
        font=("Georgia", 16, "bold"),
        fg=DARK_EARTH,
        bg=PASTEL_GREY
    )
    overview_title.pack(
        pady=15
    )
    order_data = get_order_insights()


    overview_inner = tk.Frame(
        overview_card,
        bg=PASTEL_GREY
    )

    overview_inner.pack(
        pady=20
    )

    tk.Label(
        overview_inner,
        text=str(order_data["total_orders"]),
        font=("Georgia", 24, "bold"),
        fg=DARK_EARTH,
        bg=PASTEL_GREY
    ).grid(row=0, column=0, padx=15)

    tk.Label(
        overview_inner,
        text="Orders",
        font=("Georgia", 11),
        fg=DARK_EARTH,
        bg=PASTEL_GREY
    ).grid(row=1, column=0, padx=15)

    tk.Label(
        overview_inner,
        text=str(order_data["returning_customers"]),
        font=("Georgia", 24, "bold"),
        fg=DARK_EARTH,
        bg=PASTEL_GREY
    ).grid(row=0, column=1, padx=15)

    tk.Label(
        overview_inner,
        text="Returning\nCustomers",
        font=("Georgia", 11),
        fg=DARK_EARTH,
        bg=PASTEL_GREY
    ).grid(row=1, column=1, padx=15)

    tk.Label(
        overview_inner,
        text=str(order_data["new_customers"]),
        font=("Georgia", 24, "bold"),
        fg=DARK_EARTH,
        bg=PASTEL_GREY
    ).grid(row=0, column=2, padx=15)

    tk.Label(
        overview_inner,
        text="New\nCustomers",
        font=("Georgia", 11),
        fg=DARK_EARTH,
        bg=PASTEL_GREY
    ).grid(row=1, column=2, padx=15)

    # Customer diary
    diary_card = tk.Frame(
        top_frame,
        bg=PASTEL_GREY,
        width=280,
        height=220
    )
    diary_card.pack(
        side="left",
        padx=15
    )
    diary_card.pack_propagate(False)
    diary_title = tk.Label(
        diary_card,
        text="Customer Diary",
        font=("Georgia", 16, "bold"),
        fg=DARK_EARTH,
        bg=PASTEL_GREY
    )
    diary_title.pack(
        pady=15
    )
    feedback_data = get_feedback_insights()

    diary_inner = tk.Frame(
        diary_card,
        bg=PASTEL_GREY
    )

    diary_inner.pack(
        pady=10
    )

    tk.Label(
        diary_inner,
        text=f"Most Ordered Product → {order_data['most_ordered_product']}",
        font=("Georgia", 11),
        fg=DARK_EARTH,
        bg=PASTEL_GREY
    ).pack(
        pady=8
    )

    tk.Label(
        diary_inner,
        text=f"Most Appreciated Area → {feedback_data['most_appreciated']}",
        font=("Georgia", 11),
        fg=DARK_EARTH,
        bg=PASTEL_GREY
    ).pack(
        pady=8
    )

    tk.Label(
        diary_inner,
        text=f"Common Improvement → {feedback_data['common_improvement']}",
        font=("Georgia", 11),
        fg=DARK_EARTH,
        bg=PASTEL_GREY
    ).pack(
        pady=8
    )
    growth_card = tk.Frame(
        insight_page,
        bg=PASTEL_GREY,
        width=600,
        height=350
    )
    growth_card.pack(
        pady=25
    )

    growth_card.pack_propagate(False)
    growth_title = tk.Label(
        growth_card,
        text="Growth Story",
        font=("Georgia", 18, "bold"),
        fg=DARK_EARTH,
        bg=PASTEL_GREY
    )

    growth_title.pack(
        pady=15
    )

    growth_data = get_growth_insights()

    # Create the monthly order text
    growth_display = ""

    if growth_data["last_three"]:

        for month, count in growth_data["last_three"]:
            growth_display += f"{month} → {count} orders\n"

    else:

        growth_display = "No order data yet"

    # Monthly orders
    growth_label = tk.Label(
        growth_card,
        text=growth_display.strip(),
        font=("Georgia", 13),
        fg=DARK_EARTH,
        bg=PASTEL_GREY,
        justify="center"
    )
    growth_label.pack(
        pady=(5, 0),
        padx=20
    )

    # Highest month
    highest_label = tk.Label(
        growth_card,
        text=f"{growth_data['highest_month']} had the highest orders",
        font=("Georgia", 11, "italic"),
        fg=DARK_EARTH,
        bg=PASTEL_GREY
    )

    highest_label.pack(
        pady=(3, 5)
    )
    # NOTE
    note = tk.Label(
        insight_page,
        text="Every customer helps us make the next one better.",
        font=("Georgia", 11, "italic"),
        fg=DARK_EARTH,
        bg=LIGHT_PAPER
    )

    note.pack(
        pady=20
    )
def show_settings():

    settings_page = tk.Frame(
        content_area,
        bg=LIGHT_PAPER
    )

    settings_page.pack(
        fill="both",
        expand=True
    )

    # setting

    settings_file = "data/settings.json"

    default_settings = {
        "discount_active": False,
        "discount_percentage": 0,
        "customer_type": "all"
    }

    try:

        with open(settings_file, "r") as file:
            saved_settings = json.load(file)

    except (FileNotFoundError, json.JSONDecodeError):

        saved_settings = default_settings.copy()

        with open(settings_file, "w") as file:
            json.dump(
                saved_settings,
                file,
                indent=4
            )

    title = tk.Label(
        settings_page,
        text="Settings",
        font=("Georgia", 26, "bold"),
        fg=DARK_EARTH,
        bg=LIGHT_PAPER
    )

    title.pack(
        pady=(30, 20)
    )


    #discount
    discount_card = tk.Frame(
        settings_page,
        bg=PASTEL_GREY,
        width=600,
        height=300
    )

    discount_card.pack(
        pady=15
    )

    discount_card.pack_propagate(False)
    discount_title = tk.Label(
        discount_card,
        text="Discount Settings",
        font=("Georgia", 18, "bold"),
        fg=DARK_EARTH,
        bg=PASTEL_GREY
    )
    discount_title.pack(
        pady=(20, 15)
    )

    discount_enabled = tk.BooleanVar(
        value=saved_settings.get(
            "discount_active",
            False
        )
    )

    saved_customer_type = saved_settings.get(
        "customer_type",
        "all"
    )
    customer_type_map = {
        "new": "New customers",
        "returning": "Returning customers",
        "all": "Both"
    }

    customer_type = tk.StringVar(
        value=customer_type_map.get(
            saved_customer_type,
            "Both"
        )
    )
    discount_amount = tk.StringVar(
        value=str(
            saved_settings.get(
                "discount_percentage",
                0
            )
        )
    )

    #save setting
    def save_discount_settings():

        selected_customer = customer_type.get()

        if selected_customer == "New customers":

            customer_value = "new"

        elif selected_customer == "Returning customers":

            customer_value = "returning"

        else:

            customer_value = "all"

        try:

            percentage = float(
                discount_amount.get()
            )
        except ValueError:

            percentage = 0

        # Keep percentage between 0 and 100
        percentage = max(
            0,
            min(
                100,
                percentage
            )
        )
        settings = {
            "discount_active": discount_enabled.get(),
            "discount_percentage": percentage,
            "customer_type": customer_value
        }
        try:

            with open(settings_file, "w") as file:

                json.dump(
                    settings,
                    file,
                    indent=4
                )

        except Exception as error:

            print(
                "Could not save settings:",
                error
            )

    # -type of customer
    customer_label = tk.Label(
        discount_card,
        text="Give discount to:",
        font=("Georgia", 12),
        fg=DARK_EARTH,
        bg=PASTEL_GREY
    )
    customer_label.pack(
        pady=(15, 5)
    )
    customer_menu = tk.OptionMenu(
        discount_card,
        customer_type,
        "New customers",
        "Returning customers",
        "Both",
        command=lambda value: save_discount_settings()
    )

    customer_menu.config(
        font=("Georgia", 11),
        bg=LIGHT_PAPER,
        fg=DARK_EARTH,
        activebackground=KHAKI,
        activeforeground=DARK_EARTH
    )
    customer_menu.pack(
        pady=5
    )

    # discount percentage
    amount_label = tk.Label(
        discount_card,
        text="Discount percentage:",
        font=("Georgia", 12),
        fg=DARK_EARTH,
        bg=PASTEL_GREY
    )

    amount_label.pack(
        pady=(15, 5)
    )

    amount_entry = tk.Entry(
        discount_card,
        textvariable=discount_amount,
        font=("Georgia", 11),
        width=8,
        justify="center"
    )

    amount_entry.pack(
        pady=5
    )

    def percentage_changed(*args):

        save_discount_settings()

    discount_amount.trace_add(
        "write",
        percentage_changed
    )

    def update_discount_state():

        if discount_enabled.get():

            customer_menu.config(
                state="normal"
            )

            amount_entry.config(
                state="normal"
            )

        else:

            customer_menu.config(
                state="disabled"
            )

            amount_entry.config(
                state="disabled"
            )


    # -enable discount
    enable_check = tk.Checkbutton(
        discount_card,
        text="Enable discounts",
        variable=discount_enabled,
        command=lambda: (
            save_discount_settings(),
            update_discount_state()
        ),
        font=("Georgia", 12),
        fg=DARK_EARTH,
        bg=PASTEL_GREY,
        activebackground=PASTEL_GREY,
        selectcolor=LIGHT_PAPER
    )

    enable_check.pack(
        pady=5
    )
    update_discount_state()

def show_page(page_name):

    # remove previous page
    for widget in content_area.winfo_children():
        widget.destroy()

    if page_name == "Order Entry":
        show_order_entry()
    elif page_name == "Due Alerts":
        show_due_alerts()
        update_attention_message()

    elif page_name == "Feedback":

        show_feedback_entry()

    elif page_name == "Insights":

        show_insights()

    elif page_name == "Settings":

        show_settings()

    else:

        page_title = tk.Label(

            content_area,

            text=page_name,

            font=("Georgia", 28, "bold"),

            fg=DARK_EARTH,

            bg=LIGHT_PAPER

        )
        page_title.pack(pady=100)

def calculate_remaining_days(date_text):
    try:
        delivery_date = datetime.strptime(
            date_text,
            "%d-%m-%y"
        )

        today = datetime.today()

        remaining = (delivery_date - today).days

        if remaining > 0:
            return f"Delivery Status: {remaining} days remaining"

        elif remaining == 0:
            return "Delivery Status: Delivery is today"

        else:
            return "Delivery Status: Delivery completed"

    except:
        return "Delivery Status: Enter valid date"


def show_order_entry():
    global entries, status_label, delivery_status_label, discount_status_label

    # Card background
    order_card = tk.Frame(
        content_area,
        bg=PASTEL_GREY,
        padx=30,
        pady=15
    )

    order_card.pack(
        pady=10,
        padx=10
    )
    title = tk.Label(
        order_card,
        text="Order Entry",
        font=("Georgia", 22, "bold"),
        fg=COCONUT_MILK,
        bg=COFFEE_WITH_MILK
    )

    title.pack(pady=15)

    fields = [
        "Customer Name",
        "Username / Page ID",
        "Product Name",
        "Order Date",
        "Delivery Date"
    ]

    entries.clear()

    for field in fields:

        label = tk.Label(
            order_card,
            text=field,
            font=("Georgia", 12),
            fg=COCONUT_MILK,
            bg=COFFEE_WITH_MILK
        )

        label.pack(
            anchor="w",
            pady=(3, 1)
        )

        entry = tk.Entry(
            order_card,
            font=("Georgia", 12),
            width=35,
            bg=LIGHT_PAPER,
            relief="flat"
        )

        entry.pack(
            pady=2
        )

        entries.append(entry)

        # Enter key moves to next box
        entry.bind(
            "<Return>",
            lambda event, e=entry:
                entries[entries.index(e) + 1].focus()
                if entries.index(e) + 1 < len(entries)
                else None
        )

    # Customer status label
    status = tk.Label(
        order_card,
        text="Customer Status: Checking...",
        font=("Georgia", 11, "italic"),
        fg=COCONUT_MILK,
        bg=COFFEE_WITH_MILK
    )

    status.pack(
        pady=10
    )
    status_label = status

    # Discount status label
    discount_status = tk.Label(
        order_card,
        text="",
        font=("Georgia", 11, "italic"),
        fg=COCONUT_MILK,
        bg=COFFEE_WITH_MILK
    )

    discount_status.pack(
        pady=2
    )
    discount_status_label = discount_status

    # Username checking
    entries[1].bind(
        "<FocusOut>",
        lambda event: (
            status_label.config(
                text="Customer Status: " +
                check_customer(entries[1].get())
            ),
            discount_status_label.config(
                text=get_customer_discount_message(
                    entries[1].get()
                )
            )
        )
    )

    # Delivery remaining days label
    delivery_status_label = tk.Label(
        order_card,
        text="Delivery Status: Waiting...",
        font=("Georgia", 11, "italic"),
        fg=COCONUT_MILK,
        bg=COFFEE_WITH_MILK
    )

    delivery_status_label.pack(
        pady=5
    )
    # Delivery date checking
    entries[4].bind(
        "<FocusOut>",
        lambda event:
            delivery_status_label.config(
                text=calculate_remaining_days(
                    entries[4].get()
                )
            )
    )
    # Save button
    save_button = tk.Button(
        order_card,
        text="Save Order",
        font=("Georgia", 12, "bold"),
        fg=COCONUT_MILK,
        bg=DARK_EARTH,
        relief="flat",
        padx=30,
        pady=8,
        cursor="hand2",
        command=save_order
    )

    save_button.pack(
        pady=15
    )
#menu button
menu_items = [
    "Order Entry",
    "Due Alerts",
    "Insights",
    "Feedback",
    "Settings"
]
for item in menu_items:
    button = tk.Button(
        sidebar,
        text=item,
        font=("Georgia", 12),
        fg=DARK_EARTH,
        bg=PASTEL_GREY,
        activebackground=KHAKI,
        activeforeground=COCONUT_MILK,
        relief="flat",
        width=18,
        pady=10,
        cursor="hand2",
        command=lambda name=item: show_page(name)
    )

    button.pack(pady=8)

root.mainloop()