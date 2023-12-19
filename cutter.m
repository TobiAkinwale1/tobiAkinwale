% Define the input and output video files
inputVideoFile = 'C:\Users\akinwaleov\Downloads\Screencapture.mp4';
outputVideoFile = 'C:\Users\akinwaleov\Downloads\Nos1.mp4';

% Create a VideoReader object
vidObj = VideoReader(inputVideoFile);

% Read and display the first frame
firstFrame = readFrame(vidObj);
figure;
imshow(firstFrame);

% Use imrect to interactively draw a rectangle for cropping
h = imrect;
cropPos = wait(h); % This will return [x, y, width, height] when you finalize the position

% Use the cropPos for cropping
x = cropPos(1);
y = cropPos(2);
width = cropPos(3);
height = cropPos(4);

% Close the figure
close;

% Create a VideoWriter object for output
outputVideo = VideoWriter(outputVideoFile, 'MPEG-4'); % Use 'MPEG-4' or other appropriate codec
open(outputVideo);

% Reset the video reader to the start
vidObj.CurrentTime = 0;

while hasFrame(vidObj)
    % Read the next frame
    frame = readFrame(vidObj);
    
    % Crop the frame using the coordinates from imrect
    croppedFrame = imcrop(frame, [x y width height]);
    
    % Write the cropped frame to the output video
    writeVideo(outputVideo, croppedFrame);
end

% Close the VideoWriter object
close(outputVideo);
