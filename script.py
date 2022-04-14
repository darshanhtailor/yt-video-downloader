from pytube import YouTube

print('YouTube Video/Audio Downloader')
print('Made by Nikhil Sharma, Darshan Tailor & Kushal Tejwani\n')

url = input('Enter a YouTube Video URL: ')

try:
    yt = YouTube(url)
except:
    print('Unable to process URL')
else:
    _streams = yt.streams.filter(adaptive=True)
    vidname = 'vid_' + yt.title + '.mp4'
    audname = 'aud_' + yt.title + '.mp4'
    vids = []
    mp = {}

    for _stream in _streams:
        if _stream.mime_type == 'video/mp4' and mp.get(_stream.resolution) != 1:
            vids.append(_stream)
            mp[_stream.resolution] = 1
        elif _stream.mime_type == 'audio/mp4':
            aud = _stream

    format = int(input('\n1. Video\n2. Audio\nChoose format: '))

    if format == 1:
        print('\n')
        for i in range(0, len(vids)):
            print(f'{i+1}. {vids[i].resolution}')
        resSelect = int(input('Choose resolution: '))-1

        print('Downloading...')
        vidfile = _streams.get_by_itag(vids[resSelect].itag).download(
            filename='vid_' + yt.title + '.mp4')
    elif format == 2:
        print('Downloading...')
    else:
        print('Invalid Option')

    audfile = _streams.get_by_itag(aud.itag).download(
        filename='aud_' + yt.title + '.mp4')
