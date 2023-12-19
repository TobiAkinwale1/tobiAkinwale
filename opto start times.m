tmp = find(diff(BD.lick)>0);
tmp2 = tmp+[-198:1];
optostarttimes = tmp(sum(BD.lick(tmp2),2)==1);
BD.frameCbl(optostarttimes)
optostart_dlc = round(BD.frameCbl(optostarttimes)*(1/30)/dtDLC)