from fastapi import FastAPI
app = FastAPI()
@app.get("/")
async def root():
     return {"Hello":"World"}


def calculate_meal_fee(beef_price, meal_price):
     total_price: int = beef_price + meal_price
     return total_price+1
print("Calculated meal fee", calculate_meal_fee(75, 19))
