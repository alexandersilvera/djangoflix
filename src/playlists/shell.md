from videos.models import Video
from playlists.models import Playlist

video_a = Video.objects.create(title='This is my video', video_id='abc123')
playlist_a = Playlist.objects.create(title='This is my Title', video=video_a)


