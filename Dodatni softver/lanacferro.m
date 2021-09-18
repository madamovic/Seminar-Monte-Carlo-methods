FMchain = spinw;
FMchain.genlattice('lat_const',[3 8 8],'angled',[90 90 90])
FMchain.addatom('r', [0 0 0],'S', 1,'label','MCu1','color','blue')
FMchain.plot('range',[3 1 1])

FMchain.gencoupling('maxDistance',7)

% list the 1st and 2nd neighbor bonds
FMchain.table('bond',1:2)

FMchain.addmatrix('value',-eye(3),'label','Ja','color','green')
FMchain.addcoupling('mat','Ja','bond',1);
plot(FMchain,'range',[3 0.2 0.2],'cellMode','none','baseMode','none')

FMchain.genmagstr('mode','direct', 'k',[0 0 0],'n',[1 0 0],'S',[0; 1; 0]);

disp('Magnetic structure:')
FMchain.table('mag')
plot(FMchain,'range',[3 0.9 0.9],'baseMode','none','cellMode','none')

FMchain.energy
assert(FMchain.energy == -1)

FMspec = FMchain.spinwave({[0 0 0] [1 0 0]},'hermit',false);
FMspec = sw_neutron(FMspec);
FMspec = sw_egrid(FMspec,'component','Sperp');

figure;
subplot(2,1,1)
sw_plotspec(FMspec,'mode',1,'colorbar',false)
axis([0 1 0 5])
subplot(2,1,2)
sw_plotspec(FMspec,'mode',2)
axis([0 1 0 2])
swplot.subfigure(1,3,1)