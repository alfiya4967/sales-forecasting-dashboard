import pandas as py

def load_and_preprocess_data():
    df = py.read_csv("sales_data.csv")
   
    #convert date column into datetime object
    df["Date"] = py.to_datetime(df["Date"])
    
    
    df["Month"]= df["Date"].dt.month
    
    #print(df["Month"])
    
        # Extract Year
    df["Year"] = df["Date"].dt.year
    
    return df


load_and_preprocess_data()
