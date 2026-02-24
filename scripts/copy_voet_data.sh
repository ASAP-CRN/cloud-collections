

check_bucket_exists() {
  local BUCKET_NAME="$1"
  
  if gcloud storage buckets describe "$BUCKET_NAME" > /dev/null 2>&1; then
    echo "Bucket $BUCKET_NAME exists."
  else
    echo "Bucket $BUCKET_NAME does not exist or is inaccessible."
  fi
}

# Example usage:
# check_bucket_exists "gs://your-bucket-name"

# 