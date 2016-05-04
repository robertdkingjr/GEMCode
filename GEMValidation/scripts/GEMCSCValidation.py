import sys

from ROOT import *

from cuts import *
#from drawPlots import *
from Helpers import *
from drawPlots import draw_1D
from drawPlots import draw_occ as draw_2D
from drawPlots import draw_occ_logx as draw_2D_logx
from drawPlots import draw_occ_fit as draw_2D_fit

## run quiet mode
import sys
sys.argv.append( '-b' )

import ROOT 
ROOT.gROOT.SetBatch(1)

#_______________________________________________________________________________
def GEMCSCresolution(plotter):
    
    ## 1D resolution
    draw_1D(plotter.targetDir, "gem_csc_sim_reco_resolution_ME11_even_1D_lowPt", plotter.ext, plotter.treeDelta, ";dphi_gem_sh_l1_csc_sh_l1-dphi_gem_rh_csc_seg", "h_", "(200,-0.01,0.01)", 
            "dphi_gem_sh_l1_csc_sh_l1-dphi_gem_rh_csc_seg","station==1 && (ring==1 || ring==4) && odd==0 && pt<=10")
    draw_1D(plotter.targetDir, "gem_csc_sim_reco_resolution_ME11_odd_1D_lowPt", plotter.ext, plotter.treeDelta, ";dphi_gem_sh_l1_csc_sh_l1-dphi_gem_rh_csc_seg", "h_", "(200,-0.01,0.01)", 
            "dphi_gem_sh_l1_csc_sh_l1-dphi_gem_rh_csc_seg","station==1 && (ring==1 || ring==4) && odd==1 && pt<=10")
    draw_1D(plotter.targetDir, "gem_csc_sim_reco_resolution_ME21_even_1D_lowPt", plotter.ext, plotter.treeDelta, ";dphi_gem_sh_l1_csc_sh_l1-dphi_gem_rh_csc_seg", "h_", "(200,-0.01,0.01)", 
            "dphi_gem_sh_l1_csc_sh_l1-dphi_gem_rh_csc_seg","station==2 && ring==1 && odd==0 && pt<=10")
    draw_1D(plotter.targetDir, "gem_csc_sim_reco_resolution_ME21_odd_1D_lowPt", plotter.ext, plotter.treeDelta, ";dphi_gem_sh_l1_csc_sh_l1-dphi_gem_rh_csc_seg", "h_", "(200,-0.01,0.01)", 
            "dphi_gem_sh_l1_csc_sh_l1-dphi_gem_rh_csc_seg","station==2 && ring==1 && odd==1 && pt<=10")

    draw_1D(plotter.targetDir, "gem_csc_sim_reco_resolution_ME11_even_1D_highPt", plotter.ext, plotter.treeDelta, ";dphi_gem_sh_l1_csc_sh_l1-dphi_gem_rh_csc_seg", "h_", "(200,-0.01,0.01)", 
            "dphi_gem_sh_l1_csc_sh_l1-dphi_gem_rh_csc_seg","station==1 && (ring==1 || ring==4) && odd==0 && pt>=30")
    draw_1D(plotter.targetDir, "gem_csc_sim_reco_resolution_ME11_odd_1D_highPt", plotter.ext, plotter.treeDelta, ";dphi_gem_sh_l1_csc_sh_l1-dphi_gem_rh_csc_seg", "h_", "(200,-0.01,0.01)", 
            "dphi_gem_sh_l1_csc_sh_l1-dphi_gem_rh_csc_seg","station==1 && (ring==1 || ring==4) && odd==1 && pt>=30")
    draw_1D(plotter.targetDir, "gem_csc_sim_reco_resolution_ME21_even_1D_highPt", plotter.ext, plotter.treeDelta, ";dphi_gem_sh_l1_csc_sh_l1-dphi_gem_rh_csc_seg", "h_", "(200,-0.01,0.01)", 
            "dphi_gem_sh_l1_csc_sh_l1-dphi_gem_rh_csc_seg","station==2 && ring==1 && odd==0 && pt>=30")
    draw_1D(plotter.targetDir, "gem_csc_sim_reco_resolution_ME21_odd_1D_highPt", plotter.ext, plotter.treeDelta, ";dphi_gem_sh_l1_csc_sh_l1-dphi_gem_rh_csc_seg", "h_", "(200,-0.01,0.01)", 
            "dphi_gem_sh_l1_csc_sh_l1-dphi_gem_rh_csc_seg","station==2 && ring==1 && odd==1 && pt>=30")

    ## 2D resolution
    draw_2D_fit(plotter.targetDir, "gem_csc_sim_vs_reco_resolution_ME11_even_2D_lowPt", plotter.ext, plotter.treeDelta, "; #Delta#Phi_{GEM-CSC}^{RECO};#Delta#Phi_{GEM-CSC}^{SIM}", 
            "h_", "(100,-0.02,0.02,100,-0.02,0.02)", "dphi_gem_rh_csc_seg:dphi_gem_sh_l1_csc_sh_l1","station==1 && (ring==1 || ring==4) && odd==0 && pt<=10","COLZ")
    draw_2D_fit(plotter.targetDir, "gem_csc_sim_vs_reco_resolution_ME11_odd_2D_lowPt", plotter.ext, plotter.treeDelta, "; #Delta#Phi_{GEM-CSC}^{RECO};#Delta#Phi_{GEM-CSC}^{SIM}", 
            "h_", "(100,-0.02,0.02,100,-0.02,0.02)", "dphi_gem_rh_csc_seg:dphi_gem_sh_l1_csc_sh_l1","station==1 && (ring==1 || ring==4) && odd==1 && pt<=10","COLZ")

    draw_2D_fit(plotter.targetDir, "gem_csc_sim_vs_reco_resolution_ME11_even_2D_highPt", plotter.ext, plotter.treeDelta, "; #Delta#Phi_{GEM-CSC}^{RECO};#Delta#Phi_{GEM-CSC}^{SIM}", 
            "h_", "(100,-0.02,0.02,100,-0.02,0.02)", "dphi_gem_rh_csc_seg:dphi_gem_sh_l1_csc_sh_l1","station==1 && (ring==1 || ring==4) && odd==0 && pt>=30","COLZ")
    draw_2D_fit(plotter.targetDir, "gem_csc_sim_vs_reco_resolution_ME11_odd_2D_highPt", plotter.ext, plotter.treeDelta, "; #Delta#Phi_{GEM-CSC}^{RECO};#Delta#Phi_{GEM-CSC}^{SIM}", 
            "h_", "(100,-0.003,0.003,100,-0.02,0.02)", "dphi_gem_rh_csc_seg:dphi_gem_sh_l1_csc_sh_l1","station==1 && (ring==1 || ring==4) && odd==1 && pt>=30","COLZ")

    draw_2D_fit(plotter.targetDir, "gem_csc_sim_vs_reco_resolution_ME21_even_2D_lowPt", plotter.ext, plotter.treeDelta, "; #Delta#Phi_{GEM-CSC}^{RECO};#Delta#Phi_{GEM-CSC}^{SIM}", 
            "h_", "(100,-0.02,0.02,100,-0.02,0.02)", "dphi_gem_rh_csc_seg:dphi_gem_sh_l1_csc_sh_l1","station==2 && ring==1 && odd==0 && pt<=10","COLZ")
    draw_2D_fit(plotter.targetDir, "gem_csc_sim_vs_reco_resolution_ME21_odd_2D_lowPt", plotter.ext, plotter.treeDelta, "; #Delta#Phi_{GEM-CSC}^{RECO};#Delta#Phi_{GEM-CSC}^{SIM}", 
            "h_", "(100,-0.02,0.02,100,-0.02,0.02)", "dphi_gem_rh_csc_seg:dphi_gem_sh_l1_csc_sh_l1","station==2 && ring==1 && odd==1 && pt<=10","COLZ")

    draw_2D_fit(plotter.targetDir, "gem_csc_sim_vs_reco_resolution_ME21_even_2D_highPt", plotter.ext, plotter.treeDelta, "; #Delta#Phi_{GEM-CSC}^{RECO};#Delta#Phi_{GEM-CSC}^{SIM}", 
            "h_", "(100,-0.02,0.02,100,-0.02,0.02)", "dphi_gem_rh_csc_seg:dphi_gem_sh_l1_csc_sh_l1","station==2 && ring==1 && odd==0 && pt>=30","COLZ")
    draw_2D_fit(plotter.targetDir, "gem_csc_sim_vs_reco_resolution_ME21_odd_2D_highPt", plotter.ext, plotter.treeDelta, "; #Delta#Phi_{GEM-CSC}^{ RECO};#Delta#Phi_{GEM-CSC}^{SIM}", 
            "h_", "(100,-0.02,0.02,100,-0.02,0.02)", "dphi_gem_rh_csc_seg:dphi_gem_sh_l1_csc_sh_l1","station==2 && ring==1 && odd==1 && pt>=30","COLZ")



    draw_2D_fit(plotter.targetDir, "gem_csc_sim_vs_reco_resolution_ME11_even_2D", plotter.ext, plotter.treeDelta, ";#Delta#Phi_{GEM-CSC}^{SIM}; #Delta#Phi_{GEM-CSC}^{RECO}", 
            "h_", "(100,-0.02,0.02,100,-0.02,0.02)", "dphi_gem_rh_csc_seg:dphi_gem_sh_l1_csc_sh_l1","station==1 && (ring==1 || ring==4) && odd==0","COLZ")
    draw_2D_fit(plotter.targetDir, "gem_csc_sim_vs_reco_resolution_ME11_odd_2D", plotter.ext, plotter.treeDelta, ";#Delta#Phi_{GEM-CSC}^{SIM}; #Delta#Phi_{GEM-CSC}^{RECO}", 
            "h_", "(100,-0.02,0.02,100,-0.02,0.02)", "dphi_gem_rh_csc_seg:dphi_gem_sh_l1_csc_sh_l1","station==1 && (ring==1 || ring==4) && odd==1","COLZ")

    draw_2D_fit(plotter.targetDir, "gem_csc_sim_vs_reco_resolution_ME21_even_2D", plotter.ext, plotter.treeDelta, ";#Delta#Phi_{GEM-CSC}^{SIM}; #Delta#Phi_{GEM-CSC}^{RECO}", 
            "h_", "(100,-0.02,0.02,100,-0.02,0.02)", "dphi_gem_rh_csc_seg:dphi_gem_sh_l1_csc_sh_l1","station==2 && ring==1 && odd==0","COLZ")
    draw_2D_fit(plotter.targetDir, "gem_csc_sim_vs_reco_resolution_ME21_odd_2D", plotter.ext, plotter.treeDelta, ";#Delta#Phi_{GEM-CSC}^{SIM}; #Delta#Phi_{GEM-CSC}^{RECO}", 
            "h_", "(100,-0.02,0.02,100,-0.02,0.02)", "dphi_gem_rh_csc_seg:dphi_gem_sh_l1_csc_sh_l1","station==2 && ring==1 && odd==1","COLZ")




    draw_2D_fit(plotter.targetDir, "gem_csc_sim_reco_resolution_ME11_even_2D_lowPt", plotter.ext, plotter.treeDelta, ";#Delta#Phi_{GEM-CSC}^{SIM}; #Delta#Phi_{GEM-CSC}^{RECO} - #Delta#Phi_{GEM-CSC}^{SIM}", 
            "h_", "(100,-0.02,0.02,100,-0.02,0.02)", "dphi_gem_rh_csc_seg-dphi_gem_sh_l1_csc_sh_l1:dphi_gem_sh_l1_csc_sh_l1","station==1 && (ring==1 || ring==4) && odd==0 && pt<=10","COLZ")
    draw_2D_fit(plotter.targetDir, "gem_csc_sim_reco_resolution_ME11_odd_2D_lowPt", plotter.ext, plotter.treeDelta, ";#Delta#Phi_{GEM-CSC}^{SIM}; #Delta#Phi_{GEM-CSC}^{RECO} - #Delta#Phi_{GEM-CSC}^{SIM}", 
            "h_", "(100,-0.02,0.02,100,-0.02,0.02)", "dphi_gem_rh_csc_seg-dphi_gem_sh_l1_csc_sh_l1:dphi_gem_sh_l1_csc_sh_l1","station==1 && (ring==1 || ring==4) && odd==1 && pt<=10","COLZ")

    draw_2D_fit(plotter.targetDir, "gem_csc_sim_reco_resolution_ME11_even_2D_highPt", plotter.ext, plotter.treeDelta, ";#Delta#Phi_{GEM-CSC}^{SIM}; #Delta#Phi_{GEM-CSC}^{RECO} - #Delta#Phi_{GEM-CSC}^{SIM}", 
            "h_", "(100,-0.02,0.02,100,-0.02,0.02)", "dphi_gem_rh_csc_seg-dphi_gem_sh_l1_csc_sh_l1:dphi_gem_sh_l1_csc_sh_l1","station==1 && (ring==1 || ring==4) && odd==0 && pt>=30","COLZ")
    draw_2D_fit(plotter.targetDir, "gem_csc_sim_reco_resolution_ME11_odd_2D_highPt", plotter.ext, plotter.treeDelta, ";#Delta#Phi_{GEM-CSC}^{SIM}; #Delta#Phi_{GEM-CSC}^{RECO} - #Delta#Phi_{GEM-CSC}^{SIM}", 
            "h_", "(100,-0.003,0.003,100,-0.02,0.02)", "dphi_gem_rh_csc_seg-dphi_gem_sh_l1_csc_sh_l1:dphi_gem_sh_l1_csc_sh_l1","station==1 && (ring==1 || ring==4) && odd==1 && pt>=30","COLZ")

    draw_2D_fit(plotter.targetDir, "gem_csc_sim_reco_resolution_ME21_even_2D_lowPt", plotter.ext, plotter.treeDelta, ";#Delta#Phi_{GEM-CSC}^{SIM}; #Delta#Phi_{GEM-CSC}^{RECO} - #Delta#Phi_{GEM-CSC}^{SIM}", 
            "h_", "(100,-0.02,0.02,100,-0.02,0.02)", "dphi_gem_rh_csc_seg-dphi_gem_sh_l1_csc_sh_l1:dphi_gem_sh_l1_csc_sh_l1","station==2 && ring==1 && odd==0 && pt<=10","COLZ")
    draw_2D_fit(plotter.targetDir, "gem_csc_sim_reco_resolution_ME21_odd_2D_lowPt", plotter.ext, plotter.treeDelta, ";#Delta#Phi_{GEM-CSC}^{SIM}; #Delta#Phi_{GEM-CSC}^{RECO} - #Delta#Phi_{GEM-CSC}^{SIM}", 
            "h_", "(100,-0.02,0.02,100,-0.02,0.02)", "dphi_gem_rh_csc_seg-dphi_gem_sh_l1_csc_sh_l1:dphi_gem_sh_l1_csc_sh_l1","station==2 && ring==1 && odd==1 && pt<=10","COLZ")

    draw_2D_fit(plotter.targetDir, "gem_csc_sim_reco_resolution_ME21_even_2D_highPt", plotter.ext, plotter.treeDelta, ";#Delta#Phi_{GEM-CSC}^{SIM}; #Delta#Phi_{GEM-CSC}^{RECO} - #Delta#Phi_{GEM-CSC}^{SIM}", 
            "h_", "(100,-0.02,0.02,100,-0.02,0.02)", "dphi_gem_rh_csc_seg-dphi_gem_sh_l1_csc_sh_l1:dphi_gem_sh_l1_csc_sh_l1","station==2 && ring==1 && odd==0 && pt>=30","COLZ")
    draw_2D_fit(plotter.targetDir, "gem_csc_sim_reco_resolution_ME21_odd_2D_highPt", plotter.ext, plotter.treeDelta, ";#Delta#Phi_{GEM-CSC}^{SIM}; #Delta#Phi_{GEM-CSC}^{RECO} - #Delta#Phi_{GEM-CSC}^{SIM}", 
            "h_", "(100,-0.02,0.02,100,-0.02,0.02)", "dphi_gem_rh_csc_seg-dphi_gem_sh_l1_csc_sh_l1:dphi_gem_sh_l1_csc_sh_l1","station==2 && ring==1 && odd==1 && pt>=30","COLZ")



    ## 1D resolution vs sim muon pt
    draw_2D(plotter.targetDir, "gem_csc_sim_reco_resolution_ME11_even_2D_vsPt", plotter.ext, plotter.treeDelta, ";p_{T} [GeV];#Delta#Phi_{GEM-CSC}^{RECO} - #Delta#Phi_{GEM-CSC}^{SIM}", 
            "h_", "(50,0,50,200,-0.02,0.02)", "dphi_gem_rh_csc_seg-dphi_gem_sh_l1_csc_sh_l1:pt","station==1 && (ring==1 || ring==4) && odd==0","COLZ") 
    draw_2D(plotter.targetDir, "gem_csc_sim_reco_resolution_ME11_odd_2D_vsPt", plotter.ext, plotter.treeDelta, ";p_{T} [GeV];#Delta#Phi_{GEM-CSC}^{RECO} - #Delta#Phi_{GEM-CSC}^{SIM}", 
            "h_", "(50,0,50,200,-0.02,0.02)", "dphi_gem_rh_csc_seg-dphi_gem_sh_l1_csc_sh_l1:pt","station==1 && (ring==1 || ring==4) && odd==1","COLZ")

    draw_2D(plotter.targetDir, "gem_csc_sim_reco_resolution_ME21_even_2D_vsPt", plotter.ext, plotter.treeDelta, ";p_{T} [GeV];#Delta#Phi_{GEM-CSC}^{RECO} - #Delta#Phi_{GEM-CSC}^{SIM}", 
            "h_", "(50,0,50,200,-0.02,0.02)", "dphi_gem_rh_csc_seg-dphi_gem_sh_l1_csc_sh_l1:pt","station==2 && ring==1 && odd==0","COLZ")
    draw_2D(plotter.targetDir, "gem_csc_sim_reco_resolution_ME21_odd_2D_vsPt", plotter.ext, plotter.treeDelta, ";p_{T} [GeV];#Delta#Phi_{GEM-CSC}^{RECO} - #Delta#Phi_{GEM-CSC}^{SIM}", 
            "h_", "(50,0,50,200,-0.02,0.02)", "dphi_gem_rh_csc_seg-dphi_gem_sh_l1_csc_sh_l1:pt","station==2 && ring==1 && odd==1","COLZ")
    
    ## 1D resolution vs sim muon q/pt
    draw_2D(plotter.targetDir, "gem_csc_sim_reco_resolution_ME11_even_2D_vsQoverPt", plotter.ext, plotter.treeDelta, ";q/p_{T} [1/GeV];#Delta#Phi_{GEM-CSC}^{RECO} - #Delta#Phi_{GEM-CSC}^{SIM}", 
            "h_", "(50,0.02,0.1,200,-0.02,0.02)", "dphi_gem_rh_csc_seg-dphi_gem_sh_l1_csc_sh_l1:charge/pt","station==1 && (ring==1 || ring==4) && odd==0","COLZ") 
    draw_2D(plotter.targetDir, "gem_csc_sim_reco_resolution_ME11_odd_2D_vsQoverPt", plotter.ext, plotter.treeDelta, ";q/p_{T} [1/GeV];#Delta#Phi_{GEM-CSC}^{RECO} - #Delta#Phi_{GEM-CSC}^{SIM}", 
            "h_", "(50,0.02,0.1,200,-0.02,0.02)", "dphi_gem_rh_csc_seg-dphi_gem_sh_l1_csc_sh_l1:charge/pt","station==1 && (ring==1 || ring==4) && odd==1","COLZ")

    draw_2D(plotter.targetDir, "gem_csc_sim_reco_resolution_ME21_even_2D_vsQoverPt", plotter.ext, plotter.treeDelta, ";q/p_{T} [1/GeV];#Delta#Phi_{GEM-CSC}^{RECO} - #Delta#Phi_{GEM-CSC}^{SIM}", 
            "h_", "(50,0.02,0.1,200,-0.02,0.02)", "dphi_gem_rh_csc_seg-dphi_gem_sh_l1_csc_sh_l1:charge/pt","station==2 && ring==1 && odd==0","COLZ")
    draw_2D(plotter.targetDir, "gem_csc_sim_reco_resolution_ME21_odd_2D_vsQoverPt", plotter.ext, plotter.treeDelta, ";q/p_{T} [1/GeV];#Delta#Phi_{GEM-CSC}^{RECO} - #Delta#Phi_{GEM-CSC}^{SIM}", 
            "h_", "(50,0.02,0.1,200,-0.02,0.02)", "dphi_gem_rh_csc_seg-dphi_gem_sh_l1_csc_sh_l1:charge/pt","station==2 && ring==1 && odd==1","COLZ")


    ## 1D resolution in slices of SIM bending angle
    draw_1D(plotter.targetDir, "gem_csc_sim_reco_resolution_ME11_even_1D_lowPt_slice1_neg", plotter.ext, plotter.treeDelta, ";dphi_gem_sh_l1_csc_sh_l1-dphi_gem_rh_csc_seg", "h_", "(200,-0.01,0.01)", 
            "dphi_gem_sh_l1_csc_sh_l1-dphi_gem_rh_csc_seg","station==1 && (ring==1 || ring==4) && odd==0 && -0.004 < dphi_gem_sh_l1_csc_sh_l1 && dphi_gem_sh_l1_csc_sh_l1 < 0 && pt<=10")
    draw_1D(plotter.targetDir, "gem_csc_sim_reco_resolution_ME11_even_1D_lowPt_slice2_neg", plotter.ext, plotter.treeDelta, ";dphi_gem_sh_l1_csc_sh_l1-dphi_gem_rh_csc_seg", "h_", "(200,-0.01,0.01)", 
            "dphi_gem_sh_l1_csc_sh_l1-dphi_gem_rh_csc_seg","station==1 && (ring==1 || ring==4) && odd==0 && -0.008 < dphi_gem_sh_l1_csc_sh_l1 && dphi_gem_sh_l1_csc_sh_l1 < -0.004 && pt<=10")
    draw_1D(plotter.targetDir, "gem_csc_sim_reco_resolution_ME11_even_1D_lowPt_slice3_neg", plotter.ext, plotter.treeDelta, ";dphi_gem_sh_l1_csc_sh_l1-dphi_gem_rh_csc_seg", "h_", "(200,-0.01,0.01)", 
            "dphi_gem_sh_l1_csc_sh_l1-dphi_gem_rh_csc_seg","station==1 && (ring==1 || ring==4) && odd==0 && -0.012 < dphi_gem_sh_l1_csc_sh_l1 && dphi_gem_sh_l1_csc_sh_l1 < -0.008 && pt<=10")
    draw_1D(plotter.targetDir, "gem_csc_sim_reco_resolution_ME11_even_1D_lowPt_slice4_neg", plotter.ext, plotter.treeDelta, ";dphi_gem_sh_l1_csc_sh_l1-dphi_gem_rh_csc_seg", "h_", "(200,-0.01,0.01)", 
            "dphi_gem_sh_l1_csc_sh_l1-dphi_gem_rh_csc_seg","station==1 && (ring==1 || ring==4) && odd==0 && -0.016 < dphi_gem_sh_l1_csc_sh_l1 && dphi_gem_sh_l1_csc_sh_l1 < -0.012 && pt<=10")

    draw_1D(plotter.targetDir, "gem_csc_sim_reco_resolution_ME11_odd_1D_lowPt_slice1_neg", plotter.ext, plotter.treeDelta, ";dphi_gem_sh_l1_csc_sh_l1-dphi_gem_rh_csc_seg", "h_", "(200,-0.01,0.01)", 
            "dphi_gem_sh_l1_csc_sh_l1-dphi_gem_rh_csc_seg","station==1 && (ring==1 || ring==4) && odd==1 && -0.004 < dphi_gem_sh_l1_csc_sh_l1 && dphi_gem_sh_l1_csc_sh_l1 < 0 && pt<=10")
    draw_1D(plotter.targetDir, "gem_csc_sim_reco_resolution_ME11_odd_1D_lowPt_slice2_neg", plotter.ext, plotter.treeDelta, ";dphi_gem_sh_l1_csc_sh_l1-dphi_gem_rh_csc_seg", "h_", "(200,-0.01,0.01)", 
            "dphi_gem_sh_l1_csc_sh_l1-dphi_gem_rh_csc_seg","station==1 && (ring==1 || ring==4) && odd==1 && -0.008 < dphi_gem_sh_l1_csc_sh_l1 && dphi_gem_sh_l1_csc_sh_l1 < -0.004 && pt<=10")
    draw_1D(plotter.targetDir, "gem_csc_sim_reco_resolution_ME11_odd_1D_lowPt_slice3_neg", plotter.ext, plotter.treeDelta, ";dphi_gem_sh_l1_csc_sh_l1-dphi_gem_rh_csc_seg", "h_", "(200,-0.01,0.01)", 
            "dphi_gem_sh_l1_csc_sh_l1-dphi_gem_rh_csc_seg","station==1 && (ring==1 || ring==4) && odd==1 && -0.012 < dphi_gem_sh_l1_csc_sh_l1 && dphi_gem_sh_l1_csc_sh_l1 < -0.008 && pt<=10")
    draw_1D(plotter.targetDir, "gem_csc_sim_reco_resolution_ME11_odd_1D_lowPt_slice4_neg", plotter.ext, plotter.treeDelta, ";dphi_gem_sh_l1_csc_sh_l1-dphi_gem_rh_csc_seg", "h_", "(200,-0.01,0.01)", 
            "dphi_gem_sh_l1_csc_sh_l1-dphi_gem_rh_csc_seg","station==1 && (ring==1 || ring==4) && odd==1 && -0.016 < dphi_gem_sh_l1_csc_sh_l1 && dphi_gem_sh_l1_csc_sh_l1 < -0.012 && pt<=10")
 
    ## 1D resolution in slices of SIM pt
    draw_1D(plotter.targetDir, "gem_csc_sim_reco_resolution_ME11_even_1D_slice1", plotter.ext, plotter.treeDelta, ";dphi_gem_sh_l1_csc_sh_l1-dphi_gem_rh_csc_seg", "h_", "(200,-0.01,0.01)", 
            "dphi_gem_sh_l1_csc_sh_l1-dphi_gem_rh_csc_seg","station==1 && (ring==1 || ring==4) && odd==0 && 5 < pt && pt < 10")
    draw_1D(plotter.targetDir, "gem_csc_sim_reco_resolution_ME11_even_1D_slice2", plotter.ext, plotter.treeDelta, ";dphi_gem_sh_l1_csc_sh_l1-dphi_gem_rh_csc_seg", "h_", "(200,-0.01,0.01)", 
            "dphi_gem_sh_l1_csc_sh_l1-dphi_gem_rh_csc_seg","station==1 && (ring==1 || ring==4) && odd==0 && 10 < pt && pt < 15")
    draw_1D(plotter.targetDir, "gem_csc_sim_reco_resolution_ME11_even_1D_slice3", plotter.ext, plotter.treeDelta, ";dphi_gem_sh_l1_csc_sh_l1-dphi_gem_rh_csc_seg", "h_", "(200,-0.01,0.01)", 
            "dphi_gem_sh_l1_csc_sh_l1-dphi_gem_rh_csc_seg","station==1 && (ring==1 || ring==4) && odd==0 && 15 < pt && pt < 30")
    draw_1D(plotter.targetDir, "gem_csc_sim_reco_resolution_ME11_even_1D_slice4", plotter.ext, plotter.treeDelta, ";dphi_gem_sh_l1_csc_sh_l1-dphi_gem_rh_csc_seg", "h_", "(200,-0.01,0.01)", 
            "dphi_gem_sh_l1_csc_sh_l1-dphi_gem_rh_csc_seg","station==1 && (ring==1 || ring==4) && odd==0 && 30 < pt && pt < 50")
   
    draw_1D(plotter.targetDir, "gem_csc_sim_reco_resolution_ME11_odd_1D_slice1", plotter.ext, plotter.treeDelta, ";dphi_gem_sh_l1_csc_sh_l1-dphi_gem_rh_csc_seg", "h_", "(200,-0.01,0.01)", 
            "dphi_gem_sh_l1_csc_sh_l1-dphi_gem_rh_csc_seg","station==1 && (ring==1 || ring==4) && odd==1 && 5 < pt && pt < 10")
    draw_1D(plotter.targetDir, "gem_csc_sim_reco_resolution_ME11_odd_1D_slice2", plotter.ext, plotter.treeDelta, ";dphi_gem_sh_l1_csc_sh_l1-dphi_gem_rh_csc_seg", "h_", "(200,-0.01,0.01)", 
            "dphi_gem_sh_l1_csc_sh_l1-dphi_gem_rh_csc_seg","station==1 && (ring==1 || ring==4) && odd==1 && 10 < pt && pt < 15")
    draw_1D(plotter.targetDir, "gem_csc_sim_reco_resolution_ME11_odd_1D_slice3", plotter.ext, plotter.treeDelta, ";dphi_gem_sh_l1_csc_sh_l1-dphi_gem_rh_csc_seg", "h_", "(200,-0.01,0.01)", 
            "dphi_gem_sh_l1_csc_sh_l1-dphi_gem_rh_csc_seg","station==1 && (ring==1 || ring==4) && odd==1 && 15 < pt && pt < 30")
    draw_1D(plotter.targetDir, "gem_csc_sim_reco_resolution_ME11_odd_1D_slice4", plotter.ext, plotter.treeDelta, ";dphi_gem_sh_l1_csc_sh_l1-dphi_gem_rh_csc_seg", "h_", "(200,-0.01,0.01)", 
            "dphi_gem_sh_l1_csc_sh_l1-dphi_gem_rh_csc_seg","station==1 && (ring==1 || ring==4) && odd==1 && 30 < pt && pt < 50")


    draw_1D(plotter.targetDir, "gem_csc_sim_reco_resolution_ME21_even_1D_slice1", plotter.ext, plotter.treeDelta, ";dphi_gem_sh_l1_csc_sh_l1-dphi_gem_rh_csc_seg", "h_", "(200,-0.01,0.01)", 
            "dphi_gem_sh_l1_csc_sh_l1-dphi_gem_rh_csc_seg","station==2 && ring==1 && odd==0 && 5 < pt && pt < 10")
    draw_1D(plotter.targetDir, "gem_csc_sim_reco_resolution_ME21_even_1D_slice2", plotter.ext, plotter.treeDelta, ";dphi_gem_sh_l1_csc_sh_l1-dphi_gem_rh_csc_seg", "h_", "(200,-0.01,0.01)", 
            "dphi_gem_sh_l1_csc_sh_l1-dphi_gem_rh_csc_seg","station==2 && ring==1 && odd==0 && 10 < pt && pt < 15")
    draw_1D(plotter.targetDir, "gem_csc_sim_reco_resolution_ME21_even_1D_slice3", plotter.ext, plotter.treeDelta, ";dphi_gem_sh_l1_csc_sh_l1-dphi_gem_rh_csc_seg", "h_", "(200,-0.01,0.01)", 
            "dphi_gem_sh_l1_csc_sh_l1-dphi_gem_rh_csc_seg","station==2 && ring==1 && odd==0 && 15 < pt && pt < 30")
    draw_1D(plotter.targetDir, "gem_csc_sim_reco_resolution_ME21_even_1D_slice4", plotter.ext, plotter.treeDelta, ";dphi_gem_sh_l1_csc_sh_l1-dphi_gem_rh_csc_seg", "h_", "(200,-0.01,0.01)", 
            "dphi_gem_sh_l1_csc_sh_l1-dphi_gem_rh_csc_seg","station==2 && ring==1 && odd==0 && 30 < pt && pt < 50")
   
    draw_1D(plotter.targetDir, "gem_csc_sim_reco_resolution_ME21_odd_1D_slice1", plotter.ext, plotter.treeDelta, ";dphi_gem_sh_l1_csc_sh_l1-dphi_gem_rh_csc_seg", "h_", "(200,-0.01,0.01)", 
            "dphi_gem_sh_l1_csc_sh_l1-dphi_gem_rh_csc_seg","station==2 && ring==1 && odd==1 && 5 < pt && pt < 10")
    draw_1D(plotter.targetDir, "gem_csc_sim_reco_resolution_ME21_odd_1D_slice2", plotter.ext, plotter.treeDelta, ";dphi_gem_sh_l1_csc_sh_l1-dphi_gem_rh_csc_seg", "h_", "(200,-0.01,0.01)", 
            "dphi_gem_sh_l1_csc_sh_l1-dphi_gem_rh_csc_seg","station==2 && ring==1 && odd==1 && 10 < pt && pt < 15")
    draw_1D(plotter.targetDir, "gem_csc_sim_reco_resolution_ME21_odd_1D_slice3", plotter.ext, plotter.treeDelta, ";dphi_gem_sh_l1_csc_sh_l1-dphi_gem_rh_csc_seg", "h_", "(200,-0.01,0.01)", 
            "dphi_gem_sh_l1_csc_sh_l1-dphi_gem_rh_csc_seg","station==2 && ring==1 && odd==1 && 15 < pt && pt < 30")
    draw_1D(plotter.targetDir, "gem_csc_sim_reco_resolution_ME21_odd_1D_slice4", plotter.ext, plotter.treeDelta, ";dphi_gem_sh_l1_csc_sh_l1-dphi_gem_rh_csc_seg", "h_", "(200,-0.01,0.01)", 
            "dphi_gem_sh_l1_csc_sh_l1-dphi_gem_rh_csc_seg","station==2 && ring==1 && odd==1 && 30 < pt && pt < 50")

#_______________________________________________________________________________
def simTrackToCscSimHitMatching(plotter,st=1):

    gStyle.SetTitleStyle(0);
    gStyle.SetTitleAlign(13); ##coord in top left
    gStyle.SetTitleX(0.);
    gStyle.SetTitleY(1.);
    gStyle.SetTitleW(1);
    gStyle.SetTitleH(0.058);
    gStyle.SetTitleBorderSize(0);
    
    gStyle.SetPadLeftMargin(0.126);
    gStyle.SetPadRightMargin(0.04);
    gStyle.SetPadTopMargin(0.06);
    gStyle.SetPadBottomMargin(0.13);
    gStyle.SetOptStat(0);
    gStyle.SetMarkerStyle(1);
    
    ok_eta = TCut("TMath::Abs(eta)>%f && TMath::Abs(eta)<%f"%(plotter.etaMin,plotter.etaMax))

    ## variables for the plot
    topTitle = " " * 11 + "CSC SimHit matching" + " " * 35 + "CMS Simulation Preliminary"
    xTitle = "Generated muon #eta"
    yTitle = "Efficiency"
    title = "%s;%s;%s"%(topTitle,xTitle,yTitle)
    toPlot = "TMath::Abs(eta)"
    h_bins = "(100,%f,%f)"%(plotter.etaMin,plotter.etaMax)
    nBins = int(h_bins[1:-1].split(',')[0])
    minBin = float(h_bins[1:-1].split(',')[1])
    maxBin = float(h_bins[1:-1].split(',')[2])

    c = TCanvas("c","c",700,450)
    c.Clear()
    base = TH1F("base",title,nBins,minBin,maxBin)
    base.SetMinimum(plotter.yMin)
    base.SetMaximum(plotter.yMax)
    base.Draw("")
    base.GetXaxis().SetLabelSize(0.05)
    base.GetYaxis().SetLabelSize(0.05)
    base.GetXaxis().SetTitleSize(0.05)
    base.GetYaxis().SetTitleSize(0.05)
    index = plotter.stationsToUse.index(st)

    h1 = draw_geff(plotter.treeEffSt[index], title, h_bins, toPlot, TCut(""), OR(ok_sh1,ok_sh2), "same")

    leg = TLegend(0.45,0.2,.75,0.35, "", "brNDC")
    leg.SetBorderSize(0)
    leg.SetFillStyle(0)
    leg.SetTextSize(0.06)
    leg.AddEntry(h1, "SimHits","l")
    leg.Draw("same")
    
    csc = drawCscLabel(plotter.stations.reverse_mapping[st], 0.77,0.87,0.05)
    pul = drawPuLabel(plotter.pu,0.17,0.17,0.05)
#    tex = drawEtaLabel(plotter.etaMin,plotter.etaMax,0.2,0.8,0.05)

    c.Print("%scsc_simhit_matching_efficiency_%s%s"%(plotter.targetDir, plotter.stations.reverse_mapping[st], plotter.ext))


    c = TCanvas("c","c",700,450)
    c.Clear()
    topTitle = " " * 11 + "GEM SimHit matching" + " " * 35 + "CMS Simulation Preliminary"
    title = "%s;%s;%s"%(topTitle,xTitle,yTitle)
    base = TH1F("base",title,nBins,minBin,maxBin)
    base.SetMinimum(plotter.yMin)
    base.SetMaximum(plotter.yMax)
    base.Draw("")
    base.GetXaxis().SetLabelSize(0.05)
    base.GetYaxis().SetLabelSize(0.05)
    base.GetXaxis().SetTitleSize(0.05)
    base.GetYaxis().SetTitleSize(0.05)
    index = plotter.stationsToUse.index(st)

    h1 = draw_geff(plotter.treeEffSt[index], title, h_bins, toPlot, TCut(""), OR(ok_gsh1,ok_gsh2), "same")

    leg = TLegend(0.45,0.2,.75,0.35, "", "brNDC")
    leg.SetBorderSize(0)
    leg.SetFillStyle(0)
    leg.SetTextSize(0.06)
    leg.AddEntry(h1, "SimHits","l")
    leg.Draw("same")
    
    csc = drawCscLabel(plotter.stations.reverse_mapping[st], 0.77,0.87,0.05)
    pul = drawPuLabel(plotter.pu,0.17,0.17,0.05)
#    tex = drawEtaLabel(plotter.etaMin,plotter.etaMax,0.2,0.8,0.05)

    c.Print("%sgem_simhit_matching_efficiency_%s%s"%(plotter.targetDir, plotter.stations.reverse_mapping[st], plotter.ext))


#_______________________________________________________________________________
def simTrackToCscStripsWiresMatching(plotter,st=1):

    gStyle.SetTitleStyle(0);
    gStyle.SetTitleAlign(13); ##coord in top left
    gStyle.SetTitleX(0.);
    gStyle.SetTitleY(1.);
    gStyle.SetTitleW(1);
    gStyle.SetTitleH(0.058);
    gStyle.SetTitleBorderSize(0);
    
    gStyle.SetPadLeftMargin(0.126);
    gStyle.SetPadRightMargin(0.04);
    gStyle.SetPadTopMargin(0.06);
    gStyle.SetPadBottomMargin(0.13);
    gStyle.SetOptStat(0);
    gStyle.SetMarkerStyle(1);
    
    ok_eta = TCut("TMath::Abs(eta)>%f && TMath::Abs(eta)<%f"%(plotter.etaMin,plotter.etaMax))

    ## variables for the plot
    topTitle = " " * 11 + "CSC Digi matching" + " " * 35 + "CMS Simulation Preliminary"
    xTitle = "Generated muon #eta"
    yTitle = "Efficiency"
    title = "%s;%s;%s"%(topTitle,xTitle,yTitle)
    toPlot = "TMath::Abs(eta)"
    h_bins = "(100,%f,%f)"%(plotter.etaMin,plotter.etaMax)
    nBins = int(h_bins[1:-1].split(',')[0])
    minBin = float(h_bins[1:-1].split(',')[1])
    maxBin = float(h_bins[1:-1].split(',')[2])

    c = TCanvas("c","c",700,450)
    c.Clear()
    base  = TH1F("base",title,nBins,minBin,maxBin)
    base.SetMinimum(plotter.yMin)
    base.SetMaximum(plotter.yMax)
    base.Draw("")
    base.GetXaxis().SetLabelSize(0.05)
    base.GetYaxis().SetLabelSize(0.05)
    base.GetXaxis().SetTitleSize(0.05)
    base.GetYaxis().SetTitleSize(0.05)

    index = plotter.stationsToUse.index(st)

    h1 = draw_geff(plotter.treeEffSt[index], title, h_bins, toPlot, ok_sh1, ok_w1, "same", kRed)
    h2 = draw_geff(plotter.treeEffSt[index], title, h_bins, toPlot, ok_sh1, ok_st1, "same")
   
    leg = TLegend(0.45,0.2,.75,0.35, "", "brNDC")
    leg.SetBorderSize(0)
    leg.SetFillStyle(0)
    leg.SetTextSize(0.06)
    leg.AddEntry(h1, "Wires","l")
    leg.AddEntry(h2, "Strips","l")
    leg.Draw("same")
    
    csc = drawCscLabel(plotter.stations.reverse_mapping[st], 0.77,0.87,0.05)
    pul = drawPuLabel(plotter.pu,0.17,0.17,0.05)
    #tex = drawEtaLabel(plotter.etaMin,plotter.etaMax,0.2,0.8,0.05)

    c.Print("%scsc_digi_matching_efficiency_%s%s"%(plotter.targetDir,plotter.stations.reverse_mapping[st],plotter.ext))


#_______________________________________________________________________________
def simTrackToCscStripsWiresMatching_2(plotter,st=1):

    gStyle.SetTitleStyle(0)
    gStyle.SetTitleAlign(13) ##coord in top left
    gStyle.SetTitleX(0.)
    gStyle.SetTitleY(1.)
    gStyle.SetTitleW(1)
    gStyle.SetTitleH(0.058)
    gStyle.SetTitleBorderSize(0)
    
    gStyle.SetPadLeftMargin(0.126)
    gStyle.SetPadRightMargin(0.04)
    gStyle.SetPadTopMargin(0.06)
    gStyle.SetPadBottomMargin(0.13)
    gStyle.SetOptStat(0)
    gStyle.SetMarkerStyle(1)
    
    ok_eta = TCut("TMath::Abs(eta)>%f && TMath::Abs(eta)<%f"%(plotter.etaMin,plotter.etaMax))

    ## variables for the plot
    topTitle = " " * 11 + "CSC Digi matching" + " " * 35 + "CMS Simulation Preliminary"
    xTitle = "Generated muon #eta"
    yTitle = "Efficiency"
    title = "%s;%s;%s"%(topTitle,xTitle,yTitle)
    toPlot = "TMath::Abs(eta)"
    h_bins = "(100,%f,%f)"%(plotter.etaMin,plotter.etaMax)
    nBins = int(h_bins[1:-1].split(',')[0])
    minBin = float(h_bins[1:-1].split(',')[1])
    maxBin = float(h_bins[1:-1].split(',')[2])

    c = TCanvas("c","c",700,450)
    c.Clear()
    base  = TH1F("base",title,nBins,minBin,maxBin)
    base.SetMinimum(plotter.yMin)
    base.SetMaximum(plotter.yMax)
    base.Draw("")
    base.GetXaxis().SetLabelSize(0.05)
    base.GetYaxis().SetLabelSize(0.05)
    base.GetXaxis().SetTitleSize(0.05)
    base.GetYaxis().SetTitleSize(0.05)

    index = plotter.stationsToUse.index(st)

    h1 = draw_geff(plotter.treeEffSt[index], title, h_bins, toPlot, ok_sh1, OR(ok_w1,ok_st1), "same", kRed)
    h2 = draw_geff(plotter.treeEffSt[index], title, h_bins, toPlot, ok_sh1, AND(ok_w1,ok_st1), "same")
   
    leg = TLegend(0.45,0.2,.75,0.35, "", "brNDC");
    leg.SetBorderSize(0)
    leg.SetFillStyle(0)
    leg.SetTextSize(0.06)
    leg.AddEntry(h1, "Wires OR strips","l")
    leg.AddEntry(h2, "Wires AND strips","l")
    leg.Draw("same");
    
    csc = drawCscLabel(plotter.stations.reverse_mapping[st], 0.77,0.87,0.05)
    pul = drawPuLabel(plotter.pu,0.17,0.17,0.05)
    #tex = drawEtaLabel(plotter.etaMin,plotter.etaMax,0.2,0.8,0.05)

    c.Print("%scsc_combined_digi_matching_efficiency_%s%s"%(plotter.targetDir,plotter.stations.reverse_mapping[st],plotter.ext))


#_______________________________________________________________________________
def simTrackToCscAlctClctMatching(plotter,st=1):

    gStyle.SetTitleStyle(0);
    gStyle.SetTitleAlign(13); ##coord in top left
    gStyle.SetTitleX(0.);
    gStyle.SetTitleY(1.);
    gStyle.SetTitleW(1);
    gStyle.SetTitleH(0.058);
    gStyle.SetTitleBorderSize(0);
    
    gStyle.SetPadLeftMargin(0.126);
    gStyle.SetPadRightMargin(0.04);
    gStyle.SetPadTopMargin(0.06);
    gStyle.SetPadBottomMargin(0.13);
    gStyle.SetOptStat(0);
    gStyle.SetMarkerStyle(1);
    
    ok_eta = TCut("TMath::Abs(eta)>%f && TMath::Abs(eta)<%f"%(plotter.etaMin,plotter.etaMax))

    ## variables for the plot
    topTitle = " " * 11 + "CSC Stub matching" + " " * 35 + "CMS Simulation Preliminary"
    xTitle = "Generated muon #eta"
    yTitle = "Efficiency"
    title = "%s;%s;%s"%(topTitle,xTitle,yTitle)
    toPlot = "TMath::Abs(eta)"
    h_bins = "(100,%f,%f)"%(plotter.etaMin,plotter.etaMax)
    nBins = int(h_bins[1:-1].split(',')[0])
    minBin = float(h_bins[1:-1].split(',')[1])
    maxBin = float(h_bins[1:-1].split(',')[2])

    c = TCanvas("c","c",700,450)
    c.Clear()
    base  = TH1F("base",title,nBins,minBin,maxBin)
    base.SetMinimum(plotter.yMin)
    base.SetMaximum(plotter.yMax)
    base.Draw("")
    base.GetXaxis().SetLabelSize(0.05)
    base.GetYaxis().SetLabelSize(0.05)
    base.GetXaxis().SetTitleSize(0.05)
    base.GetYaxis().SetTitleSize(0.05)

    index = plotter.stationsToUse.index(st)

    h1 = draw_geff(plotter.treeEffSt[index], title, h_bins, toPlot, ok_sh1, ok_alct1, "same", kRed)
    h11 = draw_geff(plotter.treeEffSt[index], title, h_bins, toPlot, AND(ok_sh1,ok_w1), ok_alct1, "same", kOrange+1)
    h2 = draw_geff(plotter.treeEffSt[index], title, h_bins, toPlot, ok_sh1, ok_clct1, "same",kBlue)
    h21 = draw_geff(plotter.treeEffSt[index], title, h_bins, toPlot, AND(ok_sh1,ok_st1), ok_clct1, "same",kGreen+1)
   
    leg = TLegend(0.45,0.2,.75,0.5, "", "brNDC");
    leg.SetBorderSize(0)
    leg.SetFillStyle(0)
    leg.SetTextSize(0.06)
    leg.AddEntry(h1, "ALCT","l")
    leg.AddEntry(h11, "ALCT provided wires","l")
    leg.AddEntry(h2, "CLCT","l")
    leg.AddEntry(h21, "CLCT provided strips","l")
    leg.Draw("same");
    
    csc = drawCscLabel(plotter.stations.reverse_mapping[st], 0.77,0.87,0.05)
    pul = drawPuLabel(plotter.pu,0.17,0.17,0.05)
    #tex = drawEtaLabel(plotter.etaMin,plotter.etaMax,0.2,0.8,0.05)

    c.Print("%scsc_stub_matching_efficiency_%s%s"%(plotter.targetDir,plotter.stations.reverse_mapping[st],plotter.ext))


#_______________________________________________________________________________
def simTrackToCscAlctClctMatching_2(plotter,st=1):

    gStyle.SetTitleStyle(0);
    gStyle.SetTitleAlign(13); ##coord in top left
    gStyle.SetTitleX(0.);
    gStyle.SetTitleY(1.);
    gStyle.SetTitleW(1);
    gStyle.SetTitleH(0.058);
    gStyle.SetTitleBorderSize(0);
    
    gStyle.SetPadLeftMargin(0.126);
    gStyle.SetPadRightMargin(0.04);
    gStyle.SetPadTopMargin(0.06);
    gStyle.SetPadBottomMargin(0.13);
    gStyle.SetOptStat(0);
    gStyle.SetMarkerStyle(1);
    
    ok_eta = TCut("TMath::Abs(eta)>%f && TMath::Abs(eta)<%f"%(plotter.etaMin,plotter.etaMax))

    ## variables for the plot
    topTitle = " " * 11 + "CSC Stub matching" + " " * 35 + "CMS Simulation Preliminary"
    xTitle = "Generated muon #eta"
    yTitle = "Efficiency"
    title = "%s;%s;%s"%(topTitle,xTitle,yTitle)
    toPlot = "TMath::Abs(eta)"
    h_bins = "(100,%f,%f)"%(plotter.etaMin,plotter.etaMax)
    nBins = int(h_bins[1:-1].split(',')[0])
    minBin = float(h_bins[1:-1].split(',')[1])
    maxBin = float(h_bins[1:-1].split(',')[2])

    c = TCanvas("c","c",700,450)
    c.Clear()
    base  = TH1F("base",title,nBins,minBin,maxBin)
    base.SetMinimum(plotter.yMin)
    base.SetMaximum(plotter.yMax)
    base.Draw("")
    base.GetXaxis().SetLabelSize(0.05)
    base.GetYaxis().SetLabelSize(0.05)
    base.GetXaxis().SetTitleSize(0.05)
    base.GetYaxis().SetTitleSize(0.05)

    index = plotter.stationsToUse.index(st)

    h1 = draw_geff(plotter.treeEffSt[index], title, h_bins, toPlot, ok_sh1, OR(ok_alct1,ok_clct1), "same", kRed)
    h11 = draw_geff(plotter.treeEffSt[index], title, h_bins, toPlot, AND(ok_sh1,ok_st1,ok_w1), OR(ok_alct1,ok_clct1), "same", kOrange)
    h2 = draw_geff(plotter.treeEffSt[index], title, h_bins, toPlot, ok_sh1, AND(ok_alct1,ok_clct1), "same",kBlue)
    h21 = draw_geff(plotter.treeEffSt[index], title, h_bins, toPlot, AND(ok_sh1,ok_st1,ok_w1), AND(ok_alct1,ok_clct1), "same",kGreen+1)
   
    leg = TLegend(0.45,0.2,.75,0.5, "", "brNDC");
    leg.SetBorderSize(0)
    leg.SetFillStyle(0)
    leg.SetTextSize(0.06)
    leg.AddEntry(h1, "ALCT OR CLCT","l")
    leg.AddEntry(h11, "ALCT OR CLCT provided wires and strips","l")
    leg.AddEntry(h2, "ALCT AND CLCT","l")
    leg.AddEntry(h21, "ALCT AND CLCT provided wires and strips","l")
    leg.Draw("same");
    
    csc = drawCscLabel(plotter.stations.reverse_mapping[st], 0.77,0.87,0.05)
    pul = drawPuLabel(plotter.pu,0.17,0.17,0.05)
    #tex = drawEtaLabel(plotter.etaMin,plotter.etaMax,0.2,0.8,0.05)

    c.Print("%scsc_combined_stub_matching_efficiency_%s%s"%(plotter.targetDir,plotter.stations.reverse_mapping[st],plotter.ext))


#_______________________________________________________________________________
def simTrackToCscLctMatching(plotter,st=1):

    gStyle.SetTitleStyle(0);
    gStyle.SetTitleAlign(13); ##coord in top left
    gStyle.SetTitleX(0.);
    gStyle.SetTitleY(1.);
    gStyle.SetTitleW(1);
    gStyle.SetTitleH(0.058);
    gStyle.SetTitleBorderSize(0);
    
    gStyle.SetPadLeftMargin(0.126);
    gStyle.SetPadRightMargin(0.04);
    gStyle.SetPadTopMargin(0.06);
    gStyle.SetPadBottomMargin(0.13);
    gStyle.SetOptStat(0);
    gStyle.SetMarkerStyle(1);
    
    ok_eta = TCut("TMath::Abs(eta)>%f && TMath::Abs(eta)<%f"%(plotter.etaMin,plotter.etaMax))

    ## variables for the plot
    topTitle = " " * 11 + "CSC Stub matching" + " " * 35 + "CMS Simulation Preliminary"
    xTitle = "Generated muon #eta"
    yTitle = "Efficiency"
    title = "%s;%s;%s"%(topTitle,xTitle,yTitle)
    toPlot = "TMath::Abs(eta)"
    h_bins = "(100,%f,%f)"%(plotter.etaMin,plotter.etaMax)
    nBins = int(h_bins[1:-1].split(',')[0])
    minBin = float(h_bins[1:-1].split(',')[1])
    maxBin = float(h_bins[1:-1].split(',')[2])

    c = TCanvas("c","c",700,450)
    c.Clear()
    base  = TH1F("base",title,nBins,minBin,maxBin)
    base.SetMinimum(plotter.yMin)
    base.SetMaximum(plotter.yMax)
    base.Draw("")
    base.GetXaxis().SetLabelSize(0.05)
    base.GetYaxis().SetLabelSize(0.05)
    base.GetXaxis().SetTitleSize(0.05)
    base.GetYaxis().SetTitleSize(0.05)
    
    index = plotter.stationsToUse.index(st)

    if plotter.matchAlctGem:        
        h1 = draw_geff(plotter.treeEffSt[index], title, h_bins, toPlot, AND(ok_sh1, ok_alct1,OR(ok_clct1,ok_pad1)), ok_lct1, "same", kRed)
        h2 = draw_geff(plotter.treeEffSt[index], title, h_bins, toPlot, ok_sh1, ok_lct1, "same", kBlue)
    else:
        h1 = draw_geff(plotter.treeEffSt[index], title, h_bins, toPlot, AND(ok_sh1, ok_alct1,ok_clct1), ok_lct1, "same", kRed)
        h2 = draw_geff(plotter.treeEffSt[index], title, h_bins, toPlot, ok_sh1, ok_lct1, "same", kBlue)

    leg = TLegend(0.10,0.2,.75,0.35, "", "brNDC");
    leg.SetBorderSize(0)
    leg.SetFillStyle(0)
    leg.SetTextSize(0.04)
    if plotter.matchAlctGem:
        leg.AddEntry(h1, "LCT matched to ALCT and (CLCT or GEM)","l")
        leg.AddEntry(h2, "LCT","l")
    else:
        leg.AddEntry(h1, "LCT matched to ALCT and CLCT","l")
        leg.AddEntry(h2, "LCT","l")
    leg.Draw("same");
    
    csc = drawCscLabel(plotter.stations.reverse_mapping[st], 0.77,0.87,0.05)
    pul = drawPuLabel(plotter.pu,0.17,0.17,0.05)
    #tex = drawEtaLabel(plotter.etaMin,plotter.etaMax,0.2,0.8,0.05)

    c.Print("%scsc_lct_matching_efficiency_%s%s"%(plotter.targetDir,plotter.stations.reverse_mapping[st],plotter.ext))


#_______________________________________________________________________________
def simTrackToCscMpLctMatching(plotter,st=1):

    gStyle.SetTitleStyle(0);
    gStyle.SetTitleAlign(13); ##coord in top left
    gStyle.SetTitleX(0.);
    gStyle.SetTitleY(1.);
    gStyle.SetTitleW(1);
    gStyle.SetTitleH(0.058);
    gStyle.SetTitleBorderSize(0);
    
    gStyle.SetPadLeftMargin(0.126);
    gStyle.SetPadRightMargin(0.04);
    gStyle.SetPadTopMargin(0.06);
    gStyle.SetPadBottomMargin(0.13);
    gStyle.SetOptStat(0);
    gStyle.SetMarkerStyle(1);
    
    ok_eta = TCut("TMath::Abs(eta)>%f && TMath::Abs(eta)<%f"%(plotter.etaMin,plotter.etaMax))

    ## variables for the plot
    topTitle = " " * 11 + "CSC Stub matching" + " " * 35 + "CMS Simulation Preliminary"
    xTitle = "Generated muon #eta"
    yTitle = "Efficiency"
    title = "%s;%s;%s"%(topTitle,xTitle,yTitle)
    toPlot = "TMath::Abs(eta)"
    h_bins = "(100,%f,%f)"%(plotter.etaMin,plotter.etaMax)
    nBins = int(h_bins[1:-1].split(',')[0])
    minBin = float(h_bins[1:-1].split(',')[1])
    maxBin = float(h_bins[1:-1].split(',')[2])

    c = TCanvas("c","c",700,450)
    c.Clear()
    base  = TH1F("base",title,nBins,minBin,maxBin)
    base.SetMinimum(plotter.yMin)
    base.SetMaximum(plotter.yMax)
    base.Draw("")
    base.GetXaxis().SetLabelSize(0.05)
    base.GetYaxis().SetLabelSize(0.05)
    base.GetXaxis().SetTitleSize(0.05)
    base.GetYaxis().SetTitleSize(0.05)
    
    index = plotter.stationsToUse.index(st)

    h1 = draw_geff(plotter.treeEffSt[index], title, h_bins, toPlot, AND(ok_sh1, ok_alct1, ok_clct1), ok_mplct1, "same", kRed)
    h2 = draw_geff(plotter.treeEffSt[index], title, h_bins, toPlot, ok_sh1, ok_mplct1, "same", kBlue)

    leg = TLegend(0.10,0.2,.75,0.35, "", "brNDC");
    leg.SetBorderSize(0)
    leg.SetFillStyle(0)
    leg.SetTextSize(0.04)
    leg.AddEntry(h1, "MPLCT matched to ALCT and CLCT","l")
    leg.AddEntry(h2, "MPLCT","l")
    leg.Draw("same");
    
    csc = drawCscLabel(plotter.stations.reverse_mapping[st], 0.77,0.87,0.05)
    pul = drawPuLabel(plotter.pu,0.17,0.17,0.05)
    #tex = drawEtaLabel(plotter.etaMin,plotter.etaMax,0.2,0.8,0.05)

    c.Print("%scsc_mplct_matching_efficiency_%s%s"%(plotter.targetDir,plotter.stations.reverse_mapping[st],plotter.ext))


#_______________________________________________________________________________
def simTrackToCscSegmentsMatching(plotter,st=1):

    gStyle.SetTitleStyle(0);
    gStyle.SetTitleAlign(13); ##coord in top left
    gStyle.SetTitleX(0.);
    gStyle.SetTitleY(1.);
    gStyle.SetTitleW(1);
    gStyle.SetTitleH(0.058);
    gStyle.SetTitleBorderSize(0);
    
    gStyle.SetPadLeftMargin(0.126);
    gStyle.SetPadRightMargin(0.04);
    gStyle.SetPadTopMargin(0.06);
    gStyle.SetPadBottomMargin(0.13);
    gStyle.SetOptStat(0);
    gStyle.SetMarkerStyle(1);
    
    ok_eta = TCut("TMath::Abs(eta)>%f && TMath::Abs(eta)<%f"%(plotter.etaMin,plotter.etaMax))

    ## variables for the plot
    topTitle = " " * 11 + "CSC Segment matching" + " " * 35 + "CMS Simulation Preliminary"
    xTitle = "Generated muon #eta"
    yTitle = "Efficiency"
    title = "%s;%s;%s"%(topTitle,xTitle,yTitle)
    toPlot = "TMath::Abs(eta)"
    h_bins = "(100,%f,%f)"%(plotter.etaMin,plotter.etaMax)
    nBins = int(h_bins[1:-1].split(',')[0])
    minBin = float(h_bins[1:-1].split(',')[1])
    maxBin = float(h_bins[1:-1].split(',')[2])

    c = TCanvas("c","c",700,450)
    c.Clear()
    base  = TH1F("base",title,nBins,minBin,maxBin)
    base.SetMinimum(plotter.yMin)
    base.SetMaximum(plotter.yMax)
    base.Draw("")
    base.GetXaxis().SetLabelSize(0.05)
    base.GetYaxis().SetLabelSize(0.05)
    base.GetXaxis().SetTitleSize(0.05)
    base.GetYaxis().SetTitleSize(0.05)

    index = plotter.stationsToUse.index(st)

    h1 = draw_geff(plotter.treeEffSt[index], title, h_bins, toPlot, ok_sh1, ok_seg1, "same", kRed)
    h2 = draw_geff(plotter.treeEffSt[index], title, h_bins, toPlot, ok_sh2, ok_seg2, "same")
   
    leg = TLegend(0.45,0.2,.75,0.35, "", "brNDC")
    leg.SetBorderSize(0)
    leg.SetFillStyle(0)
    leg.SetTextSize(0.06)
    leg.AddEntry(h1, "Segment in even chamber","l")
    leg.AddEntry(h2, "Segment in odd chamber","l")
    leg.Draw("same")
    
    csc = drawCscLabel(plotter.stations.reverse_mapping[st], 0.77,0.87,0.05)
    pul = drawPuLabel(plotter.pu,0.17,0.17,0.05)
    #tex = drawEtaLabel(plotter.etaMin,plotter.etaMax,0.2,0.8,0.05)

    c.Print("%scsc_segment_matching_efficiency_%s%s"%(plotter.targetDir,plotter.stations.reverse_mapping[st],plotter.ext))


#_______________________________________________________________________________
def simTrackToGemRechitsMatching(plotter,st=1):

    gStyle.SetTitleStyle(0);
    gStyle.SetTitleAlign(13); ##coord in top left
    gStyle.SetTitleX(0.);
    gStyle.SetTitleY(1.);
    gStyle.SetTitleW(1);
    gStyle.SetTitleH(0.058);
    gStyle.SetTitleBorderSize(0);
    
    gStyle.SetPadLeftMargin(0.126);
    gStyle.SetPadRightMargin(0.04);
    gStyle.SetPadTopMargin(0.06);
    gStyle.SetPadBottomMargin(0.13);
    gStyle.SetOptStat(0);
    gStyle.SetMarkerStyle(1);
    
    ok_eta = TCut("TMath::Abs(eta)>%f && TMath::Abs(eta)<%f"%(plotter.etaMin,plotter.etaMax))

    ## variables for the plot
    topTitle = " " * 11 + "GEM Rechit matching" + " " * 35 + "CMS Simulation Preliminary"
    xTitle = "Generated muon #eta"
    yTitle = "Efficiency"
    title = "%s;%s;%s"%(topTitle,xTitle,yTitle)
    toPlot = "TMath::Abs(eta)"
    h_bins = "(100,%f,%f)"%(plotter.etaMin,plotter.etaMax)
    nBins = int(h_bins[1:-1].split(',')[0])
    minBin = float(h_bins[1:-1].split(',')[1])
    maxBin = float(h_bins[1:-1].split(',')[2])

    c = TCanvas("c","c",700,450)
    c.Clear()
    base  = TH1F("base",title,nBins,minBin,maxBin)
    base.SetMinimum(plotter.yMin)
    base.SetMaximum(plotter.yMax)
    base.Draw("")
    base.GetXaxis().SetLabelSize(0.05)
    base.GetYaxis().SetLabelSize(0.05)
    base.GetXaxis().SetTitleSize(0.05)
    base.GetYaxis().SetTitleSize(0.05)

    index = plotter.stationsToUse.index(st)

    h1 = draw_geff(plotter.treeEffSt[index], title, h_bins, toPlot, ok_gsh1, ok_grh1, "same", kRed)
    h2 = draw_geff(plotter.treeEffSt[index], title, h_bins, toPlot, ok_gsh2, ok_grh2, "same")
   
    leg = TLegend(0.45,0.2,.75,0.35, "", "brNDC")
    leg.SetBorderSize(0)
    leg.SetFillStyle(0)
    leg.SetTextSize(0.06)
    leg.AddEntry(h1, "Rechit in even chamber","l")
    leg.AddEntry(h2, "Rechit in odd chamber","l")
    leg.Draw("same")
    
    gem = drawCscLabel(plotter.stations.reverse_mapping[st], 0.77,0.87,0.05)
    pul = drawPuLabel(plotter.pu,0.17,0.17,0.05)
    #tex = drawEtaLabel(plotter.etaMin,plotter.etaMax,0.2,0.8,0.05)

    c.Print("%sgem_rechit_matching_efficiency_%s%s"%(plotter.targetDir,plotter.stations.reverse_mapping[st],plotter.ext))
