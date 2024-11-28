# asap-crn-could-collections
Source-of-truth for ASAP CRN Cloud _collections_

**Collections** are sets of ASAP CRN Cloud datasets of a common _kind_.  Collections can be either of _kinds_ which have an ASAP CRN analysis workflow which include ASAP CRN curated analysis artifacts _in addition_ to the team contributed analysis artifacts.  , or "other".  "Other" datasets are simply artifacts which are platformed with just the team contributed artifacts.  In cases where a _meta_-dataset (an `asap-cohort`-dataset) can be created from the collection and the workflow analysis executed, that dataset will be platformed into its own gcp bucket.

Currenly, as of the v2.0 release, there are three PMDBS collections: the "scRNAseq PMDBS Datasets", "bulkRNAseq PMDBS Datsets", and "Other PMDBS Datasets" collections.  In the future collections will be created to organize non-PMDBS datasets, and other workflow pipelines.

## all collections summary
- collections.csv
  - collection-name, collection-version, dataset-name, dataset-version, workflow, workflow-version

## collections

datasets/<datset-name>

contains:
- `version` a text file containing the current version
- `workflow` a text file containing the DOI uri
- `workflow-GH` a text file containing the github url to the dataset in the ASAP-CRN metadata github
- `asap-cohort-bucket` a text file containing the gcp bucket name containing the workflow curated artifacts
- a empty file whose name corresponds to the current version. e.g. all datasets will start with a file named "v1.0"

## versions
Collections inherit their version from the release.

