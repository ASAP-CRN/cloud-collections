# ASAP CRN Cloud PMDBS Spatial RNAseq Collection

# README \- v1.1.2 [**10.5281/zenodo.20403929**](https://doi.org/10.5281/zenodo.20403929)

## Overview

The **PMDBS Spatial RNAseq Collection** has been updated to **v1.1.2** to reflect the updated Datasets’ metadata to conform with the **v4.4** Common Data Elements (CDE) with the **v5.0.0 [ASAP CRN Cloud Release](https://doi.org/10.5281/zenodo.8384742)**.

[10.5281/zenodo.8384742](https://doi.org/10.5281/zenodo.8384742)  
**ASAP Teams:** Team Edwards  
See [CRN Cloud Authorship List](https://storage.googleapis.com/asap-public-assets/wayfinding/CRN%20Cloud%20Authorship%20List.pdf) for the full list of contributing investigators/researchers by dataset.   
**ASAP CRN GitHub:** [github.com/ASAP-CRN](https://github.com/ASAP-CRN/)  
**Data Release Date:**  2026-06-15  
**ASAP CRN Cloud Release Number:** v5.0.0  
**ASAP CRN Release DOI:**  [10.5281/zenodo.8384742](https://doi.org/10.5281/zenodo.8384742)  
**Curated Data File Manifest:** [ASAP CRN Cloud File Manifest \- v3.1](https://docs.google.com/document/d/1E6Ok0hkiWWQ415q9-xPStMphJ_W_Wr-k7028ztww5pI/edit?usp=sharing)

### PMDBS Spatial RNAseq Collection

The raw bulk RNAseq data has been processed and harmonized to create a harmonized database of gene expression data.  The platformed data is summarized below as Upstream, Downstream and Cohort analysis summaries below.  Additional explanation for the analysis pipeline employed for processing the platformed data can be found at the [ASAP-CRN spatial-transcriptomics-wf](https://github.com/ASAP-CRN/spatial-transcriptomics-wf) github repo. These workflows include two different analysis pipelines:  

1. Spatial GeoMx Analysis (spatial\_geomx) \- [spatial\_geomx\_analysis-v1.0.0](https://github.com/ASAP-CRN/spatial-transcriptomics-wf/tree/spatial_geomx_analysis-v1.0.0)  
2. Spatial Visium Analysis (spatial\_visium) \- [spatial\_visium\_analysis-v1.0.0](https://github.com/ASAP-CRN/spatial-transcriptomics-wf/tree/spatial_visium_analysis-v1.0.0)

## Collection details

**PMDBS Spatial RNAseq Workflow Release** \- **v1.0.1**

* Release date:  2025-12-05  
  * GitHub release: [spatial\_geomx](https://github.com/ASAP-CRN/spatial-transcriptomics-wf/tree/spatial_geomx_analysis-v1.0.0), [spatial\_visium](https://github.com/ASAP-CRN/spatial-transcriptomics-wf/releases/tag/spatial_visium_analysis-v1.0.1)   
  * Pipeline version: v1.0.1

### Collection Datasets list

[spatial\_geomx](https://github.com/ASAP-CRN/spatial-transcriptomics-wf/tree/spatial_geomx_analysis-v1.0.0)

* `edwards-pmdbs-spatial-geomx-th`,  DOI: [10.5281/zenodo.15480990](https://doi.org/10.5281/zenodo.15480990)

  [spatial\_visium](https://github.com/ASAP-CRN/spatial-transcriptomics-wf/releases/tag/spatial_visium_analysis-v1.0.1) 

  * `scherzer-pmdbs-spatial-visium-mtg`, DOI: [10.5281/zenodo.17242087](https://doi.org/10.5281/zenodo.17242087)

### Curated Data

The data curation is broken up into  “*pre-processing*” and “*cohort analysis*”, for our two spatial workflows:  the **Nanostring GeoMx (**`spatial_geomx`) **and 10x Visium (**`spatial_visium`).  In general the `preprocess` stage involves alignment of the raw data and converting them into count matrices which are QC-ed and combined across slides/samples. The cohort\_analysis stage involves normalization, clustering, integration, and dimension reduction (UMAP) for visualization.  Note that for the `spatial_geomex` version the `preprocess` stage  is run with R-language tools, and the additional `process_to_adata` step completes QC and creates the overall transcriptomics data object which is python compatible..

### Raw Data

The *raw* data refers to the fastq files transferred by each ASAP CRN Team.  These data are available with the caveat that they are stored in “requester pays” buckets on the google cloud platform.   A google cloud billing account will need to be registered to access these data.  More information is available [HERE](https://workbench.verily.com/workspaces/asap-crn-reference-workspace/resources/9099df22-8412-4c7c-adb7-810f261d0820/docs/how-to-access-and-analyze-raw-files-in-verily-workbench.html).  gs://`asap-raw-<team_name>-<source>-<dataset_name>`

### Metadata & Data Dictionary

The ASAP CRN Common Data Elements ([CDE](https://docs.google.com/spreadsheets/d/1c0z5KvRELdT2AtQAH2Dus8kwAyyLrR0CROhKOjpU4Vc/edit?usp=sharing)) outlines the variables which are harmonized across the ASAP CRN.  These metadata enable the harmonization of the data submitted by multiple teams. The metadata consists of five tables, which are described below.

Metadata refers to descriptive information about the overall study, individual samples, all protocols, and references to processed and raw data file names. Metadata was aggregated using the table-based submission for each team's dataset.  The tables \- STUDY, PROTOCOL, SUBJECT, SAMPLE, DATA ,etc. \- can be thought of as spreadsheets, and each table is prepared as simple .csv files which constitute the tables outlined in the [ASAP CRN CDE](https://docs.google.com/spreadsheets/d/1c0z5KvRELdT2AtQAH2Dus8kwAyyLrR0CROhKOjpU4Vc/edit?usp=sharing).   These have been aggregated across submissions and unique ASAP IDs generated for each dataset, team, subject and sample.  I.e. ASAP\_dataset\_id, ASAP\_team\_id, ASAP\_subject\_id, and ASAP\_sample\_id. 

The metadata can be browsed on [ASAP CRN Cloud](https://cloud.parkinsonsroadmap.org/collections/postmortem-derived-brain-sequencing-collection/overview) *Explorer* and exposed in [Verily Workbench](https://workbench.verily.com/workspaces/asap-crn-reference-workspace).

[This document.](https://docs.google.com/document/d/1Yw0OVWE2Asn_bG6ZLb16czkTGUlPnC1kxRYqABL2n5g/edit?usp=sharing)

