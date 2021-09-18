tri = spinw;
tri.genlattice('lat_const',[3 3 4],'angled',[90 90 120])
tri.addatom('r',[0 0 0],'S',3/2,'label','MCr3','color','orange')
tri.gencoupling
plot(tri,'range',[2 2 1])

tri.addmatrix('value',1,'label','J','color','SteelBlue')
tri.addmatrix('value',diag([0 0 0.2]),'label','D','color','r')
tri.addcoupling('mat','J','bond',1)
tri.addaniso('D')
plot(tri,'range',[2 2 1])

tri.genmagstr('mode','helical','S',[0; 1; 0],'k',[1/3 1/3 0],'n', [0 0 1]);
plot(tri,'range',[2 2 1],'magColor','purple','baseShift',[0;-1;0],'atomLegend',false)

triSpec = tri.spinwave({[0 0 0] [1 1 0] 500});
triSpec = sw_neutron(triSpec);

figure
sw_plotspec(triSpec,'mode','disp','axLim',[0 7],'colormap',[0 0 0],'colorbar',false)

triSpec = sw_egrid(triSpec,'Evect',linspace(0,7,500),'component','Sperp');
figure
sw_plotspec(triSpec,'mode','color','axLim',[0 2],'dE',0.4)

triSpec = sw_egrid(triSpec,'Evect',linspace(0,7,500),'component',{'0.5*Sxx+0.5*Syy' 'Szz'});
figure
sw_plotspec(triSpec,'mode','color','axLim',[0 1],'dE',0.4)
sw_plotspec(triSpec,'mode','disp','axLim',[0 7],'colormap',[0 0 0],'colorbar',false,'lineStyle','-','legend',false)