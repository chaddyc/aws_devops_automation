#!/usr/bin/env python

from collections import defaultdict
import boto3

#boto3.set_stream_logger('botocore', level='DEBUG') #uncomment this line to display error logs

session = boto3.Session(profile_name='default') #add your aws access name here

def image_sort(elem):
    return elem.get('CreationDate')
ec2_client = boto3.client('ec2')
# this will be a list of all images which have a creation date and have "word" in their name
# this list is sorted with the latest image first
images = [image for image in ec2_client.describe_images(Owners=["self"]).get('Images') if (image["CreationDate"] and "word" in image["Name"])] #replace 'word' with keyword in all your ami images
images.sort(key=image_sort, reverse=True)
# Keep the most recent 3 of each type, so we build a dictionary of images based on their name
image_dict = defaultdict(list)
for image in images:
    image_dict[image["Name"].split("202")[0]].append(image)
# we now have lists of images which we can loop over
for (image_name, image_list) in image_dict.items():
    print(f'Processing "{image_name}" images')
    # if there are only 3 or fewer images the below loop won't run at all
    for image in image_list[3:]:
        print(f'{image["CreationDate"]}: {image["Name"]} ({image["ImageId"]})')
        # a boto3 command to delect an image based on its name could go here
        ec2_client.deregister_image(ImageId=image["ImageId"]) #delete/deregister ami images, you can comment out this line to do a print test first
        ec2_conn.deregister_image('ami-xxxxxxx', delete_snapshot=True) #automatically delete snapshots from blockstore associated with a deleted ami image
