# CDN

> ✔️Content Delivery Repository

HITS: [![jsDelivr](https://data.jsdelivr.com/v1/package/gh/MoChanBW/CDN/badge)](https://www.jsdelivr.com/package/gh/MoChanBW/CDN)


For HLS:

```bash
ffmpeg -i foo.mp4 -vf yadif=mode=0:parity=auto:deint=0 -c:v h264_nvenc -b:v 3000k -maxrate 4000k -minrate 2000k -pix_fmt yuv420p -preset slow -c:a aac -b:a 320k -hls_time 5 -hls_list_size 0 -f hls index.m3u8
```

```bash
ffmpeg -y -i input -c:v h264_nvenc -pix_fmt yuv420p -preset slow -vf yadif=mode=0:parity=auto:deint=0 -b:v 6000k -pass 1 -an -f mp4 NUL && ffmpeg -i input -c:v h264_nvenc -preset slow -b:v 6000k -maxrate 8000k -minrate 2000k -pass 2 -c:a aac -b:a 320k -hls_time 5 -hls_list_size 0 -f hls index.m3u8
```


```bash
for %a in ("*.flac") do ffmpeg -i "%a" -b:a 1000k "%~na.mp3" && for %a in ("*.mp3") do ffmpeg -i "%a" "%~na.jpg"
```


```bash
ffprobe -v quiet -of json -show_format example.mp3
```


```bash 
mkvextract "i.mkv" tracks {TrackID}:{OutPutFile}
```    


```javascript
ap.list.audios[ap.list["index"]]
```