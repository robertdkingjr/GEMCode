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
num_lct_dxy05_odd = "has_csc_sh>0 && (abs(eta_cscsh_odd) > 1.6 && abs(eta_cscsh_odd) < 2.4) && abs(genGdMu_dxy)<5 && (has_lct&1)>0"
den_lct_dxy1020_odd = "has_csc_sh>0 && (abs(eta_cscsh_odd) > 1.6 && abs(eta_cscsh_odd) < 2.4) && abs(genGdMu_dxy)>10 && abs(genGdMu_dxy)<20"
num_lct_dxy1020_odd = "has_csc_sh>0 && (abs(eta_cscsh_odd) > 1.6 && abs(eta_cscsh_odd) < 2.4) && abs(genGdMu_dxy)>10 && abs(genGdMu_dxy)<20 && (has_lct&1)>0"
den_lct_dxy3050_odd = "has_csc_sh>0 && (abs(eta_cscsh_odd) > 1.6 && abs(eta_cscsh_odd) < 2.4) && abs(genGdMu_dxy)>30 && abs(genGdMu_dxy)<50"
num_lct_dxy3050_odd = "has_csc_sh>0 && (abs(eta_cscsh_odd) > 1.6 && abs(eta_cscsh_odd) < 2.4) && abs(genGdMu_dxy)>30 && abs(genGdMu_dxy)<50 && (has_lct&1)>0"

# Add Lxy,Lz requirements
den_lct_dxy05_odd_lcuts = "has_csc_sh>0 && (abs(eta_cscsh_odd) > 1.6 && abs(eta_cscsh_odd) < 2.4) && abs(genGdMu_dxy)<5 && abs(genGdMu_vz)<200 && genGdMu_lxy<200"
num_lct_dxy05_odd_lcuts = den_lct_dxy05_odd_lcuts+" && (has_lct&1)>0"
den_lct_dxy1020_odd_lcuts = "has_csc_sh>0 && (abs(eta_cscsh_odd) > 1.6 && abs(eta_cscsh_odd) < 2.4) && abs(genGdMu_dxy)>10 && abs(genGdMu_dxy)<20 && abs(genGdMu_vz)<200 && genGdMu_lxy<200"
num_lct_dxy1020_odd_lcuts = den_lct_dxy1020_odd_lcuts+" && (has_lct&1)>0"
den_lct_dxy3050_odd_lcuts = "has_csc_sh>0 && (abs(eta_cscsh_odd) > 1.6 && abs(eta_cscsh_odd) < 2.4) && abs(genGdMu_dxy)>30 && abs(genGdMu_dxy)<50 && abs(genGdMu_vz)<200 && genGdMu_lxy<200"
num_lct_dxy3050_odd_lcuts = den_lct_dxy3050_odd_lcuts+" && (has_lct&1)>0"


# 3/3/17 - no L cuts

den_lct_dxy1020_odd = "has_csc_sh>0 && (abs(eta_cscsh_odd) > 1.6 && abs(eta_cscsh_odd) < 2.4) && abs(genGdMu_dxy)>10 && abs(genGdMu_dxy)<20"
num_lct_dxy1020_odd = den_lct_dxy1020_odd+" && (has_lct&1)>0"
den_lct_dxy2050_odd = "has_csc_sh>0 && (abs(eta_cscsh_odd) > 1.6 && abs(eta_cscsh_odd) < 2.4) && abs(genGdMu_dxy)>20 && abs(genGdMu_dxy)<50"
num_lct_dxy2050_odd = den_lct_dxy2050_odd+" && (has_lct&1)>0"

den_lct_dxy1020_even = "has_csc_sh>0 && (abs(eta_cscsh_even) > 1.6 && abs(eta_cscsh_even) < 2.4) && abs(genGdMu_dxy)>10 && abs(genGdMu_dxy)<20"
num_lct_dxy1020_even = den_lct_dxy1020_even+" && (has_lct&2)>0"
den_lct_dxy2050_even = "has_csc_sh>0 && (abs(eta_cscsh_even) > 1.6 && abs(eta_cscsh_even) < 2.4) && abs(genGdMu_dxy)>20 && abs(genGdMu_dxy)<50"
num_lct_dxy2050_even = den_lct_dxy2050_even+" && (has_lct&2)>0"

den_lct_prompt_odd = "has_csc_sh>0 && (abs(eta_cscsh_odd) > 1.6 && abs(eta_cscsh_odd) < 2.4)"
num_lct_prompt_odd = den_lct_prompt_odd+" && (has_lct&1)>0"

den_lct_prompt_even = "has_csc_sh>0 && (abs(eta_cscsh_even) > 1.6 && abs(eta_cscsh_even) < 2.4)"
num_lct_prompt_even = den_lct_prompt_even+" && (has_lct&2)>0"


# CLCT
den_clct_dxy1020_odd = "has_csc_sh>0 && (abs(eta_cscsh_odd) > 1.6 && abs(eta_cscsh_odd) < 2.4) && abs(genGdMu_dxy)>10 && abs(genGdMu_dxy)<20"
num_clct_dxy1020_odd = den_clct_dxy1020_odd+" && (has_clct&1)>0"
den_clct_dxy2050_odd = "has_csc_sh>0 && (abs(eta_cscsh_odd) > 1.6 && abs(eta_cscsh_odd) < 2.4) && abs(genGdMu_dxy)>20 && abs(genGdMu_dxy)<50"
num_clct_dxy2050_odd = den_clct_dxy2050_odd+" && (has_clct&1)>0"

den_clct_dxy1020_even = "has_csc_sh>0 && (abs(eta_cscsh_even) > 1.6 && abs(eta_cscsh_even) < 2.4) && abs(genGdMu_dxy)>10 && abs(genGdMu_dxy)<20"
num_clct_dxy1020_even = den_clct_dxy1020_even+" && (has_clct&2)>0"
den_clct_dxy2050_even = "has_csc_sh>0 && (abs(eta_cscsh_even) > 1.6 && abs(eta_cscsh_even) < 2.4) && abs(genGdMu_dxy)>20 && abs(genGdMu_dxy)<50"
num_clct_dxy2050_even = den_clct_dxy2050_even+" && (has_clct&2)>0"

den_clct_prompt_odd = "has_csc_sh>0 && (abs(eta_cscsh_odd) > 1.6 && abs(eta_cscsh_odd) < 2.4)"
num_clct_prompt_odd = den_clct_prompt_odd+" && (has_clct&1)>0"

den_clct_prompt_even = "has_csc_sh>0 && (abs(eta_cscsh_even) > 1.6 && abs(eta_cscsh_even) < 2.4)"
num_clct_prompt_even = den_clct_prompt_even+" && (has_clct&2)>0"

# ALCT
den_alct_dxy1020_odd = "has_csc_sh>0 && (abs(eta_cscsh_odd) > 1.6 && abs(eta_cscsh_odd) < 2.4) && abs(genGdMu_dxy)>10 && abs(genGdMu_dxy)<20"
num_alct_dxy1020_odd = den_alct_dxy1020_odd+" && (has_alct&1)>0"
den_alct_dxy2050_odd = "has_csc_sh>0 && (abs(eta_cscsh_odd) > 1.6 && abs(eta_cscsh_odd) < 2.4) && abs(genGdMu_dxy)>20 && abs(genGdMu_dxy)<50"
num_alct_dxy2050_odd = den_alct_dxy2050_odd+" && (has_alct&1)>0"

den_alct_dxy1020_even = "has_csc_sh>0 && (abs(eta_cscsh_even) > 1.6 && abs(eta_cscsh_even) < 2.4) && abs(genGdMu_dxy)>10 && abs(genGdMu_dxy)<20"
num_alct_dxy1020_even = den_alct_dxy1020_even+" && (has_alct&2)>0"
den_alct_dxy2050_even = "has_csc_sh>0 && (abs(eta_cscsh_even) > 1.6 && abs(eta_cscsh_even) < 2.4) && abs(genGdMu_dxy)>20 && abs(genGdMu_dxy)<50"
num_alct_dxy2050_even = den_alct_dxy2050_even+" && (has_alct&2)>0"

den_alct_prompt_odd = "has_csc_sh>0 && (abs(eta_cscsh_odd) > 1.6 && abs(eta_cscsh_odd) < 2.4)"
num_alct_prompt_odd = den_alct_prompt_odd+" && (has_alct&1)>0"

den_alct_prompt_even = "has_csc_sh>0 && (abs(eta_cscsh_even) > 1.6 && abs(eta_cscsh_even) < 2.4)"
num_alct_prompt_even = den_alct_prompt_even+" && (has_alct&2)>0"


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


dxycutlabels = ['Prompt Muon','Displaced Muon 10<dxy<20','Displaced Muon 20<dxy<50']

pt_bins=[50,0,50]
eta_bins=[40,1.5,2.5]
phi_bins=[40,-3.5,3.5]
dxy_bins=[50,0,50]
quality_bins=[16,0,15]
pattern_bins=[16,0,15]          # VERIFY
bend_bins=[40,-5,5]


treebase = "GEMCSCAnalyzer/trk_eff_CSC_"
#stations=["ME11","ME21","ME31","ME41","ME12","ME13"]
stations=["ME11"]
# xvars=["pt","eta","phi","genGdMu_dxy"]
# xvars=["pt","phi","eta_cscsh_odd","eta_cscsh_even"]
# binlist=[pt_bins,phi_bins,eta_bins,eta_bins]

# 3/5/17 Checking CLCT Quality
bendvars=["bend_lct_even","bend_lct_odd"]
bendbinlist=[bend_bins,bend_bins]
qualvars=["quality_even","quality_odd"]
qualbinlist=[quality_bins,quality_bins]
# pattvars=[]

# makeAnyEff('LCT_SimHits_CLCTBending',treebase,stations,bendvars,bendbinlist,samples3,numerators_even,denominators_even,dxycutlabels)
# makeAnyEff('LCT_SimHits_CLCTQuality',treebase,stations,qualvars,qualbinlist,samples3,numerators_even,denominators_even,dxycutlabels)
# makeAnyEff('LCT_SimHits_CLCTPattern',treebase,stations,bendvars,bendbinlist,samples3,numerators_even,denominators_even,dxycutlabels)


# 3/10/17 - Looking into bending/quality of LCTs
analyzePlots("Bending angle for LCTs in ME11",treebase,stations,bendvars,bendbinlist,samples3,numerators_even,dxycutlabels)
analyzePlots("Quality for LCTs in ME11",treebase,stations,qualvars,qualbinlist,samples3,numerators_even,dxycutlabels)


# makeAnyEff('LCT SimHits',"GEMCSCAnalyzer/trk_eff_CSC_",stations,xvars,binlist,samples,simpleNums,simpleDens,simpleLabels)


# makeAnyEff('LCT_SimHits-even_CLCT',"GEMCSCAnalyzer/trk_eff_CSC_",stations,xvars,binlist,samples3,numerators_clct_even,denominators_clct_even,simpleLabels+['Displaced Muon 20<dxy<50'])
# makeAnyEff('LCT_SimHits-odd_CLCT',"GEMCSCAnalyzer/trk_eff_CSC_",stations,xvars,binlist,samples3,numerators_clct_odd,denominators_clct_odd,simpleLabels+['Displaced Muon 20<dxy<50'])

# makeAnyEff('LCT_SimHits-even_ALCT',"GEMCSCAnalyzer/trk_eff_CSC_",stations,xvars,binlist,samples3,numerators_alct_even,denominators_alct_even,simpleLabels+['Displaced Muon 20<dxy<50'])
# makeAnyEff('LCT_SimHits-odd_ALCT',"GEMCSCAnalyzer/trk_eff_CSC_",stations,xvars,binlist,samples3,numerators_alct_odd,denominators_alct_odd,simpleLabels+['Displaced Muon 20<dxy<50'])


# makeCustomEfficiencies(xvars,stations,binlist,numerators_even,denominators_even,"variabledxy_even","variabledxy_even")

# makeCustomEfficiencies(xvars,stations,binlist,numerators_clct_even,denominators_clct_even,"variabledxy_clct_even","variabledxy_clct_even")
# makeCustomEfficiencies(xvars,stations,binlist,numerators_alct_even,denominators_alct_even,"variabledxy_alct_even","variabledxy_alct_even")

# makeCustomEfficiencies(xvars,stations,binlist,numerators_clct_odd,denominators_clct_odd,"variabledxy_clct_odd","variabledxy_clct_odd")
# makeCustomEfficiencies(xvars,stations,binlist,numerators_alct_odd,denominators_alct_odd,"variabledxy_alct_odd","variabledxy_alct_odd")






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

