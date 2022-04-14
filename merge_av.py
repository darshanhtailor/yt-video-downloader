import moviepy.editor as mpe

def combine_audio(vid, aud, out):
    vid_clip = mpe.VideoFileClip(vid)
    aud_clip = mpe.AudioFileClip(aud)
    final_clip = vid_clip.set_audio(aud_clip)
    final_clip.write_videofile(out)