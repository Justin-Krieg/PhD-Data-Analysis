import os
from google.cloud import storage
""" 
Author: Justin Krieg
Year: 2023
Modification codes required to interface with the google cloud platform. Here files can be stored on a storage bucket and dynamically downloaded to the boot drive for stitching before the result is uploaded back to the storage drive. 
 """

Storage_bucket = "Name_of_Bucket"
storage_client = storage.Client()
bucket = storage_client.bucket(Storage_bucket)

# Download files
for img in img_list_path:
    if not os.path.exists(img_list_path[img]):
        blob = bucket.blob(img_list[img])
        blob.download_to_filename(img_list_path[img])

# Upload the converted file
blob_upload = bucket.blob(f"{name_list}.stitched.ome.tiff")
blob_upload.upload_from_filename(name_list_Stitched)
for img in img_list_path:
    os.remove(img_list_path[img])
os.remove(name_list_Stitched)
