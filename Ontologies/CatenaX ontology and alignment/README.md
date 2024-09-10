To facilitate the reusage of EV battery passport semantic properties, we have taken the [Battery Pass](https://github.com/eclipse-tractusx/sldt-semantic-models/tree/main/io.catenax.battery.battery_pass) data model from CatenaX.

We have produced a direct alignment of the Battery Pass samm class from version 6.0.0. The files can be found [here](./samm%20version/).

However, <i>samm</i> is not an RDF standardized data structure and thus we could not integrate it with the Vocabulary Hub functionality we advertised. This lead to us producing an owl version of the Battery Pass class and properties. This has been done on the version 3.0.1 of the Battery Pass. The files can be found [here](./owl%20version/).
# SAMM CatenaX connection

To make the connection between the SAMM Battery Pass and the FEDeRATED digital twin product concept, we have employed the `rdfs:subClassOf` function. Thus we have produced the following semantic line:
```
urn:samm:io.catenax.battery.battery_pass:6.0.0#BatteryPass rdfs:subClassOf https://ontology.tno.nl/logistics/federated/DigitalTwin#Product
```

# RDF interpretation
The RDF interpretation has been achieved through manual conversion, by following the pseudocode algorithm:
1. For every bamm:Entity, create a owl:Class with the same name. Each owl:Class then has rdfs:label the value of the bamm:name and rdfs:comment the value of bamm:description.

Example:
```
    :BatteryCycleLifeEntity a bamm:Entity;
    bamm:name "BatteryCycleLifeEntity";
    bamm:properties (:cycleLifeTestCRate :cycleLifeTestDepthOfDischarge :expectedLifetime);
    bamm:preferredName "battery cycle life entity"@en;
    bamm:description "Entity to bundle the characterisitics describing the cycle life of a battery"@en.
```
Translates to:
```
    :BatteryCycleLife a owl:Class ;
    rdfs:label "BatteryCycleLifeEntity" ;
    rdfs:comment "Entity to bundle the characterisitics describing the cycle life of a battery"@en.

```

2. For each bamm:Entity with a field bamm:properties, create a distinct owl property for each of the properties inside the bamm:properties field
3. For each owl propertiy identified at step 2, determine if it is an owl:DatatypeProperty or a owl:ObjectProperty. This distinction is done by finding the corresponding bamm:Property, looking at its' bamm:characterstic and seeing if the characteristic points to a bamm-c:Measurement or a bamm:Entity. 
    
    3a. In case it points to a bamm-c:Measurement, the owl property is considered an owl:DatatypeProperty with the rdfs:range the bamm:dataType of the bamm-c:Measurement
    
    Example:

        :BatteryCycleLifeEntity a bamm:Entity;
        bamm:name "BatteryCycleLifeEntity";
        bamm:properties (:cycleLifeTestCRate :cycleLifeTestDepthOfDischarge :expectedLifetime);
        bamm:preferredName "battery cycle life entity"@en;
        bamm:description "Entity to bundle the characterisitics describing the cycle life of a battery"@en.

        :expectedLifetime a bamm:Property;
        bamm:name "expectedLifetime";
        bamm:preferredName "expected lifetime"@en;
        bamm:description "Expected battery lifetime expressed in cycles, 
         and reference test used is describing a regulatory requirement."@en;
        bamm:characteristic :ExpectedLifetime;
        bamm:exampleValue "456"^^xsd:decimal.

        :ExpectedLifetime a bamm-c:Measurement;
        bamm:name "ExpectedLifetime";
        bamm:preferredName "expected lifetime"@en;
        bamm:description "Expected battery lifetime expressed in cycles, and reference test used is describing a regulatory requirement."@en;
        bamm:dataType xsd:decimal;
        bamm-c:unit unit:piece.

    Translates to:

        :expectedLifetime a owl:DatatypeProperty ;
            rdfs:domain :BatteryCycleLife ;
            rdfs:range xsd:decimal ;
            rdfs:label "ExpectedLifetime" ;
            rdfs:comment "Expected battery lifetime expressed in cycles, and reference test used is describing a regulatory requirement."@en.


    3b. In case it points to a bamm:Entity, the owl property is considered a owl an owl:ObjectProperty with the rdfs:range the owl:Class coresponding to the bamm:Entity.
    Example:
    ```
    :ElectrochemicalPropertiesCharacteristic a bamm:Characteristic;
    bamm:name "ElectrochemicalPropertiesCharacteristic";
    bamm:preferredName "electrochemical properties characteristic"@en;
    bamm:description "Electrochemical characteristics to describe a battery"@en;
    bamm:dataType :ElectrochemicalPropertiesEntity.
    ```
    Translates to:
    ```
    :ElectrochemicalProperties a owl:ObjectProperty;
    rdfs:domain :BatteryPass ;
    rdfs:range :ElectrochemicalProperties ;
    rdfs:label "ElectrochemicalPropertiesCharacteristic";
    rdfs:comment "Electrochemical characteristics to describe a battery"@en .
    ```

Additionally, a helping ontology developed by TNO is also provided, so all the fields of the attribute longlist document from [Battery Pass](https://thebatterypass.eu/) are covered.