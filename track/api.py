from typing import List, Optional
from django.http import JsonResponse
from ninja import NinjaAPI
from .models import Track
from .schema import TrackSchema, NotFoundSchema

api = NinjaAPI()

@api.get("/tracks", response=List[TrackSchema])
def tracks(request, title:Optional[str] = None):
   if title:
      return Track.objects.filter(title__icontains=title)
   return Track.objects.all()

@api.get("/tracks/{id}", response={200: TrackSchema, 404: NotFoundSchema})
def specific_track(request, id:int):
   try:
      track = Track.objects.get(id=id)
      return track
   except Track.DoesNotExist as e:
      return 404, {"message": "Track does not exist"}
   
@api.post("/tracks", response={201: TrackSchema})
def create_track(request, track:TrackSchema):
   track = Track.objects.create(**track.dict())
   return track

@api.put("/tracks/{id}", response={200: TrackSchema, 404: NotFoundSchema})
def update_track(request, id:int, data:TrackSchema):
   try:
      track = Track.objects.get(id=id)
      for key, value in data.dict().items():
         setattr(track, key, value)
      track.save()
      return track
   except Track.DoesNotExist as e:
      return 404, {"message": "Track does not exist"}

@api.delete("/tracks/{id}", response={204: None, 404: NotFoundSchema})
def delete_track(request, id:int):
   try:
      track = Track.objects.get(id=id)
      track.delete()
      return JsonResponse({"sucess": True})
   except Track.DoesNotExist as e:
      return 404, {"message": "Track does not exist"}