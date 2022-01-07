The goal of this exercise was to create google cloud function which:
1. is triggered by .csv file upload to monitored bucket
2. create a table in BQ dataset
3. load csv file data into created BQ table

The additional assumptions:
1. column names are present in the 1st row of the .csv file
2. file name can have only one dot
3. the .csv file can have any number of columns of any types
4. upload of the .csv file with the same name as already existing one, cause overwriting of the BQ table


The command necessary to run the code:
1. authenticate:
gcloud auth application-default login
2. deploy function:
gcloud functions deploy ex1_trigger --runtime python39 --trigger-resource ex1_alterdata_pd  --trigger-event google.storage.object.finalize --region europe-west1