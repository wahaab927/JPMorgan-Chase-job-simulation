import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
# Load data
df = pd.read_csv("/mnt/data/Nat_Gas (2).csv")

# Rename columns if needed (adjust if column names differ)
df.columns = ["Date", "Price"]

# Convert Date to datetime
df["Date"] = pd.to_datetime(df["Date"])

# Sort data
df = df.sort_values("Date").reset_index(drop=True)

df.head()
plt.figure()
plt.plot(df["Date"], df["Price"])
plt.xlabel("Date")
plt.ylabel("Natural Gas Price")
plt.title("Monthly Natural Gas Prices")
plt.show()
df["Month"] = df["Date"].dt.month
df["TimeIndex"] = np.arange(len(df))
Price = Trend + Seasonal Effect
from sklearn.linear_model import LinearRegression

X = df[["TimeIndex", "Month"]]
y = df["Price"]

model = LinearRegression()
model.fit(X, y)
def estimate_gas_price(input_date):
    input_date = pd.to_datetime(input_date)

    # Calculate time index
    time_index = (input_date.year - df["Date"].iloc[0].year) * 12 + \
                 (input_date.month - df["Date"].iloc[0].month)

    month = input_date.month

    X_input = np.array([[time_index, month]])
    predicted_price = model.predict(X_input)[0]

    return round(predicted_price, 2)
print("Past date:", estimate_gas_price("2022-06-15"))
print("Future date:", estimate_gas_price("2025-08-01"))
future_dates = pd.date_range(
    start=df["Date"].max(),
    periods=12,
    freq="M"
)

future_df = pd.DataFrame({
    "Date": future_dates,
})

future_df["TimeIndex"] = np.arange(
    df["TimeIndex"].iloc[-1] + 1,
    df["TimeIndex"].iloc[-1] + 1 + len(future_df)
)

future_df["Month"] = future_df["Date"].dt.month
future_df["PredictedPrice"] = model.predict(
    future_df[["TimeIndex", "Month"]]
)

plt.figure()
plt.plot(df["Date"], df["Price"], label="Historical")
plt.plot(future_df["Date"], future_df["PredictedPrice"], linestyle="dashed", label="Forecast")
plt.legend()
plt.title("Natural Gas Price Forecast")
plt.show()
