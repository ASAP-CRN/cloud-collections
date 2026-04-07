# asap-crn-could-collections
Mechanics and archive for maintaining ASAP CRN Cloud _collections_
- DOIs
- version definitions
- curated buckets for VWB interface.

**Collections** are sets of ASAP CRN Cloud datasets of a common _kind_.  Collections can be either of _kinds_ which have an ASAP CRN analysis workflow which include ASAP CRN curated analysis artifacts _in addition_ to the team contributed analysis artifacts.  "Other" datasets are simply artifacts which are platformed with just the team contributed artifacts.  

Currenly, as of the v4.0 release, there are 5 versioned CRN Cloud Collections: the "PMDBS scRNAseq Collection", "PMDBS bulkRNAseq Collection", "PMDBS Spatial Transcriptomics Collection", "Mouse Spatial Transcriptomics Collection", and "Mouse scRNAseq Collection".  Datasets from these collections are exposed in VWB workbench in versioned "Data Collections" which have imutable copies of the _curated_ in gcp buckets unique to them.   The individual Dataset curated buckets are mutable and contain the curated data artifacts of workflow outputs for all released versions.   

Un-curated "Other" datasets are exposed in un-versioned Data Collections which reference each Datasets curated buckets.   


## all collections summary
- PMDBS
    - sc RNAseq
    - bulk RNAseq
    - spatial RNAseq

- Mouse
    - sc RNAseq
    - spatial RNAseq


## Structure

- `collections.json`: JSON index containing all collections with their DOIs and references
- `collections/<collection_name>/`: Individual collection directories
  - version: current version of the dataset
  - `collection.json`: Collection metadata including title, description, DOI, version, and list of datasets
  - 'collection.doi': all versions reference 
  - 'collection_version.doi': current versions reference 
  - '<collection_name>_README.md' (optional)
  - '<collection_name>_README.pdf'
  - 'scripts/' sub directory which contains any scripts related to the most current version of the collection
  - 'archive/' sub directory which contains all files from all      - 'version.doi': current versions reference 
 versions of the collection
    - '<version>' sub directory which contains all files from all  versions of the collection
      - 'collection_version.doi': current versions reference 
      - `collection.json`: Collection metadata including title, description, DOI, version, and list of datasets




## Collection Metadata Schema
```json
{
 {
  "name": "pmdbs-bulk-rnaseq",
  "title": "PMDBS bulkRNAseq",
  "types": [
    "pmdbs-bulk-rnaseq"
  ],
  "versions": {
    "v1.0.0" : {
      "doi": null,
      "datasets": [
        "hardy-pmdbs-bulk-rnaseq",
        "lee-pmdbs-bulk-rnaseq-mfg",
        "wood-pmdbs-bulk-rnaseq",
        "cohort-pmdbs-bulk-rnaseq"
      ],
      "teams": [
        "cohort",
        "hardy",
        "jakobsson",
        "lee",
        "wood"
      ],
      "release": {
        "version": "v1.0.0",
        "cde_version" : "v3.0",
        "date": null
      },
    },
    "v1.1.0" : {
      "doi": null,
      "datasets": [
        "hardy-pmdbs-bulk-rnaseq",
        "lee-pmdbs-bulk-rnaseq-mfg",
        "wood-pmdbs-bulk-rnaseq",
        "cohort-pmdbs-bulk-rnaseq",
      ],
      "teams": [
        "cohort",
        "hardy",
        "jakobsson",
        "lee",
        "wood"
      ],
      "release": {
        "version": "v1.1.0",
        "cde_version" : "v3.2",
        "date": null
      }
    },
    "v1.2.0" : {
      "doi": null,
      "datasets": [
        "hardy-pmdbs-bulk-rnaseq",
        "lee-pmdbs-bulk-rnaseq-mfg",
        "wood-pmdbs-bulk-rnaseq",
        "cohort-pmdbs-bulk-rnaseq",
        "jakobsson-pmdbs-bulk-rnaseq"
      ],
      "teams": [
        "cohort",
        "hardy",
        "jakobsson",
        "lee",
        "wood"
      ],
      "release": {
        "version": "v1.2.0",
        "cde_version" : "v3.3",
        "date": null
      }
    }
  }
}
```



## collections
<collection-name>/
  datasets/<datset-name>


### Bucket Structure (Example)
asap-crn-pmdbs-sc-rnaseq-collection-v3/
    ├── hafler-pmdbs-sn-rnaseq-pfc
    │    ├── artifacts/
    │    ├── file_metadata/
    │    ├── metadata/
    │    │   ├── *.csv
    │    │   └── cde_version
    │    └── <workflow_name>/
    │        ├── <curated_outputs>/
    │        └── workflow_version
    ├── lee-pmdbs-sn-rnaseq
    ├── hardy-pmdbs-sn-rnaseq
    ├── scherzer-pmdbs-sn-rnaseq-mtg
    ├── jakobsson-pmdbs-sn-rnaseq
    ├── sulzer-pmdbs-sn-rnaseq
    └── asap-cohort-pmdbs-sc-rnaseq

### Curated Bucket Pathing
<curated-bucket>/
    ├── artifacts/
    ├── <raw_data>/
    ├── file_metadata/
    ├── metadata/
    │   └── release/<release_version>/*.csv, cde_version
    └── <workflow_name>/
        └── release/<release_version>/
            ├── <curated_outputs>/
            └── workflow_version



## versions
Collections versions are updated with Minor and Major releases when additional datasets are added, or the curation workflows are updated and curated data is modified.

- Release Version
- workflow Version
- Dataset Version
- CDE Version

