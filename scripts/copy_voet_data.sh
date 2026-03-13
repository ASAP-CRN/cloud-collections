

check_bucket_exists() {
  local BUCKET_NAME="$1"
  
  if gcloud storage buckets describe "$BUCKET_NAME" > /dev/null 2>&1; then
    echo "Bucket $BUCKET_NAME exists."
  else
    echo "Bucket $BUCKET_NAME does not exist or is inaccessible."
  fi
}



set_gcloud_config() {
  gcloud config set storage/parallel_composite_upload_enabled False
}




# Example usage:
# check_bucket_exists "gs://your-bucket-name"

# 
PROJECT="dnastack-asap-parkinsons"
REGION="us-central1"
DESTINATION_BUCKET="gs://asap-crn-pmdbs-sc-rnaseq-collection-v3"
SOURCE_BUCKET="gs://asap-curated-cohort-pmdbs-sc-rnaseq"


# To generate md5sum
gcloud config set storage/parallel_composite_upload_enabled False

# Create a bucket in us-central1
gcloud storage buckets create \
  --project="${PROJECT}" \
  --location="${REGION}" "${DESTINATION_BUCKET}"

# Add permissions to bucket
gcloud storage buckets add-iam-policy-binding "${DESTINATION_BUCKET}" \
  --member="group:asap-cloud-readers@verily-bvdp.com" \
  --role="roles/storage.objectViewer" \
  --project="${PROJECT}"

gcloud storage buckets add-iam-policy-binding "${DESTINATION_BUCKET}" \
  --member="group:asap-dti@dnastack.com" \
  --role="roles/storage.Admin" \
  --project="${PROJECT}"

# Copy files
gcloud storage cp \
  --recursive \
  "${SOURCE_BUCKET}"/path/to/folder \
  "${DESTINATION_BUCKET}"/path/to/folder \
  --billing-project="${PROJECT}"
 

# Rsync files - dry run (remove flag for real run)
gcloud storage rsync \
  --recursive \
  --dry-run \
  "${SOURCE_BUCKET}"/path/to/folder \
  "${DESTINATION_BUCKET}"/path/to/folder \
  --billing-project="${PROJECT}"