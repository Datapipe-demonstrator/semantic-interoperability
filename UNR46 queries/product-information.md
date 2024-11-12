# UNR46 to FEDeRATED conceptual mapping

| UNR46 category              | Data fields | FEDeRATED concept |
| :----------------: | :------: |:----: |
| Origin        |   Country / region   | schema.org/Country |
| Composition           |   Materials composition   | catenax-Material |
|| Product components| federated-involvesDigitalTwin  |
| Technical Specification    |  Materials Specifications   | federated-document ; exAP:documentName "Materials Specifications" |
| | Product Specifications | federated:document ; exAP:documentName "Product Specifications" |
| Quality | Characteristics | exAP:characteristics |
| | Insepctions | exAP:inspections |
| | Certificates/audit reports | federated:document ; exAP:documentName "Certificate" | 

# Example data

    ex:ProductCompositionEvent a federatedEV:Event ;
        federatedEV:involvesDigitalTwin ex:DemoBattery ;
        federatedEV:involvesDigitalTwin ex:CellPack ;
        federatedEV:involvesDigitalTwin ex:ThermalManagementSystem ;
        federatedEV:involvesLocation ex:Japan ;
    .
    ex:DemoBattery a catenax:BatteryPass ;
        exAP:batteryMaterial catenax:Ingredient1 ;
        exAP:batteryMaterial catenax:Ingredient2 ;
        exAP:hasDocument ex:MatSpec ;
        exAP:hasDocument ex:ProductSpec ;
        exAP:characteristics "Nickel Manganese Cobalt Battery" ;
        exAP:inspections "ISO6469" ;
        exAP:hasDocument ex:Certificate1 ex:Certificate2 
    .
    
    ex:CellPack a federatedDT:Goods 
    .
    ex:ThermalManagementSystem a federatedDT:Goods 
    .

    ex:Japan a schema:Country ;
        schema:name "Japan" ;
        schema:identifier "JP" 
    .

    catenax:Ingredient1 a catenax:Material ;
        catenax:materialName "Cobalt" ;
        catenax:materialWeight "40 kg" ;
        catenaxAddition:hasPreConsumerRecycledMaterialShare 0.85 ;
        catenaxAddition:hasPostConsumerRecycledMaterialShare 0.15
    .

    catenax:Ingredient2 a catenax:Material ;
        catenax:materialName "Lithium" ;
        catenax:materialWeight "5 kg" ;
        catenaxAddition:hasPreConsumerRecycledMaterialShare 0.90 ;
        catenaxAddition:hasPostConsumerRecycledMaterialShare 0.10
    .

    ex:MatSpec a federatedDT:Document ;
        exAP:documentName "Materials Specifications"
    .
    exAP:hasDocument ex:ProductSpec ;
        exAP:documentName "Product Specifications"
    .

    ex:Certificate1 a federatedDT:Document ;
        exAP:documentName "UN 38.3" .
    
    ex:Certificate2 a federatedDT:Document ;
        exAP:documentName "IEC 62660-1" .


The query that would request all the data fields of the product information category of UN Recommendation 46:

        SELECT ?origin, ?materialComposition, ?productComponents, ?materialsSpecifications, ?productSpecifications, ?characteristics, ?inspections, ?certificates
        WHERE {
            ?battery a catenax:BatteryPass .
            ?assemblyEvent a federatedEV:Event .
            ?assemblyEvent federatedEV:involvesDigitalTwin ?battery ?productComponents .
            ?assemblyEvent federatedEV:involvesLocation ?origin .
            ?battery exAP:batteryMaterial ?materialComposition .
            ?battery exAP:hasDocument ?certificates ?materialsSpecifications ?productSpecifications .
            ?materialsSpecifications exAP:documentName "Materials Specifications" .
            ?productSpecifications exAP:documentName "Product Specifications" .
            ?battery exAP:characteristics ?characteristics .
            ?battery exAP:inspections ?inspections .
        }