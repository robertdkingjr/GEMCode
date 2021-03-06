#ifndef GEMCode_GEMValidation_L1TrackMatcher_h
#define GEMCode_GEMValidation_L1TrackMatcher_h

/**\class L1TrackMatcher

 Description: Matching of tracks to SimTrack

 Original Author:  "Sven Dildick"
*/

#include "GEMCode/GEMValidation/interface/GEMDigiMatcher.h"
#include "GEMCode/GEMValidation/interface/RPCDigiMatcher.h"
#include "GEMCode/GEMValidation/interface/CSCStubMatcher.h"
#include "GEMCode/GEMValidation/interface/DTDigiMatcher.h"

#include "GEMCode/GEMValidation/interface/TFTrack.h" 
#include "GEMCode/GEMValidation/interface/TFCand.h" 
/* #include "GEMCode/GEMValidation/interface/GMTRegCand.h"  */
/* #include "GEMCode/GEMValidation/interface/GMTCand.h"  */
/* #include "GEMCode/GEMValidation/interface/L1Extra.h"  */

#include "L1Trigger/CSCCommonTrigger/interface/CSCConstants.h"
#include "L1Trigger/CSCCommonTrigger/interface/CSCTriggerGeometry.h"
#include "L1Trigger/CSCTrackFinder/interface/CSCTFPtLUT.h"
#include "L1Trigger/CSCTrackFinder/interface/CSCTFSectorProcessor.h"
#include "L1Trigger/CSCTrackFinder/interface/CSCSectorReceiverLUT.h"
#include "L1Trigger/CSCTrackFinder/interface/CSCTrackFinderDataTypes.h"
#include "L1Trigger/CSCTrackFinder/src/CSCTFDTReceiver.h"

#include "CondFormats/L1TObjects/interface/L1MuTriggerScales.h"
#include "CondFormats/DataRecord/interface/L1MuTriggerScalesRcd.h"
#include "CondFormats/L1TObjects/interface/L1MuTriggerPtScale.h"
#include "CondFormats/DataRecord/interface/L1MuTriggerPtScaleRcd.h"

#include "DataFormats/L1CSCTrackFinder/interface/L1CSCTrackCollection.h"
#include "DataFormats/L1Trigger/interface/L1MuonParticle.h"
#include "DataFormats/L1Trigger/interface/L1MuonParticleFwd.h"

typedef std::pair<float, float> EtaPhi;
typedef std::vector<L1MuRegionalCand> L1MuRegionalCandCollection;
typedef std::vector<L1MuGMTExtendedCand> L1MuGMTExtendedCandCollection;
//typedef std::pair<PSimHit, GlobalPoint> HitAndGP;

class L1TrackMatcher : public BaseMatcher
{
 public:
  /// constructor
  L1TrackMatcher(CSCStubMatcher&, DTDigiMatcher&, RPCDigiMatcher&);
  /// destructor
  ~L1TrackMatcher();
  
  const std::vector<TFTrack*> tfTracks() const {return tfTracks_;}
  const std::vector<TFCand*>& tfCands() const {return tfCands_;}
  /* const std::vector<GMTRegCand*>& gmtRegCands() const {return gmtRegCands_;} */
  /* const std::vector<GMTCand*>& gmtCands() const {return gmtCands_;} */
  /* const std::vector<L1Extra*>& l1Extras() const {return l1Extras_;} */
  
  const std::vector< EtaPhi > simTrackPropagateGPs_odd() const {return simTrackPropagateGPs_odd_;} 
  const std::vector< EtaPhi > simTrackPropagateGPs_even() const {return simTrackPropagateGPs_even_;} 
  void propagateSimTrack();  
  const std::map<int, GlobalPoint> interStatPropagation_odd() const {return interStatPropagation_odd_;} 
  const std::map<int, GlobalPoint> interStatPropagation_even() const {return interStatPropagation_even_;} 
  GlobalPoint propagationInterStation(int firstSt, int SecondSt, bool odd);  
  void propagationInterStation();  
  
  TFTrack* bestTFTrack(bool sortPtFirst=1) const;
  TFCand* bestTFCand(bool sortPtFirst=1) const;
  /* GMTRegCand* bestGMTRegCand(bool sortPtFirst=1) const; */
  /* GMTCand* bestGMTCand(bool sortPtFirst=1) const; */
  /* L1Extra* bestL1Extra(bool sortPtFirst=1) const; */

 private:
  
  void clear();
  void init(); 
  
  void matchTfTrackToSimTrack(const L1CSCTrackCollection&); 
  void matchTfCandToSimTrack(const L1MuRegionalCandCollection&); 
  /* void matchGmtRegCandToSimTrack(const L1MuRegionalCandCollection&);  */
  /* void matchGmtCandToSimTrack(const L1MuGMTExtendedCandCollection&);  */
  /* void matchL1MuonParticleToSimTrack(const l1extra::L1MuonParticleCollection&);  */

   csctf::TrackStub buildTrackStub(const CSCCorrelatedLCTDigi& d, CSCDetId id); 
   std::pair<float, float> intersectionEtaPhi(CSCDetId id, int wg, int hs); 
   std::vector< EtaPhi > simTrackPropagateGPs_even_; 
   std::vector< EtaPhi > simTrackPropagateGPs_odd_; 
   std::map<int, GlobalPoint> interStatPropagation_odd_; 
   std::map<int, GlobalPoint> interStatPropagation_even_; 
   //std::map<int, int > simTrackDummy_; 
   //  reco::TrackExtra*  

  const CSCStubMatcher* csc_stub_matcher_; 
  const DTDigiMatcher* dt_digi_matcher_; 
  const RPCDigiMatcher* rpc_digi_matcher_; 

  std::vector<edm::InputTag> cscTfTrackInputLabel_; 
  std::vector<edm::InputTag> cscTfCandInputLabel_; 
  std::vector<edm::InputTag> gmtRegCandInputLabel_; 
  std::vector<edm::InputTag> gmtCandInputLabel_; 
  std::vector<edm::InputTag> l1ExtraInputLabel_; 
  
  int minBXTFTrack_, maxBXTFTrack_; 
  int minBXTFCand_, maxBXTFCand_; 
  int minBXGMTRegCand_, maxBXGMTRegCand_; 
  int minBXGMTCand_, maxBXGMTCand_; 
  int minBXL1Extra_, maxBXL1Extra_; 
  
   int verboseTFTrack_; 
   int verboseTFCand_; 
   int verboseGMTRegCand_; 
   int verboseGMTCand_; 
   int verboseL1Extra_; 

   double deltaRTFTrack_; 
   double deltaRTFCand_; 
   double deltaRGMTRegCand_; 
   double deltaRGMTCand_; 
   double deltaRL1Extra_; 

   std::vector<TFTrack*> tfTracks_;
   std::vector<TFCand*> tfCands_;
   /* std::vector<GMTRegCand*> gmtRegCands_; */
   /* std::vector<GMTCand*> gmtCands_; */
   /* std::vector<L1Extra*> l1Extras_; */
   
   edm::ParameterSet ptLUTset_; 
   edm::ParameterSet CSCTFSPset_; 
   edm::ParameterSet srLUTset_; 

   CSCTFPtLUT* ptLUT_; 
   CSCTFSectorProcessor* my_SPs_[2][6]; 
   CSCSectorReceiverLUT* srLUTs_[5][6][2]; 
   CSCTFDTReceiver* dtrc_; 

   unsigned long long  muScalesCacheID_; 
   unsigned long long  muPtScaleCacheID_; 

   edm::ESHandle<L1MuTriggerScales> muScalesHd_; 
   edm::ESHandle<L1MuTriggerPtScale> muPtScaleHd_; 

   bool hasMuScales_; 
   bool hasMuPtScale_; 

   const L1MuTriggerScales* muScales_; 
   const L1MuTriggerPtScale* muPtScale_; 
};

#endif
