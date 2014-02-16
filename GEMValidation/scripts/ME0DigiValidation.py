from ROOT import *

from cuts import *
from drawPlots import *

## run quiet mode
import sys
sys.argv.append( '-b' )

import ROOT 
ROOT.gROOT.SetBatch(1)

#_______________________________________________________________________________
def me0DigiOccupancyXY(plotter):

  draw_occ(plotter.targetDir, "strip_dg_xy_rm1_l1", plotter.ext, plotter.treeME0Digis, "Digi occupancy: region-1, layer1; globalX [cm]; globalY [cm]", 
	   "h_", "(120,-280,280,120,-280,280)", "g_x:g_y", AND(rm1,l1), "COLZ")
  draw_occ(plotter.targetDir, "strip_dg_xy_rm1_l2", plotter.ext, plotter.treeME0Digis, "Digi occupancy: region-1, layer2; globalX [cm]; globalY [cm]", 
	   "h_", "(120,-280,280,120,-280,280)", "g_x:g_y", AND(rm1,l2), "COLZ")
  draw_occ(plotter.targetDir, "strip_dg_xy_rm1_l3", plotter.ext, plotter.treeME0Digis, "Digi occupancy: region-1, layer3; globalX [cm]; globalY [cm]", 
	   "h_", "(120,-280,280,120,-280,280)", "g_x:g_y", AND(rm1,l3), "COLZ")
  draw_occ(plotter.targetDir, "strip_dg_xy_rm1_l4", plotter.ext, plotter.treeME0Digis, "Digi occupancy: region-1, layer4; globalX [cm]; globalY [cm]", 
	   "h_", "(120,-280,280,120,-280,280)", "g_x:g_y", AND(rm1,l4), "COLZ")
  draw_occ(plotter.targetDir, "strip_dg_xy_rm1_l5", plotter.ext, plotter.treeME0Digis, "Digi occupancy: region-1, layer5; globalX [cm]; globalY [cm]", 
	   "h_", "(120,-280,280,120,-280,280)", "g_x:g_y", AND(rm1,l5), "COLZ")
  draw_occ(plotter.targetDir, "strip_dg_xy_rm1_l6", plotter.ext, plotter.treeME0Digis, "Digi occupancy: region-1, layer6; globalX [cm]; globalY [cm]", 
	   "h_", "(120,-280,280,120,-280,280)", "g_x:g_y", AND(rm1,l6), "COLZ")


  draw_occ(plotter.targetDir, "strip_dg_xy_rp1_l1", plotter.ext, plotter.treeME0Digis, "Digi occupancy: region1, layer1; globalX [cm]; globalY [cm]", 
	   "h_", "(120,-280,280,120,-280,280)", "g_x:g_y", AND(rp1,l1), "COLZ")
  draw_occ(plotter.targetDir, "strip_dg_xy_rp1_l2", plotter.ext, plotter.treeME0Digis, "Digi occupancy: region1, layer2; globalX [cm]; globalY [cm]", 
	   "h_", "(120,-280,280,120,-280,280)", "g_x:g_y", AND(rp1,l2), "COLZ") 
  draw_occ(plotter.targetDir, "strip_dg_xy_rp1_l3", plotter.ext, plotter.treeME0Digis, "Digi occupancy: region1, layer3; globalX [cm]; globalY [cm]", 
	   "h_", "(120,-280,280,120,-280,280)", "g_x:g_y", AND(rp1,l3), "COLZ")
  draw_occ(plotter.targetDir, "strip_dg_xy_rp1_l4", plotter.ext, plotter.treeME0Digis, "Digi occupancy: region1, layer4; globalX [cm]; globalY [cm]", 
	   "h_", "(120,-280,280,120,-280,280)", "g_x:g_y", AND(rp1,l4), "COLZ") 
  draw_occ(plotter.targetDir, "strip_dg_xy_rp1_l5", plotter.ext, plotter.treeME0Digis, "Digi occupancy: region1, layer5; globalX [cm]; globalY [cm]", 
	   "h_", "(120,-280,280,120,-280,280)", "g_x:g_y", AND(rp1,l5), "COLZ")
  draw_occ(plotter.targetDir, "strip_dg_xy_rp1_l6", plotter.ext, plotter.treeME0Digis, "Digi occupancy: region1, layer6; globalX [cm]; globalY [cm]", 
	   "h_", "(120,-280,280,120,-280,280)", "g_x:g_y", AND(rp1,l6), "COLZ")

#_______________________________________________________________________________
def me0DigiOccupancyRZ(plotter):
  draw_occ(plotter.targetDir, "strip_dg_zr_rm1", plotter.ext, plotter.treeME0Digis, "Digi occupancy: region-1; globalZ [cm]; globalR [cm]", 
           "h_", "(80,-555,-515,120,20,280)", "g_r:g_z", rm1, "COLZ")
  draw_occ(plotter.targetDir, "strip_dg_zr_rp1", plotter.ext, plotter.treeME0Digis, "Digi occupancy: region1; globalZ [cm]; globalR [cm]", 
           "h_", "(80,515,555,120,20,280)", "g_r:g_z", rp1, "COLZ")

#_______________________________________________________________________________
def me0DigiDeltaX(plotter):
  draw_1D(plotter.targetDir, "digiDX", plotter.ext, plotter.treeME0Digis, "x^{digi}_{sim} - x^{digi}_{rec}; x^{digi}_{sim} - x^{digi}_{rec} [cm]; entries", 
	   "h_", "(100,-10,+10)", "(x - x_sim)", TCut(""), "");

  draw_1D(plotter.targetDir, "digiDX_rm1_l1", plotter.ext, plotter.treeME0Digis, "x^{digi}_{sim} - x^{digi}_{rec} region-1, layer1; x^{digi}_{sim} - x^{digi}_{rec} [cm]; entries", "h_", "(100,-10,+10)", "(x - x_sim)", AND(rm1,l1), "");
  draw_1D(plotter.targetDir, "digiDX_rm1_l2", plotter.ext, plotter.treeME0Digis, "x^{digi}_{sim} - x^{digi}_{rec} region-1, layer2; x^{digi}_{sim} - x^{digi}_{rec} [cm]; entries", "h_", "(100,-10,+10)", "(x - x_sim)", AND(rm1,l2), "");
  draw_1D(plotter.targetDir, "digiDX_rm1_l3", plotter.ext, plotter.treeME0Digis, "x^{digi}_{sim} - x^{digi}_{rec} region-1, layer3; x^{digi}_{sim} - x^{digi}_{rec} [cm]; entries", "h_", "(100,-10,+10)", "(x - x_sim)", AND(rm1,l3), "");
  draw_1D(plotter.targetDir, "digiDX_rm1_l4", plotter.ext, plotter.treeME0Digis, "x^{digi}_{sim} - x^{digi}_{rec} region-1, layer4; x^{digi}_{sim} - x^{digi}_{rec} [cm]; entries", "h_", "(100,-10,+10)", "(x - x_sim)", AND(rm1,l4), "");
  draw_1D(plotter.targetDir, "digiDX_rm1_l5", plotter.ext, plotter.treeME0Digis, "x^{digi}_{sim} - x^{digi}_{rec} region-1, layer5; x^{digi}_{sim} - x^{digi}_{rec} [cm]; entries", "h_", "(100,-10,+10)", "(x - x_sim)", AND(rm1,l5), "");
  draw_1D(plotter.targetDir, "digiDX_rm1_l6", plotter.ext, plotter.treeME0Digis, "x^{digi}_{sim} - x^{digi}_{rec} region-1, layer6; x^{digi}_{sim} - x^{digi}_{rec} [cm]; entries", "h_", "(100,-10,+10)", "(x - x_sim)", AND(rm1,l6), "");

  draw_1D(plotter.targetDir, "digiDX_rp1_l1", plotter.ext, plotter.treeME0Digis, "x^{digi}_{sim} - x^{digi}_{rec} region1, layer1; x^{digi}_{sim} - x^{digi}_{rec} [cm]; entries", "h_", "(100,-10,+10)", "(x - x_sim)", AND(rp1,l1), "");
  draw_1D(plotter.targetDir, "digiDX_rp1_l2", plotter.ext, plotter.treeME0Digis, "x^{digi}_{sim} - x^{digi}_{rec} region1, layer2; x^{digi}_{sim} - x^{digi}_{rec} [cm]; entries", "h_", "(100,-10,+10)", "(x - x_sim)", AND(rp1,l2), "");
  draw_1D(plotter.targetDir, "digiDX_rp1_l3", plotter.ext, plotter.treeME0Digis, "x^{digi}_{sim} - x^{digi}_{rec} region1, layer3; x^{digi}_{sim} - x^{digi}_{rec} [cm]; entries", "h_", "(100,-10,+10)", "(x - x_sim)", AND(rp1,l3), "");
  draw_1D(plotter.targetDir, "digiDX_rp1_l4", plotter.ext, plotter.treeME0Digis, "x^{digi}_{sim} - x^{digi}_{rec} region1, layer4; x^{digi}_{sim} - x^{digi}_{rec} [cm]; entries", "h_", "(100,-10,+10)", "(x - x_sim)", AND(rp1,l4), "");
  draw_1D(plotter.targetDir, "digiDX_rp1_l5", plotter.ext, plotter.treeME0Digis, "x^{digi}_{sim} - x^{digi}_{rec} region1, layer5; x^{digi}_{sim} - x^{digi}_{rec} [cm]; entries", "h_", "(100,-10,+10)", "(x - x_sim)", AND(rp1,l5), "");
  draw_1D(plotter.targetDir, "digiDX_rp1_l6", plotter.ext, plotter.treeME0Digis, "x^{digi}_{sim} - x^{digi}_{rec} region1, layer6; x^{digi}_{sim} - x^{digi}_{rec} [cm]; entries", "h_", "(100,-10,+10)", "(x - x_sim)", AND(rp1,l6), "");

