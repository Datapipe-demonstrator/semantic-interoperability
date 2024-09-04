This repository folder contains the application profile, example data and queries that correlate to the data fields included by the UN Recommendation 46.

Since UNR46 is structured based on topics (e.g., Product-related information, Process-related information etc.), we have created a separate markdown file with the query and its' explanation, for each topic.

As not all data fields could be mapped 1 to 1 to the semantic solution, we have created an Application Profile as an interpretation of the existent properties of the ontologies included in the repository. For example, in FEDeRATED an external identifier can refer to various means of identification, which induces us to relate the batch identification and trade unit values to this external identfier property.

# Application profile: 


        @prefix federatedDT: <https://ontology.tno.nl/logistics/federated/DigitalTwin#> .
        @prefix federatedAR: <https://ontology.tno.nl/logistics/federated/ActorRoles#> .
        @prefix federatedEV: <https://ontology.tno.nl/logistics/federated/Event#>
        @prefix schema: <http://schema.org/> .
        @prefix ex: <https://own-data-shape#>
        
        # PRODUCT IDENTIFICATION
        exAP:batchID a owl:DatatypeProperty ;
            owl:equivalentProperty federatedDT:externalIdetifier .

        exAP:tradeUnit a owl:DatatypeProperty ;
            owl:equivalentProperty federatedDT:externalIdetifier .

        # QUALITY
        exAP:characteristics a owl:DatatypeProperty ;
            owl:equivalentProperty federatedDT:goodsDescription .

        exAP:inspections a owl:DatatypeProperty ;
            owl:equivalentProperty federatedDT:goodsDescription .

        # PROCESS RELATED INFORMATION
        exAP:involvesInputVolume a owl:DatatypeProperty ;
            owl:equivalentProperty federatedEV:involves ;
            rdfs:range xsd:decimal .

        exAP:involvesOutputVolume a owl:DatatypeProperty ;
            owl:equivalentProperty federatedEV:involves ;
            rdfs:range xsd:decimal .

        exAP:equipment a owl:Class ;
            owl:equivalentClass federatedDT:PhysicalObject .

        exAP:owner a owl:Class ;
            owl:subClassOf federatedAR:ActorRoles .

        exAP:hasDocument a owl:ObjectProperty ;
            rdfs:domain catenax:BatteryPass ;
            rdfs:range federatedDT:document .

        exAP:documentName a owl:DatatypeProperty ;
            owl:equivalentProperty federatedDT:documentID .

        exAP:batteryMaterial a owl:ObjectProperty ; 
                rdfs:range catenax:Material ;
                rdfs:domain catenax:BatteryPass .
        