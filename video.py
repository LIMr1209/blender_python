import os

os.environ['FFMPEG_BINARY'] = 'auto-detect'  # 使用系统 ffmpeg
from moviepy.video.io.ImageSequenceClip import ImageSequenceClip
import cv2
import ffmpeg
from moviepy.video.io.ffmpeg_writer import ffmpeg_write_video


def merge_image_to_video_moviepy(folder_name):
    # 需要改源码
    '''
     def make_frame(t):
        index = find_image_index(t)
        return self.sequence[index][:,:,:4]

     cmd = [
        get_setting("FFMPEG_BINARY"),
        '-y',
        '-loglevel', 'error' if logfile == sp.PIPE else 'info',
        '-f', 'rawvideo',
        '-vcodec', 'rawvideo',
        '-s', '%dx%d' % (size[0], size[1]),
        '-pix_fmt', 'rgba',
        '-r', '%.02f' % fps,
        '-an', '-i', '-'
    ]
    '''
    fps = 30
    image_files = []
    for f1 in os.listdir(folder_name):
        filename = os.path.join(folder_name, f1)
        i = cv2.imread(filename, -1)  # RGBA 通道
        image_files.append(i)
    clip = ImageSequenceClip(image_files, fps=fps)
    ffmpeg_write_video(clip, "output3.mp4", fps=fps, codec="png", threads=4)
    # clip.write_videofile("output3.mov", fps=fps, codec="qtrle", threads=4)


def merge_image_to_video_ffmpeg(folder_name):
    folder_name = os.path.join(folder_name, '*.png')
    (
        ffmpeg
            .input(folder_name, pattern_type='glob', framerate=30)
            .output('movie.mp4', format='image2', vcodec='png')
            .run()
    )


if __name__ == '__main__':
    # 要求文件夹中的文件尺寸必须一致，否则必须统一
    folder_name = r"C:\Users\thn\Desktop\output_copy"
    merge_image_to_video_moviepy(folder_name)
    # merge_image_to_video_ffmpeg(folder_name)

# ffmpeg -y -loglevel error -f rawvideo -vcodec rawvideo -s 1920x1080 -pix_fmt rgba -r 30.00 -an -i - -vcodec png -preset medium -threads 4 output3.mp4