from pydantic import BaseModel
class RecommendationSystem(BaseModel):
    userId: int
    movieId: int
    rating: float