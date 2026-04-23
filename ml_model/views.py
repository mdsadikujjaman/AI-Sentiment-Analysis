import os
import joblib
from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings

# --- LOAD THE MODEL GLOBALLY ONCE ---
# Construct the path to the saved model
MODEL_PATH = os.path.join(settings.BASE_DIR, 'ml_model', 'saved_model.joblib')

# Load the model into memory when Django starts
try:
    ml_pipeline = joblib.load(MODEL_PATH)
except Exception as e:
    ml_pipeline = None
    print(f"Failed to load model: {e}")

# --- VIEWS ---
def index(request):
    return render(request, 'ml_model/index.html')

def predict_sentiment(request):
    user_text = request.GET.get('text', '') 
    
    if not user_text:
        return JsonResponse({"error": "No text provided"}, status=400)

    if ml_pipeline is None:
        return JsonResponse({"error": "ML model is offline"}, status=500)

    # 1. Run inference using the scikit-learn pipeline
    prediction = str(ml_pipeline.predict([user_text])[0])
    
    # 2. Get the probability (confidence score)
    probabilities = ml_pipeline.predict_proba([user_text])[0]
    confidence = float(max(probabilities))

    # 3. Return the real results
    response_data = {
        "status": "success",
        "input_received": user_text,
        "prediction": prediction,
        "confidence_score": round(confidence * 100, 2) # Return as a percentage
    }
    
    return JsonResponse(response_data)