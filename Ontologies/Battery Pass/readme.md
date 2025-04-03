# Battery Pass example

## Customize Battery Pass
To properly test the data communication, generate a unique identifier for your battery pass by running the unique identifier python script [BatteryPassUnique.py](./BatteryPassUnique.py). It generates a `.json` file with the same structure as the `BatteryPassDemo.json` but with the `identifiaction/idDmc` value as the unique identifier.
```bash
python BatteryPassUnique.py
```

## Posting a new Battery Pass

Call POST endpoint `https://demo-node1.k8s.basicdatasharinginfrastructure.net/api/events` with 
- Headers: 
    1. Key:`Event-Type`, Value: `demo-final-battpass`
    2. Key:`Event-Destinations`, Value: `O=Demo,L=Utrecht,C=NL` body (text/plain):
- Body: Unique [BatteryPass](./BatteryPassDemo.json) generated at previous step

## Query for metadata attributes filtered by pass identifier 
Edit the FILTER value for the pass identifier.

If you want to run example queries without posting your own data, you can replace the ?passIdentifier value in the FILTER clause with "jzk4Z"

Call POST endpoint `https://demo-node2.k8s.basicdatasharinginfrastructure.net/api/sparql` with body (text/plain):

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

Call POST endpoint `https://demo-node1.k8s.basicdatasharinginfrastructure.net/api/events` with 
- Headers: 
    1. Key:`Event-Type`, Value: `dynamic-batpass-v1`
    2. Key:`Event-Destinations`, Value: `O=Demo,L=Utrecht,C=NL` body (text/plain):
- Body: [DynamicData](./DynamicData.json) with unique identifier

## Queries for self discharing rate and state of charge

### SoC and SDC filtered by passport identifier
If you want to run example queries without posting your own data, you can replace the ?passIdentifier value in the FILTER clause with "jzk4Z"

Call POST endpoint `https://demo-node2.k8s.basicdatasharinginfrastructure.net/api/sparql` with body (text/plain):

```
SELECT DISTINCT ?passIdentifier ?lastModification ?status ?SoC ?selfDischargingRate ?economicOperatorId
WHERE {
  ?s a <http://dpp.example.org/batt-pass#battpass_update> .
  ?s <http://example.org/battpass#metadata> ?metadata.
  ?metadata <http://example.org/battpass#passportIdentifier> ?passIdentifier.
  ?metadata <http://example.org/battpass#lastModification> ?lastModification.
  ?metadata <http://example.org/battpass#status> ?status.
  ?metadata <http://example.org/battpass#economicOperatorId> ?economicOperatorId .
  ?s <http://example.org/battpass#dynamic> ?dynamicUpdate.
  ?dynamicUpdate <http://example.org/battpass#stateOfCharge> ?SoC.
  ?dynamicUpdate <http://example.org/battpass#selfDischargingRate> ?selfDischargingRate.
  FILTER(?passIdentifier = "#INSERT YOUR IDENTIFIER HERE#")
}
LIMIT 100

```

### Latest SoC and SDC per each battery
```
SELECT DISTINCT ?passIdentifier ?lastModification ?status ?SoC ?selfDischargingRate
WHERE {
  ?s a <http://dpp.example.org/batt-pass#battpass_update> .
  ?s <http://example.org/battpass#metadata> ?metadata.
  ?metadata <http://example.org/battpass#passportIdentifier> ?passIdentifier.
  ?metadata <http://example.org/battpass#lastModification> ?lastModification.
  ?metadata <http://example.org/battpass#status> ?status.
  ?metadata <http://example.org/battpass#economicOperatorId> ?economicOperatorId .
  ?s <http://example.org/battpass#dynamic> ?dynamicUpdate.
  ?dynamicUpdate <http://example.org/battpass#stateOfCharge> ?SoC.
  ?dynamicUpdate <http://example.org/battpass#selfDischargingRate> ?selfDischargingRate.

  # Restrict to the latest modification timestamp
  FILTER(?lastModification = ?latestModification)
  
  # Subquery to get the latest timestamp per passIdentifier
  {
    SELECT ?passIdentifier (MAX(?lastModification) AS ?latestModification)
    WHERE {
      ?metadata <http://example.org/battpass#passportIdentifier> ?passIdentifier.
      ?metadata <http://example.org/battpass#lastModification> ?lastModification.
    }
    GROUP BY ?passIdentifier
  }
}
LIMIT 100

```
