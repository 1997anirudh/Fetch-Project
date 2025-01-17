Step 1 - Download the file 
Step 2 - Make sure to have docker installed in the system where the test is going to be performed. 
Type the below command in Terminal
docker -- version 
Step 3 - Run the following commands from where the folder is installed 
docker build -t receipt-processor-api .
Step 4 -  Run the following commands from where the folder is installed 
docker run -p 8080:8080 receipt-processor-api
Step 5 - curl http://127.0.0.1:8080/

