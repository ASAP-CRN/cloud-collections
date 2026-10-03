# ASAP CRN Cloud PMDBS bulk RNAseq Collection

# README \- v1.2.2 [**10.5281/zenodo.20403867**](https://doi.org/10.5281/zenodo.20403867)

## Overview

The **PMDBS Bulk RNAseq Collection** has been updated to **v1.2.2** to capture the reformatting of the Datasets' metadata with **v5.0.0 [ASAP CRN Cloud Release](https://doi.org/10.5281/zenodo.8384742)**.  

**ASAP Teams:** Team Lee, Team Hardy, Team Wood, Team Jakobsson  
See [CRN Cloud Authorship List](https://storage.googleapis.com/asap-public-assets/wayfinding/CRN%20Cloud%20Authorship%20List.pdf) for the full list of contributing investigators/researchers by dataset.   
**ASAP CRN GitHub:** [github.com/ASAP-CRN](https://github.com/ASAP-CRN/)  
**Data Release Date:**  2026-05-30  
**ASAP CRN Cloud Release Number:** v5.0.0  
**ASAP CRN Release DOI:**  [10.5281/zenodo.8384742](https://doi.org/10.5281/zenodo.8384742)  
**Curated Data File Manifest:** [ASAP CRN Cloud File Manifest \- v3.1](https://docs.google.com/document/d/1E6Ok0hkiWWQ415q9-xPStMphJ_W_Wr-k7028ztww5pI/edit?usp=sharing)

### PMDBS Bulk RNAseq Collection

The raw bulk RNAseq data has been processed and harmonized to create a harmonized database of gene expression data.  The platformed data is summarized below as Upstream, Downstream and Cohort analysis summaries below.  Additional explanation for the analysis pipeline employed for processing the platformed data can be found at the [ASAP-CRN pmdbs-bulk-rnaseq-wf](https://github.com/ASAP-CRN/pmdbs-bulk-rnaseq-wf) github repo.

## Collection details

**PMDBS Bulk RNAseq Workflow Release** \- **v1.1.1**

* Release date:  2025-12-01  
  * GitHub release [link](https://github.com/ASAP-CRN/pmdbs-bulk-rnaseq-wf/releases/tag/pmdbs_bulk_rnaseq_analysis-v1.1.1)  
  * Pipeline version: v1.1.1

### Collection Datasets list

* `team-hardy-pmdbs-bulk-rnaseq`, DOI:[10.5281/zenodo.16749098](https://doi.org/10.5281/zenodo.16749098) `-> v1.1`  
  * `team-lee-pmdbs-bulk-rnaseq-mfg`, DOI:[10.5281/zenodo.16748937](https://doi.org/10.5281/zenodo.16748937) `-> v1.1`  
  * `team-wood-pmdbs-bulk-rnaseq`, DOI:[10.5281/zenodo.16749007](https://doi.org/10.5281/zenodo.16749007) `-> v1.1`  
  * `team-jakobsson-pmdbs-bulk-rnaseq`, DOI:[10.5281/zenodo.16929448](https://doi.org/10.5281/zenodo.16929448) `-> unchanged`   
  * `asap-cohort-pmdbs-bulk-rnaseq -> v1.2.1`

### Curated Data

The curated data can be categorized as “*upstream*” and “*downstream*”, and “*cohort analysis*”.  They are further segregated by mode: *“mapping mode”* and *“alignment mode”*. 

***Upstream.***   
The bulk RNAseq pipeline begins with QC and trimming of raw fastq files to ensure high-quality input for downstream processing. Following these steps, users can select one or both of the available processing modes: alignment mode and/or mapping mode. In alignment mode, the trimmed fastq files are aligned to a reference genome using STAR, producing BAM files with aligned reads. These BAM files are then processed using Salmon (alignment mode) to quantify gene expression, generating output such as transcript counts or TPM values. In contrast, mapping mode bypasses the alignment step and directly quantifies gene expression from the trimmed fastq files using Salmon (mapping mode).  
   
***Downstream***  
Differential analysis is performed with PyDeseq2 to identify statistically significant differentially expressed genes between Parkinson’s Disease and Control samples. The filtering cutoffs were chosen to be:

* Adjusted p-value \< 0.05  
* Absolute log2 fold change \> 1

***Cohort analysis***  
A cohort analysis is made by looking across all the gene expression data to find modes of expression across genes between our experimental groups.

### Raw Data

The *raw* data refers to the fastq files transferred by each ASAP CRN Team.  These data are available with the caveat that they are stored in “requester pays” buckets on the google cloud platform.   A google cloud billing account will need to be registered to access these data.  More information is available [HERE](https://workbench.verily.com/workspaces/asap-crn-reference-workspace/resources/9099df22-8412-4c7c-adb7-810f261d0820/docs/how-to-access-and-analyze-raw-files-in-verily-workbench.html).  gs://`asap-raw-<team_name>-<source>-<dataset_name>`

### Metadata & Data Dictionary

The ASAP CRN Common Data Elements ([CDE](https://docs.google.com/spreadsheets/d/1c0z5KvRELdT2AtQAH2Dus8kwAyyLrR0CROhKOjpU4Vc/edit?usp=sharing)) outlines the variables which are harmonized across the ASAP CRN.  These metadata enable the harmonization of the data submitted by multiple teams. The metadata consists of five tables, which are described below.

Metadata refers to descriptive information about the overall study, individual samples, all protocols, and references to processed and raw data file names. Metadata was aggregated using the table-based submission for each team's dataset.  The tables \- STUDY, PROTOCOL, SUBJECT, SAMPLE, DATA ,etc. \- can be thought of as spreadsheets, and each table is prepared as simple .csv files which constitute the tables outlined in the [ASAP CRN CDE](https://docs.google.com/spreadsheets/d/1c0z5KvRELdT2AtQAH2Dus8kwAyyLrR0CROhKOjpU4Vc/edit?usp=sharing).   These have been aggregated across submissions and unique ASAP IDs generated for each dataset, team, subject and sample.  I.e. ASAP\_dataset\_id, ASAP\_team\_id, ASAP\_subject\_id, and ASAP\_sample\_id. 

The metadata can be browsed on [ASAP CRN Cloud](https://cloud.parkinsonsroadmap.org/collections/postmortem-derived-brain-sequencing-collection/overview) *Explorer* and exposed in [Verily Workbench](https://workbench.verily.com/workspaces/asap-crn-reference-workspace).

[This document.](https://docs.google.com/document/d/11Af2A6LIH07QeFvwUAmcFOGTiadysHr07Dqgo9F07y4/edit?usp=sharing)

