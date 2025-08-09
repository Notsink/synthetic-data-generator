#!/usr/bin/env python3
"""
Dark-theme Synthetic Data Generator (Tkinter)
"""

import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import csv, random, datetime, os, threading
import string

# ---------------  HUGE DATA  ---------------
FIRST_NAMES = [
    "James", "Mary", "John", "Patricia", "Robert", "Jennifer", "Michael", "Linda",
    "William", "Elizabeth", "David", "Barbara", "Richard", "Susan", "Joseph", "Jessica",
    "Thomas", "Sarah", "Charles", "Karen", "Christopher", "Nancy", "Daniel", "Lisa",
    "Matthew", "Betty", "Anthony", "Dorothy", "Donald", "Sandra", "Mark", "Ashley",
    "Paul", "Kimberly", "Steven", "Donna", "Andrew", "Emily", "Kenneth", "Carol",
    "Joshua", "Michelle", "Kevin", "Amanda", "Brian", "Melissa", "George", "Deborah",
    "Edward", "Stephanie", "Ronald", "Rebecca", "Timothy", "Laura", "Jason", "Sharon",
    "Jeffrey", "Cynthia", "Ryan", "Kathleen", "Jacob", "Helen", "Gary", "Amy",
    "Nicholas", "Shirley", "Eric", "Angela", "Jonathan", "Anna", "Stephen", "Brenda",
    "Larry", "Emma", "Scott", "Samantha", "Frank", "Katherine", "Justin", "Christine",
    "Brandon", "Debra", "Raymond", "Rachel", "Gregory", "Catherine", "Samuel", "Janet",
    "Benjamin", "Ruth", "Patrick", "Maria", "Jack", "Heather", "Dennis", "Diane"
]

LAST_NAMES = [
    "Smith", "Johnson", "Williams", "Brown", "Jones", "Miller", "Davis", "Garcia",
    "Rodriguez", "Wilson", "Martinez", "Anderson", "Taylor", "Thomas", "Hernandez",
    "Moore", "Martin", "Jackson", "Thompson", "White", "Lopez", "Lee", "Gonzalez",
    "Harris", "Clark", "Lewis", "Robinson", "Walker", "Hall", "Allen", "Young",
    "King", "Wright", "Scott", "Torres", "Nguyen", "Hill", "Flores", "Green",
    "Adams", "Nelson", "Baker", "Hall", "Rivera", "Campbell", "Mitchell", "Carter",
    "Roberts", "Gomez", "Phillips", "Evans", "Turner", "Diaz", "Parker", "Cruz",
    "Edwards", "Collins", "Reyes", "Stewart", "Morris", "Morales", "Murphy", "Cook",
    "Rogers", "Gutierrez", "Ortiz", "Morgan", "Cooper", "Peterson", "Bailey", "Reed",
    "Kelly", "Howard", "Ramos", "Kim", "Cox", "Ward", "Richardson", "Watson",
    "Brooks", "Chavez", "Wood", "James", "Bennett", "Gray", "Mendoza", "Ruiz",
    "Hughes", "Price", "Alvarez", "Castillo", "Sanders", "Patel", "Myers", "Long"
]

EMAIL_DOMAINS = [
    "gmail.com", "yahoo.com", "outlook.com", "icloud.com", "proton.me",
    "aol.com", "hotmail.com", "zoho.com", "mail.com", "yandex.com"
]

CITIES = [
    "New York, USA", "Los Angeles, USA", "Chicago, USA", "Houston, USA",
    "London, UK", "Birmingham, UK", "Manchester, UK", "Glasgow, UK",
    "Toronto, Canada", "Vancouver, Canada", "Montreal, Canada", "Calgary, Canada",
    "Sydney, Australia", "Melbourne, Australia", "Brisbane, Australia", "Perth, Australia",
    "Berlin, Germany", "Munich, Germany", "Hamburg, Germany", "Frankfurt, Germany",
    "Paris, France", "Lyon, France", "Marseille, France", "Nice, France",
    "Tokyo, Japan", "Osaka, Japan", "Kyoto, Japan", "Yokohama, Japan",
    "Beijing, China", "Shanghai, China", "Shenzhen, China", "Guangzhou, China",
    "Mumbai, India", "Delhi, India", "Bangalore, India", "Hyderabad, India",
    "São Paulo, Brazil", "Rio de Janeiro, Brazil", "Brasília, Brazil", "Salvador, Brazil",
    "Cape Town, South Africa", "Johannesburg, South Africa", "Durban, South Africa",
    "Dubai, UAE", "Abu Dhabi, UAE", "Sharjah, UAE",
    "Moscow, Russia", "Saint Petersburg, Russia", "Novosibirsk, Russia",
    "Mexico City, Mexico", "Guadalajara, Mexico", "Monterrey, Mexico"
]

BANKS = [
    "JPMorgan Chase", "HSBC", "Deutsche Bank", "Barclays", "Citi", "Bank of America",
    "Wells Fargo", "BNP Paribas", "Santander", "UBS", "Credit Suisse", "Goldman Sachs",
    "Morgan Stanley", "ICBC", "China Construction Bank", "Agricultural Bank of China",
    "Toronto-Dominion Bank", "Royal Bank of Canada", "Commonwealth Bank", "ANZ",
    "Sberbank", "Alfa-Bank", "DBS Bank", "Standard Chartered"
]

PRODUCTS = [
    ("Smartphone", 300, 1200),
    ("Laptop", 800, 2500),
    ("Headphones", 50, 300),
    ("Coffee Machine", 150, 700),
    ("Book", 10, 40),
    ("Fitness Tracker", 30, 150),
    ("Tablet", 200, 900),
    ("Smart Watch", 150, 600),
    ("Gaming Console", 250, 500),
    ("Bluetooth Speaker", 40, 200),
    ("Digital Camera", 300, 1500),
    ("Drone", 400, 2000),
    ("Monitor", 200, 800),
    ("Mechanical Keyboard", 80, 250),
    ("Mouse", 20, 120),
    ("External SSD", 70, 300),
    ("Microphone", 50, 400),
    ("Desk Lamp", 25, 150),
    ("Electric Toothbrush", 30, 200),
    ("Air Purifier", 100, 600)
]

PAYMENT_OPTIONS = ["Bank ({})", "Crypto", "Cash"]

# --------------- generator ---------------
def random_date(start: datetime.datetime, end: datetime.datetime):
    delta = end - start
    return start + datetime.timedelta(seconds=random.randint(0, int(delta.total_seconds())))

def generate_email(first: str, last: str):
    domain = random.choice(EMAIL_DOMAINS)
    return f"{first.lower()}.{last.lower()}@{domain}"

def generate_records(rows, start, end):
    data = []
    for i in range(1, rows + 1):
        first, last = random.choice(FIRST_NAMES), random.choice(LAST_NAMES)
        product, min_p, max_p = random.choice(PRODUCTS)
        qty   = random.randint(1, 5)
        unit  = round(random.uniform(min_p, max_p), 2)
        total = round(qty * unit, 2)
        date  = random_date(start, end).strftime("%Y-%m-%d %H:%M:%S")
        city  = random.choice(CITIES)
        pay   = random.choice(PAYMENT_OPTIONS)
        if "{}" in pay:
            pay = pay.format(random.choice(BANKS))
        data.append({
            "order_id": i,
            "first_name": first,
            "last_name": last,
            "email": generate_email(first, last),
            "product": product,
            "quantity": qty,
            "unit_price": unit,
            "total_price": total,
            "order_date": date,
            "city": city,
            "payment_type": pay,
            "loyalty_card": random.choice([True, False]),
        })
    return data

# --------------- dark GUI ---------------
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Dark Synthetic Data Generator")
        self.geometry("880x680")
        self.configure(bg="#0d0d0d")
        self.data = None

        style = ttk.Style(self)
        style.theme_use("clam")

        # --- dark color scheme ---
        dark_bg   = "#0d0d0d"
        dark_fg   = "#e6e6e6"
        accent    = "#00ff99"
        mid_bg    = "#1a1a1a"
        style.configure("TLabel", background=dark_bg, foreground=dark_fg)
        style.configure("TLabelframe", background=dark_bg, foreground=dark_fg)
        style.configure("TLabelframe.Label", background=dark_bg, foreground=dark_fg)
        style.configure("TButton", background=accent, foreground=dark_bg, borderwidth=0, focusthickness=0)
        style.map("TButton", background=[("active", "#00cc7a")])
        style.configure("TEntry", fieldbackground=mid_bg, foreground=dark_fg, insertcolor=dark_fg)
        style.configure("TSpinbox", fieldbackground=mid_bg, foreground=dark_fg, insertcolor=dark_fg)
        style.configure("Treeview", background=mid_bg, foreground=dark_fg, fieldbackground=mid_bg)
        style.map("Treeview", background=[("selected", accent)], foreground=[("selected", dark_bg)])
        style.configure("Horizontal.TProgressbar", background=accent, troughcolor=mid_bg, lightcolor=accent, darkcolor=accent)

        # --- settings frame ---
        frm = ttk.LabelFrame(self, text="Settings", padding=10)
        frm.pack(fill="x", padx=10, pady=10)

        ttk.Label(frm, text="Number of rows:").grid(row=0, column=0, sticky="w")
        self.ent_rows = ttk.Spinbox(frm, from_=1, to=200_000, width=10)
        self.ent_rows.set(500)
        self.ent_rows.grid(row=0, column=1, padx=5)

        ttk.Label(frm, text="Start date:").grid(row=1, column=0, sticky="w")
        self.ent_start = ttk.Entry(frm, width=12)
        self.ent_start.insert(0, "2022-01-01")
        self.ent_start.grid(row=1, column=1, padx=5)

        ttk.Label(frm, text="End date:").grid(row=2, column=0, sticky="w")
        self.ent_end = ttk.Entry(frm, width=12)
        self.ent_end.insert(0, "2024-12-31")
        self.ent_end.grid(row=2, column=1, padx=5)

        ttk.Button(frm, text="Generate", command=self.generate) \
            .grid(row=3, column=0, columnspan=2, pady=8)

        # --- progress ---
        self.progress = ttk.Progressbar(self, orient="horizontal", mode="indeterminate")
        self.progress.pack(fill="x", padx=10)

        # --- table ---
        self.tree = ttk.Treeview(self, show="headings")
        vsb = ttk.Scrollbar(self, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=vsb.set)
        vsb.pack(side="right", fill="y")
        self.tree.pack(fill="both", expand=True, padx=10, pady=5)

        # --- save button ---
        self.btn_save = ttk.Button(self, text="Save CSV...", command=self.save_csv, state="disabled")
        self.btn_save.pack(pady=5)

    # ---------- handlers ----------
    def generate(self):
        try:
            rows  = int(self.ent_rows.get())
            start = datetime.datetime.strptime(self.ent_start.get(), "%Y-%m-%d")
            end   = datetime.datetime.strptime(self.ent_end.get(), "%Y-%m-%d")
            if rows <= 0 or rows > 200_000:
                raise ValueError
        except ValueError:
            messagebox.showerror("Error", "Please enter valid inputs.")
            return

        self.btn_save.config(state="disabled")
        self.progress.start()

        def worker():
            self.data = generate_records(rows, start, end)
            self.after(0, self.done)

        threading.Thread(target=worker, daemon=True).start()

    def done(self):
        self.progress.stop()
        for col in self.tree["columns"]:
            self.tree.heading(col, text="")
        self.tree.delete(*self.tree.get_children())

        if not self.data:
            return
        cols = list(self.data[0].keys())
        self.tree["columns"] = cols
        for c in cols:
            self.tree.heading(c, text=c.title())
            self.tree.column(c, width=100, anchor="center")
        for row in self.data:
            self.tree.insert("", "end", values=list(row.values()))

        self.btn_save.config(state="normal")

    def save_csv(self):
        if not self.data:
            return
        path = filedialog.asksaveasfilename(
            defaultextension=".csv",
            filetypes=[("CSV files", "*.csv"), ("All files", "*.*")]
        )
        if not path:
            return
        try:
            with open(path, "w", newline='', encoding="utf-8-sig") as f:
                writer = csv.DictWriter(f, fieldnames=self.data[0].keys())
                writer.writeheader()
                writer.writerows(self.data)
            messagebox.showinfo("Done", f"Saved: {os.path.basename(path)}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

if __name__ == "__main__":
    App().mainloop()