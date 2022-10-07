import os
import grpc
from django.shortcuts import render
from recommendations_pb2 import BookCategory, RecommendationRequest
from recommendations_pb2_grpc import RecommendationsStub

def render_homepage(request):
    recommendations_host = os.getenv("RECOMMENDATIONS_HOST", "localhost")
    recommendations_channel = grpc.insecure_channel(f"{recommendations_host}:50051")
    recommendations_client = RecommendationsStub(recommendations_channel)
    recommendations_request = RecommendationRequest(
        user_id=1, category=BookCategory.SCIENCE_FICTION, max_results=3
    )
    recommendations_response = recommendations_client.Recommend(
        recommendations_request
    )
    return render(request, "homepage.html",{'recommendations':recommendations_response.recommendations})