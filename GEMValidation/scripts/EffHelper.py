# This file contains helper functions for LCTEfficiency.py

from ROOT import *
import os
import datetime as dt

# 'YYYY-MM-DD'
today = dt.date.today().isoformat()
time = dt.date.today().strftime("%H_%M")

promptMuonDir = '/eos/uscms/store/user/tahuang/SLHC23_patch1_2023Muon_gen_sim_Pt2_50_1M/GEMCSCAna_ctau0_Pt2_50_20170131/170218_213142/0000/'

displacedMuonDir = '/eos/uscms/store/user/tahuang/DisplacedMuonGun_1M_FlatPt1_50_FlatDxy0_50CM_GEN_SIM_CMSSW620SLHC_v5/GEMCSC_Ana_displacedMuonGun_2023Muon_20170222_v5/170223_195129/0000/'



def getEff(file,dir,den,num):
    f = TFile(file)
    t = f.Get(dir)
    h1 = TH1F("h1","h1",40,1.5,2.5)
    t.Draw("(-eta) >> h1",den)
    h2 = TH1F("h2","h2",40,1.5,2.5)
    t.Draw("(-eta) >> h2",num)
    e = TEfficiency(h2,h1)
    return e


def makeChain(treename,filedir):
    chain = TChain(treename)
    counter = 0
    if os.path.isdir(filedir):
        ls = os.listdir(filedir)
        for x in ls:
            x = filedir[:]+x
            # print x
            if os.path.isfile(x):
                counter=counter+1
                chain.Add(x)
    elif os.path.isfile(filedir):
        counter=counter+1
        chain.Add(filedir)
    else:
        print " it is not file or dir ", filedir
    print 'Chain created with',counter,'files.'
    return chain

# title = "ME11 efficiency for ___(title)___"
# treenamebase = path to samples within root file tree (excluding station #)
# stations = loop over samples from different stations (ME11,ME21,etc.)
#---> treenamebase + station = root file path to samples
# xvars = x-variable for each efficiency plot
# xbinlist = [num bins, min bin, max bin] with each xvar
# samples = source directory for each comparison
# nums = numerator (cuts) for each comparison
# dens = denominator (cuts) for each comparison
# labels = legend title and indentifier for each comparison

def makeAnyEff(title,treenamebase,stations,xvars,xbinlist,samples,nums,dens,labels,analyze=None):
    if len(xvars) != len(xbinlist):
        print 'X-Variable and Bin lists must be same length!'
        exit
    elif len(samples) != len(nums):
        print 'Samples list must be same length as *nums*,dens,labels!'
        exit
    elif len(samples) != len(dens):
        print 'Samples list must be same length as nums,*dens*,labels!'
        exit
    elif len(samples) != len(labels):
        print 'Samples list must be same length as nums,dens,*labels*!'
        exit

    for stn in stations:
        treename = treenamebase+stn

        # make list of chains -> each for different comparison
        chainlist = []
        entrylist = [] 
        for index in range(len(samples)):
            newChain = makeChain(treename,samples[index])
            print 'Chain created for',labels[index]
            chainlist.append(newChain)
            numEntries = newChain.GetEntries()
            print 'Number of entries:',numEntries
            entrylist.append(numEntries)

        # index -> xvars,xbinlist
        for index in range(len(xvars)):
            print 'Station:',stn
            print 'X-variable:',xvars[index]
            print 'Bins:',xbinlist[index]
            print ''

            c1 = TCanvas()
            c1.SetGridx()
            c1.SetGridy()
            c1.SetTickx()
            c1.SetTicky()
            gStyle.SetOptFit(0111)
            gStyle.SetOptStat(0)
            
            th1flist = []       # store TH1F pairs
            tefflist = []       # store TEfficiency plots
            # sample -> samples,nums,dens,labels
            for sample in range(len(samples)):
                print 'Num:',nums[sample]
                print 'Den:',dens[sample]
                print 'Label:',labels[sample]
                print ''

                h1 = TH1F("h1_"+str(sample),"h1_"+str(sample),*xbinlist[index])
                h2 = TH1F("h2_"+str(sample),"h2_"+str(sample),*xbinlist[index])
                chainlist[sample].Draw(xvars[index]+">>h1_"+str(sample),dens[sample])
                chainlist[sample].Draw(xvars[index]+">>h2_"+str(sample),nums[sample])
                th1flist.append([h1,h2])

                e1 = TEfficiency(h2,h1)
                e1.SetFillColor(sample+2)
                e1.SetMarkerColor(sample+2)
                e1.SetMarkerStyle(sample+20)
                tefflist.append(e1)
                del h1,h2,e1 # data stored in lists
    
            b1 = TH1F("b1","b1",*xbinlist[index])
            b1.GetYaxis().SetRangeUser(0.50,1.05)
            b1.GetYaxis().SetNdivisions(520)
            b1.GetYaxis().SetTitle("Efficiency")
            b1.GetXaxis().SetTitle("Simulated muon "+xvars[index])
            b1.SetTitle(" "*12 +stn+" efficiency for "+title+" "*14 + "CMS Phase-II Simulation Preliminary")
            b1.SetStats(0)
            b1.Draw("")

            for eff in tefflist:
                eff.Draw("same")
                
            legend = TLegend(0.20,0.15,.89,0.42, "", "brNDC")
            legend.SetBorderSize(0)
            legend.SetFillColor(kWhite)
            legend.SetHeader(" "*5+"Efficiency")
            for entry in range(len(labels)):
                legend.AddEntry(tefflist[entry],labels[entry],"l") # VERIFY
            legend.Draw("same")
    
            c1.SaveAs("/Eff_"+title+"_"+str(len(labels))+"_"+stn+"_"+xvars[index]+"_"+today+"_"+time+".png")
    
            del b1
            
# title = Full title of plots
# treenamebase = path to samples within root file tree (excluding station #)
# stations = loop over samples from different stations (ME11,ME21,etc.)
# avars = x-variable to analyze
# avarbins = bins for each x-variable -> [num,min,max]
# samples = data sets to pull from
# cuts = cuts made on each data set
def analyzePlots(title,treenamebase,stations,avars,avarbins,samples,cuts,labels):
    if len(avars) != len(avarbins):
        print 'Analyzed X-Variablea and Bin lists must be same length!'
        exit
    elif len(samples) != len(cuts):
        print 'Samples list must be same length as *cuts*,labels!'
        exit
    elif len(samples) != len(labels):
        print 'Samples list must be same length as cuts,*labels*!'
        exit

    for stn in stations:
        treename = treenamebase+stn

        # make list of chains -> each for different comparison
        chainlist = []
        entrylist = [] 
        for index in range(len(samples)):
            newChain = makeChain(treename,samples[index])
            print 'Chain created for',labels[index]
            chainlist.append(newChain)
            numEntries = newChain.GetEntries()
            print 'Number of entries:',numEntries
            entrylist.append(numEntries)

        # index -> avars,avarbins
        for index in range(len(avars)):
            print 'Station:',stn
            print 'X-variable:',avars[index]
            print 'Bins:',avarbins[index]
            print ''

            c1 = TCanvas()
            c1.SetGridx()
            c1.SetGridy()
            c1.SetTickx()
            c1.SetTicky()
            gStyle.SetOptFit(0111)
            gStyle.SetOptStat(111111)
            
            th1flist = []       # store histograms
            th1stack = THStack("th1stack"," "*12 +title+" "*14 + "CMS Phase-II Simulation Preliminary");
            # sample -> samples,cuts,labels
            for sample in range(len(samples)):
                print 'Cut:',cuts[sample]
                print 'Label:',labels[sample]
                print ''

                h1 = TH1F(labels[sample],labels[sample],*avarbins[index])
                chainlist[sample].Draw(avars[index]+">>"+labels[sample],cuts[sample])
                h1.Scale(1.0/h1.GetEntries())

                # h1 = TH1F("h1_"+str(sample),"h1_"+str(sample),*avarbins[index])
                # h2 = TH1F("h2_"+str(sample),"h2_"+str(sample),*avarbins[index])
                # chainlist[sample].Draw(avars[index]+">>h1_"+str(sample),dens[sample])
                # chainlist[sample].Draw(avars[index]+">>h2_"+str(sample),nums[sample])

                # h1.SetFillColor(sample+2)
                h1.SetMarkerColor(sample+2)
                h1.SetMarkerStyle(sample+20)
                th1flist.append(h1)
                th1stack.Add(h1)
                del h1 # data stored in lists
    
            # b1 = TH1F("b1","b1",*avarbins[index])
            # # b1.GetYaxis().SetRangeUser(0.50,1.05)
            # # b1.GetYaxis().SetNdivisions(520)
            # # b1.GetYaxis().SetTitle("Efficiency")
            # b1.GetXaxis().SetTitle("Simulated muon "+avars[index])
            # b1.SetTitle(" "*12 +title+" "*14 + "CMS Phase-II Simulation Preliminary")
            # b1.SetStats(0)
            # b1.Draw("")
            # for hist in th1flist:
            #     hist.Draw("psame")

            th1stack.Draw("nostack,p")
                
            # legend = TLegend(0.20,0.15,0.89,0.42, "", "brNDC")
            # legend = TLegend(0.1,0.7,0.48,0.9, "", "brNDC")
            # legend.SetBorderSize(0)
            # legend.SetFillStyle(0)
            # legend.SetHeader(" "*5+"Samples")
            # for entry in range(len(labels)):
            #     legend.AddEntry(th1flist[entry],labels[entry],"f") # VERIFY
            # legend.Draw("same")

            gPad.BuildLegend(0.25,0.25,0.45,0.55,"")
    
            c1.SaveAs(title+"_"+str(len(labels))+"_"+stn+"_"+avars[index]+"_"+today+"_"+time+".png")
    
            # del b1    



def makeEfficiencies(xvars,stations,binlist,num,den,suffix,label):
    treenamebase = "GEMCSCAnalyzer/trk_eff_CSC_"        
    if len(xvars) != len(binlist):
        print 'X-Variables and Bins must be same length'
        exit
    for stn in stations:
        treename = treenamebase+stn
        promptChain = makeChain(treename,promptMuonDir)
        print "Prompt Entries:",promptChain.GetEntries()
        displacedChain = makeChain(treename,displacedMuonDir)
        print "Displaced Entries:",displacedChain.GetEntries()

        for index in range(0,len(xvars)):
            print 'xvar:',xvars[index]
            print 'station:',stn
            print 'bins:',binlist[index]
            print 'num:',num
            print 'den:',den
            print 'suffix:',suffix
            print 'label:',label
            print ''
            # print 'X-Variable=',xvars[index]
            # print 'Station=',stn
            # print 'Efficiency vs.',xvars[index],'at',treename
            c1 = TCanvas()
            c1.SetGridx()
            c1.SetGridy()
            c1.SetTickx()
            c1.SetTicky()
            gStyle.SetOptFit(0111)
            gStyle.SetOptStat(0)
            
            # Prompt
            h1 = TH1F("h1","h1",*binlist[index])
            h2 = TH1F("h2","h2",*binlist[index])
            promptChain.Draw(xvars[index]+">>h1",den)
            promptChain.Draw(xvars[index]+">>h2",num)
            e1 = TEfficiency(h2,h1)
            e1.SetFillColor(kRed)
            e1.SetMarkerColor(kRed)
            # e1.SetMarkerSize(2)
            e1.SetMarkerStyle(22)

            # Displaced
            h3 = TH1F("h3","h3",*binlist[index])
            h4 = TH1F("h4","h4",*binlist[index])
            displacedChain.Draw(xvars[index]+">>h3",den)
            displacedChain.Draw(xvars[index]+">>h4",num)
            e2 = TEfficiency(h4,h3)
            e2.SetFillColor(kBlue)
            e2.SetMarkerColor(kBlue)
            # e2.SetMarkerSize(2)
            e2.SetMarkerStyle(23)

    
            b1 = TH1F("b1","b1",*binlist[index])
            b1.GetYaxis().SetRangeUser(0.50,1.05)
            b1.GetYaxis().SetNdivisions(520)
            b1.GetYaxis().SetTitle("Efficiency")
            b1.GetXaxis().SetTitle("Simulated muon "+xvars[index])
            b1.SetTitle(" "*12 +stn+" efficiency for "+label+" "*14 + "CMS Phase-II Simulation Preliminary")
            b1.SetStats(0)
            
            b1.Draw("")
            e1.Draw("same")
            e2.Draw("same")
                
            legend = TLegend(0.20,0.15,.89,0.42, "", "brNDC")
            legend.SetBorderSize(0)
            legend.SetFillColor(kWhite)
            legend.SetHeader(" "*5+"Efficiency")
            legend.AddEntry(e1,"Prompt Muon","f")
            legend.AddEntry(e2,"Displaced Muon","f")
            # legend.AddEntry(e4,"lastest version, P_{T} < 15 GeV","f")
            # legend.AddEntry(e3,"before Jose's correction, P_{T} > 10 GeV","f")
            legend.Draw("same")
    
            c1.SaveAs("LCT_"+stn+"_has_sh_"+xvars[index]+"_"+suffix+"_Mar_3_1410.png")
    
            del e1,e2
            del h1,h2,h3,h4
            del b1
    

def makeCustomEfficiencies(xvars,stations,binlist,num,den,suffix,label):
    treenamebase = "GEMCSCAnalyzer/trk_eff_CSC_"        
    if len(xvars) != len(binlist):
        print 'X-Variables and Bins must be same length'
        exit
    for stn in stations:
        treename = treenamebase+stn
        promptChain = makeChain(treename,promptMuonDir)
        print "Prompt Entries:",promptChain.GetEntries()
        displacedChain = makeChain(treename,displacedMuonDir)
        print "Displaced Entries:",displacedChain.GetEntries()

        for index in range(len(xvars)):
            print 'INDEX:',index
            print 'xvar:',xvars[index]
            print 'station:',stn
            print 'bins:',binlist[index]
            print 'num:',num
            print 'den:',den
            print 'suffix:',suffix
            print 'label:',label
            print ''
            # print 'X-Variable=',xvars[index]
            # print 'Station=',stn
            # print 'Efficiency vs.',xvars[index],'at',treename
            c1 = TCanvas()
            c1.SetGridx()
            c1.SetGridy()
            c1.SetTickx()
            c1.SetTicky()
            gStyle.SetOptFit(0111)
            gStyle.SetOptStat(0)
            
            # Prompt
            h1 = TH1F("h1","h1",*binlist[index])
            h2 = TH1F("h2","h2",*binlist[index])
            promptChain.Draw(xvars[index]+">>h1",den[0])
            promptChain.Draw(xvars[index]+">>h2",num[0])
            e1 = TEfficiency(h2,h1)
            e1.SetFillColor(kRed)
            e1.SetMarkerColor(kRed)
            # e1.SetMarkerSize(2)
            e1.SetMarkerStyle(22)

            # Displaced 10<dxy<20
            h3 = TH1F("h3","h3",*binlist[index])
            h4 = TH1F("h4","h4",*binlist[index])
            displacedChain.Draw(xvars[index]+">>h3",den[1])
            displacedChain.Draw(xvars[index]+">>h4",num[1])
            e2 = TEfficiency(h4,h3)
            e2.SetFillColor(kBlue)
            e2.SetMarkerColor(kBlue)
            # e2.SetMarkerSize(2)
            e2.SetMarkerStyle(23)

            # Displaced 20<dxy<50
            h5 = TH1F("h5","h5",*binlist[index])
            h6 = TH1F("h6","h6",*binlist[index])
            displacedChain.Draw(xvars[index]+">>h5",den[2])
            displacedChain.Draw(xvars[index]+">>h6",num[2])
            e3 = TEfficiency(h6,h5)
            e3.SetFillColor(kGreen)
            e3.SetMarkerColor(kGreen)
            # e3.SetMarkerSize(2)
            e3.SetMarkerStyle(20)

    
            b1 = TH1F("b1","b1",*binlist[index])
            b1.GetYaxis().SetRangeUser(0.50,1.05)
            b1.GetYaxis().SetNdivisions(520)
            b1.GetYaxis().SetTitle("Efficiency")
            b1.GetXaxis().SetTitle("Simulated muon "+xvars[index])
            b1.SetTitle(" "*12 +stn+" efficiency for "+label+" "*14 + "CMS Phase-II Simulation Preliminary")
            b1.SetStats(0)
            
            b1.Draw("")
            e1.Draw("same")
            e2.Draw("same")
            e3.Draw("same")
                
            legend = TLegend(0.20,0.15,.89,0.42, "", "brNDC")
            legend.SetBorderSize(0)
            legend.SetFillColor(kWhite)
            legend.SetHeader(" "*5+"Efficiency")
            legend.AddEntry(e1,"Prompt Muon","f")
            legend.AddEntry(e2,"Displaced Muon 10<dxy<20","f")
            legend.AddEntry(e3,"Prompt Muon 20<dxy<50","f")
            # legend.AddEntry(e4,"lastest version, P_{T} < 15 GeV","f")
            # legend.AddEntry(e3,"before Jose's correction, P_{T} > 10 GeV","f")
            legend.Draw("same")
    
            c1.SaveAs("LCT_"+stn+"_has_sh_"+xvars[index]+"_"+suffix+"_Mar_3.png")
    
            del e1,e2,e3
            del h1,h2,h3,h4,h5,h6
            del b1
