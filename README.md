# cloud-collections

Source-of-truth archive for ASAP CRN Cloud _Collections_. A collection is a versioned, DOI-backed grouping of datasets sharing a common tissue type and assay modality. Collections are published as immutable VWB Data Collections with version-specific GCS buckets for curated data access.

This repository is automatically managed by the [cloud-orchestration](https://github.com/ASAP-CRN/cloud-orchestration) system. Manual changes should be avoided.

## Collections (as of v4.0.0)

| Collection | Name | Description |
|---|---|---|
| `pmdbs-sc-rnaseq` | PMDBS scRNAseq | Post-mortem donor brain single-cell/single-nucleus RNA-seq |
| `pmdbs-bulk-rnaseq` | PMDBS bulkRNAseq | Post-mortem donor brain bulk RNA-seq |
| `pmdbs-spatial` | PMDBS Spatial Transcriptomics | Post-mortem donor brain spatial transcriptomics |
| `mouse-sc-rnaseq` | Mouse scRNAseq | Mouse single-cell/single-nucleus RNA-seq |
| `mouse-spatial` | Mouse Spatial Transcriptomics | Mouse spatial transcriptomics |

Collections with an ASAP CRN analysis workflow include CRN-curated analysis artifacts in addition to team-contributed artifacts. "Other" (uncurated) datasets are exposed via unversioned Data Collections that reference each dataset's curated bucket directly.

## Structure

```
collections.json                           # Master index of all collections
collections/<collection-name>/
├── collection.json                        # Canonical metadata (see schema below)
├── scripts/                               # Scripts for current version
└── archive/                               # Immutable snapshots of past versions
    └── <version>/
        └── collection.json                # Version-specific metadata snapshot
```

## Collection Metadata Schema

```json
{
  "name": "pmdbs-sc-rnaseq",
  "title": "PMDBS scRNAseq",
  "types": ["pmdbs-sc-rnaseq"],
  "versions": {
    "v1.0.0": {
      "version": "v1.0.0",
      "doi": "10.5281/zenodo.xxxxxxx",
      "datasets": [
        "hafler-pmdbs-sn-rnaseq-pfc",
        "lee-pmdbs-sn-rnaseq",
        "jakobsson-pmdbs-sn-rnaseq",
        "scherzer-pmdbs-sn-rnaseq-mtg",
        "cohort-pmdbs-sc-rnaseq"
      ],
      "teams": ["cohort", "hafler", "jakobsson", "lee", "scherzer"],
      "release": {
        "version": "v1.0.0",
        "cde_version": "v2.1",
        "date": null
      }
    },
    "v3.1.0": {
      "version": "v3.1.0",
      "doi": "10.5281/zenodo.xxxxxxx",
      "datasets": [
        "hafler-pmdbs-sn-rnaseq-pfc",
        "lee-pmdbs-sn-rnaseq",
        "jakobsson-pmdbs-sn-rnaseq",
        "scherzer-pmdbs-sn-rnaseq-mtg",
        "hardy-pmdbs-sn-rnaseq",
        "sulzer-pmdbs-sn-rnaseq",
        "cohort-pmdbs-sc-rnaseq"
      ],
      "teams": ["cohort", "hafler", "hardy", "jakobsson", "lee", "scherzer", "sulzer"],
      "release": {
        "version": "v4.0.0",
        "cde_version": "v3.3",
        "date": null
      }
    }
  }
}
```

### Key Fields

- **`versions`**: Map of collection version → snapshot of datasets, teams, and the release/CDE version it was published with
- **`datasets`**: All datasets included in this collection version
- **`release.cde_version`**: The Common Data Elements schema applied to all datasets in this collection version

## Versioning Scheme

Collection versions follow `vMAJOR.MINOR.PATCH` and are updated when:

- **Minor/Major** — datasets are added or curation workflows are updated (regenerating curated data)
- **Patch** — metadata corrections or DOI updates

Each collection version also tracks the associated **Release Version**, **CDE Version**, and per-dataset **Dataset Version**.

## VWB Data Collections and GCS Bucket Structure

Each versioned collection is exposed in VWB as a Data Collection backed by an **immutable** versioned GCS bucket:

```
gs://asap-crn-<collection-name>-collection-<version>/
├── <dataset-name>/
│   ├── artifacts/
│   ├── file_metadata/
│   ├── metadata/
│   │   ├── *.csv
│   │   └── cde_version
│   └── <workflow_name>/
│       ├── <curated_outputs>/
│       └── workflow_version
└── ...
```

Individual dataset curated buckets (`gs://asap-curated-<dataset-name>/`) are **mutable** and hold outputs for all released versions organized under `release/<release_version>/`. Collection buckets hold the frozen snapshot for a specific collection version.

## Release Process

1. Datasets are scoped and associated with the release
2. Collection versions are bumped to include new/updated datasets
3. DOIs are generated via Zenodo for new collection versions
4. `collections.json` index and per-collection `collection.json` are updated
5. Version snapshots are written to `archive/`
6. VWB Data Collections are provisioned with the new versioned GCS bucket

## Management

For collection submissions or updates, use the orchestration system or contact the ASAP CRN team.
