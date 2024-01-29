This repository is part of the [Datapipe research project](https://www.tudelft.nl/tbm/onderzoek/projecten/datapipe-project), which aims to help the Customs Administration of the Netherlands and the Ministry of Infrastructure and Water Management of the Netherlands to be better equipped to meet their responsibilities in the context of the circular economy. The project will deliver a diagnostic problem analysis report, blueprint for piloting, and recommendations.
# Ontologies included
All the industry-specific ontologies are aligned to the FEDeRATED upper ontology. More resources on the FEDeRATED semantic model can be found at [FEDeRATED](https://github.com/Federated-BDI/FEDeRATED-Semantic-Model) and about the [FEDeRATED project](https://federatedplatforms.eu/) in general.
## Automotive industry
The ontology used for automobiles has been developed by EDM Council, and can be found [here](https://github.com/edmcouncil/auto/tree/master).
## Electric batteries industry
The ontology used for electric batteries is an RDF interpretation of the [CatenaX Battery Pass 3.0.1 Aspect Meta Model](https://github.com/eclipse-tractusx/sldt-semantic-models/tree/main/io.catenax.battery.battery_pass/3.0.1).
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
## Electronics
The ontology used for electronics has been developed by Anelia Kurteva at TU Delft and can be found [here](https://github.com/RePlanIT/Ontology).

## Demo environment to test semantic interoperability
In the Datapipe research project we have set up a network of [FEDeRATED nodes](https://github.com/Federated-BDI/Docker-BDI-Node/tree/main) to highlight how message models created from semantic models interconnected through the upper ontology and the industry-specific alignments can be transmitted between multiple parties in a decentralized manner.

We have constructed the message models using [Semantic Treehouse](https://service-registry.federatedplatforms.eu/#/).

## More to come - Textiles and LCA