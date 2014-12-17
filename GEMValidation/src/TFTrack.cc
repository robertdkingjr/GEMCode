#include "GEMCode/GEMValidation/src/TFTrack.h"

TFTrack::TFTrack(const csc::L1Track* t, const CSCCorrelatedLCTDigiCollection* lcts)
{
  l1track_ = t;
  triggerDigis_.clear();
  triggerIds_.clear();
  
  for (auto detUnitIt = lcts->begin(); detUnitIt != lcts->end(); detUnitIt++) {
    const CSCDetId& id = (*detUnitIt).first;
    //std::cout << "DetId " << id << std::endl;
    const auto range = (*detUnitIt).second;
    for (auto digiIt = range.first; digiIt != range.second; digiIt++) {
      if (!(*digiIt).isValid()) continue;
      //std::cout << "Digi " << *digiIt << std::endl;
      addTriggerDigi(&(*digiIt));
      addTriggerDigiId(id);
    }
  }
}

TFTrack::TFTrack(const TFTrack& rhs)
{}

TFTrack::~TFTrack()
{}

void 
TFTrack::init(CSCTFPtLUT* ptLUT,
	      edm::ESHandle< L1MuTriggerScales > &muScales,
	      edm::ESHandle< L1MuTriggerPtScale > &muPtScale)
{
  // This section is copied from L1Trigger/CSCTrackFinder/interface/CSCTFMuonSorter.h

  unsigned gbl_phi(l1track_->localPhi() + ((l1track_->sector() - 1)*24) + 6);
  if(gbl_phi > 143) gbl_phi -= 143;
  phi_packed_ = gbl_phi & 0xff;
  
  const unsigned eta_sign(l1track_->endcap() == 1 ? 0 : 1);
  const int gbl_eta(l1track_->eta_packed() | eta_sign << (L1MuRegionalCand::ETA_LENGTH - 1));
  eta_packed_  = gbl_eta & 0x3f;
  
  unsigned gpt = 0, quality = 0;
  csc::L1Track::decodeRank(l1track_->rank(), gpt, quality);
  q_packed_ = quality & 0x3;
  pt_packed_ = gpt & 0x1f;
    
  // calculate pt, eta and phi (don't forget to store the sign)
  pt_ = muPtScale->getPtScale()->getLowEdge(pt_packed_) + 1.e-6;
  eta_ = muScales->getRegionalEtaScale(2)->getCenter(l1track_->eta_packed()) * l1track_->endcap(); 
  phi_ = normalizedPhi(muScales->getPhiScale()->getLowEdge(phi_packed_));
}

void 
TFTrack::setDR(double dr)
{
  dr_ = dr;
}

bool 
TFTrack::hasStubEndcap(int st) const
{
  if(st==1 and l1track_->me1ID() > 0) return true;
  if(st==2 and l1track_->me2ID() > 0) return true;
  if(st==3 and l1track_->me3ID() > 0) return true;
  if(st==4 and l1track_->me4ID() > 0) return true;
  return false;
}

bool
TFTrack::hasStubBarrel() const
{
  return l1track_->mb1ID() > 0;
}

bool 
TFTrack::hasStubStation(int st) const
{
  if(st==0 and hasStubBarrel())       return true;
  if(st==1 and l1track_->me1ID() > 0) return true;
  if(st==2 and l1track_->me2ID() > 0) return true;
  if(st==3 and l1track_->me3ID() > 0) return true;
  if(st==4 and l1track_->me4ID() > 0) return true;
  return false;
}


bool 
TFTrack::hasStubCSCOk(int st) const
{
//   if (!hasStubStation(st)) return false;
//   bool cscok = 0;
//   for (size_t s=0; s<ids_.size(); s++) {
//     if (ids_[s].station() == st and mplcts_[s]->deltaOk) { 
//       cscok = 1; 
//       break; 
//     }
//   }
//   return cscok;
  return true;
}


unsigned int 
TFTrack::nStubs(bool mb1, bool me1, bool me2, bool me3, bool me4) const
{
  return ( (mb1 and hasStubStation(0)) + (me1 and hasStubStation(1)) + 
	   (me2 and hasStubStation(2)) + (me3 and hasStubStation(3)) + 
	   (me4 and hasStubStation(4)) );
}


unsigned int 
TFTrack::nStubsCSCOk(bool me1, bool me2, bool me3, bool me4) const
{
  return ( (me1 and hasStubCSCOk(1)) + (me2 and hasStubCSCOk(2)) + 
	   (me3 and hasStubCSCOk(3)) + (me4 and hasStubCSCOk(4)) );
}


bool 
TFTrack::passStubsMatch(double steta, int minLowHStubs, int minMidHStubs, int minHighHStubs) const
{
//    const double steta(match->strk->momentum().eta());
  const int nstubs(nStubs(1,1,1,1,1));
  const int nstubsok(nStubsCSCOk(1,1,1,1));
  if (fabs(steta) <= 1.2)      return nstubsok >=1 and nstubs >= minLowHStubs;
  else if (fabs(steta) <= 2.1) return nstubsok >=2 and nstubs >= minMidHStubs;
  else                         return nstubsok >=2 and nstubs >= minHighHStubs;
}


void 
TFTrack::print()
{
  /*
    std::cout<<"#### TFTRACK PRINT: "<<msg<<" #####"<<std::endl;
    //std::cout<<"## L1MuRegionalCand print: ";
    //l1track_->print();
    //std::cout<<"\n## L1Track Print: ";
    //l1track_->Print();
    //std::cout<<"## TFTRACK:  
    std::cout<<"\tpt_packed: "<<pt_packed<<"  eta_packed: " << eta_packed<<"  phi_packed: " << phi_packed<<"  q_packed: "<< q_packed<<"  bx: "<<l1track_->bx()<<std::endl;
    std::cout<<"\tpt: "<<pt<<"  eta: "<<eta<<"  phi: "<<phi<<"  sector: "<<l1track_->sector()<<"  dr: "<<dr<<"   ok1: "<<deltaOk1<<"  ok2: "<<deltaOk2<<"  okME1: "<<deltaOkME1<<std::endl;
    std::cout<<"\tMB1 ME1 ME2 ME3 ME4 = "<<l1track_->mb1ID()<<" "<<l1track_->me1ID()<<" "<<l1track_->me2ID()<<" "<<l1track_->me3ID()<<" "<<l1track_->me4ID()
        <<" ("<<hasStub(0)<<" "<<hasStub(1)<<" "<<hasStub(2)<<" "<<hasStub(3)<<" "<<hasStub(4)<<")  "
        <<" ("<<hasStubCSCOk(1)<<" "<<hasStubCSCOk(2)<<" "<<hasStubCSCOk(3)<<" "<<hasStubCSCOk(4)<<")"<<std::endl;
    std::cout<<"\tptAddress: 0x"<<std::hex<<l1track_->ptLUTAddress()<<std::dec<<"  mode: "<<mode()<<"  sign: "<<sign()<<"  dphi12: "<<dPhi12()<<"  dphi23: "<<dPhi23()<<std::endl;
    std::cout<<"\thas "<<trgdigis.size()<<" stubs in ";
    for (size_t s=0; s<trgids.size(); s++) 
        std::cout<<trgids[s]<<" w:"<<trgdigis[s]->getKeyWG()<<" s:"<<trgdigis[s]->getStrip()/2 + 1<<" p:"<<trgdigis[s]->getPattern()<<" bx:"<<trgdigis[s]->getBX()<<"; ";
    std::cout<<std::endl;
    std::cout<<"\tstub_etaphis:";
    for (size_t s=0; s<trgids.size(); s++)
        std::cout<<"  "<<trgetaphis[s].first<<" "<<trgetaphis[s].second;
    std::cout<<std::endl;
    std::cout<<"\tstub_petaphis:";
    for (size_t s=0; s<trgstubs.size(); s++)
        std::cout<<"  "<<trgstubs[s].etaPacked()<<" "<<trgstubs[s].phiPacked();
    std::cout<<std::endl;
    std::cout<<"\thas "<<mplcts.size()<<" associated MPCs in ";
    for (size_t s=0; s<ids.size(); s++) 
        std::cout<<ids[s]<<" w:"<<mplcts[s]->trgdigi->getKeyWG()<<" s:"<<mplcts[s]->trgdigi->getStrip()/2 + 1<<" Ok="<<mplcts[s]->deltaOk<<"; ";
    std::cout<<std::endl;
    std::cout<<"\tMPCs meEtap and mePhip: ";
    for (size_t s=0; s<ids.size(); s++) std::cout<<mplcts[s]->meEtap<<", "<<mplcts[s]->mePhip<<";  ";
    std::cout<<std::endl;
    std::cout<<"#### TFTRACK END PRINT #####"<<std::endl;
  */
}

void 
TFTrack::addTriggerDigi(const CSCCorrelatedLCTDigi* digi)
{
  triggerDigis_.push_back(digi);
}

void 
TFTrack::addTriggerDigiId(const CSCDetId& id)
{
  triggerIds_.push_back(id);
}

void 
TFTrack::addTriggerEtaPhi(const std::pair<float,float>& p)
{
  triggerEtaPhis_.push_back(p);
}

void 
TFTrack::addTriggerStub(const csctf::TrackStub& st)
{
  triggerStubs_.push_back(st);
}
