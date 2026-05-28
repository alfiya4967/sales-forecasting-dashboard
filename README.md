# Predictive Sales Analytics & Forecasting Dashboard

A complete end-to-end project that connects a FastAPI backend, a Scikit-learn sales forecasting model, and a Streamlit frontend dashboard with Plotly visualizations.

## Project Structure

```
Predictive-Sales-Analytics-Forecasting-Dashboard/
├── backend/
│   ├── main.py
│   ├── model.py
│   ├── preprocess.py
│   ├── sales_data.csv
│   └── requirements.txt
├── frontend/
│   └── app.py
├── authentication_cred.json
├── requirements.txt
└── README.md
```

## What is complete

- `backend/main.py`: FastAPI app with routes for health check, sales data, and prediction
- `backend/preprocess.py`: CSV loading and date feature engineering
- `backend/model.py`: model training using `LinearRegression`
- `frontend/app.py`: Streamlit dashboard that fetches data from backend and posts prediction requests
- `requirements.txt`: Python dependencies for the project

## Setup

1. Create and activate your virtual environment:

```bash
python -m venv myvenv
myvenv\Scripts\activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Make sure `backend/sales_data.csv` exists with the required columns: `Date,Region,Sales,Marketing_Spend`.

## Run the backend

From the repository root:

```bash
cd backend
uvicorn main:app --reload
```

The backend should be available at:

- `http://127.0.0.1:8000/`
- `http://127.0.0.1:8000/docs`

### Swagger Basic Auth

If your backend uses protected Swagger docs, use these credentials from `authentication_cred.json`:

- Username: `user_admin`
- Password: `user_pass#`

## Run the frontend

Open a second terminal and run:

```bash
cd frontend
streamlit run app.py
```

Then open:

- `http://localhost:8501`

## How the flow works

1. Start the backend first.
2. Start the Streamlit frontend.
3. The frontend loads data from `GET /sales-data`.
4. The dashboard renders the sales table and chart.
5. User enters `marketing_spend` and selects `month`.
6. Frontend sends `POST /predict` to the backend.
7. Backend returns `predicted_sales`.
8. Frontend displays the prediction.

## Testing endpoints

### Health check

```bash
curl http://127.0.0.1:8000/
```

### Sales data

```bash
curl http://127.0.0.1:8000/sales-data
```

### Predict sales

```bash
curl -X POST http://127.0.0.1:8000/predict \
  -H "Content-Type: application/json" \
  -d '{"marketing_spend": 600.0, "month": 11}'
```

## Notes

- No CORS error is expected because Streamlit makes the request from the Python server side, not from browser JS.
- If you want to protect Swagger docs and the OpenAPI spec, keep the auth setup in `backend/main.py`.
- The backend route used by the frontend is `GET /sales-data`.

## Optional improvements

- Save the trained model with `pickle` so it does not retrain on every reload.
- Add a database for persistent storage.
- Add more features like `Region` filtering, `Marketing ROI`, and `trend analysis`.
- Add Docker support for easier deployment.

