This markdown file documents the available data, as can be read from the [configuration template](./battpass-yarrml.yml).

## If querying for static data we have available:

###  subject: dpp-battpass:battpass

predicates:
1. battpass:identification => object a battPass:Identification

    further predicates:
    - battPass:category
    - battPass:idDmc
    - battPass:chemistry
    - battPass:manufacturerPartId
    - battPass:nameAtManufacturer
    - battPass:carrierType
    - battPass:carrierLayout

2. battPass:metadata => object a battPass:Metadata

    further predicates:
    - battPass:expirationDate
    - battPass:passportIdentifier
    - battPass:registrationIdentifier
    - battPass:issueDate
    - battPass:version
    - battPass:lastModification
    - battPass:predecessor
    - battPass:economicOperatorId
    - battPass:status

3. battPass:commercial => object a battPass:Commercial

    further predicates:
    - battPass:placedOnMarket
    - battPass:passportIdentifier

4. battPass:characteristics => object a battPass:Characteristics

    further predicates:
    - battPass:warrantyLifeValue
    - battPass:warrantyLifeUnit
    - battPass:lengthValue
    - battPass:lengthUnit
    - battPass:widthValue
    - battPass:widthUnit
    - battPass:weightalue
    - battPass:weightUnit
    - battPass:heightValue
    - battPass:heightUnit

5. battPass:sustainability => object a battPass:Sustainability

    further predicates: 
    
    a. battPass:sustainabilityCarbonFootprint => object a battPass:SustainabilityCarbonFootprint

    further predicates: 
    - battPass:sustainabilityCarbonFootprintLifeCycle
    - battPass:sustainabilityCarbonFootprintUnit
    - battPass:sustainabilityCarbonFootprintPerformanceClass
    - battPass:sustainabilityCarbonFootprintType
    - battPass:sustainabilityCarbonFootprintValue

    b. battPass:sustainabilityDocuments => object a battPass:SustainabilityDocument

    further predicates:
    - battPass:sustainabilityDocumentCategory
    - battPass:sustainabilityDocumentName
    - battPass:sustainabilityDocumentContentType
    - battPass:sustainabilityDocumentContent

6. battPass:materials => object a battPass:Materials

    further predicates:
    
    a. battPass:materialsHazardous
    
    further predicates:
    - battPass:materialName
    - battPass:materialConcentration
    - battPass:materialRecycled
    - battPass:materialLocation
    - battPass:materialCritical
    - battPass:materialUnit

    b. battPass:materialsActive
    
    further predicates:
    - battPass:materialName
    - battPass:materialRecycled
    - battPass:materialLocation
    - battPass:materialCritical

## If querying for dynamic data we have available:

### subject: battPass:demoBattPassMetadata

predicates:
- battPass:passportIdentifier
- battPass:version
- battPass:lastModification
- battPass:predecessor
- battPass:status
- battPass:economicOperatorId

### subject: battPass:demoBattPassDynamic

predicates:
- battPass:selfDischargingRate
- battPass:stateOfCharge
  
      
  