import requests
import pandas as pd

funds = {
    "HDFC":125497,
    "SBI":119551,
    "ICICI":120503,
    "NIPPON":118632,
    "AXIS":119092,
    "KOTAK":120841
}

for name,code in funds.items():

    url=f"https://api.mfapi.in/mf/{code}"

    response=requests.get(url)

    data=response.json()

    df=pd.DataFrame(data["data"])

    df.to_csv(
        f"../data/raw/{name}_NAV.csv",
        index=False
    )

    print(name,"Downloaded")