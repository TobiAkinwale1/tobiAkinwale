% Sample data
y = (dlc(:, [2, 4, 6]));
x = 1:2501;

% Create a figure and axes
figure;
axesHandle = axes;

% Create animated line objects
lineHandles = gobjects(1, size(y, 2));
lineColors = {'b', 'r', 'g'};
for i = 1:size(y, 2)
    lineHandles(i) = animatedline(axesHandle, 'Color', lineColors{i}, 'LineWidth', 2);
end

% Set axis limits
ylim(axesHandle, [255, 285]);
xlim(axesHandle, [1, 2501]);

% Loop through the data and update the lines
numFrames = numel(x);
frames = cell(1, numFrames); % Preallocate frames array
for i = 1:numFrames
    for j = 1:size(y, 2)
        % Add a point to the line
        addpoints(lineHandles(j), x(i), y(i, j));
    end
    
    % Update the plot
    drawnow;
    
    % Capture the frame
    frames{i} = getframe(gcf);
    
    % Pause for a short duration to control the animation speed
    pause(1 / 115);
end

% Create an MP4 file
filename = 'animation5.mp4';
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



