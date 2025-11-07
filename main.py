from fastapi import FastAPI
from typing import Dict

app = FastAPI()

# FAKE in-memory database
users = {
    "alice": {"balance": 100},
    "bob": {"balance": 50}
}

@app.get("/")
def home():
    return {"status": "backend online"}

@app.get("/balance/{username}")
def get_balance(username: str):
    if username in users:
        return {"balance": users[username]["balance"]}
    return {"error": "User not found"}

@app.post("/add_credits/{username}")
def add_credits(username: str, amount: int):
    if username in users:
        users[username]["balance"] += amount
        return {"balance": users[username]["balance"]}
    return {"error": "User not found"}

@app.post("/subtract_credits/{username}")
def subtract_credits(username: str, amount: int):
    if username in users:
        users[username]["balance"] -= amount
        return {"balance": users[username]["balance"]}
    return {"error": "User not found"}
