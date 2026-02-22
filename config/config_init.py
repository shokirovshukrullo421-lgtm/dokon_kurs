import csv
import os

USERS_FILE = "config/user_data.csv"
PROFUCTS_FILE = "config/products.csv"
DATA="config/data.csv"

def init_users_file():
    if not os.path.exists(USERS_FILE):
        with open(USERS_FILE, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["name", "login", "password"])
def init_products_file():
    if not os.path.exists(PROFUCTS_FILE):
        with open(PROFUCTS_FILE, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["name", "price", "miqdor"])
def init_products_file():
    if not os.path.exists(DATA):
        with open(DATA, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([ "login", "royxat", "total_price" ])