trial_great=find(dlc(:,5)>485);
trial_greatdiff=diff(trial_great);
trial_diff=find(trial_greatdiff>2);
trials=trial_great(trial_diff);
start=trials-262;
start_trials=[start,trials+50];
trar=[];
for f=2:size(start_trials,1)
    start_trialsdlc=dlc(start_trials(f,1):start_trials(f,2),[5,7]);
    trar=[trar,start_trialsdlc];
end
perm_dlc=permute(reshape(trar,size(trar,1),2,[]),[1,2,3]);
perm_sub=(perm_dlc(:,1,:))>(perm_dlc(:,2,:));
perm_sum=squeeze(sum(perm_sub,1));
start_trials=start_trials(2:size(start_trials),:);
