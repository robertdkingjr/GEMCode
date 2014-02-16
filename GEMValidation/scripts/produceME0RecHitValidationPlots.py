import sys

from ROOT import *

from cuts import *
from drawPlots import *

## run quiet mode
import sys
sys.argv.append( '-b' )

import ROOT 
ROOT.gROOT.SetBatch(1)

if __name__ == "__main__":  

  inputFile = '/afs/cern.ch/work/c/calabria/private/ME0Marcello2/CMSSW_6_2_0_SLHC7/src/GEMCode/GEMValidation/test/gem_localrec_ana.root'
  #outputFile = '/afs/cern.ch/work/c/calabria/private/ME0Marcello2/CMSSW_6_2_0_SLHC7/src/GEMCode/GEMValidation/test/gem_localrec_ana_tmp.root'
  targetDir = './'
  
  ## extension for figures - add more?
  ext = ".png"
  
  ## GEM system settings
  nregion = 2
  nlayer = 6
  npart = 1
  
  ## Trees
  analyzer = "GEMRecHitAnalyzer"
  recHits = "ME0RecHitTree"
  simHits = "ME0SimHits"
  simTracks = "TrackTree"

  ## Style
  gStyle.SetStatStyle(0);

  ## input
  file = TFile.Open(inputFile)
  if not file:
    sys.exit('Input ROOT file %s is missing.' %(inputFile))

  dirAna = file.Get(analyzer)
  if not dirAna:
    sys.exit('Directory %s does not exist.' %(dirAna))
    
  treeHits = dirAna.Get(recHits)
  if not treeHits:
    sys.exit('Tree %s does not exist.' %(treeHits))

  treeSimHits = dirAna.Get(simHits)
  if not treeSimHits:
    sys.exit('Tree %s does not exist.' %(treeSimHits))

  #fileOut = TFile.Open(outputFile, "RECREATE")

#-------------------------------------------------------------------------------------------------------------------------------------#

  draw_1D(targetDir, "recHitDX", ext, treeHits, "x^{local}_{sim} - x^{local}_{rec}; x^{local}_{sim} - x^{local}_{rec} [cm]; entries", 
	   "h_", "(100,-5,+5)", "(x - x_sim)", TCut(""), "");

  draw_1D(targetDir, "recHitDX_rm1_l1", ext, treeHits, "x^{local}_{sim} - x^{local}_{rec} region-1, layer1; x^{local}_{sim} - x^{local}_{rec} [cm]; entries", 
	   "h_", "(100,-5,+5)", "(x - x_sim)", AND(rm1,l1), "");
  draw_1D(targetDir, "recHitDX_rm1_l2", ext, treeHits, "x^{local}_{sim} - x^{local}_{rec} region-1, layer2; x^{local}_{sim} - x^{local}_{rec} [cm]; entries", 
	   "h_", "(100,-5,+5)", "(x - x_sim)", AND(rm1,l2), "");
  draw_1D(targetDir, "recHitDX_rm1_l3", ext, treeHits, "x^{local}_{sim} - x^{local}_{rec} region-1, layer3; x^{local}_{sim} - x^{local}_{rec} [cm]; entries", 
	   "h_", "(100,-5,+5)", "(x - x_sim)", AND(rm1,l3), "");
  draw_1D(targetDir, "recHitDX_rm1_l4", ext, treeHits, "x^{local}_{sim} - x^{local}_{rec} region-1, layer4; x^{local}_{sim} - x^{local}_{rec} [cm]; entries", 
	   "h_", "(100,-5,+5)", "(x - x_sim)", AND(rm1,l4), "");
  draw_1D(targetDir, "recHitDX_rm1_l5", ext, treeHits, "x^{local}_{sim} - x^{local}_{rec} region-1, layer5; x^{local}_{sim} - x^{local}_{rec} [cm]; entries", 
	   "h_", "(100,-5,+5)", "(x - x_sim)", AND(rm1,l5), "");
  draw_1D(targetDir, "recHitDX_rm1_l6", ext, treeHits, "x^{local}_{sim} - x^{local}_{rec} region-1, layer6; x^{local}_{sim} - x^{local}_{rec} [cm]; entries", 
	   "h_", "(100,-5,+5)", "(x - x_sim)", AND(rm1,l6), "");

  draw_1D(targetDir, "recHitDX_rp1_l1", ext, treeHits, "x^{local}_{sim} - x^{local}_{rec} region1, layer1; x^{local}_{sim} - x^{local}_{rec} [cm]; entries", 
	   "h_", "(100,-5,+5)", "(x - x_sim)", AND(rp1,l1), "");
  draw_1D(targetDir, "recHitDX_rp1_l2", ext, treeHits, "x^{local}_{sim} - x^{local}_{rec} region1, layer2; x^{local}_{sim} - x^{local}_{rec} [cm]; entries", 
	   "h_", "(100,-5,+5)", "(x - x_sim)", AND(rp1,l2), "");
  draw_1D(targetDir, "recHitDX_rp1_l3", ext, treeHits, "x^{local}_{sim} - x^{local}_{rec} region1, layer3; x^{local}_{sim} - x^{local}_{rec} [cm]; entries", 
	   "h_", "(100,-5,+5)", "(x - x_sim)", AND(rp1,l3), "");
  draw_1D(targetDir, "recHitDX_rp1_l4", ext, treeHits, "x^{local}_{sim} - x^{local}_{rec} region1, layer4; x^{local}_{sim} - x^{local}_{rec} [cm]; entries", 
	   "h_", "(100,-5,+5)", "(x - x_sim)", AND(rp1,l4), "");
  draw_1D(targetDir, "recHitDX_rp1_l5", ext, treeHits, "x^{local}_{sim} - x^{local}_{rec} region1, layer5; x^{local}_{sim} - x^{local}_{rec} [cm]; entries", 
	   "h_", "(100,-5,+5)", "(x - x_sim)", AND(rp1,l5), "");
  draw_1D(targetDir, "recHitDX_rp1_l6", ext, treeHits, "x^{local}_{sim} - x^{local}_{rec} region1, layer6; x^{local}_{sim} - x^{local}_{rec} [cm]; entries", 
	   "h_", "(100,-5,+5)", "(x - x_sim)", AND(rp1,l6), "");

#-------------------------------------------------------------------------------------------------------------------------------------#

  draw_1D(targetDir, "recHitPullLocalX", ext, treeHits, "(x^{local}_{sim} - x^{local}_{rec})/#sigma_{x}; (x^{local}_{sim} - x^{local}_{rec})/#sigma_{x}; entries", "h_", "(100,-5,+5)", "pull*sqrt(xErr)", TCut(""), "");

  draw_1D(targetDir, "recHitPullLocalX_rm1_l1", ext, treeHits, "(x^{local}_{sim} - x^{local}_{rec})/#sigma_{x} region-1, layer1; (x^{local}_{sim} - x^{local}_{rec})/#sigma_{x}; entries", "h_", "(100,-5,+5)", "pull*sqrt(xErr)", AND(rm1,l1), "");
  draw_1D(targetDir, "recHitPullLocalX_rm1_l2", ext, treeHits, "(x^{local}_{sim} - x^{local}_{rec})/#sigma_{x} region-1, layer2; (x^{local}_{sim} - x^{local}_{rec})/#sigma_{x}; entries", "h_", "(100,-5,+5)", "pull*sqrt(xErr)", AND(rm1,l2), "");
  draw_1D(targetDir, "recHitPullLocalX_rm1_l3", ext, treeHits, "(x^{local}_{sim} - x^{local}_{rec})/#sigma_{x} region-1, layer3; (x^{local}_{sim} - x^{local}_{rec})/#sigma_{x}; entries", "h_", "(100,-5,+5)", "pull*sqrt(xErr)", AND(rm1,l3), "");
  draw_1D(targetDir, "recHitPullLocalX_rm1_l4", ext, treeHits, "(x^{local}_{sim} - x^{local}_{rec})/#sigma_{x} region-1, layer4; (x^{local}_{sim} - x^{local}_{rec})/#sigma_{x}; entries", "h_", "(100,-5,+5)", "pull*sqrt(xErr)", AND(rm1,l4), "");
  draw_1D(targetDir, "recHitPullLocalX_rm1_l5", ext, treeHits, "(x^{local}_{sim} - x^{local}_{rec})/#sigma_{x} region-1, layer5; (x^{local}_{sim} - x^{local}_{rec})/#sigma_{x}; entries", "h_", "(100,-5,+5)", "pull*sqrt(xErr)", AND(rm1,l5), "");
  draw_1D(targetDir, "recHitPullLocalX_rm1_l6", ext, treeHits, "(x^{local}_{sim} - x^{local}_{rec})/#sigma_{x} region-1, layer6; (x^{local}_{sim} - x^{local}_{rec})/#sigma_{x}; entries", "h_", "(100,-5,+5)", "pull*sqrt(xErr)", AND(rm1,l6), "");

  draw_1D(targetDir, "recHitPullLocalX_rp1_l1", ext, treeHits, "(x^{local}_{sim} - x^{local}_{rec})/#sigma_{x} region1, layer1; (x^{local}_{sim} - x^{local}_{rec})/#sigma_{x}; entries", "h_", "(100,-5,+5)", "pull*sqrt(xErr)", AND(rp1,l1), "");
  draw_1D(targetDir, "recHitPullLocalX_rp1_l2", ext, treeHits, "(x^{local}_{sim} - x^{local}_{rec})/#sigma_{x} region1, layer2; (x^{local}_{sim} - x^{local}_{rec})/#sigma_{x}; entries", "h_", "(100,-5,+5)", "pull*sqrt(xErr)", AND(rp1,l2), "");
  draw_1D(targetDir, "recHitPullLocalX_rp1_l3", ext, treeHits, "(x^{local}_{sim} - x^{local}_{rec})/#sigma_{x} region1, layer3; (x^{local}_{sim} - x^{local}_{rec})/#sigma_{x}; entries", "h_", "(100,-5,+5)", "pull*sqrt(xErr)", AND(rp1,l3), "");
  draw_1D(targetDir, "recHitPullLocalX_rp1_l4", ext, treeHits, "(x^{local}_{sim} - x^{local}_{rec})/#sigma_{x} region1, layer4; (x^{local}_{sim} - x^{local}_{rec})/#sigma_{x}; entries", "h_", "(100,-5,+5)", "pull*sqrt(xErr)", AND(rp1,l4), "");
  draw_1D(targetDir, "recHitPullLocalX_rp1_l5", ext, treeHits, "(x^{local}_{sim} - x^{local}_{rec})/#sigma_{x} region1, layer5; (x^{local}_{sim} - x^{local}_{rec})/#sigma_{x}; entries", "h_", "(100,-5,+5)", "pull*sqrt(xErr)", AND(rp1,l5), "");
  draw_1D(targetDir, "recHitPullLocalX_rp1_l6", ext, treeHits, "(x^{local}_{sim} - x^{local}_{rec})/#sigma_{x} region1, layer6; (x^{local}_{sim} - x^{local}_{rec})/#sigma_{x}; entries", "h_", "(100,-5,+5)", "pull*sqrt(xErr)", AND(rp1,l6), "");

#-------------------------------------------------------------------------------------------------------------------------------------#

  draw_1D(targetDir, "recHitDPhi", ext, treeHits, "#phi_{rec} - #phi_{sim}; #phi_{rec} - #phi_{sim} [rad]; entries", 
	   "h_", "(100,-0.001,+0.001)", "(globalPhi - globalPhi_sim)", TCut(""), "");

  draw_1D(targetDir, "recHitDPhi_rm1_l1", ext, treeHits, "#phi_{rec} - #phi_{sim} region-1, layer1; #phi_{rec} - #phi_{sim} [rad]; entries", 
	   "h_", "(100,-0.001,+0.001)", "(globalPhi - globalPhi_sim)", AND(rm1,l1), "");
  draw_1D(targetDir, "recHitDPhi_rm1_l2", ext, treeHits, "#phi_{rec} - #phi_{sim} region-1, layer2; #phi_{rec} - #phi_{sim} [rad]; entries", 
	   "h_", "(100,-0.001,+0.001)", "(globalPhi - globalPhi_sim)", AND(rm1,l2), "");
  draw_1D(targetDir, "recHitDPhi_rm1_l3", ext, treeHits, "#phi_{rec} - #phi_{sim} region-1, layer3; #phi_{rec} - #phi_{sim} [rad]; entries", 
	   "h_", "(100,-0.001,+0.001)", "(globalPhi - globalPhi_sim)", AND(rm1,l3), "");
  draw_1D(targetDir, "recHitDPhi_rm1_l4", ext, treeHits, "#phi_{rec} - #phi_{sim} region-1, layer4; #phi_{rec} - #phi_{sim} [rad]; entries", 
	   "h_", "(100,-0.001,+0.001)", "(globalPhi - globalPhi_sim)", AND(rm1,l4), "");
  draw_1D(targetDir, "recHitDPhi_rm1_l5", ext, treeHits, "#phi_{rec} - #phi_{sim} region-1, layer5; #phi_{rec} - #phi_{sim} [rad]; entries", 
	   "h_", "(100,-0.001,+0.001)", "(globalPhi - globalPhi_sim)", AND(rm1,l5), "");
  draw_1D(targetDir, "recHitDPhi_rm1_l6", ext, treeHits, "#phi_{rec} - #phi_{sim} region-1, layer6; #phi_{rec} - #phi_{sim} [rad]; entries", 
	   "h_", "(100,-0.001,+0.001)", "(globalPhi - globalPhi_sim)", AND(rm1,l6), "");

  draw_1D(targetDir, "recHitDPhi_rp1_l1", ext, treeHits, "#phi_{rec} - #phi_{sim} region1, layer1; #phi_{rec} - #phi_{sim} [rad]; entries", 
	   "h_", "(100,-0.001,+0.001)", "(globalPhi - globalPhi_sim)", AND(rp1,l1), "");
  draw_1D(targetDir, "recHitDPhi_rp1_l2", ext, treeHits, "#phi_{rec} - #phi_{sim} region1, layer2; #phi_{rec} - #phi_{sim} [rad]; entries", 
	   "h_", "(100,-0.001,+0.001)", "(globalPhi - globalPhi_sim)", AND(rp1,l2), "");
  draw_1D(targetDir, "recHitDPhi_rp1_l3", ext, treeHits, "#phi_{rec} - #phi_{sim} region1, layer3; #phi_{rec} - #phi_{sim} [rad]; entries", 
	   "h_", "(100,-0.001,+0.001)", "(globalPhi - globalPhi_sim)", AND(rp1,l3), "");
  draw_1D(targetDir, "recHitDPhi_rp1_l4", ext, treeHits, "#phi_{rec} - #phi_{sim} region1, layer4; #phi_{rec} - #phi_{sim} [rad]; entries", 
	   "h_", "(100,-0.001,+0.001)", "(globalPhi - globalPhi_sim)", AND(rp1,l4), "");
  draw_1D(targetDir, "recHitDPhi_rp1_l5", ext, treeHits, "#phi_{rec} - #phi_{sim} region1, layer5; #phi_{rec} - #phi_{sim} [rad]; entries", 
	   "h_", "(100,-0.001,+0.001)", "(globalPhi - globalPhi_sim)", AND(rp1,l5), "");
  draw_1D(targetDir, "recHitDPhi_rp1_l6", ext, treeHits, "#phi_{rec} - #phi_{sim} region1, layer6; #phi_{rec} - #phi_{sim} [rad]; entries", 
	   "h_", "(100,-0.001,+0.001)", "(globalPhi - globalPhi_sim)", AND(rp1,l6), "");

#-------------------------------------------------------------------------------------------------------------------------------------#

  draw_geff2(targetDir, "recHitEfficiencyPerChamber_rm1_l1", ext, treeHits, treeSimHits, "Local Reco Efficiency vs. chamber : region-1, layer1;chamber", 
	   "h_", "(38,0,38)", "chamber", AND(rm1,l1),AND(rm1,l1), "P", kBlue);
  draw_geff2(targetDir, "recHitEfficiencyPerChamber_rm1_l2", ext, treeHits, treeSimHits, "Local Reco Efficiency vs. chamber : region-1, layer2;chamber", 
	   "h_", "(38,0,38)", "chamber", AND(rm1,l2),AND(rm1,l2), "P", kBlue);
  draw_geff2(targetDir, "recHitEfficiencyPerChamber_rm1_l3", ext, treeHits, treeSimHits, "Local Reco Efficiency vs. chamber : region-1, layer3;chamber", 
	   "h_", "(38,0,38)", "chamber", AND(rm1,l3),AND(rm1,l3), "P", kBlue);
  draw_geff2(targetDir, "recHitEfficiencyPerChamber_rm1_l4", ext, treeHits, treeSimHits, "Local Reco Efficiency vs. chamber : region-1, layer4;chamber", 
	   "h_", "(38,0,38)", "chamber", AND(rm1,l4),AND(rm1,l4), "P", kBlue);
  draw_geff2(targetDir, "recHitEfficiencyPerChamber_rm1_l5", ext, treeHits, treeSimHits, "Local Reco Efficiency vs. chamber : region-1, layer5;chamber", 
	   "h_", "(38,0,38)", "chamber", AND(rm1,l5),AND(rm1,l5), "P", kBlue);
  draw_geff2(targetDir, "recHitEfficiencyPerChamber_rm1_l6", ext, treeHits, treeSimHits, "Local Reco Efficiency vs. chamber : region-1, layer6;chamber", 
	   "h_", "(38,0,38)", "chamber", AND(rm1,l6),AND(rm1,l6), "P", kBlue);

  draw_geff2(targetDir, "recHitEfficiencyPerChamber_rp1_l1", ext, treeHits, treeSimHits, "Local Reco Efficiency vs. chamber : region+1, layer1;chamber", 
	   "h_", "(38,0,38)", "chamber", AND(rp1,l1),AND(rp1,l1), "P", kBlue);
  draw_geff2(targetDir, "recHitEfficiencyPerChamber_rp1_l2", ext, treeHits, treeSimHits, "Local Reco Efficiency vs. chamber : region+1, layer2;chamber", 
	   "h_", "(38,0,38)", "chamber", AND(rp1,l2),AND(rp1,l2), "P", kBlue);
  draw_geff2(targetDir, "recHitEfficiencyPerChamber_rp1_l3", ext, treeHits, treeSimHits, "Local Reco Efficiency vs. chamber : region+1, layer3;chamber", 
	   "h_", "(38,0,38)", "chamber", AND(rp1,l1),AND(rp1,l3), "P", kBlue);
  draw_geff2(targetDir, "recHitEfficiencyPerChamber_rp1_l4", ext, treeHits, treeSimHits, "Local Reco Efficiency vs. chamber : region+1, layer4;chamber", 
	   "h_", "(38,0,38)", "chamber", AND(rp1,l2),AND(rp1,l4), "P", kBlue);
  draw_geff2(targetDir, "recHitEfficiencyPerChamber_rp1_l5", ext, treeHits, treeSimHits, "Local Reco Efficiency vs. chamber : region+1, layer5;chamber", 
	   "h_", "(38,0,38)", "chamber", AND(rp1,l1),AND(rp1,l5), "P", kBlue);
  draw_geff2(targetDir, "recHitEfficiencyPerChamber_rp1_l6", ext, treeHits, treeSimHits, "Local Reco Efficiency vs. chamber : region+1, layer6;chamber", 
	   "h_", "(38,0,38)", "chamber", AND(rp1,l2),AND(rp1,l6), "P", kBlue);

#-------------------------------------------------------------------------------------------------------------------------------------#

  draw_occ(targetDir, "localrh_xy_rm1_l1", ext, treeHits, " ME0 RecHit occupancy: region-1, layer1;globalX [cm];globalY [cm]", 
	   "h_", "(120,-280,280,120,-280,280)", "globalY:globalX", AND(rm1,l1), "COLZ");
  draw_occ(targetDir, "localrh_xy_rm1_l2", ext, treeHits, " ME0 RecHit occupancy: region-1, layer2;globalX [cm];globalY [cm]", 
	   "h_", "(120,-280,280,120,-280,280)", "globalY:globalX", AND(rm1,l2), "COLZ");
  draw_occ(targetDir, "localrh_xy_rm1_l3", ext, treeHits, " ME0 RecHit occupancy: region-1, layer3;globalX [cm];globalY [cm]", 
	   "h_", "(120,-280,280,120,-280,280)", "globalY:globalX", AND(rm1,l3), "COLZ");
  draw_occ(targetDir, "localrh_xy_rm1_l4", ext, treeHits, " ME0 RecHit occupancy: region-1, layer4;globalX [cm];globalY [cm]", 
	   "h_", "(120,-280,280,120,-280,280)", "globalY:globalX", AND(rm1,l4), "COLZ");
  draw_occ(targetDir, "localrh_xy_rm1_l5", ext, treeHits, " ME0 RecHit occupancy: region-1, layer5;globalX [cm];globalY [cm]", 
	   "h_", "(120,-280,280,120,-280,280)", "globalY:globalX", AND(rm1,l5), "COLZ");
  draw_occ(targetDir, "localrh_xy_rm1_l6", ext, treeHits, " ME0 RecHit occupancy: region-1, layer6;globalX [cm];globalY [cm]", 
	   "h_", "(120,-280,280,120,-280,280)", "globalY:globalX", AND(rm1,l6), "COLZ");

  draw_occ(targetDir, "localrh_xy_rp1_l1", ext, treeHits, " ME0 RecHit occupancy: region+1, layer1;globalX [cm];globalY [cm]", 
	   "h_", "(120,-280,280,120,-280,280)", "globalY:globalX", AND(rp1,l1), "COLZ");
  draw_occ(targetDir, "localrh_xy_rp1_l2", ext, treeHits, " ME0 RecHit occupancy: region+1, layer2;globalX [cm];globalY [cm]", 
	   "h_", "(120,-280,280,120,-280,280)", "globalY:globalX", AND(rm1,l2), "COLZ");
  draw_occ(targetDir, "localrh_xy_rp1_l3", ext, treeHits, " ME0 RecHit occupancy: region+1, layer3;globalX [cm];globalY [cm]", 
	   "h_", "(120,-280,280,120,-280,280)", "globalY:globalX", AND(rp1,l3), "COLZ");
  draw_occ(targetDir, "localrh_xy_rp1_l4", ext, treeHits, " ME0 RecHit occupancy: region+1, layer4;globalX [cm];globalY [cm]", 
	   "h_", "(120,-280,280,120,-280,280)", "globalY:globalX", AND(rm1,l4), "COLZ");
  draw_occ(targetDir, "localrh_xy_rp1_l5", ext, treeHits, " ME0 RecHit occupancy: region+1, layer5;globalX [cm];globalY [cm]", 
	   "h_", "(120,-280,280,120,-280,280)", "globalY:globalX", AND(rp1,l5), "COLZ");
  draw_occ(targetDir, "localrh_xy_rp1_l6", ext, treeHits, " ME0 RecHit occupancy: region+1, layer6;globalX [cm];globalY [cm]", 
	   "h_", "(120,-280,280,120,-280,280)", "globalY:globalX", AND(rm1,l6), "COLZ");
  
  draw_occ(targetDir, "localrh_zr_rm1", ext, treeHits, " ME0 RecHit occupancy: region-1;globalZ [cm];globalR [cm]", 
	   "h_", "(80,-555,-515,120,20,280)", "sqrt(globalX*globalX+globalY*globalY):globalZ", rm1, "COLZ");
  draw_occ(targetDir, "localrh_zr_rp1", ext, treeHits, " ME0 RecHit occupancy: region1;globalZ [cm];globalR [cm]", 
	   "h_", "(80,515,555,120,20,280)", "sqrt(globalX*globalX+globalY*globalY):globalZ", rp1, "COLZ");

  file.Close()
  #fileOut.Close()
  
