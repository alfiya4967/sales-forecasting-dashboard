from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
from preprocess import load_and_preprocess_data

print("FILE STARTED")
def train_sale_split():
    print("FUNCTION STARTED")
    df = load_and_preprocess_data()
    
    x = df[["Marketing_Spend","Month"]]
    #print (x)
    
    # Target
    y = df["Sales"]
    #print(y)
    
    #split data
    
    x_train,x_test,y_train,y_test = train_test_split(
        x,
        y,
        test_size=0.2,
        random_state=42
    )
    print(x_test)
    print(x_train)
    
    #create model
    model = LinearRegression()
    
    #train model
    model.fit(x_train,y_train)
    
    #prediction
    prediction = model.predict(x_test)
    print (prediction)
    
    print("\nACTUAL SALES VALUES")
    print(y_test.values)
    
    print(model)
    
    # Evaluate model
    error = mean_absolute_error(y_test, prediction)
    print(error)
    print(f"Model Error: {error}")
    
    
    
    return model

print("CALLING FUNCTION")
train_sale_split()