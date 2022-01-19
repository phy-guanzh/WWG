from WMCore.Configuration import Configuration 

config = Configuration()
config.section_("General")
config.General.requestName = "GluGluHToWWTo2L2Nu_M125_TuneCP5_13TeV_powheg2_JHUGenV714_pythia8_2018"
config.General.transferLogs = False 
config.General.workArea = "crab2018"

config.section_("JobType")
config.JobType.pluginName = "Analysis"
config.JobType.psetName = "PSet.py"
config.JobType.scriptExe = "./WWG_crab_script.sh" 
config.JobType.inputFiles = ["../../../scripts/haddnano.py","../WWG_selector/WWG_postproc.py","../WWG_selector/WWG_Module.py","../WWG_selector/WWG_keep_and_drop.txt","../WWG_selector/WWG_output_branch.txt","../WWG_selector/DAS_filesearch.py"] #hadd nano will not be needed once nano tools are in cmssw 
config.JobType.scriptArgs = ["isdata=MC","year=2018","era=A"] 
config.JobType.sendPythonFolder  = True
config.JobType.allowUndistributedCMSSW = True 

config.section_("Data")
config.Data.inputDataset = "/GluGluHToWWTo2L2Nu_M125_TuneCP5_13TeV_powheg2_JHUGenV714_pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM" 
config.Data.inputDBS = "global"
# config.Data.splitting = "FileBased"
# config.Data.unitsPerJob = 1
config.Data.splitting = "FileBased"
config.Data.unitsPerJob = 1
config.Data.publication = False
config.Data.ignoreLocality = True
config.Data.allowNonValidInputDataset = True
config.Data.outputDatasetTag = "GluGluHToWWTo2L2Nu_M125_TuneCP5_13TeV_powheg2_JHUGenV714_pythia8_2018" 

config.section_("Site")
config.Site.storageSite = "T3_CH_CERNBOX"
config.Site.whitelist = ["T2_US_MIT","T2_US_Wisconsin","T2_US_Purdue","T2_US_UCSD","T2_US_Caltech","T2_US_Nebraska"] 
