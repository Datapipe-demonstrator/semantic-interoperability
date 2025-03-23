# Battery Pass example

## Posting a new Battery Pass

Call endpoint `https://demo-node1.k8s.basicdatasharinginfrastructure.net/api/events` with 
- Headers: 
    1. Key:`Event-Type`, Value: `demo-final-battpass`
    2. Key:`Event-Destinations`, Value: `O=Demo,L=Utrecht,C=NL` body (text/plain):
- Body: [BatteryPass](./BatteryPassDemo.json)

## Query for identification attributes

Call endpoint `https://demo-node2.k8s.basicdatasharinginfrastructure.net/api/sparql` with body (text/plain):

```
select ?passIdentifier ?lastModification ?status where { ?s a <http://dpp.example.org/batt-pass#battpass> . ?s <http://example.org/battpass#metadata> ?metadata. ?metadata <http://example.org/battpass#passportIdentifier> ?passIdentifier. ?metadata <http://example.org/battpass#lastModification> ?lastModification. ?metadata <http://example.org/battpass#status> ?status} limit 100
```

# Dynamic data example

## Posting a dynamic data updates

Call endpoint `https://demo-node1.k8s.basicdatasharinginfrastructure.net/api/events` with 
- Headers: 
    1. Key:`Event-Type`, Value: `dynamic-batpass-v1`
    2. Key:`Event-Destinations`, Value: `O=Demo,L=Utrecht,C=NL` body (text/plain):
- Body: [DynamicData](./DynamicData.json)

## Queries for self discharing rate and state of charge

### All SoC and SDC

Call endpoint `https://demo-node2.k8s.basicdatasharinginfrastructure.net/api/sparql` with body (text/plain):

```
select distinct ?passIdentifier ?lastModification ?status ?SoC ?selfDischargingRate where { ?s a <http://dpp.example.org/batt-pass#battpass_update> . ?s <http://example.org/battpass#metadata> ?metadata. ?metadata <http://example.org/battpass#passportIdentifier> ?passIdentifier. ?metadata <http://example.org/battpass#lastModification> ?lastModification. ?metadata <http://example.org/battpass#status> ?status. ?s <http://example.org/battpass#dynamic> ?dynamicUpdate. ?dyanmicUpdate <http://example.org/battpass#stateOfCharge> ?SoC. ?dynamicUpdate <http://example.org/battpass#selfDischargingRate> ?selfDischargingRate} limit 100
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
