% Sample data
y = dlc(1:3000,[3,5,7]);
x = 1:3000;

% Create a figure and axes
figure;
axesHandle = axes;

% Create animated line objects for each column of y
lineHandles = gobjects(1, size(y, 2));
colors = ['c', 'y', 'r']; % Line colors for each column
for i = 1:size(y, 2)
    lineHandles(i) = animatedline(axesHandle, 'Color', colors(i), 'LineWidth', 2);
end

% Set axis limits
ylim(axesHandle, [220, 354]);
xlim(axesHandle, [1, 3000]);

% Loop through the data and update the lines
numFrames = numel(x);
frames = cell(1, numFrames); % Preallocate frames array
for i = 1:numFrames
    % Add points to each line
    for j = 1:size(y, 2)
        addpoints(lineHandles(j), x(i), y(i, j));
    end

    % Update the plot
    drawnow;

    % Capture the frame
    frames{i} = getframe(gcf);

    % Pause for a short duration to control the animation speed
    pause(1/115);
end


% Create an MP4 file
filename = 'animation3.mp4';
frameRate = 115; % Set the desired frame rate (frames per second)

writerObj = VideoWriter(filename, 'MPEG-4');
writerObj.FrameRate = frameRate;
open(writerObj);

for i = 1:numFrames
    frame = frames{i};
    writeVideo(writerObj, frame);
end

close(writerObj);

disp('Animation saved as MP4 file.');



