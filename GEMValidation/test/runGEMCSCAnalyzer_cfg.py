import FWCore.ParameterSet.Config as cms

process = cms.Process("GEMCSCANA")

## Standard sequence
process.load('Configuration.StandardSequences.Services_cff')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('Configuration.Geometry.GeometryExtended2023HGCalMuonReco_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_PostLS1_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

## TrackingComponentsRecord required for matchers
process.load('TrackPropagation.SteppingHelixPropagator.SteppingHelixPropagatorOpposite_cfi')
process.load('TrackPropagation.SteppingHelixPropagator.SteppingHelixPropagatorAlong_cfi')

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(10000) )

process.options = cms.untracked.PSet( wantSummary = cms.untracked.bool(True) )

process.source = cms.Source("PoolSource",
	fileNames = cms.untracked.vstring('file:/uscms/home/dildick/nobackup/work/MuonPhaseIIScopeDoc/CMSSW_6_2_0_SLHC28/src/out_digi.root'),
)

from GEMCode.GEMValidation.InputFileHelpers import *

Inputdir=['/eos/uscms/store/user/tahuang/SLHC23_patch1_2023Muon_gen_sim_Pt2_50_1M/SLHC25_patch1_2023Muon_1M_L1_PU0_Pt2_50_updategemeta/1bf93df4dfbb43dc918bd6e47dedbf79/']
Inputdir=['/eos/uscms/store/user/lpcgem/SingleMuFwdPt2to50_v2/SingleMuFwdPt2to50_v2_DIGI_L1/160318_043123/0000/']
process = useInputDir(process, Inputdir)
#process = useInputDir(process, eosfiles["cT_100_14TeV_PU140_HLT_fullScope"])
#print process.source.fileNames

process.TFileService = cms.Service("TFileService",
    #fileName = cms.string("out_ana_DarkSUSY_mH_125_mGammaD_20000_cT_100_14TeV_PU140_HLT_fullScope.root")
    fileName = cms.string("out_ana_elehits.test.root")
)

## global tag for upgrade studies
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:upgradePLS3', '')

from GEMCode.GEMValidation.simTrackMatching_cfi import SimTrackMatching
process.GEMCSCAnalyzer = cms.EDAnalyzer("GEMCSCAnalyzer",
    verbose = cms.int32(0),
    simTrackMatching = SimTrackMatching
)
matching = process.GEMCSCAnalyzer.simTrackMatching
matching.simTrack.minPt = 2
matching.matchprint = cms.bool(False)

doGem = False
if doGem:
  matching.cscSimHit.minNHitsChamber = 4
  matching.cscStripDigi.minNHitsChamber =4
  matching.cscWireDigi.minNHitsChamber = 4
  matching.cscCLCT.minNHitsChamber = 4
  matching.cscALCT.minNHitsChamber = 4
  matching.cscLCT.minNHitsChamber = 4
  matching.cscLCT.matchAlctGemME11 = True
  matching.cscLCT.matchAlctGemME21 = True
  matching.cscMPLCT.minNHitsChamber = 4
doRpc = False
if doRpc:
  matching.cscLCT.matchAlctRpc = True

process.p = cms.Path(process.GEMCSCAnalyzer)

## messages
print
#print 'Input files:'
print '----------------------------------------'
#print process.source.fileNames
print
print 'Output file:'
print '----------------------------------------'
print process.TFileService.fileName
print
