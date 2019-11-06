from rest_framework import serializers

from swengs.songs.models import Song

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['title','length','release_date','artists',]