sq = sw_model('squareAF',1,0);

% We add magnetic form factor after the model is defined. Using the same
% atom label and position as an existing atom in the model, the atom
% properties will be updated, no new atom is created using the
% spinw.addatom method. We will use the form factor of Ni2+ that has S=1.

sq.addatom('label','atom_1','r',[0 0 0],'formfact','MNi2+','S',1)
plot(sq)
swplot.zoom(2)

nQ = 201;
nE = 501;
Qhv = linspace(0,2,nQ);
Qkv = linspace(0,2,nQ);
Qlv = 0;
[Qh, Qk, Ql] = ndgrid(Qhv,Qkv,Qlv);

% Create a list of Q point, with dimensions of [3 nQ^2].
Q = [Qh(:) Qk(:) Ql(:)]';

spec = sq.spinwave(Q);

Ev = linspace(0,5,nE);
spec = sw_egrid(spec,'component','Sxx+Syy+Szz','Evect',Ev);
spec = sw_instrument(spec,'dE',0.1);

spec3D = reshape(spec.swConv,nE-1,nQ,nQ);

Ecut = [3.5 4.0]; %meV
Eidx = find(Ev>Ecut(1) & Ev<Ecut(2));
figure;
cut1 = squeeze(sum(spec3D(Eidx,:,:),1))/numel(Eidx)/(Ev(2)-Ev(1));
imagesc(Qhv,Qkv,cut1);
set(gca,'YDir','normal')
xlabel('(H 0 0) (r.l.u.)')
ylabel('(0 K 0) (r.l.u.)')
title('Spin wave spectrum at E = 3 meV, square lattice Heisenberg AF')
caxis([0 3])
colorbar