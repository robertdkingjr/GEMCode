from ROOT import *
import os
import datetime
from EffHelper import *

gROOT.SetBatch(1)
gStyle.SetStatW(0.07)
gStyle.SetStatH(0.06)

gStyle.SetOptStat(0)
gStyle.SetTitleStyle(0)
gStyle.SetTitleAlign(13) ## coord in top left
gStyle.SetTitleX(0.)
gStyle.SetTitleY(1.)
gStyle.SetTitleW(1)
gStyle.SetTitleH(0.058)
gStyle.SetTitleBorderSize(0)

gStyle.SetPadLeftMargin(0.126)
gStyle.SetPadRightMargin(0.04)
gStyle.SetPadTopMargin(0.06)
gStyle.SetPadBottomMargin(0.13)

gStyle.SetMarkerStyle(1)


# displacedMuonDir = '/eos/uscms/store/user/tahuang/DispalcedMuonGun_1M_FlatPt1_50_FlatDxy0_50CM_GEN_SIM_CMSSW620SLHC/'
# displacedMuonDir = '/eos/uscms/store/user/tahuang/DispalcedMuonGun_1M_FlatPt1_50_FlatDxy0_50CM_GEN_SIM_CMSSW620SLHC_v3/GEMCSCAna_DisplacedMuonGun/170219_224752/0000/'
# promptMuonDir = '/eos/uscms/store/user/tahuang/SLHC23_patch1_2023Muon_gen_sim_Pt2_50_1M/GEMCSCAna_ctau0_Pt2_50_20170131/170201_015620/0000/'
promptMuonDir = '/eos/uscms/store/user/tahuang/SLHC23_patch1_2023Muon_gen_sim_Pt2_50_1M/GEMCSCAna_ctau0_Pt2_50_20170131/170218_213142/0000/'

displacedMuonDir = '/eos/uscms/store/user/tahuang/DisplacedMuonGun_1M_FlatPt1_50_FlatDxy0_50CM_GEN_SIM_CMSSW620SLHC_v5/GEMCSC_Ana_displacedMuonGun_2023Muon_20170222_v5/170223_195129/0000/'

    


# no eta cuts
den_lct = "has_csc_sh>0 && pt>10"
num_lct = "has_csc_sh>0 && pt>10 && has_lct>0"


# Add dxy separations, eta cuts
den_lct_dxy05 = "has_csc_sh>0 && ((abs(eta_cscsh_odd) > 1.6 && abs(eta_cscsh_odd) < 2.4) || (abs(eta_cscsh_even) > 1.6 && abs(eta_cscsh_even) < 2.4)) && genGdMu_dxy<5"
num_lct_dxy05 = "has_csc_sh>0 && ((abs(eta_cscsh_odd) > 1.6 && abs(eta_cscsh_odd) < 2.4) || (abs(eta_cscsh_even) > 1.6 && abs(eta_cscsh_even) < 2.4))&& genGdMu_dxy<5 && has_lct>0"
den_lct_dxy1020 = "has_csc_sh>0 && ((abs(eta_cscsh_odd) > 1.6 && abs(eta_cscsh_odd) < 2.4) || (abs(eta_cscsh_even) > 1.6 && abs(eta_cscsh_even) < 2.4)) && genGdMu_dxy>10 && genGdMu_dxy<20"
num_lct_dxy1020 = "has_csc_sh>0 && ((abs(eta_cscsh_odd) > 1.6 && abs(eta_cscsh_odd) < 2.4) || (abs(eta_cscsh_even) > 1.6 && abs(eta_cscsh_even) < 2.4)) && genGdMu_dxy>10 && genGdMu_dxy<20 && has_lct>0"
den_lct_dxy3050 = "has_csc_sh>0 && ((abs(eta_cscsh_odd) > 1.6 && abs(eta_cscsh_odd) < 2.4) || (abs(eta_cscsh_even) > 1.6 && abs(eta_cscsh_even) < 2.4)) && genGdMu_dxy>30 && genGdMu_dxy<50"
num_lct_dxy3050 = "has_csc_sh>0 && ((abs(eta_cscsh_odd) > 1.6 && abs(eta_cscsh_odd) < 2.4) || (abs(eta_cscsh_even) > 1.6 && abs(eta_cscsh_even) < 2.4)) && genGdMu_dxy>30 && genGdMu_dxy<50 && has_lct>0"


# Only odd csc chambers, abs(dxy)
den_lct_dxy05_odd = "has_csc_sh>0 && (abs(eta_cscsh_odd) > 1.6 && abs(eta_cscsh_odd) < 2.4) && abs(genGdMu_dxy)<5"
num_lct_dxy05_odd = "has_csc_sh>0 && (abs(eta_cscsh_odd) > 1.6 && abs(eta_cscsh_odd) < 2.4) && abs(genGdMu_dxy)<5 && has_lct>0"
den_lct_dxy1020_odd = "has_csc_sh>0 && (abs(eta_cscsh_odd) > 1.6 && abs(eta_cscsh_odd) < 2.4) && abs(genGdMu_dxy)>10 && abs(genGdMu_dxy)<20"
num_lct_dxy1020_odd = "has_csc_sh>0 && (abs(eta_cscsh_odd) > 1.6 && abs(eta_cscsh_odd) < 2.4) && abs(genGdMu_dxy)>10 && abs(genGdMu_dxy)<20 && has_lct>0"
den_lct_dxy3050_odd = "has_csc_sh>0 && (abs(eta_cscsh_odd) > 1.6 && abs(eta_cscsh_odd) < 2.4) && abs(genGdMu_dxy)>30 && abs(genGdMu_dxy)<50"
num_lct_dxy3050_odd = "has_csc_sh>0 && (abs(eta_cscsh_odd) > 1.6 && abs(eta_cscsh_odd) < 2.4) && abs(genGdMu_dxy)>30 && abs(genGdMu_dxy)<50 && has_lct>0"

# Add Lxy,Lz requirements
den_lct_dxy05_odd_lcuts = "has_csc_sh>0 && (abs(eta_cscsh_odd) > 1.6 && abs(eta_cscsh_odd) < 2.4) && abs(genGdMu_dxy)<5 && abs(genGdMu_vz)<200 && genGdMu_lxy<200"
num_lct_dxy05_odd_lcuts = den_lct_dxy05_odd_lcuts+" && has_lct>0"
den_lct_dxy1020_odd_lcuts = "has_csc_sh>0 && (abs(eta_cscsh_odd) > 1.6 && abs(eta_cscsh_odd) < 2.4) && abs(genGdMu_dxy)>10 && abs(genGdMu_dxy)<20 && abs(genGdMu_vz)<200 && genGdMu_lxy<200"
num_lct_dxy1020_odd_lcuts = den_lct_dxy1020_odd_lcuts+" && has_lct>0"
den_lct_dxy3050_odd_lcuts = "has_csc_sh>0 && (abs(eta_cscsh_odd) > 1.6 && abs(eta_cscsh_odd) < 2.4) && abs(genGdMu_dxy)>30 && abs(genGdMu_dxy)<50 && abs(genGdMu_vz)<200 && genGdMu_lxy<200"
num_lct_dxy3050_odd_lcuts = den_lct_dxy3050_odd_lcuts+" && has_lct>0"


# 3/3/17 - no L cuts

den_lct_dxy1020_odd = "has_csc_sh>0 && (abs(eta_cscsh_odd) > 1.6 && abs(eta_cscsh_odd) < 2.4) && abs(genGdMu_dxy)>10 && abs(genGdMu_dxy)<20"
num_lct_dxy1020_odd = den_lct_dxy1020_odd+" && has_lct>0"
den_lct_dxy2050_odd = "has_csc_sh>0 && (abs(eta_cscsh_odd) > 1.6 && abs(eta_cscsh_odd) < 2.4) && abs(genGdMu_dxy)>20 && abs(genGdMu_dxy)<50"
num_lct_dxy2050_odd = den_lct_dxy2050_odd+" && has_lct>0"

den_lct_dxy1020_even = "has_csc_sh>0 && (abs(eta_cscsh_even) > 1.6 && abs(eta_cscsh_even) < 2.4) && abs(genGdMu_dxy)>10 && abs(genGdMu_dxy)<20"
num_lct_dxy1020_even = den_lct_dxy1020_even+" && has_lct>0"
den_lct_dxy2050_even = "has_csc_sh>0 && (abs(eta_cscsh_even) > 1.6 && abs(eta_cscsh_even) < 2.4) && abs(genGdMu_dxy)>20 && abs(genGdMu_dxy)<50"
num_lct_dxy2050_even = den_lct_dxy2050_even+" && has_lct>0"

den_lct_prompt_odd = "has_csc_sh>0 && (abs(eta_cscsh_odd) > 1.6 && abs(eta_cscsh_odd) < 2.4)"
num_lct_prompt_odd = den_lct_prompt_odd+" && has_lct>0"

den_lct_prompt_even = "has_csc_sh>0 && (abs(eta_cscsh_even) > 1.6 && abs(eta_cscsh_even) < 2.4)"
num_lct_prompt_even = den_lct_prompt_even+" && has_lct>0"


# CLCT
den_clct_dxy1020_odd = "has_csc_sh>0 && (abs(eta_cscsh_odd) > 1.6 && abs(eta_cscsh_odd) < 2.4) && abs(genGdMu_dxy)>10 && abs(genGdMu_dxy)<20"
num_clct_dxy1020_odd = den_clct_dxy1020_odd+" && has_clct>0"
den_clct_dxy2050_odd = "has_csc_sh>0 && (abs(eta_cscsh_odd) > 1.6 && abs(eta_cscsh_odd) < 2.4) && abs(genGdMu_dxy)>20 && abs(genGdMu_dxy)<50"
num_clct_dxy2050_odd = den_clct_dxy2050_odd+" && has_clct>0"

den_clct_dxy1020_even = "has_csc_sh>0 && (abs(eta_cscsh_even) > 1.6 && abs(eta_cscsh_even) < 2.4) && abs(genGdMu_dxy)>10 && abs(genGdMu_dxy)<20"
num_clct_dxy1020_even = den_clct_dxy1020_even+" && has_clct>0"
den_clct_dxy2050_even = "has_csc_sh>0 && (abs(eta_cscsh_even) > 1.6 && abs(eta_cscsh_even) < 2.4) && abs(genGdMu_dxy)>20 && abs(genGdMu_dxy)<50"
num_clct_dxy2050_even = den_clct_dxy2050_even+" && has_clct>0"

den_clct_prompt_odd = "has_csc_sh>0 && (abs(eta_cscsh_odd) > 1.6 && abs(eta_cscsh_odd) < 2.4)"
num_clct_prompt_odd = den_clct_prompt_odd+" && has_clct>0"

den_clct_prompt_even = "has_csc_sh>0 && (abs(eta_cscsh_even) > 1.6 && abs(eta_cscsh_even) < 2.4)"
num_clct_prompt_even = den_clct_prompt_even+" && has_clct>0"

# ALCT
den_alct_dxy1020_odd = "has_csc_sh>0 && (abs(eta_cscsh_odd) > 1.6 && abs(eta_cscsh_odd) < 2.4) && abs(genGdMu_dxy)>10 && abs(genGdMu_dxy)<20"
num_alct_dxy1020_odd = den_alct_dxy1020_odd+" && has_alct>0"
den_alct_dxy2050_odd = "has_csc_sh>0 && (abs(eta_cscsh_odd) > 1.6 && abs(eta_cscsh_odd) < 2.4) && abs(genGdMu_dxy)>20 && abs(genGdMu_dxy)<50"
num_alct_dxy2050_odd = den_alct_dxy2050_odd+" && has_alct>0"

den_alct_dxy1020_even = "has_csc_sh>0 && (abs(eta_cscsh_even) > 1.6 && abs(eta_cscsh_even) < 2.4) && abs(genGdMu_dxy)>10 && abs(genGdMu_dxy)<20"
num_alct_dxy1020_even = den_alct_dxy1020_even+" && has_alct>0"
den_alct_dxy2050_even = "has_csc_sh>0 && (abs(eta_cscsh_even) > 1.6 && abs(eta_cscsh_even) < 2.4) && abs(genGdMu_dxy)>20 && abs(genGdMu_dxy)<50"
num_alct_dxy2050_even = den_alct_dxy2050_even+" && has_alct>0"

den_alct_prompt_odd = "has_csc_sh>0 && (abs(eta_cscsh_odd) > 1.6 && abs(eta_cscsh_odd) < 2.4)"
num_alct_prompt_odd = den_alct_prompt_odd+" && has_alct>0"

den_alct_prompt_even = "has_csc_sh>0 && (abs(eta_cscsh_even) > 1.6 && abs(eta_cscsh_even) < 2.4)"
num_alct_prompt_even = den_alct_prompt_even+" && has_alct>0"



pt_bins=[50,0,50]
eta_bins=[40,1.5,2.5]
phi_bins=[40,-3.5,3.5]
dxy_bins=[50,0,50]

#stations=["ME11","ME21","ME31","ME41","ME12","ME13"]
stations=["ME11"]
# xvars=["pt","eta","phi","genGdMu_dxy"]
xvars=["pt","phi","eta_cscsh_odd","eta_cscsh_even"]
binlist=[pt_bins,phi_bins,eta_bins,eta_bins]


# makeEfficiencies(xvars,stations,binlist,num_lct_dxy1020_odd,den_lct_dxy1020_odd,"dx10_20odd","10<dxy<20, odd cscs")
# makeEfficiencies(xvars,stations,binlist,num_lct_dxy2050_odd,den_lct_dxy2050_odd,"dx20_50odd","20<dxy<50, odd cscs")

# [prompt,dxy=10-20,dxy=20-50]
# odd
numerators_odd=[num_lct_prompt_odd,num_lct_dxy1020_odd,num_lct_dxy2050_odd]
denominators_odd=[den_lct_prompt_odd,den_lct_dxy1020_odd,den_lct_dxy2050_odd]
# even
numerators_even=[num_lct_prompt_even,num_lct_dxy1020_even,num_lct_dxy2050_even]
denominators_even=[den_lct_prompt_even,den_lct_dxy1020_even,den_lct_dxy2050_even]

# CLCT
# odd
numerators_clct_odd=[num_clct_prompt_odd,num_clct_dxy1020_odd,num_clct_dxy2050_odd]
denominators_clct_odd=[den_clct_prompt_odd,den_clct_dxy1020_odd,den_clct_dxy2050_odd]
# even
numerators_clct_even=[num_clct_prompt_even,num_clct_dxy1020_even,num_clct_dxy2050_even]
denominators_clct_even=[den_clct_prompt_even,den_clct_dxy1020_even,den_clct_dxy2050_even]

# ALCT
# odd
numerators_alct_odd=[num_alct_prompt_odd,num_alct_dxy1020_odd,num_alct_dxy2050_odd]
denominators_alct_odd=[den_alct_prompt_odd,den_alct_dxy1020_odd,den_alct_dxy2050_odd]
# even
numerators_alct_even=[num_alct_prompt_even,num_alct_dxy1020_even,num_alct_dxy2050_even]
denominators_alct_even=[den_alct_prompt_even,den_alct_dxy1020_even,den_alct_dxy2050_even]


samples2 = [promptMuonDir,displacedMuonDir]
samples3 = [promptMuonDir,displacedMuonDir,displacedMuonDir]
simpleNums = [num_lct_prompt_odd,num_lct_dxy1020_odd]
simpleDens = [den_lct_prompt_odd,den_lct_dxy1020_odd]
simpleLabels = ['Prompt Muon','Displaced Muon 10<dxy<20']

# makeAnyEff('LCT SimHits',"GEMCSCAnalyzer/trk_eff_CSC_",stations,xvars,binlist,samples,simpleNums,simpleDens,simpleLabels)


makeAnyEff('LCT_SimHits-even_CLCT',"GEMCSCAnalyzer/trk_eff_CSC_",stations,xvars,binlist,samples3,numerators_clct_even,denominators_clct_even,simpleLabels+['Displaced Muon 20<dxy<50'])
makeAnyEff('LCT_SimHits-odd_CLCT',"GEMCSCAnalyzer/trk_eff_CSC_",stations,xvars,binlist,samples3,numerators_clct_odd,denominators_clct_odd,simpleLabels+['Displaced Muon 20<dxy<50'])

makeAnyEff('LCT_SimHits-even_ALCT',"GEMCSCAnalyzer/trk_eff_CSC_",stations,xvars,binlist,samples3,numerators_alct_even,denominators_alct_even,simpleLabels+['Displaced Muon 20<dxy<50'])
makeAnyEff('LCT_SimHits-odd_ALCT',"GEMCSCAnalyzer/trk_eff_CSC_",stations,xvars,binlist,samples3,numerators_alct_odd,denominators_alct_odd,simpleLabels+['Displaced Muon 20<dxy<50'])


# makeCustomEfficiencies(xvars,stations,binlist,numerators_even,denominators_even,"variabledxy_even","variabledxy_even")

makeCustomEfficiencies(xvars,stations,binlist,numerators_clct_even,denominators_clct_even,"variabledxy_clct_even","variabledxy_clct_even")
makeCustomEfficiencies(xvars,stations,binlist,numerators_alct_even,denominators_alct_even,"variabledxy_alct_even","variabledxy_alct_even")

makeCustomEfficiencies(xvars,stations,binlist,numerators_clct_odd,denominators_clct_odd,"variabledxy_clct_odd","variabledxy_clct_odd")
makeCustomEfficiencies(xvars,stations,binlist,numerators_alct_odd,denominators_alct_odd,"variabledxy_alct_odd","variabledxy_alct_odd")






# makeEfficiencies(xvars,stations,binlist,num_lct_dxy05_odd_lcuts,den_lct_dxy05_odd_lcuts,"dx0_5odd_lcuts","0<dxy<5, odd cscs, |L_z|<200 L_xy<200")
# makeEfficiencies(xvars,stations,binlist,num_lct_dxy1020_odd_lcuts,den_lct_dxy1020_odd_lcuts,"dx10_20odd_lcuts","10<dxy<20, odd cscs,|L_z|<200 L_xy<200")
# makeEfficiencies(xvars,stations,binlist,num_lct_dxy3050_odd_lcuts,den_lct_dxy3050_odd_lcuts,"dx30_50odd_lcuts","30<dxy<50, odd cscs, |L_z|<200 L_xy<200")


# make efficiencies for just even or odd
# make d_xy abs

# makeEfficiencies("pt",pt_bins,num_lct_dxy05_odd,den_lct_dxy05_odd,"dx0_5odd","0<dxy<5, odd cscs")
# makeEfficiencies("pt",pt_bins,num_lct_dxy1020_odd,den_lct_dxy1020_odd,"dx10_20odd","10<dxy<20, odd cscs")
# makeEfficiencies("pt",pt_bins,num_lct_dxy3050_odd,den_lct_dxy3050_odd,"dx30_50odd","30<dxy<50, odd cscs")


# makeEfficiencies("pt",pt_bins,num_lct_dxy05,den_lct_dxy05,"dx0_5","0<dxy<5")
# makeEfficiencies("pt",pt_bins,num_lct_dxy1020,den_lct_dxy1020,"dx10_20","10<dxy<20")
# makeEfficiencies("pt",pt_bins,num_lct_dxy3050,den_lct_dxy3050,"dx30_50","30<dxy<50")

# makeEfficiencies("eta",eta_bins,num_lct_dxy05,den_lct_dxy05,"dxy0_5")
# makeEfficiencies("eta",eta_bins,num_lct_dxy1020,den_lct_dxy1020,"dxy10_20")
# makeEfficiencies("eta",eta_bins,num_lct_dxy3050,den_lct_dxy3050,"dxy30_50")


# makeEfficiencies("eta",eta_bins,num_lct,den_lct)
# makeEfficiencies("phi",phi_bins,num_lct,den_lct)
# makeEfficiencies("genGdMu_dxy",dxy_bins,num_lct,den_lct)

# den_pt15 = "has_csc_sh>0 && pt<15"
# num_pt15 = "has_csc_sh>0 && has_lct>0 && pt<15"
        
# displacedChain = makeChain(treename,displacedMuonDir)

# Example
# treename = "GEMCSCAnalyzer/trk_eff_ME31"
# den = "has_csc_sh>0 && pt >10"
# num = "has_csc_sh>0 && has_lct>0 && pt>10"
# den_pt15 = "has_csc_sh>0 && pt <15"
# num_pt15 = "has_csc_sh>0 && has_lct>0 && pt<15"

# c1 = TCanvas()
# c1.SetGridx()
# c1.SetGridy()
# c1.SetTickx()
# c1.SetTicky()

# h1 = TH1F("h1","h1",50,0,50)
# h2 = TH1F("h2","h2",50,0,50)
# promptChain.Draw("pt>>h1",den)
# promptChain.Draw("pt>>h2",num)
# e = TEfficiency(h2,h1)
# e.Draw("Efficiency")


# b1 = TH1F("b1","b1",50,0,50)
# # b1.GetYaxis().SetRangeUser(0.50,1.02)
# # b1.GetYaxis().SetNdivisions(520)
# b1.GetYaxis().SetTitle("Efficiency")
# b1.GetXaxis().SetTitle("Simulated muon #eta")
# # b1.SetTitle(" "*12 +"YE3/1 stub reconstruction"+" "*14 + "CMS Phase-II Simulation Preliminary")
# b1.SetStats(0)

# b1.Draw()
# e.Draw("same")

# c1.SaveAs("LCT_has_sh_pt.png")

# t = promptChain.Get(treename)
# h1 = TH1F("h1","h1",40,1.5,2.5)
# t.Draw("(-eta) >> h1",den)
# h2 = TH1F("h2","h2",40,1.5,2.5)
# t.Draw("(-eta) >> h2",num)
# e = TEfficiency(h2,h1)

# e.Draw("e")
# promptChain.Draw()


# c1 = TCanvas()
# c1.SetGridx()
# c1.SetGridy()
# c1.SetTickx()
# c1.SetTicky()





# def getEff(file,dir,den,num):
#     f = TFile(file)
#     t = f.Get(dir)
#     h1 = TH1F("h1","h1",40,1.5,2.5)
#     t.Draw("(-eta) >> h1",den)
#     h2 = TH1F("h2","h2",40,1.5,2.5)
#     t.Draw("(-eta) >> h2",num)
#     e = TEfficiency(h2,h1)
#     return e

# b1 = TH1F("b1","b1",40,1.5,2.5)
# b1.GetYaxis().SetRangeUser(0.50,1.02)
# b1.GetYaxis().SetNdivisions(520)
# b1.GetYaxis().SetTitle("Efficiency")
# b1.GetXaxis().SetTitle("Simulated muon #eta")
# b1.SetTitle(" "*12 +"YE3/1 stub reconstruction"+" "*14 + "CMS Phase-II Simulation Preliminary")
# b1.SetStats(0)

# treename = "GEMCSCAnalyzer/trk_eff_ME31"
# den = "has_csc_sh>0 && pt >10"
# num = "has_csc_sh>0 && has_lct>0 && pt>10"
# den_pt15 = "has_csc_sh>0 && pt <15"
# num_pt15 = "has_csc_sh>0 && has_lct>0 && pt<15"
# #e2 = getEff("PU140_100k_2019withoutGEM_GEMCSCAna.root",treename,den,num)
# e3 = getEff("PU140_200k_Pt2-50_2023_GE21dphi_v3_GEMCSC.root",treename,den,num)
# e2 = getEff("PU140_200k_Pt2-50_GEMCSC_LCTTiming.root",treename,den,num)
# e4 = getEff("PU140_200k_Pt2-50_GEMCSC_LCTTiming.root",treename,den_pt15,num_pt15)
# #e4 = getEff("PU140_200k_GE21dphi_v3_GEMCSC_hsfromgem_ana.root",treename,den,num)
# #e = getEff("PU140_100k_2023_fixeven_GEMCSCAna.root",treename,den,num)

# #e5 = getEff("GSA_GEMCSC_Step2_Com_PU140.root",treename,den,num)
# #e6 = getEff("GSA_GEMCSC_Step3_Com_PU140.root",treename,den,num)
# #e7 = getEff("GSA_GEMCSC_Step4_Com_PU140.root",treename,den,num)

# #e1.SetLineWidth(2)
# #e2.SetLineColor(kRed)
# #e2.SetLineWidth(2)
# e3.SetFillColor(kRed)
# #e3.SetLineWidth(2)
# e2.SetFillColor(kAzure-1)
# e4.SetFillColor(kMagenta)
# b1.Draw("e3")
# e2.Draw("e3same")
# e4.Draw("e3same")
# e3.Draw("e3same")

# legend = TLegend(0.20,0.15,.89,0.42, "", "brNDC")
# legend.SetBorderSize(0)
# #legend.SetFillStyle(0)
# legend.SetFillColor(kWhite)
# #legend.SetTextSize(0.05)
# legend.SetHeader(" "*5+"PU140,ILT algorithm")
# #legend.AddEntry(e1,"CSC SLHC Algorithm (4 hits)","l")
# #legend.AddEntry(e2,"CSC only SLHC Algorithm in 2019","l")
# #legend.AddEntry(e3,"GEM-CSC Algorithm in 2023 Jason","l")
# #legend.AddEntry(e4,"after Jose's correction and bugfixed","f")
# legend.AddEntry(e2,"latest version, P_{T} > 10 GeV","f")
# legend.AddEntry(e4,"lastest version, P_{T} < 15 GeV","f")
# legend.AddEntry(e3,"before Jose's correction, P_{T} > 10 GeV","f")
# #legend.AddEntry(e7,"GEM-CSC Algorithm (step 4)","l")
# legend.Draw("same")

# #tex = TLatex(0.25,0.5,"PU140, P\_T > 10Gev")
# #tex.SetTextSize(0.05)
# #tex.SetNDC()
# #tex.Draw("same")

# c1.SaveAs("LCT_100k_ME31_reco_eff_com4_PU140.pdf")
# c1.SaveAs("LCT_100k_ME31_reco_eff_com4_PU140.png")
