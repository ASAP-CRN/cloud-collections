# %% 
# 23 Feb 2026
# Andy Henrie

#%%
import pandas as pd
from pathlib import Path
import os, sys

from crn_utils.util import (
    read_CDE,
    NULL,
    prep_table,
    read_meta_table,
    read_CDE_asap_ids,
    export_meta_tables,
    load_tables,
    write_version,
)

from crn_utils.asap_ids import *
from crn_utils.validate import validate_table, ReportCollector, process_table

from crn_utils.bucket_util import gcloud_ls, gcloud_ls_long

from crn_utils.constants import *
from crn_utils.doi import *

%load_ext autoreload
%autoreload 2

# %%
repo_root = Path.cwd().parents[1]
datasets_path = repo_root / "datasets"

# %%
# HELPER FUNCTIONS

import subprocess
PROJECT="dnastack-asap-parkinsons"
REGION="us-central1"

def gcloud_bucket_exists(bucket_name:str) -> bool:
    """
    checks for the existance of a bucket
    """    
    cmd = f"gcloud storage buckets describe gs://{bucket_name}  --billing-project={PROJECT} "

    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    found = False
    if result.returncode == 0:
        found = True
        print(f"Bucket {bucket_name} found")

    return found

bucket_exists = gcloud_bucket_exists("asap-raw-team-voet-pmdbs-sn-multimodal-parsebio")

# %%


def gcloud_create_bucket(bucket_name:str):
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
    cmd1 = f"""gcloud storage buckets create "gs://{bucket_name}" --project="{PROJECT}" --location="{REGION}" """

    print(cmd1)
    # Add permissions to bucket
    cmd2 = f"""gcloud storage buckets add-iam-policy-binding "gs://{bucket_name}" \
    --member="group:asap-cloud-readers@verily-bvdp.com" \
    --role="roles/storage.objectViewer" \
    --project="{PROJECT}" """
    cmd3 = f"""gcloud storage buckets add-iam-policy-binding "gs://{bucket_name}" \
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
        print(f"Step 2: Bucket {bucket_name} add-iam-policy-binding 1 applied")
    else:
        print(f"Step 2: Bucket {bucket_name} add-iam-policy-binding 1 apply failed")
        return result

    result = subprocess.run(cmd3, shell=True, capture_output=True, text=True)
    if result.returncode == 0:
        print(f"Step 3: Bucket {bucket_name} add-iam-policy-binding 2 applied")
    else:
        print(f"Step 3: Bucket {bucket_name} add-iam-policy-binding 2 apply  failed")
        return result

    print(f"FINAL: Bucket {bucket_name} created and configured")
    return True



# %%
def gcloud_copy_file(source_uri:str, destination_uri:str) -> bool:
    """
    copies a file
    """

    project = "dnastack-asap-parkinsons"
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


# %%
# %%
for idx, ds_name in enumerate(datasets):
    print(f"Processing {ds_name}")
    rows = export_plan[export_plan["ds_name"] == ds_name]
    dtype = datasets[idx]
    og_ds_name = rows["og_ds_name"].values[0]

    # check that the bucket we want exists
    source_bucket = f"asap-raw-team-{og_ds_name}"
    destination_bucket = f"asap-raw-team-{ds_name}"

    if not gcloud_bucket_exists(destination_bucket):
        result = gcloud_create_bucket(destination_bucket)
        if result != True:
            print(f"ERROR: Bucket {destination_bucket} not created")
            print(f"  result: {result.stdout}")
            print(f"  returncode: {result.returncode}")
            break

# %%
for idx, ds_name in enumerate(datasets):
    print(f"Processing {ds_name}")
    rows = export_plan[export_plan["ds_name"] == ds_name]
    dtype = datasets[idx]
    og_ds_name = rows["og_ds_name"].values[0]

    # check that the bucket we want exists
    source_bucket = f"asap-raw-team-{og_ds_name}"
    destination_bucket = f"asap-raw-team-{ds_name}"

    if not gcloud_bucket_exists(destination_bucket):
        gcloud_create_bucket(destination_bucket)

    # copy each file
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
