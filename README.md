# Steps to Run the Receipt Processor API in Docker

### Step 1: Download the file
Download the necessary file for the receipt processor API.

### Step 2: Ensure Docker is Installed
Make sure Docker is installed on the system where the test will be performed. You can check the Docker installation by running the following command in the Terminal:
```bash
docker --version
```

### Step 3: Run the following commands from where the folder is installed 
```bash
docker build -t receipt-processor-api .
```

### Step 4 -  Run the following commands from where the folder is installed 
```bash
docker run -p 8080:8080 receipt-processor-api
```
### Step 5 -

```bash
curl http://127.0.0.1:8080/
```

### Step 6 - Curl an example case to generate receipr_id

```bash
curl -X POST http://127.0.0.1:8080/receipts/process -H "Content-Type: application/json" -d '{
  "retailer": "M&M Corner Market",
  "purchaseDate": "2022-03-20",
  "purchaseTime": "14:33",
  "items": [
    {
      "shortDescription": "Gatorade",
      "price": "2.25"
    },
    {
      "shortDescription": "Gatorade",
      "price": "2.25"
    },
    {
      "shortDescription": "Gatorade",
      "price": "2.25"
    },
    {
      "shortDescription": "Gatorade",
      "price": "2.25"
    }
  ],
  "total": "9.00"
}'


``` 
