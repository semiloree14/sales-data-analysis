
import matplotlib.pyplot as plt
import os

os.makedirs("charts", exist_ok=True)

# First chart: Units sold by product
product_sales = sales.groupby("Product")["Quantity"].sum()

plt.figure(figsize=(8, 5))
product_sales.plot(kind="bar", color="skyblue")
plt.title("Units Sold by Product")
plt.xlabel("Product")
plt.ylabel("Units Sold")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("charts/units_sold_by_product.png", dpi=300)


# Second chart: Revenue by region
region_revenue = sales.groupby("Region")["Revenue"].sum()

plt.figure(figsize=(8, 5))
region_revenue.plot(kind="bar", color="orange")
plt.title("Revenue by Region")
plt.xlabel("Region")
plt.ylabel("Revenue (₦)")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("charts/revenue_by_region.png", dpi=300)


# Third chart: Revenue by product
product_revenue = sales.groupby("Product")["Revenue"].sum()

plt.figure(figsize=(7, 7))
product_revenue.plot(
    kind="pie",
    autopct="%1.1f%%",
    startangle=90
)
plt.title("Revenue Contribution by Product")
plt.ylabel("")
plt.tight_layout()
plt.savefig("charts/revenue_by_product.png", dpi=300)


# Display all three charts
plt.show()

print("All three charts have been saved!")
