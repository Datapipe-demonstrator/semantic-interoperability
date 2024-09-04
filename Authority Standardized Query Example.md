## Ontologies considered

To easily identify the ontologies used in this example, we provide an abbreviation with the following explanation:
- [Example Application Profile](./Technical%20resources/Application%20Profile%20example.ttl) abbreviated as `exAP`
- [Catenax Interpretation](./Ontologies/CatenaX%20ontology%20and%20alignment/CatenaX%20TNO%20interpretation.ttl) abbreviated as `catenax`
- [Catenax Addition](./Ontologies/CatenaX%20ontology%20and%20alignment/CatenaX%20TNO%20Addition.ttl) abbreviated as `catenaxAddition`

## Data fields

<table>
  <thead>
    <tr>
      <th>Concept</th>
      <th>Property</th>
      <th>Data representation</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>EU Conformity Document</td>
      <td>BatteryPass hasDocument</td>
      <td>VC of certification document</td>
    </tr>
    <tr>
      <td>Manufacturer Identification</td>
      <td>BatteryPass manufacterIdentification</td>
      <td>VC of manufacturer</td>
    </tr>
    <tr>
      <td>Place of Manufacturing</td>
      <td>BatteryPass placeOfManufacturing</td>
      <td>GLN 13-digit number</td>
    </tr>
    <tr>
      <td>Battery Materials with their Recycle Shares</td>
      <td>BatteryPass batteryMaterial</td>
      <td>Decimal value</td>
    </tr>
    <tr>
      <td>Battery Energy Properties</td>
      <td>BatteryPass certifiedUBE, usableUBE, stateOfCertifiedEnergy</td>
      <td>integer (kWh)</td>
    </tr>
  </tbody>
</table>



## Data validation


## Standardized authorities' query

```
PREFIX exAP: <https://own-data-shape#>
PREFIX catenax: <https://ontology.tno.nl/catenaxInterpretation#>
PREFIX catenaxAddition: <https://ontology.tno.nl/catenax-addition#>
select distinct ?s ?EUconformity ?manufacturerIdentification ?manufacturingSiteIdentification ?nickelPostConsumer ?nickelPreConsumer ?cobaltPreConsumer ?cobaltPostConsumer ?lithiumPreConsumer ?lithiumPostConsumer ?leadPreConsumer ?leadPostConsumer ?stateCertifiedEnergy ?remainingUBE ?UBE where {
    ?s a catenax:BatteryPass .
    ?s exAP:hasDocument ?EUconformitydoc .
    ?EUconformitydoc exAP:documentName ?EUconformity .
    ?s exAP:manufacturerIdentification ?manufacturerIdentification .
    ?s exAP:placeOfManufacturing ?manufacturingSiteIdentification .
    ?s exAP:batteryMaterial ?nickel, ?cobalt, ?lithium, ?lead .
    ?nickel a catenax:Material ;
    	catenax:materialName "Nickel" ;
    	catenaxAddition:hasPreConsumerRecycledMaterialShare ?nickelPreConsumer ;
        catenaxAddition:hasPostConsumerRecycledMaterialShare ?nickelPostConsumer
    .
    ?cobalt a catenax:Material ;
    	catenax:materialName "Cobalt" ;
    	catenaxAddition:hasPreConsumerRecycledMaterialShare ?cobaltPreConsumer ;
        catenaxAddition:hasPostConsumerRecycledMaterialShare ?cobaltPostConsumer
    .
    ?lithium a catenax:Material ;
    	catenax:materialName "Lithium" ;
    	catenaxAddition:hasPreConsumerRecycledMaterialShare ?lithiumPreConsumer ;
        catenaxAddition:hasPostConsumerRecycledMaterialShare ?lithiumPostConsumer
    .
    ?lead a catenax:Material ;
    	catenax:materialName "Lead" ;
    	catenaxAddition:hasPreConsumerRecycledMaterialShare ?leadPreConsumer ;
        catenaxAddition:hasPostConsumerRecycledMaterialShare ?leadPostConsumer
    .
    ?s catenax:hasBatteryEnergyProperties ?batteryEnergyProperties .
    ?batteryEnergyProperties catenaxAddition:certifiedUsableBatteryEnergy ?UBE ;
    	catenaxAddition:remainingUsableBatteryEnergy ?remainingUBE ;
    	catenaxAddition:stateOfCertifiedEnergy ?stateCertifiedEnergy
    .
} 
``` 

## Piloting environment

To run the example data and queries, you can deploy GraphDB.
```
docker run -p 7200:7200 -t ontotext/graphdb:10.6.4
```
Afterwards, create your repository and upload the ontologies and example data:
- [FEDeRATED upper ontology](https://github.com/federatedplatforms/FEDeRATED-Semantic-Model)
- [catenax ontologies and alignment](./Ontologies/CatenaX%20ontology%20and%20alignment/)
- [Example data](./Technical%20resources/Example%20data.ttl)

Finally, run the SPARQL query defined above to see an example result of the standardized queries.