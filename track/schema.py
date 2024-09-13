from ninja import ModelSchema, Schema
from .models import Track

class TrackSchema(ModelSchema):
   class Meta:
      model = Track
      fields = ["id", "title", "artist", "duration", "last_play"]

class NotFoundSchema(Schema):
   message: str