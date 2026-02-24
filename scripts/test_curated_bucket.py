# %% 
# 23 Feb 2026
# Andy Henrie

#%%
import pandas as pd
from pathlib import Path
import os, sys

import subprocess

%load_ext autoreload
%autoreload 2


PROJECT="dnastack-asap-parkinsons"
REGION="us-central1"



# %%
# HELPER FUNCTIONS

def set_gcloud_config()->bool:
    cmd = f"gcloud config set storage/parallel_composite_upload_enabled False "

    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if result.returncode == 0:
        return True
    else
        return False



def gcloud_bucket_exists(bucket_uri:str) -> bool:
    """
    checks for the existance of a bucket
    """    
    cmd = f"gcloud storage buckets describe {bucket_uri}  --billing-project={PROJECT} "

    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    found = False
    if result.returncode == 0:
        found = True
        print(f"Bucket {bucket_uri} found")

    return found


# %%


def gcloud_create_bucket(bucket_uri:str):
    """
    creates a bucket
    """

    # first check if bucket exists
    # if gcloud_bucket_exists(bucket_name):
    #     print(f"Bucket {bucket_name} already exists")
    #     return True
    # else:
    #     print(f"Bucket {bucket_name} does not exist, creating now")

    # Create a bucket in us-central1
    cmd1 = f"""gcloud storage buckets create "{bucket_uri}" --project="{PROJECT}" --location="{REGION}" """

    print(cmd1)
    # Add permissions to bucket
    cmd2 = f"""gcloud storage buckets add-iam-policy-binding "{bucket_uri}" \
    --member="group:asap-cloud-readers@verily-bvdp.com" \
    --role="roles/storage.objectViewer" \
    --project="{PROJECT}" """
    cmd3 = f"""gcloud storage buckets add-iam-policy-binding "{bucket_uri}" \
    --member="group:asap-dti@dnastack.com" \
    --role="roles/storage.Admin" \
    --project="{PROJECT}" """


    print(cmd2)
    print(cmd3)

    # result = subprocess.run(cmd1, shell=True, capture_output=True, text=True)
    # if result.returncode == 0:
    #     print(f"Step 1: Bucket {bucket_name} created")
    # else:
    #     print(f"Step 1: Bucket {bucket_name} not created")
    #     return result

    result = subprocess.run(cmd2, shell=True, capture_output=True, text=True)
    if result.returncode == 0:
        print(f"Step 2: Bucket {bucket_uri} add-iam-policy-binding 1 applied")
    else:
        print(f"Step 2: Bucket {bucket_uri} add-iam-policy-binding 1 apply failed")
        return result

    result = subprocess.run(cmd3, shell=True, capture_output=True, text=True)
    if result.returncode == 0:
        print(f"Step 3: Bucket {bucket_uri} add-iam-policy-binding 2 applied")
    else:
        print(f"Step 3: Bucket {bucket_uri} add-iam-policy-binding 2 apply  failed")
        return result

    print(f"FINAL: Bucket {bucket_uri} created and configured")
    return True


# %%
def gcloud_copy_file(source_uri:str, destination_uri:str) -> bool:
    """
    copies a file
    """
    set_gcloud_config()

    cmd = f"gcloud storage rsync --billing-project={PROJECT} {source_uri} {destination_uri}"
    print(cmd)
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if result.returncode == 0:
        print(f"File {source_uri} copied to {destination_uri}")
        return True
    else:
        output = f"ERROR: File {source_uri} not copied to {destination_uri})"
        output += f"| result: {result.stdout})"
        output += f", returncode: {result.returncode}"
        print(output)
        return False

# %%
def gcloud_copy_path(source_path:str, destination_path:str) -> bool:
    """
    copies a file
    """

    project = "dnastack-asap-parkinsons"
    cmd = f"gcloud storage rsync --recursive --billing-project={PROJECT} {source_path} {destination_path}"
    print(cmd)
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if result.returncode == 0:
        print(f"File {source_path} copied to {destination_path}")
        return True
    else:
        output = f"ERROR: File {source_path} not copied to {destination_path})"
        output += f"| result: {result.stdout})"
        output += f", returncode: {result.returncode}"
        print(output)
        return False



# %%
repo_root = Path.cwd().parents[1]
datasets_path = repo_root / "datasets"


test_collection = "pmdbs-sc-rnaseq"
collection_version = "v1"

latest_release = "v4.0.0"
# %%
bucket_name = f"asap-crn-{test_collection}-collection-{collection_version}"

collection_datasets = [
    "asap-curated-cohort-pmdbs-sc-rnaseq", 
    "asap-curated-team-hafler-pmdbs-sn-rnaseq-pfc", 
    "asap-curated-team-lee-pmdbs-sn-rnaseq", 
    "asap-curated-team-jakobsson-pmdbs-sn-rnaseq", 
    "asap-curated-team-scherzer-pmdbs-sn-rnaseq-mtg", 
    "asap-curated-team-hardy-pmdbs-sn-rnaseq", 
]

# %%


collection_bucket = f"gs://{bucket_name}"
if not gcloud_bucket_exists(collection_bucket):
    result = gcloud_create_bucket(destination_bucket)
    if result != True:
        print(f"ERROR: Bucket {destination_bucket} not created")
        print(f"  result: {result.stdout}")
        print(f"  returncode: {result.returncode}")

# if not gcloud_bucket_exists(destination_bucket):
#     gcloud_create_bucket(destination_bucket)

workflow_name = "pmdbs_sc_rnaseq"
# %%
for idx, ds_name in enumerate(collection_datasets):
    print(f"Processing {ds_name}")

    source_bucket = f"gs://{ds_name}"
    

    # copy artifacts
    
    source_uri = f"{source_bucket}/artifacts"
    destination_uri = f"{collection_bucket}/{ds_name}/artifacts"
    if not gcloud_copy_path(source_uri, destination_uri):
        print("ERROR copying artifacts for {ds_name}")

    # copy file_metadata
    source_uri = f"{source_bucket}/file_metadata"
    destination_uri = f"{collection_bucket}/{ds_name}/file_metadata"
    if not gcloud_copy_path(source_uri, destination_uri):
        print("ERROR copying file_metadata for {ds_name}")


    # copy metadata
    source_uri = f"{source_bucket}/metadata"
    destination_uri = f"{collection_bucket}/{ds_name}/metadata"
    if not gcloud_copy_path(source_uri, destination_uri):
        print("ERROR copying metadata for {ds_name}")
    # copy the current release to metadata/?


    # copy curated data
    # preprocess
    source_uri = f"{source_bucket}/{workflow_name}/preprocess/"
    destination_uri = f"{collection_bucket}/{ds_name}/{workflow_name}/preprocess/"
    if not gcloud_copy_path(source_uri, destination_uri):
        print("ERROR copying preprocess artifacts for {ds_name}")
    # cohort_analysis
    source_uri = f"{source_bucket}/{workflow_name}/cohort_analysis/"
    destination_uri = f"{collection_bucket}/{ds_name}/{workflow_name}/cohort_analysis/"
    if not gcloud_copy_path(source_uri, destination_uri):
        print("ERROR copying cohort_analysis artifacts for {ds_name}")





    copied_files = []
    failed_files = []
    for i, row in rows.iterrows():
        source_uri = row["gs_uri"]
        destination_uri = row["destination_uri"]
        if gcloud_copy_file(source_uri, destination_uri):
            copied_files.append(destination_uri)
        else:
            failed_files.append(destination_uri)

    print(f"Summary for {ds_name}:")
    print(f"  {len(copied_files)} files copied")
    print(f"  {len(failed_files)} files failed")
    print(f"  Copied files written to {split_path / f'{ds_name}_copied_files.txt'}")
    print(f"  Failed files written to {split_path / f'{ds_name}_failed_files.txt'}")

    # write a log of the files copied
    with open(split_path / f"{ds_name}_copied_files.txt", "w") as f:
        for file in copied_files:
            f.write(f"{file}\n")
    with open(split_path / f"{ds_name}_failed_files.txt", "w") as f:
        for file in failed_files:
            f.write(f"{file}\n")

    # # %%
    # # Copy METADATA
    # for idx, ds_name in enumerate(datasets):
    print(f"Processing {ds_name}")
    rows = export_plan[export_plan["ds_name"] == ds_name]
    dtype = datasets[idx]

    source_path = split_path / f"{ds_name}/metadata/cde/{intake_schema_version}"

    destination_bucket = f"asap-raw-team-{ds_name}"
    destination_path = f"gs://{destination_bucket}/metadata/cde/{intake_schema_version}"


    # copy each path
    copied_files = []
    failed_files = []
    if gcloud_copy_path(source_path, destination_path):
        copied_files.append(destination_path)
    else:
        failed_files.append(destination_path)

    print(f"Summary for {ds_name}:")
    print(f"  {len(copied_files)} files copied")
    print(f"  {len(failed_files)} files failed")
    print(f"  Copied files written to {split_path / f'{ds_name}_copied_metadata.txt'}")
    print(f"  Failed files written to {split_path / f'{ds_name}_failed_metadata.txt'}")

    # write a log of the files copied
    with open(split_path / f"{ds_name}_copied_metadata.txt", "w") as f:
        for file in copied_files:
            f.write(f"{file}\n")
    with open(split_path / f"{ds_name}_failed_metadata.txt", "w") as f:
        for file in failed_files:
            f.write(f"{file}\n")

    source_path = split_path / f"{ds_name}/refs"

    destination_path = f"gs://{destination_bucket}/refs"

    # # copy each path
    # copied_files = []
    # failed_files = []
    # if gcloud_copy_path(source_path, destination_path):
    #     copied_files.append(destination_path)
    # else:
    #     failed_files.append(destination_path)

    # print(f"Summary for {ds_name}:")
    # print(f"  {len(copied_files)} files copied")
    # print(f"  {len(failed_files)} files failed")
    # print(f"  Copied files written to {split_path / f'{ds_name}_copied_refs.txt'}")
    # print(f"  Failed files written to {split_path / f'{ds_name}_failed_refs.txt'}")

    # # write a log of the files copied
    # with open(split_path / f"{ds_name}_copied_refs.txt", "w") as f:
    #     for file in copied_files:
    #         f.write(f"{file}\n")
    # with open(split_path / f"{ds_name}_failed_refs.txt", "w") as f:
    #     for file in failed_files:
    #         f.write(f"{file}\n")


# %%
