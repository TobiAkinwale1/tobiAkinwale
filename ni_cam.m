sol = Untitled(:,10);
lick = Untitled(:,9);
cam = Untitled(:,13);
cam_on=find(Untitled(:,13)==1);
first_cam=cam_on(1,1);
last_cam=(max(cam));
last_cam1=find(cam(:,:)==last_cam, 1, 'last' );
ni_camm=Untitled(first_cam:last_cam1,:);

solopen = find(sol==1);
dif = diff(solopen);
delstarts = [1;find(dif~=1)];
solstarts=solopen(delstarts+1);
sol_ni=ni_camm(:,10);
lick_ni=ni_camm(:,9);
cam_ni=ni_camm(:,13);

solopen_ni=find(sol_ni==1);
dif_ni=diff(solopen_ni);
delstarts_ni=[1;find(dif_ni~=1)];
solstarts_ni=solopen_ni(delstarts_ni+1);
solstarts_cam=cam_ni(solstarts_ni);
solstartscam_dlc=g(solstarts_cam,:);


lick_perc = zeros(length(solstarts),2);
for s = 1:length(solstarts)-1
    soltime = solstarts(s);
    move = soltime-200;
    fin = soltime+200;
    lick_before = lick(move:soltime-1); before_perc = sum(lick_before)/length(lick_before);
    lick_after = lick(soltime:fin); after_perc = sum(lick_after)/length(lick_after);
    lick_perc(s,1) = before_perc; lick_perc(s,2) = after_perc;
%     disp(strcat("trial ", string(s), " anticipatory licking ", string(before_perc), " reward licking ", string(after_perc)))
%     pause;
end

% mouse 21102-Black
% day 1: 0.2102, 0.4246
% day 2: 0.4091, 0.7528
% day 3: 0.3394, 0.3884
% day 4: 0.7590, 0.9382
avg_before = mean(lick_perc(:,1)); 
avg_after = mean(lick_perc(:,2));

