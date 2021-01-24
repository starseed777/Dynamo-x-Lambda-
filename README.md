This AWS lambda function is for parsing JSON files uploaded to a remote s3 bucket. 
The code gets triggered by an s3 create event (captured via cloudwatch). 
As this code gets triggered, it will parse the uploaded JSON file and turn the values into a dictionary (key/value pairs). 
Upon conversion it will then write automatically to our already created dynamoDB table.

line 1-4: starting off by importing the necessities for this code >> boto3 for aws compatiblity + json for when it comes to parsing of the uploaded JSON file

line 6-9: our lambda function begins, first starting by referencing our s3 bucket based off the captured cloudwatch event + our filename of the said uploaded item to our s3 bucket.

line 11-22: takes our previously refrenced bucket + key and parses the item, afterwards converts it into the dictionary structure and is added to our dynamoDB table.

line 25-26: the commented line is for cross verification that the right bucket + file are being refrenced 


