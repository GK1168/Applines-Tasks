import ffmpeg

input_video = ffmpeg.input(r'car.mp4')
input_video = ffmpeg.hflip(input_video)
input_video = ffmpeg.output(input_video,r'/WEEK-02/FFMPEG-TRIAL/input1.mp4')

ffmpeg.run(input_video)

