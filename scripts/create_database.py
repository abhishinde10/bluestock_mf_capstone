import pandas as pd
import os
from sqlalchemy import create_engine

engine = create_engine(
    "sqlite:///../data/db/bluestock_mf.db"
)

folder="../data/processed"

for file in os.listdir(folder):

    if file.endswith(".csv"):

        df = pd.read_csv(
            os.path.join(folder,file)
        )

        table = file.replace(".csv","")

        df.to_sql(
            table,
            engine,
            if_exists="replace",
            index=False
        )

        print(table,"loaded")

print("Database Ready")