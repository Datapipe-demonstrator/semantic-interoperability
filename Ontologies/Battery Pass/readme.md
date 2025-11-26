# Battery Pass example

## Customize Battery Pass
To properly test the data communication, generate a unique identifier for your battery pass by running the unique identifier python script [BatteryPassUnique.py](./BatteryPassUnique.py). It generates a `.json` file with the same structure as the `BatteryPassDemo.json` but with the `identifiaction/idDmc` value as the unique identifier.
```bash
python BatteryPassUnique.py
```

## Posting a new Battery Pass

Call POST endpoint `https://node1-event-api.datapipe.digital-passport.org/api/events` with 
- Headers: 
    1. Key:`Event-Type`, Value: `Event-Type:devX-demo-batpas-static`
    2. Key:`Event-Destinations`, Value: `Event-Destinations:did:web:node2.datapipe.digital-passport.org` 
    3. Key `x-api-key`, Value: ask TNO for api key
- Body (text/plain): Unique [BatteryPass](./BatteryPassDemo.json) generated at previous step

## Query for metadata attributes filtered by pass identifier 
Edit the FILTER value for the pass identifier.

If you want to run example queries without posting your own data, you can replace the ?passIdentifier value in the FILTER clause with "jzk4Z"

Call POST endpoint `https://node2-event-api.datapipe.digital-passport.org/api/sparql` with body (text/plain):

```
select distinct ?passIdentifier ?lastModification ?status ?issueDate ?version ?economicOperatorId where { 
?s a <http://dpp.example.org/batt-pass#battpass> .
?s <http://example.org/battpass#identification> ?identification. 
?s <http://example.org/battpass#metadata> ?metadata. 
?identification <http://example.org/battpass#idDmc> ?passIdentifier. 
?metadata <http://example.org/battpass#lastModification> ?lastModification. 
?metadata <http://example.org/battpass#status> ?status.
?metadata <http://example.org/battpass#issueDate> ?issueDate.
?metadata <http://example.org/battpass#version> ?version.
?metadata <http://example.org/battpass#economicOperatorId> ?economicOperatorId.
FILTER(?passIdentifier = "#INSERT YOUR IDENTIFIER HERE#")} limit 100
```

# Dynamic data example

## Posting a dynamic data updates

Copy your unique identifier generated at step "Customize Battery Pass"

Call POST endpoint `https://node1-event-api.datapipe.digital-passport.org/api/events` with 
- Headers: 
    1. Key:`Event-Type`, Value: `june-dynamic`
    2. Key:`Event-Destinations`, Value: `O=Demo,L=Utrecht,C=NL` 
    3. Key: `x-api-key`, Value: ask TNO for api key
- Body (text/plain): [DynamicData](./updated-dynamicdata.json) with unique identifier

## Queries for self discharing rate and state of charge

### SoC, SoH, cell voltage, and cell temperature filtered by passport identifier
If you want to run example queries without posting your own data, you can replace the ?passIdentifier value in the FILTER clause with the value of the metadata.passportIdentifier from the [Dynamic data](./DynamicData.json) JSON file.

Call POST endpoint `https://demo-node2.k8s.basicdatasharinginfrastructure.net/api/sparql` with body (text/plain):

```
SELECT DISTINCT ?idDmc ?passIdentifier ?lastModification ?predecessor ?status ?SoC ?selfDischargingRate ?SoH ?cellVoltage ?cellTemperature
WHERE {
  ?s a <http://dpp.example.org/batt-pass#battpass_update> .
  ?s <http://example.org/battpass#idDmc> ?idDmc.
  ?s <http://example.org/battpass#metadata> ?metadata.
  ?metadata <http://example.org/battpass#passportIdentifier> ?passIdentifier.
  ?metadata <http://example.org/battpass#lastModification> ?lastModification.
  ?metadata <http://example.org/battpass#predecessor> ?predecessor.
  ?metadata <http://example.org/battpass#status> ?status.
  ?s <http://example.org/battpass#dynamic> ?dynamicUpdate.
  ?dynamicUpdate <http://example.org/battpass#stateOfCharge> ?SoC.
  ?dynamicUpdate <http://example.org/battpass#stateOfHealth> ?SoH.
  ?dynamicUpdate <http://example.org/battpass#cellVoltage> ?cellVoltage.
  ?dynamicUpdate <http://example.org/battpass#cellTemperature> ?cellTemperature.
  ?dynamicUpdate <http://example.org/battpass#selfDischargingRate> ?selfDischargingRate.
  # choose which identification to use, ?passIdentifier or ?idDmc
  FILTER(?idDmc = "INSERT HERE YOUR IDDMC")
}
LIMIT 100

```

### Latest SoC, SoH, cell voltage, and cell temperature per each battery
```
SELECT DISTINCT ?idDmc ?passIdentifier ?lastModification ?status ?SoC ?selfDischargingRate ?SoH ?cellVoltage ?cellTemperature
WHERE {
  ?s a <http://example.org/battpass#BattPassUpdate> .
  ?s <http://example.org/battpass#idDmc> ?idDmc .
  ?s <http://example.org/battpass#metadata> ?metadata .
  ?metadata <http://example.org/battpass#passportIdentifier> ?passIdentifier.
  ?metadata <http://example.org/battpass#lastModification> ?lastModification.
  ?metadata <http://example.org/battpass#status> ?status.
  ?metadata <http://example.org/battpass#predecessor> ?predecessor.
  ?s <http://example.org/battpass#dynamic> ?dynamicUpdate.
  ?dynamicUpdate <http://example.org/battpass#stateOfCharge> ?SoC.
  ?dynamicUpdate <http://example.org/battpass#stateOfHealth> ?SoH.
  ?dynamicUpdate <http://example.org/battpass#cellVoltage> ?cellVoltage.
  ?dynamicUpdate <http://example.org/battpass#cellTemperature> ?cellTemperature.
  ?dynamicUpdate <http://example.org/battpass#selfDischargingRate> ?selfDischargingRate.
}
LIMIT 100

```
