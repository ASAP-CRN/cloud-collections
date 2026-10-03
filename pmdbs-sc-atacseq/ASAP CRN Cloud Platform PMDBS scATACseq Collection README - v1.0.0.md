# ASAP CRN Cloud PMDBS scATACseq Collection

# README \- v1.0.0 [**10.5281/zenodo.20400469**](https://doi.org/10.5281/zenodo.20400469)

## Overview

The ASAP CRN Cloud is pleased to present the **PMDBS Single Cell (sc) ATACseq Collection** as part of the v5.0.0 [ASAP CRN Cloud Release](https://doi.org/10.5281/zenodo.8384742).  There is currently a single ATAC dataset from Team Voet, but additional ATACseq contributions are expected to be released in the near future.  Stay tuned\!

**ASAP Team:** Team Voet  
See [CRN Cloud Authorship List](https://storage.googleapis.com/asap-public-assets/wayfinding/CRN%20Cloud%20Authorship%20List.pdf) for the full list of contributing investigators/researchers by dataset.   
**ASAP CRN GitHub:** [github.com/ASAP-CRN](https://github.com/ASAP-CRN/)  
**Data Release Date:**  2026-06-15  
**ASAP CRN Cloud Release Number:** v5.0.0  
**ASAP CRN Release DOI:**  [10.5281/zenodo.8384742](https://doi.org/10.5281/zenodo.8384742)  
**Curated Data File Manifest:** [ASAP CRN Cloud File Manifest \- v3.1](https://docs.google.com/document/d/1E6Ok0hkiWWQ415q9-xPStMphJ_W_Wr-k7028ztww5pI/edit?usp=sharing)

### PMDBS scATACseq Collection 

The raw scATACseq data has been processed and harmonized to create a harmonized database of chromatin accessibility data.  The platformed data is summarized below as Raw Data, Curated Data, and QC Summaries below.  Code, explanations, and schematics for processing the platformed data can be found at the [ASAP-CRN sc-atacseq-wf](https://github.com/ASAP-CRN/sc-atacseq-wf) repo.

## Collection details

**scATACseq Workflow Release** \- **v1.0.0**

* Release date:  2026-06-15  
  * GitHub release [link](https://github.com/ASAP-CRN/sc-atacseq-wf/releases/tag/sc_atacseq_analysis-v1.0.0)  
  * Pipeline version: v1.0.0

### Collection Datasets list

* `voet-pmdbs-sn-atacseq-10x`, DOI:[10.5281/zenodo.18988729](https://doi.org/10.5281/zenodo.18988729)

### Curated Data 

* Preprocessing per pool with [Cell Ranger ATAC](https://www.10xgenomics.com/support/software/cell-ranger-atac/latest), and splitting the Cell Ranger fragment files with Vireo demultiplexed assignment files and [scatac\_fragment\_tools](https://github.com/aertslab/scatac_fragment_tools/tree/main/src/scatac_fragment_tools) provided by the contributing author  
* Cohort analysis per sample *(one subject \= one sample \+ pool)* with [SnapATAC2](https://scverse.org/SnapATAC2/version/2.9/index.html), [scanpy](https://scanpy.readthedocs.io/en/stable/), and [scvi-tools](https://scvi-tools.org/) by:  
  * Peak calling with MACS3  
  * Harmony and PeakVI integration  
  * Generating a gene matrix to perform cell type annotation via MapMyCells (Allen SEA-AD) used in the [sc RNA-seq pipeline](https://github.com/ASAP-CRN/sc-rnaseq-wf/tree/main)  
  * Motif enrichment analysis on per-cell-type peaks

Full Changelog: [https://github.com/ASAP-CRN/sc-atacseq-wf/commits/sc\_atacseq\_analysis-v1.0.0](https://github.com/ASAP-CRN/sc-atacseq-wf/commits/sc_atacseq_analysis-v1.0.0)

### Raw Data

The *raw* data refers to the fastq files transferred by each ASAP CRN Team.  These data are available with the caveat that they are stored in “requester pays” buckets on the google cloud platform.   A google cloud billing account will need to be registered to access these data.  More information is available [HERE](https://workbench.verily.com/workspaces/asap-crn-reference-workspace/resources/9099df22-8412-4c7c-adb7-810f261d0820/docs/how-to-access-and-analyze-raw-files-in-verily-workbench.html).  gs://`asap-raw-<team_name>-<source>-<dataset_name>`  
 

### Metadata & Data Dictionary

The ASAP CRN Common Data Elements ([CDE](https://docs.google.com/spreadsheets/d/1c0z5KvRELdT2AtQAH2Dus8kwAyyLrR0CROhKOjpU4Vc/edit?usp=sharing)) outlines the variables which are harmonized across the ASAP CRN.  These metadata enable the harmonization of the data submitted by multiple teams. The metadata consists of five tables, which are described below.

Metadata refers to descriptive information about the overall study, individual samples, all protocols, and references to processed and raw data file names. Metadata was aggregated using the table-based submission for each team's dataset.  The tables \- STUDY, PROTOCOL, SUBJECT, SAMPLE, DATA ,etc. \- can be thought of as spreadsheets, and each table is prepared as simple .csv files which constitute the tables outlined in the [ASAP CRN CDE](https://docs.google.com/spreadsheets/d/1c0z5KvRELdT2AtQAH2Dus8kwAyyLrR0CROhKOjpU4Vc/edit?usp=sharing).   These have been aggregated across submissions and unique ASAP IDs generated for each dataset, team, subject and sample.  I.e. ASAP\_dataset\_id, ASAP\_team\_id, ASAP\_subject\_id, and ASAP\_sample\_id. 

The metadata can be browsed on [ASAP CRN Cloud](https://cloud.parkinsonsroadmap.org/) *Explorer* and exposed in [Verily Workbench](https://workbench.verily.com/workspaces/asap-crn-reference-workspace).

[This document.](https://docs.google.com/document/d/1VRD52bkFPAHpplfhShvc7bcxhzLcGf8BCTcGxsxDUKs/edit?usp=sharing)

