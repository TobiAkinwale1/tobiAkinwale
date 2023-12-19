V=VideoReader('C:\Users\akinwaleov\Desktop\Video0001.mp4')
nFrames=V.NumFrames();
npix_w = V.Width;
npix_h = V.Height;
vidgray = zeros(npix_h,npix_w,nFrames,"uint8");
i=1;
while hasFrame(V) 
    f1=readFrame(V);
    vidgray(:,:,i) = f1(:,:,1);
    i=i+1;
    if rem(i,1000)==0, disp(i); end
end
% 

figure; imshow(f1)
firstframe = vidgray(:,:,1);
laseroff_pixel_count = sum(firstframe(:)>=250);
middleframes = vidgray(:,:,round(nFrames/2)+(-50:50));
laseron_pixel_counts = squeeze(sum(sum(middleframes>=250,1),2));
laseron_pixel_count_min = min(laseron_pixel_counts);
my_threshold = mean([laseroff_pixel_count,laseron_pixel_count_min]);
total_pixels = npix_w*npix_h;

pixel_counts_allframes = squeeze(sum(sum(vidgray>=250,1),2));
pixel_counts_allframes_thresh = pixel_counts_allframes>my_threshold;
figure; plot(pixel_counts_allframes_thresh); ylim([-0.1 1.1])

first1 = find(pixel_counts_allframes_thresh, 1, "first");
last1 = find(pixel_counts_allframes_thresh, 1, "last");
frames = read(V, [first1, last1]);

cd("C:\Users\akinwaleov\OneDrive - National Institutes of Health\")
video = VideoWriter('tk_cropp','MPEG-4');
video.FrameRate = 30; 
open(video)
for i = 1:size(frames,4)    
    img = frames(:,:,:,i); 
    writeVideo(video,img); 
end
close(video);

