# _Please note: The queries included in this document are consistent with the FEDeRATED, RePlanIT and CatenaX TNO interpretation ontologies as of 6th of December 2023._

### The queries mentioned below may be run on a triple store after uploading the example data given in the file "Example-Triples.ttl"

## Competency question 1:
### _What is the expected lifetime of the switch of the car window with identifier “CW- 01” from this moment?_

### SPARQL Query:
```
PREFIX Event: <https://ontology.tno.nl/logistics/federated/Event#>
PREFIX DigitalTwin: <https://ontology.tno.nl/logistics/federated/DigitalTwin#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX replanit: <http://www.semanticweb.org/RePlanIT/> 

SELECT (?hasExpectedLifetime - ?hasCurrentLifetime AS ?expectedLifetimeLeft)
WHERE {
    ?carWindow a DigitalTwin:Product .
    ?carWindow DigitalTwin:DigitalTwinID “CW-01” .
    ?associationEvent a Event:Event .
    ?associationEvent Event:involvesDigitalTwin
    ?carWindow, ?controlSystem .
    ?associationEvent Event:involvesDigitalTwin
    ?controlSystem ?switch .
    ?switch replanit:hasExpectedLifetime ?hasExpectedLifetime
    ?switch replanit:hasCurrentLifetime ?hasCurrentLifetime
}
```

## Competency question 2:
### _What is the weight of the plastic casing of the car window with identifier “CW- 01”?_

### SPARQL Query:

```
PREFIX Event: <https://ontology.tno.nl/logistics/federated/Event#>
PREFIX DigitalTwin: <https://ontology.tno.nl/logistics/federated/DigitalTwin#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT ?weight 
WHERE {
    ?carWindow a DigitalTwin:Product .
    ?carWindow DigitalTwin:DigitalTwinID “CW-01” .
    ?associationEvent a Event:Event .
    ?associationEvent Event:involvesDigitalTwin ?carWindow, ?plasticCasing .
    ?plasticCasing DigitalTwin:netMass ?weight .
}
```

## Competency question 3:
### _What is the state of health of the battery of the electric vehicle with VIN "fe2a25e1-e5a1-4ed5-b555-4c4bb16dc34e"_

### SPARQL Query:

```
PREFIX Event: <https://ontology.tno.nl/logistics/federated/Event#>
PREFIX DigitalTwin: <https://ontology.tno.nl/logistics/federated/DigitalTwin#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX auto-vc: <https://spec.edmcouncil.org/auto/ontology/VC/VehicleCore/> 
PREFIX catenax: <https://ontology.tno.nl/catenaxInterpretation#> 

SELECT ?stateOfHealth 
WHERE {
    ?car a auto-vc:PassengerCar .
    ?car auto-vc:vehicleIdentificationNumber ?VIN .
    ?assemblyEvent a Event:Event .
    ?assemblyEvent Event:involvesDigitalTwin ?car, ?battery .
    ?battery a catenax:BatteryPass .
    ?battery catenax:stateOfHealth ?stateOfHealth .
    FILTER(regex(?VIN, "fe2a25e1-e5a1-4ed5-b555-4c4bb16dc34e"))
}
```