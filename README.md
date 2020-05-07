# CDN
> ✔️Content Delivery Repository

HITS: [![jsDelivr](https://data.jsdelivr.com/v1/package/gh/MoChanBW/CDN/badge)](https://www.jsdelivr.com/package/gh/MoChanBW/CDN)

For MPEG DASH:

```bash(with bug)
MP4Box -dash-strict 5000 -profile dashavc264:live -rap foo.mp4#video foo.mp4#audio -out index.mpd
```

 

For HLS(recommend):

```bash
ffmpeg -i foo.mp4 -c:v h264_nvenc -b:v 3000k -pix_fmt yuv420p -preset slow -c:a aac -hls_time 10 -hls_list_size 0 -f hls index.m3u8
```
```bash
ffmpeg -y -i input -c:v h264_nvenc -pix_fmt yuv420p -preset slow -b:v 6000k -pass 1 -an -f mp4 NUL && ffmpeg -i input -c:v h264_nvenc -preset slow -b:v 6000k -maxrate 8000k -minrate 2000k -pass 2 -c:a aac -b:a 320k -hls_time 5 -hls_list_size 0 -f hls index.m3u8
```