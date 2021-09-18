AFsq = spinw;
AFsq.genlattice('lat_const',[3 3 6],'angled',[90 90 90],'spgr',0)
AFsq.addatom('r',[0 0 0],'S', 1,'label','Cu1','color','b')
AFsq.table('atom')
plot(AFsq)
swplot.zoom(1.5)

AFsq.gencoupling('maxDistance',5)
AFsq.table('bond',[])

AFsq.addmatrix('label','J1','value',   1,'color','red')
AFsq.addmatrix('label','J2','value',-0.1,'color','green')
AFsq.addcoupling('mat','J1','bond',1)
AFsq.addcoupling('mat','J2','bond',2)
plot(AFsq,'range',[2 2 0.5])

AFsq.genmagstr('mode','helical','k',[1/2 1/2 0],'n',[0 0 1], 'S',[1; 0; 0],'nExt',[1 1 1]);
disp('Magnetic structure:')
AFsq.table('mag')

AFsq.energy
plot(AFsq,'range',[2 2 1])

Qcorner = {[0 0 0] [1/2 0 0] [1/2 1/2 0] [0 0 0] 200};
sqSpec = AFsq.spinwave(Qcorner, 'hermit', false);
sqSpec = sw_neutron(sqSpec);
sqSpec = sw_egrid(sqSpec,'Evect',linspace(0,6.5,500));
figure
sw_plotspec(sqSpec,'mode',3,'dashed',true,'dE',0.4,'qLabel',{'\Gamma' 'X' 'M' '\Gamma'})
caxis([0 4])