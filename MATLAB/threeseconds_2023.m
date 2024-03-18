mean_lick=mean(midAlgn.lick);
figure;plot(mean_lick)
xplt = winfn(tmpxx,[-6 6]);
trgrps = {};
trgrps = cellfun(@(x)x(x<length(rewarded)),trgrps,UniformOutput=false);
omiss_lick=find(rewarded==0);
omitted_trials=startAlgn.lick([omiss_lick],:);
rewarded_trials=startAlgn.lick;
rewarded_trials([omiss_lick],:)=[];

lickraw = double(rewarded_trials);
%lickraw = double(omitted_trials);

lickrate = (diff(lickraw,[],2)>0)./0.005;
lickfilt = butter_filter(2,0.02,lickraw')';
lickrate_filt = butter_filter(2,0.02,lickrate')';
probnormsig = ones(size(lickraw));
probnormwin = winfn(tmpxx,[-1 -0]);
normsig = sum(lickrate(:,probnormwin),2); 
lickrate_prob = lickrate./normsig;
lickrate_prob(normsig==0,:) = 1./length(probnormwin);
lickrate_prob = butter_filter(2,0.02,lickrate_prob')';
lickrate_filt_prob = lickrate_prob*100;

mean_lickrate_prob=mean(lickrate_prob);
mean_lickraw=smooth(mean(lickraw));
mean_lickfilt=mean(lickfilt);
mean_lickrate_filt=mean(lickrate_filt);

newy=-2:4/2400:2;
newy1=-2:4/2399:2;
%newy1=-4:4/1599.5:4;
figure;plot(newy1,mean_lickrate_prob,'LineWidth',1.3)
hold on 
title('Lick Rate')
xline(-1,'--r')
%xline(1,'--r')
xlabel("Time relative to reward(s)")
x_fill=[-1,0,0,-1];
y_limits=ylim;
y_fill=[y_limits(1),y_limits(1),y_limits(2),y_limits(2)];
h=fill(x_fill,y_fill,[1,0,0]);
alpha(h,0.5);
hold off;

region=[-1:1];
patch(region)
figure; plot(newy1,mean_lickraw)
hold on 1
title('Raw Licking data')
hold off
figure; plot(newy1,mean_lickrate_prob)
hold on
title("Lick data")
hold off

