import sqlite3
import pandas as pd
conn = sqlite3.Connection('chinook.db')
cursor = conn.cursor()

customers = pd.read_sql("SELECT * FROM customers", conn)
invoices = pd.read_sql("SELECT * FROM invoices", conn)
conn.close()


customer_spending = (
    invoices
    .groupby("CustomerId", as_index=False)["Total"]
    .sum()
    .rename(columns={"Total": "TotalSpent"})
)
print("\n", customer_spending)

customer_spending = customer_spending.merge(customers, on="CustomerId")

customer_spending["CustomerName"] = (
    customer_spending["FirstName"] + " " + customer_spending["LastName"]
)

top_5_customers = (
    customer_spending
    .sort_values("TotalSpent", ascending=False)
    .head(5)
    [["CustomerId", "CustomerName", "TotalSpent"]]
)

print("\n", top_5_customers)

import sqlite3
import pandas as pd

conn = sqlite3.connect("chinook.db")

purchases = pd.read_sql("""
    SELECT
        i.CustomerId,
        t.AlbumId,
        ii.TrackId
    FROM invoice_items ii
    JOIN invoices i ON ii.InvoiceId = i.InvoiceId
    JOIN tracks t ON ii.TrackId = t.TrackId
""", conn)

album_tracks = pd.read_sql("""
    SELECT AlbumId, COUNT(*) AS TotalTracks
    FROM tracks
    GROUP BY AlbumId
""", conn)

conn.close()

customer_album = (
    purchases
    .groupby(["CustomerId", "AlbumId"])
    .agg(PurchasedTracks=("TrackId", "nunique"))
    .reset_index()
)

customer_album = customer_album.merge(album_tracks, on="AlbumId")

customer_album["PurchaseType"] = customer_album.apply(
    lambda x: "Full Album" if x["PurchasedTracks"] == x["TotalTracks"]
    else "Partial Album",
    axis=1
)

customer_summary = (
    customer_album
    .groupby(["CustomerId", "PurchaseType"])
    .size()
    .unstack(fill_value=0)
    .reset_index()
)

customer_summary["Preference"] = customer_summary.apply(
    lambda x: "Individual Tracks"
    if x.get("Partial Album", 0) > x.get("Full Album", 0)
    else "Full Albums",
    axis=1
)

preference_summary = (
    customer_summary["Preference"]
    .value_counts(normalize=True)
    .mul(100)
    .round(2)
    .reset_index()
)

preference_summary.columns = ["Purchase Preference", "Percentage"]

print(preference_summary)
