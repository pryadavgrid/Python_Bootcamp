import pandas as pd

df = pd.read_csv("data.csv")

df["full_name"] = df["name"] + " " + df["surname"]

print(df)

df.to_csv("updated_data.csv", index=False)