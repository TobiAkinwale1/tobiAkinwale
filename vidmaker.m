% Read the input videos
video1 = VideoReader('10.mp4');
video2 = VideoReader('animation3.mp4');

% Read the first frame of each video
frame1 = readFrame(video1);
frame2 = readFrame(video2);

% Determine the dimensions of the videos
videoHeight = video1.Height;
videoWidth = video1.Width;

% Create a new video file
outputVideo = VideoWriter('stacked_video2.mp4', 'MPEG-4');
outputVideo.FrameRate = video1.FrameRate;
open(outputVideo);

% Loop through the frames of the videos
while hasFrame(video1) && hasFrame(video2)
    % Resize the frames to have the same dimensions
    frame1Resized = imresize(frame1, [videoHeight, videoWidth]);
    frame2Resized = imresize(frame2, [videoHeight, videoWidth]);
    
    % Stack the resized frames vertically
    stackedFrame = imtile({frame1Resized, frame2Resized}, 'GridSize', [2, 1]);
    
    % Write the stacked frame to the output video
    writeVideo(outputVideo, stackedFrame);
    
    % Read the next frame of each video
    frame1 = readFrame(video1);
    frame2 = readFrame(video2);
end

% Close the output video file
close(outputVideo);

disp('Stacked video saved.');


