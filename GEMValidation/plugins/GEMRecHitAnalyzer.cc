#include <memory>
#include <fstream>
#include <sys/time.h>
#include <string>
#include <sstream>
#include <iostream>
#include <iomanip>

// root include files
#include "TTree.h"
#include "TFile.h"

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDAnalyzer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/ESHandle.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/ServiceRegistry/interface/Service.h"

#include <DataFormats/GEMRecHit/interface/GEMRecHit.h>
#include "DataFormats/GEMRecHit/interface/GEMRecHitCollection.h"
#include <DataFormats/GEMRecHit/interface/ME0RecHit.h>
#include "DataFormats/GEMRecHit/interface/ME0RecHitCollection.h"
#include <DataFormats/GEMRecHit/interface/ME0SegmentCollection.h>
#include "DataFormats/Provenance/interface/Timestamp.h"
#include <DataFormats/MuonDetId/interface/GEMDetId.h>

#include "SimDataFormats/TrackingHit/interface/PSimHitContainer.h"
#include "SimDataFormats/Track/interface/SimTrackContainer.h"
 
#include "Geometry/GEMGeometry/interface/GEMGeometry.h"
#include "Geometry/GEMGeometry/interface/ME0Geometry.h"
#include <Geometry/GEMGeometry/interface/GEMEtaPartition.h>
#include "Geometry/GEMGeometry/interface/GEMEtaPartitionSpecs.h"
#include <Geometry/Records/interface/MuonGeometryRecord.h>
#include <Geometry/CommonDetUnit/interface/GeomDet.h>
#include <Geometry/CommonTopologies/interface/RectangularStripTopology.h>
#include <Geometry/CommonTopologies/interface/TrapezoidalStripTopology.h>

#include "CommonTools/UtilAlgos/interface/TFileService.h"
#include "DataFormats/Math/interface/deltaR.h"
#include "GEMCode/GEMValidation/src/SimTrackMatchManager.h"
#include "GEMCode/GEMValidation/src/DigiMatcher.h"

using namespace matching;

//
// class declaration
//
struct MyGEMRecHit
{  
  Int_t detId, particleType;
  Float_t x, y, xErr, yErr;
  Float_t xExt, yExt;
  Int_t region, ring, station, layer, chamber, roll;
  Float_t globalR, globalEta, globalPhi, globalX, globalY, globalZ;
  Int_t bx, clusterSize, firstClusterStrip;
  Float_t x_sim, y_sim;
  Float_t globalEta_sim, globalPhi_sim, globalX_sim, globalY_sim, globalZ_sim;
  Float_t pull;
};

struct MyGEMRecHitEvent
{ 
  Int_t eventNumber; 
};

struct MyGEMRecHitNoise
{ 
  Int_t detId;
  Float_t x, y, xErr, yErr;
  Int_t region, ring, station, layer, chamber, roll;
  Float_t globalR, globalEta, globalPhi, globalX, globalY, globalZ;
  Int_t bx, clusterSize, firstClusterStrip;
  Int_t nStrips;
  Float_t trArea, trStripArea, striplength, pitch;
};

struct MyGEMSimHit
{  
  Int_t eventNumber;
  Int_t detUnitId, particleType;
  Float_t x, y, energyLoss, pabs, timeOfFlight;
  Int_t region, ring, station, layer, chamber, roll;
  Float_t globalR, globalEta, globalPhi, globalX, globalY, globalZ;
  Int_t strip;
  Float_t Phi_0, DeltaPhi, R_0;
  Int_t countMatching;
};

struct MyME0Segment
{  
  Int_t detId;
  Float_t localX, localY, localZ;
  Float_t dirTheta, dirPhi;
  Int_t numberRH, ndof;
  Float_t chi2;
};

struct MySimTrack
{
  Float_t pt, eta, phi;
  Char_t charge;
  Char_t endcap;
  Char_t gem_sh_layer1, gem_sh_layer2;
  Char_t gem_rh_layer1, gem_rh_layer2;
  Float_t gem_sh_eta, gem_sh_phi;
  Float_t gem_sh_x, gem_sh_y;
  Float_t gem_rh_eta, gem_rh_phi;
  Float_t gem_lx_even, gem_ly_even;
  Float_t gem_lx_odd, gem_ly_odd;
  Char_t has_gem_sh_l1, has_gem_sh_l2;
  Char_t has_gem_rh_l1, has_gem_rh_l2;
  Float_t gem_trk_eta, gem_trk_phi, gem_trk_rho;
};

class GEMRecHitAnalyzer : public edm::EDAnalyzer 
{
public:
  /// constructor
  explicit GEMRecHitAnalyzer(const edm::ParameterSet&);
  /// destructor
  ~GEMRecHitAnalyzer();

  virtual void beginRun(edm::Run const&, edm::EventSetup const&);

  virtual void beginJob() ;

  virtual void analyze(const edm::Event&, const edm::EventSetup&);

  virtual void endJob() ;
  
  static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);

private:
 
  void bookGEMEventsTree(); 
  void bookGEMRecHitTree();
  void bookGEMRecHitNoiseTree();
  void bookGEMSimHitsTree();
  void bookME0SimHitsTree();
  void bookME0RecHitsTree();
  void bookME0SegTree();
  void bookME0RHFromSegTree();
  void bookSimTracksTree();
  bool isSimTrackGood(const SimTrack &);
  bool isGEMRecHitMatched(MyGEMRecHit gem_recHit_, MyGEMSimHit gem_sh);
  void analyzeGEM(const edm::Event& iEvent);
  void analyzeME0(const edm::Event& iEvent);
  void analyzeME0Seg();
  void analyzeTracks(edm::ParameterSet, const edm::Event&, const edm::EventSetup&);
  void buildLUT();
  std::pair<int,int> getClosestChambers(int region, float phi);

  TTree* gem_events_tree_;
  TTree* gem_tree_;
  TTree* gem_noise_tree_;
  TTree* gem_sh_tree_;
  TTree* me0_sh_tree_;
  TTree* me0_rh_tree_;
  TTree* me0_seg_tree_;
  TTree* me0_rhSeg_tree_;
  TTree* track_tree_;

  edm::Handle<GEMRecHitCollection> gemRecHits_;
  edm::Handle<ME0RecHitCollection> me0RecHits_; 
  edm::Handle<ME0SegmentCollection> me0Segment_;
  edm::Handle<edm::PSimHitContainer> GEMHits;
  edm::Handle<edm::PSimHitContainer> ME0Hits;
  edm::Handle<edm::SimTrackContainer> sim_tracks;
  edm::Handle<edm::SimVertexContainer> sim_vertices;
  edm::ESHandle<GEMGeometry> gem_geom_;
  edm::ESHandle<ME0Geometry> me0_geom;

  const GEMGeometry* gem_geometry_;
  const ME0Geometry* me0_geometry_;

  MyGEMRecHit gem_recHit_;
  MyGEMRecHitNoise gem_noise_recHit_;
  MyGEMRecHitEvent gem_events_;
  MyGEMSimHit gem_sh;
  MyGEMSimHit me0_sh;
  MyGEMRecHit me0_rh;
  MyME0Segment me0_seg;
  MyGEMRecHit me0_rhFromSeg;
  MySimTrack track_;

  edm::ParameterSet cfg_;

  edm::InputTag simTrackInput_;
  edm::InputTag gemSimHitInput_;
  edm::InputTag gemRecHitInput_;
  edm::InputTag me0SimHitInput_;
  edm::InputTag me0RecHitInput_;
  edm::InputTag me0SegInput_;

  double simTrackMinPt_;
  double simTrackMaxPt_;
  double simTrackMinEta_;
  double simTrackMaxEta_;
  double simTrackOnlyMuon_;
  float radiusCenter_;
  float chamberHeight_;

  std::pair<std::vector<float>,std::vector<int> > positiveLUT_;
  std::pair<std::vector<float>,std::vector<int> > negativeLUT_;

  bool hasGEMGeometry_;
  bool hasME0Geometry_;
};

//
// constructors and destructor
//
GEMRecHitAnalyzer::GEMRecHitAnalyzer(const edm::ParameterSet& iConfig)
  : hasGEMGeometry_(true)
  , hasME0Geometry_(true)
{
  auto cfg_ = iConfig.getParameter<edm::ParameterSet>("simTrackMatching");
  auto simTrack = cfg_.getParameter<edm::ParameterSet>("simTrack");
  simTrackInput_ = simTrack.getParameter<edm::InputTag>("input");
  simTrackMinPt_ = simTrack.getParameter<double>("minPt");
  simTrackMaxPt_ = simTrack.getParameter<double>("maxPt");
  simTrackMinEta_ = simTrack.getParameter<double>("minEta");
  simTrackMaxEta_ = simTrack.getParameter<double>("maxEta");
  simTrackOnlyMuon_ = simTrack.getParameter<bool>("onlyMuon");

  auto gemSimHit = cfg_.getParameter<edm::ParameterSet>("gemSimHit");
  gemSimHitInput_ = gemSimHit.getParameter<edm::InputTag>("input");

  auto gemRecHit = cfg_.getParameter<edm::ParameterSet>("gemRecHit");
  gemRecHitInput_ = gemRecHit.getParameter<edm::InputTag>("input");

  auto me0SimHit = cfg_.getParameter<edm::ParameterSet>("me0SimHit");
  me0SimHitInput_ = me0SimHit.getParameter<edm::InputTag>("input");

  auto me0RecHit = cfg_.getParameter<edm::ParameterSet>("me0RecHit");
  me0RecHitInput_ = me0RecHit.getParameter<edm::InputTag>("input");

  auto me0Seg = cfg_.getParameter<edm::ParameterSet>("me0Seg");
  me0SegInput_ = me0Seg.getParameter<edm::InputTag>("input");

  bookGEMEventsTree();
  bookGEMRecHitTree();
  bookGEMRecHitNoiseTree();
  bookGEMSimHitsTree();
  bookME0SimHitsTree();
  bookME0RecHitsTree();
  bookME0SegTree();
  bookME0RHFromSegTree();
  bookSimTracksTree();
}

GEMRecHitAnalyzer::~GEMRecHitAnalyzer()
{
}

void GEMRecHitAnalyzer::beginRun(edm::Run const& iRun, edm::EventSetup const& iSetup)
{
  try {
    iSetup.get<MuonGeometryRecord>().get(gem_geom_);
    gem_geometry_ = &*gem_geom_;
  } catch (edm::eventsetup::NoProxyException<GEMGeometry>& e) {
    hasGEMGeometry_ = false;
    edm::LogWarning("GEMRecHitAnalyzer") << "+++ Info: GEM geometry is unavailable. +++\n";
  }

  try {
    iSetup.get<MuonGeometryRecord>().get(me0_geom);
    me0_geometry_ = &*me0_geom;
  } catch (edm::eventsetup::NoProxyException<ME0Geometry>& e) {
    hasME0Geometry_ = false;
    LogDebug("GEMRecHitAnalyzer") << "+++ Info: ME0 geometry is unavailable. +++\n";
  }

  if(hasGEMGeometry_) {

    // FIXME - when a geometry with different partition numbers will be released, the code will brake!
    const auto top_chamber = static_cast<const GEMEtaPartition*>(gem_geometry_->idToDetUnit(GEMDetId(1,1,1,1,1,1)));
    const int nEtaPartitions(gem_geometry_->chamber(GEMDetId(1,1,1,1,1,1))->nEtaPartitions());
    const auto bottom_chamber = static_cast<const GEMEtaPartition*>(gem_geometry_->idToDetUnit(GEMDetId(1,1,1,1,1,nEtaPartitions)));
    const float top_half_striplength = top_chamber->specs()->specificTopology().stripLength()/2.;
    const float bottom_half_striplength = bottom_chamber->specs()->specificTopology().stripLength()/2.;
    const LocalPoint lp_top(0., top_half_striplength, 0.);
    const LocalPoint lp_bottom(0., -bottom_half_striplength, 0.);
    const GlobalPoint gp_top = top_chamber->toGlobal(lp_top);
    const GlobalPoint gp_bottom = bottom_chamber->toGlobal(lp_bottom);
    
    radiusCenter_ = (gp_bottom.perp() + gp_top.perp())/2.;
    chamberHeight_ = gp_top.perp() - gp_bottom.perp();
    
    using namespace std;
    //cout<<"half top "<<top_half_striplength<<" bot "<<lp_bottom<<endl;
    //cout<<"r top "<<gp_top.perp()<<" bot "<<gp_bottom.perp()<<endl;
    LocalPoint p0(0.,0.,0.);
    //cout<<"r0 top "<<top_chamber->toGlobal(p0).perp()<<" bot "<< bottom_chamber->toGlobal(p0).perp()<<endl;
    //cout<<"rch "<<radiusCenter_<<" hch "<<chamberHeight_<<endl;

    buildLUT();
  }
}


void GEMRecHitAnalyzer::beginJob()
{
}

void GEMRecHitAnalyzer::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
  iEvent.getByLabel(gemRecHitInput_, gemRecHits_);
  iEvent.getByLabel(gemSimHitInput_, GEMHits);
  iEvent.getByLabel(simTrackInput_, sim_tracks);
  iEvent.getByLabel(simTrackInput_, sim_vertices);
  iEvent.getByLabel(me0SimHitInput_, ME0Hits);
  iEvent.getByLabel(me0RecHitInput_, me0RecHits_);
  iEvent.getByLabel(me0SegInput_, me0Segment_);
  //if(hasGEMGeometry_ and gemRecHits_->size()) analyzeGEM(iEvent);
  if(hasME0Geometry_ and me0RecHits_->size()) analyzeME0(iEvent);
  if(hasME0Geometry_ and me0Segment_->size()) analyzeME0Seg();
  //if(hasGEMGeometry_ and gemRecHits_->size()) analyzeTracks(cfg_,iEvent,iSetup); 
}

void GEMRecHitAnalyzer::bookGEMEventsTree()
{
  edm::Service<TFileService> fs;
  gem_events_tree_ = fs->make<TTree>("GEMEventsTree", "GEMEventsTree");
  gem_events_tree_->Branch("eventNumber", &gem_events_.eventNumber);
}

void GEMRecHitAnalyzer::bookGEMRecHitTree()
{
  edm::Service<TFileService> fs;
  gem_tree_ = fs->make<TTree>("GEMRecHitTree", "GEMRecHitTree");
  gem_tree_->Branch("detId", &gem_recHit_.detId);
  gem_tree_->Branch("region", &gem_recHit_.region);
  gem_tree_->Branch("ring", &gem_recHit_.ring);
  gem_tree_->Branch("station", &gem_recHit_.station);
  gem_tree_->Branch("layer", &gem_recHit_.layer);
  gem_tree_->Branch("chamber", &gem_recHit_.chamber);
  gem_tree_->Branch("roll", &gem_recHit_.roll);
  gem_tree_->Branch("bx", &gem_recHit_.bx);
  gem_tree_->Branch("clusterSize", &gem_recHit_.clusterSize);
  gem_tree_->Branch("firstClusterStrip", &gem_recHit_.firstClusterStrip);
  gem_tree_->Branch("x", &gem_recHit_.x);
  gem_tree_->Branch("xErr", &gem_recHit_.xErr);
  gem_tree_->Branch("y", &gem_recHit_.y);
  gem_tree_->Branch("globalR", &gem_recHit_.globalR);
  gem_tree_->Branch("globalEta", &gem_recHit_.globalEta);
  gem_tree_->Branch("globalPhi", &gem_recHit_.globalPhi);
  gem_tree_->Branch("globalX", &gem_recHit_.globalX);
  gem_tree_->Branch("globalY", &gem_recHit_.globalY);
  gem_tree_->Branch("globalZ", &gem_recHit_.globalZ);
  gem_tree_->Branch("x_sim", &gem_recHit_.x_sim);
  gem_tree_->Branch("y_sim", &gem_recHit_.y_sim);
  gem_tree_->Branch("globalEta_sim", &gem_recHit_.globalEta_sim);
  gem_tree_->Branch("globalPhi_sim", &gem_recHit_.globalPhi_sim);
  gem_tree_->Branch("globalX_sim", &gem_recHit_.globalX_sim);
  gem_tree_->Branch("globalY_sim", &gem_recHit_.globalY_sim);
  gem_tree_->Branch("globalZ_sim", &gem_recHit_.globalZ_sim);
  gem_tree_->Branch("pull", &gem_recHit_.pull);
}

void GEMRecHitAnalyzer::bookGEMRecHitNoiseTree()
{
  edm::Service<TFileService> fs;
  gem_noise_tree_ = fs->make<TTree>("GEMRecHitNoiseTree", "GEMRecHitNoiseTree");
  gem_noise_tree_->Branch("detId", &gem_noise_recHit_.detId);
  gem_noise_tree_->Branch("region", &gem_noise_recHit_.region);
  gem_noise_tree_->Branch("ring", &gem_noise_recHit_.ring);
  gem_noise_tree_->Branch("station", &gem_noise_recHit_.station);
  gem_noise_tree_->Branch("layer", &gem_noise_recHit_.layer);
  gem_noise_tree_->Branch("chamber", &gem_noise_recHit_.chamber);
  gem_noise_tree_->Branch("roll", &gem_noise_recHit_.roll);
  gem_noise_tree_->Branch("bx", &gem_noise_recHit_.bx);
  gem_noise_tree_->Branch("clusterSize", &gem_noise_recHit_.clusterSize);
  gem_noise_tree_->Branch("firstClusterStrip", &gem_noise_recHit_.firstClusterStrip);
  gem_noise_tree_->Branch("x", &gem_noise_recHit_.x);
  gem_noise_tree_->Branch("xErr", &gem_noise_recHit_.xErr);
  gem_noise_tree_->Branch("y", &gem_noise_recHit_.y);
  gem_noise_tree_->Branch("globalR", &gem_noise_recHit_.globalR);
  gem_noise_tree_->Branch("globalEta", &gem_noise_recHit_.globalEta);
  gem_noise_tree_->Branch("globalPhi", &gem_noise_recHit_.globalPhi);
  gem_noise_tree_->Branch("globalX", &gem_noise_recHit_.globalX);
  gem_noise_tree_->Branch("globalY", &gem_noise_recHit_.globalY);
  gem_noise_tree_->Branch("globalZ", &gem_noise_recHit_.globalZ);
  gem_noise_tree_->Branch("nStrips", &gem_noise_recHit_.nStrips);
  gem_noise_tree_->Branch("trArea", &gem_noise_recHit_.trArea);
  gem_noise_tree_->Branch("trStripArea", &gem_noise_recHit_.trStripArea);
  gem_noise_tree_->Branch("striplength", &gem_noise_recHit_.striplength);
  gem_noise_tree_->Branch("pitch", &gem_noise_recHit_.pitch);
}

void GEMRecHitAnalyzer::bookGEMSimHitsTree()
{
  edm::Service< TFileService > fs;
  gem_sh_tree_ = fs->make< TTree >("GEMSimHits", "GEMSimHits");
  gem_sh_tree_->Branch("eventNumber", &gem_sh.eventNumber);
  gem_sh_tree_->Branch("detUnitId", &gem_sh.detUnitId);
  gem_sh_tree_->Branch("particleType", &gem_sh.particleType);
  gem_sh_tree_->Branch("x", &gem_sh.x);
  gem_sh_tree_->Branch("y", &gem_sh.y);
  gem_sh_tree_->Branch("energyLoss", &gem_sh.energyLoss);
  gem_sh_tree_->Branch("pabs", &gem_sh.pabs);
  gem_sh_tree_->Branch("timeOfFlight", &gem_sh.timeOfFlight);
  gem_sh_tree_->Branch("region", &gem_sh.region);
  gem_sh_tree_->Branch("ring", &gem_sh.ring);
  gem_sh_tree_->Branch("station", &gem_sh.station);
  gem_sh_tree_->Branch("chamber", &gem_sh.chamber);
  gem_sh_tree_->Branch("layer", &gem_sh.layer);
  gem_sh_tree_->Branch("roll", &gem_sh.roll);
  gem_sh_tree_->Branch("globalR", &gem_sh.globalR);
  gem_sh_tree_->Branch("globalEta", &gem_sh.globalEta);
  gem_sh_tree_->Branch("globalPhi", &gem_sh.globalPhi);
  gem_sh_tree_->Branch("globalX", &gem_sh.globalX);
  gem_sh_tree_->Branch("globalY", &gem_sh.globalY);
  gem_sh_tree_->Branch("globalZ", &gem_sh.globalZ);
  gem_sh_tree_->Branch("strip", &gem_sh.strip);
  gem_sh_tree_->Branch("Phi_0", &gem_sh.Phi_0);
  gem_sh_tree_->Branch("DeltaPhi", &gem_sh.DeltaPhi);
  gem_sh_tree_->Branch("R_0", &gem_sh.R_0);
  gem_sh_tree_->Branch("countMatching", &gem_sh.countMatching);
}

void GEMRecHitAnalyzer::bookSimTracksTree()
{
  edm::Service< TFileService > fs;
  track_tree_ = fs->make<TTree>("TrackTree", "TrackTree");
  track_tree_->Branch("pt", &track_.pt);
  track_tree_->Branch("eta", &track_.eta);
  track_tree_->Branch("phi", &track_.phi);
  track_tree_->Branch("charge", &track_.charge);
  track_tree_->Branch("endcap", &track_.endcap);
  track_tree_->Branch("gem_sh_layer1", &track_.gem_sh_layer1);
  track_tree_->Branch("gem_sh_layer2", &track_.gem_sh_layer2);
  track_tree_->Branch("gem_rh_layer1", &track_.gem_rh_layer1);
  track_tree_->Branch("gem_rh_layer2", &track_.gem_rh_layer2);
  track_tree_->Branch("gem_sh_eta", &track_.gem_sh_eta);
  track_tree_->Branch("gem_sh_phi", &track_.gem_sh_phi);
  track_tree_->Branch("gem_sh_x", &track_.gem_sh_x);
  track_tree_->Branch("gem_sh_y", &track_.gem_sh_y);
  track_tree_->Branch("gem_rh_eta", &track_.gem_rh_eta);
  track_tree_->Branch("gem_rh_phi", &track_.gem_rh_phi);
  track_tree_->Branch("gem_lx_even",&track_.gem_lx_even);
  track_tree_->Branch("gem_ly_even",&track_.gem_ly_even);
  track_tree_->Branch("gem_lx_odd",&track_.gem_lx_odd);
  track_tree_->Branch("gem_ly_odd",&track_.gem_ly_odd);
  track_tree_->Branch("has_gem_sh_l1",&track_.has_gem_sh_l1);
  track_tree_->Branch("has_gem_sh_l2",&track_.has_gem_sh_l2);
  track_tree_->Branch("has_gem_rh_l1",&track_.has_gem_rh_l1);
  track_tree_->Branch("has_gem_rh_l2",&track_.has_gem_rh_l2);
}

void GEMRecHitAnalyzer::bookME0SimHitsTree()
{
  edm::Service< TFileService > fs;
  me0_sh_tree_ = fs->make< TTree >("ME0SimHits", "ME0SimHits");
  me0_sh_tree_->Branch("eventNumber", &me0_sh.eventNumber);
  me0_sh_tree_->Branch("detUnitId", &me0_sh.detUnitId);
  me0_sh_tree_->Branch("particleType", &me0_sh.particleType);
  me0_sh_tree_->Branch("x", &me0_sh.x);
  me0_sh_tree_->Branch("y", &me0_sh.y);
  me0_sh_tree_->Branch("energyLoss", &me0_sh.energyLoss);
  me0_sh_tree_->Branch("pabs", &me0_sh.pabs);
  me0_sh_tree_->Branch("timeOfFlight", &me0_sh.timeOfFlight);
  me0_sh_tree_->Branch("region", &me0_sh.region);
  me0_sh_tree_->Branch("ring", &me0_sh.ring);
  me0_sh_tree_->Branch("station", &me0_sh.station);
  me0_sh_tree_->Branch("chamber", &me0_sh.chamber);
  me0_sh_tree_->Branch("layer", &me0_sh.layer);
  me0_sh_tree_->Branch("roll", &me0_sh.roll);
  me0_sh_tree_->Branch("globalR", &me0_sh.globalR);
  me0_sh_tree_->Branch("globalEta", &me0_sh.globalEta);
  me0_sh_tree_->Branch("globalPhi", &me0_sh.globalPhi);
  me0_sh_tree_->Branch("globalX", &me0_sh.globalX);
  me0_sh_tree_->Branch("globalY", &me0_sh.globalY);
  me0_sh_tree_->Branch("globalZ", &me0_sh.globalZ);
  me0_sh_tree_->Branch("strip", &me0_sh.strip);
  me0_sh_tree_->Branch("Phi_0", &me0_sh.Phi_0);
  me0_sh_tree_->Branch("DeltaPhi", &me0_sh.DeltaPhi);
  me0_sh_tree_->Branch("R_0", &me0_sh.R_0);
  me0_sh_tree_->Branch("countMatching", &me0_sh.countMatching);
}

void GEMRecHitAnalyzer::bookME0RecHitsTree()
{
  edm::Service<TFileService> fs;
  me0_rh_tree_ = fs->make<TTree>("ME0RecHitTree", "ME0RecHitTree");
  me0_rh_tree_->Branch("detId", &me0_rh.detId);
  me0_rh_tree_->Branch("region", &me0_rh.region);
  me0_rh_tree_->Branch("ring", &me0_rh.ring);
  me0_rh_tree_->Branch("station", &me0_rh.station);
  me0_rh_tree_->Branch("layer", &me0_rh.layer);
  me0_rh_tree_->Branch("chamber", &me0_rh.chamber);
  me0_rh_tree_->Branch("roll", &me0_rh.roll);
  me0_rh_tree_->Branch("bx", &me0_rh.bx);
  me0_rh_tree_->Branch("clusterSize", &me0_rh.clusterSize);
  me0_rh_tree_->Branch("firstClusterStrip", &me0_rh.firstClusterStrip);
  me0_rh_tree_->Branch("x", &me0_rh.x);
  me0_rh_tree_->Branch("xErr", &me0_rh.xErr);
  me0_rh_tree_->Branch("y", &me0_rh.y);
  me0_rh_tree_->Branch("globalR", &me0_rh.globalR);
  me0_rh_tree_->Branch("globalEta", &me0_rh.globalEta);
  me0_rh_tree_->Branch("globalPhi", &me0_rh.globalPhi);
  me0_rh_tree_->Branch("globalX", &me0_rh.globalX);
  me0_rh_tree_->Branch("globalY", &me0_rh.globalY);
  me0_rh_tree_->Branch("globalZ", &me0_rh.globalZ);
  me0_rh_tree_->Branch("x_sim", &me0_rh.x_sim);
  me0_rh_tree_->Branch("y_sim", &me0_rh.y_sim);
  me0_rh_tree_->Branch("globalEta_sim", &me0_rh.globalEta_sim);
  me0_rh_tree_->Branch("globalPhi_sim", &me0_rh.globalPhi_sim);
  me0_rh_tree_->Branch("globalX_sim", &me0_rh.globalX_sim);
  me0_rh_tree_->Branch("globalY_sim", &me0_rh.globalY_sim);
  me0_rh_tree_->Branch("globalZ_sim", &me0_rh.globalZ_sim);
  me0_rh_tree_->Branch("pull", &me0_rh.pull);
}

void GEMRecHitAnalyzer::bookME0SegTree()
{
  edm::Service<TFileService> fs;
  me0_seg_tree_ = fs->make<TTree>("ME0SegTree", "ME0SegTree");
  me0_seg_tree_->Branch("detId", &me0_seg.detId);
  me0_seg_tree_->Branch("localX", &me0_seg.localX);
  me0_seg_tree_->Branch("localY", &me0_seg.localY);
  me0_seg_tree_->Branch("localZ", &me0_seg.localZ);
  me0_seg_tree_->Branch("dirTheta", &me0_seg.dirTheta);
  me0_seg_tree_->Branch("dirPhi", &me0_seg.dirPhi);
  me0_seg_tree_->Branch("numberRH", &me0_seg.numberRH);
  me0_seg_tree_->Branch("chi2", &me0_seg.chi2);
  me0_seg_tree_->Branch("ndof", &me0_seg.ndof);
}

void GEMRecHitAnalyzer::bookME0RHFromSegTree()
{
  edm::Service<TFileService> fs;
  me0_rhSeg_tree_ = fs->make<TTree>("ME0RHFromSegTree", "ME0RHFromSegTree");
  me0_rhSeg_tree_->Branch("detId", &me0_rhFromSeg.detId);
  me0_rhSeg_tree_->Branch("region", &me0_rhFromSeg.region);
  me0_rhSeg_tree_->Branch("ring", &me0_rhFromSeg.ring);
  me0_rhSeg_tree_->Branch("station", &me0_rhFromSeg.station);
  me0_rhSeg_tree_->Branch("layer", &me0_rhFromSeg.layer);
  me0_rhSeg_tree_->Branch("chamber", &me0_rhFromSeg.chamber);
  me0_rhSeg_tree_->Branch("roll", &me0_rhFromSeg.roll);
  //me0_rhSeg_tree_->Branch("bx", &me0_rhFromSeg.bx);
  //me0_rhSeg_tree_->Branch("clusterSize", &me0_rhFromSeg.clusterSize);
  //me0_rhSeg_tree_->Branch("firstClusterStrip", &me0_rhFromSeg.firstClusterStrip);
  me0_rhSeg_tree_->Branch("x", &me0_rhFromSeg.x);
  me0_rhSeg_tree_->Branch("xErr", &me0_rhFromSeg.xErr);
  me0_rhSeg_tree_->Branch("y", &me0_rhFromSeg.y);
  me0_rhSeg_tree_->Branch("yErr", &me0_rhFromSeg.yErr);
  me0_rhSeg_tree_->Branch("globalR", &me0_rhFromSeg.globalR);
  me0_rhSeg_tree_->Branch("globalEta", &me0_rhFromSeg.globalEta);
  me0_rhSeg_tree_->Branch("globalPhi", &me0_rhFromSeg.globalPhi);
  me0_rhSeg_tree_->Branch("globalX", &me0_rhFromSeg.globalX);
  me0_rhSeg_tree_->Branch("globalY", &me0_rhFromSeg.globalY);
  me0_rhSeg_tree_->Branch("globalZ", &me0_rhFromSeg.globalZ);
  //me0_rhSeg_tree_->Branch("x_sim", &me0_rhFromSeg.x_sim);
  //me0_rhSeg_tree_->Branch("y_sim", &me0_rhFromSeg.y_sim);
  //me0_rhSeg_tree_->Branch("globalEta_sim", &me0_rhFromSeg.globalEta_sim);
  //me0_rhSeg_tree_->Branch("globalPhi_sim", &me0_rhFromSeg.globalPhi_sim);
  //me0_rhSeg_tree_->Branch("globalX_sim", &me0_rhFromSeg.globalX_sim);
  //me0_rhSeg_tree_->Branch("globalY_sim", &me0_rhFromSeg.globalY_sim);
  //me0_rhSeg_tree_->Branch("globalZ_sim", &me0_rhFromSeg.globalZ_sim);
  //me0_rhSeg_tree_->Branch("pull", &me0_rhFromSeg.pull);
  me0_rhSeg_tree_->Branch("xExt", &me0_rhFromSeg.xExt);
  me0_rhSeg_tree_->Branch("yExt", &me0_rhFromSeg.yExt);
}

bool GEMRecHitAnalyzer::isGEMRecHitMatched(MyGEMRecHit gem_recHit_, MyGEMSimHit gem_sh)
{

  Int_t gem_region = gem_recHit_.region;
  Int_t gem_layer = gem_recHit_.layer;
  Int_t gem_station = gem_recHit_.station;
  Int_t gem_chamber = gem_recHit_.chamber;
  Int_t gem_roll = gem_recHit_.roll;
  Int_t gem_firstStrip = gem_recHit_.firstClusterStrip;
  Int_t gem_cls = gem_recHit_.clusterSize;
   
  Int_t gem_sh_region = gem_sh.region;
  Int_t gem_sh_layer = gem_sh.layer;
  Int_t gem_sh_station = gem_sh.station;
  Int_t gem_sh_chamber = gem_sh.chamber;
  Int_t gem_sh_roll = gem_sh.roll;
  Int_t gem_sh_strip = gem_sh.strip;

  std::vector<int> stripsFired;
  for(int i = gem_firstStrip; i < (gem_firstStrip + gem_cls); i++){

   stripsFired.push_back(i);

  }
 
  bool cond1, cond2, cond3;

  if(gem_sh_region == gem_region && gem_sh_layer == gem_layer && gem_sh_station == gem_station) cond1 = true;
  else cond1 = false;
  if(gem_sh_chamber == gem_chamber && gem_sh_roll == gem_roll) cond2 = true;
  else cond2 = false;
  if(std::find(stripsFired.begin(), stripsFired.end(), (gem_sh_strip + 1)) != stripsFired.end()) cond3 = true;
  else cond3 = false;

  if(gem_cls == 0) cond3 = true;

  //std::cout<<"cond1: "<<cond1<<" cond2: "<<cond2<<" cond3: "<<cond3<<std::endl;
  return (cond1 & cond2 & cond3);

}

// ======= GEM RecHits =======
void GEMRecHitAnalyzer::analyzeGEM(const edm::Event& iEvent)
{
  std::vector<int> trackIds;
  std::vector<int> trackType;
  const edm::SimTrackContainer & sim_trks = *sim_tracks.product();
  
  for (auto& t: sim_trks)
  {
    if (!isSimTrackGood(t)) continue;
    trackType.push_back(t.type());
    trackIds.push_back(t.trackId());
  }

  for (edm::PSimHitContainer::const_iterator itHit = GEMHits->begin(); itHit != GEMHits->end(); ++itHit)
  {
    if(abs(itHit->particleType()) != 13) continue;
    if(std::find(trackIds.begin(), trackIds.end(), itHit->trackId()) == trackIds.end()) continue;

    //std::cout<<"Size "<<trackIds.size()<<" id1 "<<trackIds[0]<<" type1 "<<trackType[0]<<" id2 "<<trackIds[1]<<" type2 "<<trackType[1]<<std::endl;
    
    gem_sh.eventNumber = iEvent.id().event();
    gem_sh.detUnitId = itHit->detUnitId();
    gem_sh.particleType = itHit->particleType();
    gem_sh.x = itHit->localPosition().x();
    gem_sh.y = itHit->localPosition().y();
    gem_sh.energyLoss = itHit->energyLoss();
    gem_sh.pabs = itHit->pabs();
    gem_sh.timeOfFlight = itHit->timeOfFlight();
    
    const GEMDetId id(itHit->detUnitId());
    
    gem_sh.region = id.region();
    gem_sh.ring = id.ring();
    gem_sh.station = id.station();
    gem_sh.layer = id.layer();
    gem_sh.chamber = id.chamber();
    gem_sh.roll = id.roll();
    
    const LocalPoint p0(0., 0., 0.);
    const GlobalPoint Gp0(gem_geometry_->idToDet(itHit->detUnitId())->surface().toGlobal(p0));
    
    gem_sh.Phi_0 = Gp0.phi();
    gem_sh.R_0 = Gp0.perp();
    gem_sh.DeltaPhi = atan(-1*id.region()*pow(-1,id.chamber())*itHit->localPosition().x()/(Gp0.perp() + itHit->localPosition().y()));
    
    const LocalPoint hitLP(itHit->localPosition());
    const GlobalPoint hitGP(gem_geometry_->idToDet(itHit->detUnitId())->surface().toGlobal(hitLP));
    gem_sh.globalR = hitGP.perp();
    gem_sh.globalEta = hitGP.eta();
    gem_sh.globalPhi = hitGP.phi();
    gem_sh.globalX = hitGP.x();
    gem_sh.globalY = hitGP.y();
    gem_sh.globalZ = hitGP.z();
    
    //  Now filling strip info using entry point rather than local position to be
    //  consistent with digi strips. To change back, just switch the comments - WHF
    //  gem_sh.strip=gem_geometry_->etaPartition(itHit->detUnitId())->strip(hitLP);
    const LocalPoint hitEP(itHit->entryPoint());
    gem_sh.strip = gem_geometry_->etaPartition(itHit->detUnitId())->strip(hitEP);
    
    int count = 0;
    //std::cout<<"SimHit: region "<<gem_sh.region<<" station "<<gem_sh.station<<" layer "<<gem_sh.layer<<" chamber "<<gem_sh.chamber<<" roll "<<gem_sh.roll<<" strip "<<gem_sh.strip<<" type "<<itHit->particleType()<<" id "<<itHit->trackId()<<std::endl;
    
    for (GEMRecHitCollection::const_iterator recHit = gemRecHits_->begin(); recHit != gemRecHits_->end(); ++recHit) 
    {
      gem_recHit_.x = recHit->localPosition().x();
      gem_recHit_.xErr = recHit->localPositionError().xx();
      gem_recHit_.y = recHit->localPosition().y();
      gem_recHit_.detId = (Short_t) (*recHit).gemId();
      gem_recHit_.bx = recHit->BunchX();
      gem_recHit_.clusterSize = recHit->clusterSize();
      gem_recHit_.firstClusterStrip = recHit->firstClusterStrip();
      
      GEMDetId id((*recHit).gemId());
      
      gem_recHit_.region = (Short_t) id.region();
      gem_recHit_.ring = (Short_t) id.ring();
      gem_recHit_.station = (Short_t) id.station();
      gem_recHit_.layer = (Short_t) id.layer();
      gem_recHit_.chamber = (Short_t) id.chamber();
      gem_recHit_.roll = (Short_t) id.roll();
      
      LocalPoint rhLP = recHit->localPosition();
      GlobalPoint rhGP = gem_geometry_->idToDet((*recHit).gemId())->surface().toGlobal(rhLP);
      
      gem_recHit_.globalR = rhGP.perp();
      gem_recHit_.globalEta = rhGP.eta();
      gem_recHit_.globalPhi = rhGP.phi();
      gem_recHit_.globalX = rhGP.x();
      gem_recHit_.globalY = rhGP.y();
      gem_recHit_.globalZ = rhGP.z();
      
      gem_recHit_.x_sim = gem_sh.x;
      gem_recHit_.y_sim = gem_sh.y;
      gem_recHit_.globalEta_sim = gem_sh.globalEta;
      gem_recHit_.globalPhi_sim = gem_sh.globalPhi;
      gem_recHit_.globalX_sim = gem_sh.globalX;
      gem_recHit_.globalY_sim = gem_sh.globalY;
      gem_recHit_.globalZ_sim = gem_sh.globalZ;
      gem_recHit_.pull = (gem_sh.x - gem_recHit_.x) / gem_recHit_.xErr;
      
      if(gem_recHit_.bx != 0) continue;
      if(isGEMRecHitMatched(gem_recHit_, gem_sh)) 
      {
	bool verbose(false);
	if (verbose)
	  std::cout<<"RecHit: region "<<gem_recHit_.region<<" station "<<gem_recHit_.station
		   <<" layer "<<gem_recHit_.layer<<" chamber "<<gem_recHit_.chamber
		   <<" roll "<<gem_recHit_.roll<<" firstStrip "<<gem_recHit_.firstClusterStrip
		   <<" cls "<<gem_recHit_.clusterSize<<" bx "<<gem_recHit_.bx<<std::endl;
	gem_tree_->Fill();
	count++;
      }
    }
    gem_sh.countMatching = count;
    gem_sh_tree_->Fill();
  }

  gem_events_.eventNumber = iEvent.id().event();
  gem_events_tree_->Fill();

  for (GEMRecHitCollection::const_iterator recHit = gemRecHits_->begin(); recHit != gemRecHits_->end(); ++recHit) 
  {
    gem_noise_recHit_.x = recHit->localPosition().x();
    gem_noise_recHit_.xErr = recHit->localPositionError().xx();
    gem_noise_recHit_.y = recHit->localPosition().y();
    gem_noise_recHit_.detId = (Short_t) (*recHit).gemId();
    gem_noise_recHit_.bx = recHit->BunchX();
    gem_noise_recHit_.clusterSize = recHit->clusterSize();
    gem_noise_recHit_.firstClusterStrip = recHit->firstClusterStrip();
   
    GEMDetId id((*recHit).gemId());

    gem_noise_recHit_.region = (Short_t) id.region();
    gem_noise_recHit_.ring = (Short_t) id.ring();
    gem_noise_recHit_.station = (Short_t) id.station();
    gem_noise_recHit_.layer = (Short_t) id.layer();
    gem_noise_recHit_.chamber = (Short_t) id.chamber();
    gem_noise_recHit_.roll = (Short_t) id.roll();
    
    LocalPoint rhLP = recHit->localPosition();
    GlobalPoint rhGP = gem_geometry_->idToDet((*recHit).gemId())->surface().toGlobal(rhLP);
   
    gem_noise_recHit_.globalR = rhGP.perp();
    gem_noise_recHit_.globalEta = rhGP.eta();
    gem_noise_recHit_.globalPhi = rhGP.phi();
    gem_noise_recHit_.globalX = rhGP.x();
    gem_noise_recHit_.globalY = rhGP.y();
    gem_noise_recHit_.globalZ = rhGP.z();
    
    const GEMEtaPartition* roll(gem_geom_->etaPartition(id));
    const TrapezoidalStripTopology* top(dynamic_cast<const TrapezoidalStripTopology*> (&(roll->topology())));
    
    gem_noise_recHit_.nStrips = roll->nstrips();
    gem_noise_recHit_.striplength = top->stripLength();
    gem_noise_recHit_.pitch = roll->pitch();
    gem_noise_recHit_.trStripArea = gem_noise_recHit_.pitch * gem_noise_recHit_.striplength;
    gem_noise_recHit_.trArea = gem_noise_recHit_.trStripArea * gem_noise_recHit_.nStrips;
  
    gem_noise_tree_->Fill();
  }
}

// ======= ME0 RecHits =======
void GEMRecHitAnalyzer::analyzeME0(const edm::Event& iEvent)
{
  std::vector<int> trackIds;
  std::vector<int> trackType;
  const edm::SimTrackContainer & sim_trks = *sim_tracks.product();
  
  for (auto& t: sim_trks)
  {
    if (!isSimTrackGood(t)) continue;
    trackType.push_back(t.type());
    trackIds.push_back(t.trackId());
  }

  for (edm::PSimHitContainer::const_iterator itHit = ME0Hits->begin(); itHit != ME0Hits->end(); ++itHit)
  {
    if(abs(itHit->particleType()) != 13) continue;
    if(std::find(trackIds.begin(), trackIds.end(), itHit->trackId()) == trackIds.end()) continue;

    //std::cout<<"Size "<<trackIds.size()<<" id1 "<<trackIds[0]<<" type1 "<<trackType[0]<<" id2 "<<trackIds[1]<<" type2 "<<trackType[1]<<std::endl;
    
    me0_sh.eventNumber = iEvent.id().event();
    me0_sh.detUnitId = itHit->detUnitId();
    me0_sh.particleType = itHit->particleType();
    me0_sh.x = itHit->localPosition().x();
    me0_sh.y = itHit->localPosition().y();
    me0_sh.energyLoss = itHit->energyLoss();
    me0_sh.pabs = itHit->pabs();
    me0_sh.timeOfFlight = itHit->timeOfFlight();
    
    const ME0DetId id(itHit->detUnitId());
    
    me0_sh.region = id.region();
    me0_sh.ring = 0;
    me0_sh.station = 0;
    me0_sh.layer = id.layer();
    me0_sh.chamber = id.chamber();
    me0_sh.roll = id.roll();
    
    const LocalPoint p0(0., 0., 0.);
    const GlobalPoint Gp0(me0_geometry_->idToDet(itHit->detUnitId())->surface().toGlobal(p0));
    
    me0_sh.Phi_0 = Gp0.phi();
    me0_sh.R_0 = Gp0.perp();
    me0_sh.DeltaPhi = atan(-1*id.region()*pow(-1,id.chamber())*itHit->localPosition().x()/(Gp0.perp() + itHit->localPosition().y()));
    
    const LocalPoint hitLP(itHit->localPosition());
    const GlobalPoint hitGP(me0_geometry_->idToDet(itHit->detUnitId())->surface().toGlobal(hitLP));
    me0_sh.globalR = hitGP.perp();
    me0_sh.globalEta = hitGP.eta();
    me0_sh.globalPhi = hitGP.phi();
    me0_sh.globalX = hitGP.x();
    me0_sh.globalY = hitGP.y();
    me0_sh.globalZ = hitGP.z();
    
    //  Now filling strip info using entry point rather than local position to be
    //  consistent with digi strips. To change back, just switch the comments - WHF
    //  me0_sh.strip=gem_geometry_->etaPartition(itHit->detUnitId())->strip(hitLP);
    const LocalPoint hitEP(itHit->entryPoint());
    me0_sh.strip = me0_geometry_->etaPartition(itHit->detUnitId())->strip(hitEP);
    
    int count = 0;
    //std::cout<<"SimHit: region "<<me0_sh.region<<" station "<<me0_sh.station<<" layer "<<me0_sh.layer<<" chamber "<<me0_sh.chamber<<" roll "<<me0_sh.roll<<" strip "<<me0_sh.strip<<" type "<<itHit->particleType()<<" id "<<itHit->trackId()<<" x: "<<me0_sh.x<<std::endl;
    
    for (ME0RecHitCollection::const_iterator recHit = me0RecHits_->begin(); recHit != me0RecHits_->end(); ++recHit) 
    {

      me0_rh.x = recHit->localPosition().x();
      me0_rh.xErr = recHit->localPositionError().xx();
      me0_rh.y = recHit->localPosition().y();
      me0_rh.detId = (Short_t) (*recHit).me0Id();
      me0_rh.bx = 0;
      me0_rh.clusterSize = 0;
      me0_rh.firstClusterStrip = 0;
      
      ME0DetId id((*recHit).me0Id());
      
      me0_rh.region = (Short_t) id.region();
      me0_rh.ring = 0;
      me0_rh.station = 0;
      me0_rh.layer = (Short_t) id.layer();
      me0_rh.chamber = (Short_t) id.chamber();
      me0_rh.roll = (Short_t) id.roll();
      
      LocalPoint rhLP = recHit->localPosition();
      GlobalPoint rhGP = me0_geometry_->idToDet((*recHit).me0Id())->surface().toGlobal(rhLP);
      
      me0_rh.globalR = rhGP.perp();
      me0_rh.globalEta = rhGP.eta();
      me0_rh.globalPhi = rhGP.phi();
      me0_rh.globalX = rhGP.x();
      me0_rh.globalY = rhGP.y();
      me0_rh.globalZ = rhGP.z();
      
      me0_rh.x_sim = me0_sh.x;
      me0_rh.y_sim = me0_sh.y;
      me0_rh.globalEta_sim = me0_sh.globalEta;
      me0_rh.globalPhi_sim = me0_sh.globalPhi;
      me0_rh.globalX_sim = me0_sh.globalX;
      me0_rh.globalY_sim = me0_sh.globalY;
      me0_rh.globalZ_sim = me0_sh.globalZ;
      me0_rh.pull = (me0_sh.x - me0_rh.x) / me0_rh.xErr;
      
      if(me0_rh.bx != 0) continue;
      if(isGEMRecHitMatched(me0_rh, me0_sh))
      {
	bool verbose(false);
	if (verbose){
    	  std::cout<<"SimHit: region "<<me0_sh.region<<" station "<<me0_sh.station
		   <<" layer "<<me0_sh.layer<<" chamber "<<me0_sh.chamber<<" roll "
		   <<me0_sh.roll<<" strip "<<me0_sh.strip<<" type "<<itHit->particleType()
		   <<" id "<<itHit->trackId()<<" x: "<<me0_sh.x<<std::endl;
	  std::cout<<"RecHit: region "<<me0_rh.region<<" station "<<me0_rh.station
		   <<" layer "<<me0_rh.layer<<" chamber "<<me0_rh.chamber
		   <<" roll "<<me0_rh.roll<<" firstStrip "<<me0_rh.firstClusterStrip
		   <<" cls "<<me0_rh.clusterSize<<" bx "<<me0_rh.bx<<" x: "<<me0_rh.x
		   <<" sigma: "<<me0_rh.xErr<<std::endl;
	}
	me0_rh_tree_->Fill();
	count++;
      }
    }
    me0_sh.countMatching = count;
    me0_sh_tree_->Fill();
  }

}

// ======= ME0 Segments =======
void GEMRecHitAnalyzer::analyzeME0Seg()
{

  for (auto me0s = me0Segment_->begin(); me0s != me0Segment_->end(); me0s++) {

    // The ME0 Ensamble DetId refers to layer = 1
    ME0DetId id = me0s->me0DetId();
    //std::cout <<" Original ME0DetID "<<id<<std::endl;
    auto roll = me0_geometry_->etaPartition(id);
    //std::cout <<"Global Segment Position "<< roll->toGlobal(me0s->localPosition())<<std::endl;
    auto segLP = me0s->localPosition();
    auto segLD = me0s->localDirection();
    //std::cout <<" Global Direction theta = "<<segLD.theta()<<" phi="<<segLD.phi()<<std::endl;
    auto me0rhs = me0s->specificRecHits();
    //std::cout <<"ME0 Ensamble Det Id "<<id<<" Number of RecHits "<<me0rhs.size()<<std::endl;

    me0_seg.detId = id;
    me0_seg.localX = segLP.x();
    me0_seg.localY = segLP.y();
    me0_seg.localZ = segLP.z();
    me0_seg.dirTheta = segLD.theta();
    me0_seg.dirPhi = segLD.phi();
    me0_seg.numberRH = me0rhs.size();
    me0_seg.chi2 = me0s->chi2();
    me0_seg.ndof = me0s->degreesOfFreedom();

    for (auto rh = me0rhs.begin(); rh!= me0rhs.end(); rh++){

      auto me0id = rh->me0Id();
      auto rhr = me0_geometry_->etaPartition(me0id);
      auto rhLP = rh->localPosition();
      auto erhLEP = rh->localPositionError();
      auto rhGP = rhr->toGlobal(rhLP);
      auto rhLPSegm = roll->toLocal(rhGP);
      float xe = segLP.x()+segLD.x()*rhLPSegm.z()/segLD.z();
      float ye = segLP.y()+segLD.y()*rhLPSegm.z()/segLD.z();
      float ze = rhLPSegm.z();
      LocalPoint extrPoint(xe,ye,ze); // in segment rest frame
      auto extSegm = rhr->toLocal(roll->toGlobal(extrPoint)); // in layer restframe

      me0_rhFromSeg.detId = me0id; 

      me0_rhFromSeg.region = me0id.region(); 
      me0_rhFromSeg.station = 0; 
      me0_rhFromSeg.ring = 0; 
      me0_rhFromSeg.layer = me0id.layer(); 
      me0_rhFromSeg.chamber = me0id.chamber(); 
      me0_rhFromSeg.roll = me0id.roll(); 

      me0_rhFromSeg.x = rhLP.x();
      me0_rhFromSeg.xErr = erhLEP.xx();
      me0_rhFromSeg.y = rhLP.y();
      me0_rhFromSeg.yErr = erhLEP.yy();

      me0_rhFromSeg.globalR = rhGP.perp();
      me0_rhFromSeg.globalX = rhGP.x();
      me0_rhFromSeg.globalY = rhGP.y();
      me0_rhFromSeg.globalZ = rhGP.z();
      me0_rhFromSeg.globalEta = rhGP.eta();
      me0_rhFromSeg.globalPhi = rhGP.phi();

      me0_rhFromSeg.xExt = extSegm.x();
      me0_rhFromSeg.yExt = extSegm.y();

      bool verbose(false);
      if (verbose)
      	std::cout <<" ME0 Layer Id "<<rh->me0Id()<<" error on the local point "<< erhLEP
	<<"\n-> Ensamble Rest Frame RH local position "<<rhLPSegm<<" Segment extrapolation "<<extrPoint
	<<"\n-> Layer Rest Frame RH local position "<<rhLP<<" Segment extrapolation "<<extSegm<<std::endl;

      me0_rhSeg_tree_->Fill();

    }

    me0_seg_tree_->Fill();

  }

}

bool GEMRecHitAnalyzer::isSimTrackGood(const SimTrack &t)
{
  // SimTrack selection
  if (t.noVertex()) return false;
  if (t.noGenpart()) return false;
  // only muons 
  if (std::abs(t.type()) != 13 and simTrackOnlyMuon_) return false;
  // pt selection
  if (t.momentum().pt() < simTrackMinPt_) return false;
  // eta selection
  const float eta(std::abs(t.momentum().eta()));
  if (eta > simTrackMaxEta_ || eta < simTrackMinEta_) return false; 
  return true;
}

// ======= GEM Matching ========
void GEMRecHitAnalyzer::analyzeTracks(edm::ParameterSet cfg_, const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
  const edm::SimVertexContainer & sim_vert = *sim_vertices.product();
  const edm::SimTrackContainer & sim_trks = *sim_tracks.product();

  for (auto& t: sim_trks)
  {
    if (!isSimTrackGood(t)) continue;
    
    // match hits and digis to this SimTrack
    SimTrackMatchManager match(t, sim_vert[t.vertIndex()], cfg_, iEvent, iSetup);
    
    const SimHitMatcher& match_sh = match.simhits();
    const GEMRecHitMatcher& match_rh = match.gemRecHits();

    track_.pt = t.momentum().pt();
    track_.phi = t.momentum().phi();
    track_.eta = t.momentum().eta();
    track_.charge = t.charge();
    track_.endcap = (track_.eta > 0.) ? 1 : -1;
    track_.gem_sh_layer1 = 0;
    track_.gem_sh_layer2 = 0;
    track_.gem_rh_layer1 = 0;
    track_.gem_rh_layer2 = 0;
    track_.gem_sh_eta = -9.;
    track_.gem_sh_phi = -9.;
    track_.gem_sh_x = -999;
    track_.gem_sh_y = -999;
    track_.gem_rh_eta = -9.;
    track_.gem_rh_phi = -9.;
    track_.gem_trk_rho = -999.;
    track_.gem_lx_even = -999.;
    track_.gem_ly_even = -999.;
    track_.gem_lx_odd = -999.;
    track_.gem_ly_odd = -999.;
    track_.has_gem_sh_l1 = 0;
    track_.has_gem_sh_l2 = 0;
    track_.has_gem_rh_l1 = 0;
    track_.has_gem_rh_l2 = 0;
    
    // ** GEM SimHits ** //
    auto gem_sh_ids_sch = match_sh.superChamberIdsGEM();
    for(auto d: gem_sh_ids_sch)
    {
      auto gem_simhits = match_sh.hitsInSuperChamber(d);
      auto gem_simhits_gp = match_sh.simHitsMeanPosition(gem_simhits);

      track_.gem_sh_eta = gem_simhits_gp.eta();
      track_.gem_sh_phi = gem_simhits_gp.phi();
      track_.gem_sh_x = gem_simhits_gp.x();
      track_.gem_sh_y = gem_simhits_gp.y();
    }
    
    // Calculation of the localXY efficiency
    GlobalPoint gp_track(match_sh.propagatedPositionGEM());
    track_.gem_trk_eta = gp_track.eta();
    track_.gem_trk_phi = gp_track.phi();
    track_.gem_trk_rho = gp_track.perp();
    //std::cout << "track eta phi rho = " << track_.gem_trk_eta << " " << track_.gem_trk_phi << " " << track_.gem_trk_rho << std::endl;
    
    float track_angle = gp_track.phi().degrees();
    if (track_angle < 0.) track_angle += 360.;
    //std::cout << "track angle = " << track_angle << std::endl;
    const int track_region = (gp_track.z() > 0 ? 1 : -1);
    
    // closest chambers in phi
    const auto mypair = getClosestChambers(track_region, track_angle);
    
    // chambers
    GEMDetId detId_first(mypair.first);
    GEMDetId detId_second(mypair.second);

    // assignment of local even and odd chambers (there is always an even and an odd chamber)
    bool firstIsOdd = detId_first.chamber() & 1;
    
    GEMDetId detId_even_L1(firstIsOdd ? detId_second : detId_first);
    GEMDetId detId_odd_L1(firstIsOdd ? detId_first : detId_second);

    auto even_partition = gem_geometry_->idToDetUnit(detId_even_L1)->surface();
    auto odd_partition = gem_geometry_->idToDetUnit(detId_odd_L1)->surface();

    // global positions of partitions' centers
    LocalPoint p0(0.,0.,0.);
    GlobalPoint gp_even_partition = even_partition.toGlobal(p0);
    GlobalPoint gp_odd_partition = odd_partition.toGlobal(p0);
    
    LocalPoint lp_track_even_partition = even_partition.toLocal(gp_track);
    LocalPoint lp_track_odd_partition = odd_partition.toLocal(gp_track);

    // track chamber local x is the same as track partition local x
    track_.gem_lx_even = lp_track_even_partition.x();
    track_.gem_lx_odd = lp_track_odd_partition.x();

    // track chamber local y is the same as track partition local y
    // corrected for partition's local y WRT chamber
    track_.gem_ly_even = lp_track_even_partition.y() + (gp_even_partition.perp() - radiusCenter_);
    track_.gem_ly_odd = lp_track_odd_partition.y() + (gp_odd_partition.perp() - radiusCenter_);

    //std::cout << track_.gem_lx_even << " " << track_.gem_ly_even << std::endl;
    //std::cout << track_.gem_lx_odd << " " << track_.gem_ly_odd << std::endl;


    auto gem_sh_ids_ch = match_sh.chamberIdsGEM();
    for(auto d: gem_sh_ids_ch)
    {
      GEMDetId id(d);
      bool odd(id.chamber() & 1);
      
      if (id.layer() == 1)
      {
        if (odd) track_.gem_sh_layer1 |= 1;
        else track_.gem_sh_layer1 |= 2;
      }
      else if (id.layer() == 2)
      {
        if (odd) track_.gem_sh_layer2 |= 1;
        else track_.gem_sh_layer2 |= 2;
      }
    }
    
    // ** GEM RecHits ** //
    auto gem_rh_ids_sch = match_rh.superChamberIds();
    for(auto d: gem_rh_ids_sch)
    {
      auto gem_recHits = match_rh.recHitsInSuperChamber(d);
      auto gem_rh_gp = match_rh.recHitMeanPosition(gem_recHits);

      track_.gem_rh_eta = gem_rh_gp.eta();
      track_.gem_rh_phi = gem_rh_gp.phi();	
      
    }

    auto gem_rh_ids_ch = match_rh.chamberIds();
    for(auto d: gem_rh_ids_ch)
    {
      GEMDetId id(d);
      bool odd(id.chamber() & 1);
      
      if (id.layer() == 1)
      {
	if (odd)
	{
	  track_.gem_rh_layer1 |= 1;
	}
	else
	{
	  track_.gem_rh_layer1 |= 2;
	}
      }
      else if (id.layer() == 2)
      {
	if (odd)
	{
	  track_.gem_rh_layer2 |= 1;
	}
	else
	{
	  track_.gem_rh_layer2 |= 2;
	}
      }
    }

    // Construct Chamber DetIds from the "projected" ids:
    GEMDetId id_ch_even_L1(detId_even_L1.region(), detId_even_L1.ring(), detId_even_L1.station(), 1, detId_even_L1.chamber(), 0);
    GEMDetId id_ch_odd_L1(detId_odd_L1.region(), detId_odd_L1.ring(), detId_odd_L1.station(), 1, detId_odd_L1.chamber(), 0);
    GEMDetId id_ch_even_L2(detId_even_L1.region(), detId_even_L1.ring(), detId_even_L1.station(), 2, detId_even_L1.chamber(), 0);
    GEMDetId id_ch_odd_L2(detId_odd_L1.region(), detId_odd_L1.ring(), detId_odd_L1.station(), 2, detId_odd_L1.chamber(), 0);

    // check if track has sh
    if(gem_sh_ids_ch.count(id_ch_even_L1)!=0) track_.has_gem_sh_l1 |= 2;
    if(gem_sh_ids_ch.count(id_ch_odd_L1)!=0) track_.has_gem_sh_l1 |= 1;
    if(gem_sh_ids_ch.count(id_ch_even_L2)!=0) track_.has_gem_sh_l2 |= 2;
    if(gem_sh_ids_ch.count(id_ch_odd_L2)!=0) track_.has_gem_sh_l2 |= 1;

    // check if track has rh
    if(gem_rh_ids_ch.count(id_ch_even_L1)!=0){
      track_.has_gem_rh_l1 |= 2;
    }
    if(gem_rh_ids_ch.count(id_ch_odd_L1)!=0){
      track_.has_gem_rh_l1 |= 1;
    }
    if(gem_rh_ids_ch.count(id_ch_even_L2)!=0){
      track_.has_gem_rh_l2 |= 2;
    }
    if(gem_rh_ids_ch.count(id_ch_odd_L2)!=0){
      track_.has_gem_rh_l2 |= 1;
    }

    track_tree_->Fill();

  } // track loop
}

void GEMRecHitAnalyzer::endJob() 
{
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void GEMRecHitAnalyzer::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  // The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

void GEMRecHitAnalyzer::buildLUT()
{
  std::vector<int> pos_ids;
  pos_ids.push_back(GEMDetId(1,1,1,1,36,1).rawId());

  std::vector<int> neg_ids;
  neg_ids.push_back(GEMDetId(-1,1,1,1,36,1).rawId());

  // VK: I would really suggest getting phis from GEMGeometry
  
  std::vector<float> phis;
  phis.push_back(0.);
  for(int i=1; i<37; ++i)
  {
    pos_ids.push_back(GEMDetId(1,1,1,1,i,1).rawId());
    neg_ids.push_back(GEMDetId(-1,1,1,1,i,1).rawId());
    phis.push_back(i*10.);
  }
  positiveLUT_ = std::make_pair(phis,pos_ids);
  negativeLUT_ = std::make_pair(phis,neg_ids);
}

std::pair<int,int>
GEMRecHitAnalyzer::getClosestChambers(int region, float phi)
{
  auto& phis(positiveLUT_.first);
  auto upper = std::upper_bound(phis.begin(), phis.end(), phi);
  //std::cout << "lower = " << upper - phis.begin() << std::endl;
  //std::cout << "upper = " << upper - phis.begin() + 1 << std::endl;
  auto& LUT = (region == 1 ? positiveLUT_.second : negativeLUT_.second);
  return std::make_pair(LUT.at(upper - phis.begin()), (LUT.at((upper - phis.begin() + 1)%36)));
}

//define this as a plug-in
DEFINE_FWK_MODULE(GEMRecHitAnalyzer);
