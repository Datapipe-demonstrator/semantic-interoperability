This repository is part of the [Datapipe research project](https://www.tudelft.nl/tbm/onderzoek/projecten/datapipe-project), which aims to help the Customs Administration of the Netherlands and the Ministry of Infrastructure and Water Management of the Netherlands to be better equipped to meet their responsibilities in the context of the circular economy. The project will deliver a diagnostic problem analysis report, blueprint for piloting, and recommendations.

# Semantic Interoperability and Application Profiles

In the Datapipe research project we have created 2 [Application Profiles](https://joinup.ec.europa.eu/collection/semic-support-centre/application-profiles-what-are-they-and-how-model-and-reuse-them-properly-look-through-dcat-ap), to highlight the flexibility of a unified semantic approach based on a set of generic and industry specific ontologies that are customized to the needs of a use case through means of semantic connections. 

The Application Profiles have been created based on the definition given by the European Comission through the Interoperable Europe SEMIC Support Centre:
1. considering the Core Vocabulary as the union of the [FEDeRATED upper ontology, the industry-specific ontologies and their alignment](./Ontologies/README.md)
2. for each use case identify the concepts not covered by the upper and aligned ontologies
3. design the Application Profile as an RDF/OWL file, referencing within the file to the existing ontologies

## Application Profile for EV Battery compliance check by authorities

The Application Profile we have created for this use case can be found [here](./Technical%20resources/Application%20Profile%20example.ttl). Using this Application Profile, we have answered to the [authorities queries](./Authority%20Standardized%20Query%20Example.md).

## Application Profile for UN Recommendation 46

We have interpreted the definition and created our [UN Recommendation 46](https://unece.org/trade/publications/recommendation-no46-enhancing-traceability-and-transparency-sustainable-value) Application Profile . We have created the Application Profile to cover all the traceability properties found in the [product information](./UNR46%20queries/product-information.md) category. We have produced a separate file with example data and a SPARQL query, expressed using the Application Profile contained in this repository.

# Blueprint for piloting

We have created a blueprint for any company to follow, should they want to join the semantic data sharing network. The whitepaper detailing every step of the blueprint can be found at: [10.13140/RG.2.2.34052.74885](https://www.researchgate.net/publication/383659169_Government_Accessing_Business_Data_for_Compliance_Monitoring_of_Circular_Economy_DATAPIPE_White_paper?channel=doi&linkId=66d59bbdfa5e11512c47cd97&showFulltext=true). In the table below we focus on the technical steps (mainly Step 2), providing aiding resources in understanding the technical implementation.

## Technical Blueprint for Piloting

<table>
    <thead>
        <tr>
            <th>Step description</th>
            <th>Methods / Tools</th>
            <th>Example</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td style="text-align: center;" colspan=4>  1. Define the high-level pilot scoping
        </tr>
        <tr>
            <td>a. Define the high-level scope in terms of circular flows, digital infrastructures, and authorities </td>
            <td>Define on a high level: The use case of the circular economy flows / supply chains for the piloting, and which product focus <br><i> Note: for customs relevance, the use case would need to include a border crossing aspects</i></td>
            <td> Import of cars with EV batteries from Asia to the EU (e.g. the Netherlands), use in the Netherlands and end-of-life in the Netherlands. </td>
        </tr>
        <tr>
            <td>b. Define the high-level scope in terms of digital infrastructures</td>
            <td>Define on a high level which digital infrastructures that will be included in the piloting.</td>
            <td> The business systems of the EV battery producer and of the car manufacturer.</td>
        </tr>
        <tr>
            <td>c. Define the high-level scope in terms of government authorities</td>
            <td>Define the scope from the point of view of the government authorities involved</td>
            <td>Customs in the country of import, registration authority, inspection agencies.</td>
        </tr>
        <tr>
            <td style="text-align: center;" colspan=4>  2. Detail the pilot by defining the legislative and refining the digital scope, prepare the pilot environment and formulate and execute queries
        </tr>
        <tr>
            <td style="text-align: center;" colspan=4>  2.1. Defining the legislative scope and requirements on what to monitor
        </tr>
        <tr>
            <td>a. Decide on the legislative scope</td>
            <td>Select the relevant legislations for the piloting Additional support A: the long list of legislation from D2.1. If legislations are missing add to the list </td>
            <td>The Battery regulation, The Eco-design for sustainable Products regulation and the Forced Labor regulation proposal. </td>
        </tr>
        <tr>
            <td>b. Define on high-level pilot requirements on what to monitor</td>
            <td>Use the high-level concept to screen the selected legislations and to select which areas of what to monitor are required. If some key concept areas are missing, add to the framework and perform the high-level screening of the legislations </td>
            <td>Information about the economic operators identifiers, product identifiers, material composition, CO2 footprint, as forced labour information </td>
        </tr>
        <tr>
            <td style="text-align: center;" colspan=4>  2.2. Refining the digital scope
        </tr>
        <tr>
            <td>a. Decide which actors and <a href="https://github.com/federatedplatforms/Docker-BDI-Node">FEDeRATED nodes</a> will be part of the data sharing network with the authorities for the piloting</td>
            <td>Decide on which actors are going to deploy their own nodes and which actors will make use of shared nodes in the data sharing network with the
            <br> Make decisions whether some actors will implement a data push functionality in their system to the network or expose a data fetching endpoint to their system to allow authorities to pull minimal data through the data sharing network.
            <br> Make decsinios whether some actors will implement a data fetching endpoint to their systems to allow authorities to pull sensitive data or they will implement a data push functionality
            <br> Make decisions about the scope of testing (e.g. conceptual to test the semantics, with test nodes or with middleware solutions and close to operational systems) 
            <br> <i> Support: For inspiration, see the short and the long DATAPIPE demo videos  https://collegerama.tudelft.nl/Mediasite/Channel/datapipe-project/browse/null/most-recent/null/0/null </td>
            <td>the data sharing environment can be with one node for customs and one for the EV producer, where the battery data is made available to customs via the responsible economic operator, the EV producer. <br> Alternatively, there can be a set-up with three nodes, where customs queries the responsible economic operator, the EV producer about the battery. The EV producer redirects customs to the EV battery node producer who shares the data to customs via thier own node </td>
        </tr>
        <tr>
            <td style="text-align: center;" colspan=4> 2.3. Align ontologies and prepare the pilot data sharing environment
        </tr>
        <tr>
            <td> a. Check the <a href="./Ontologies/README.md">industry specific ontologies </a>, <a href="https://github.com/federatedplatforms/FEDeRATED-Semantic-Model">the upper ontology</a> and if needed update the existing <a href="./Ontologies/CatenaX ontology and alignment/owl version/CatenaX to FEDeRATED Alignment.ttl">alignment</a> of the industry specific ontologies to the upper ontology </td>
            <td> Check whether the industry specific ontologies and the upper ontology cover concepts that correspond to the information needs of the authorities. If additional customizations are needed, identify additional relevant ontologies and create a custom Application Profile. <br> <i> Support tools: <a href="https://www.semantic-treehouse.nl/docs/wizard/">Semantic treehouse Message model wizard</i></a> <br> <i> Additional documents:  D2.1, paper Chirvasuta et al. (2025), DATAPIPE GitHub (https://github.com/Datapipe-demonstrator/semantic-interoperability) and DATAPIPE developer’s video, the part on ontology alignment (https://collegerama.tudelft.nl/Mediasite/Channel/datapipe-project/browse/null/most-recent/null/0/null) </i>
            <td> Authorities would like to access information about electronics in the car. When checking about existing alignments they may find out that alignment of the upper ontology has been performed with the logistics, a battery and a car ontology, but not with an electronics ontology. In this case, a relevant electronic ontology would need to be identified and aligned. If no appropriate ontology is identified this may need to lead to an ontology development task
        </tr>
        <tr>
            <td> b. Generate node configurations for the pilot parties for data sharing and validation schemes </td>
            <td> Generate node configurations with the Semantic Treehouse Message Model FIT Wizard. <br> Based on the configurations, customize the node to participate in the data sharing network.  </td>
            <td> The car producer instructions how to configure their own node and how to map the data about the car and the batteries available in the business systems to the semantics of the aligned ontologies. </td>
        </tr>
        <tr>
            <td style="text-align: center;" colspan=4> 2.4. Formulate queries and query data
        </tr>
        <tr>
            <td> a. Formulate queries using specific requirements on what to monitor, based on the aligned ontologies </td>
            <td> Formulate queries based on the government requirements (see example <a href="./Import Example Query.md">here</a>) on what to monitor, based on the mapping between selected legislation and the semantic solution (aligned ontologies and application profile) </td>
            <td> In view of the battery regulation, customs may want to monitor the recycled content of Cobalt in a EV battery. In case this information is available by the battery producer to the EV producer and EV producer via its node can provide access to customs to this data, via a query to the EV producer node that is connected to the EV producer back end system, customs can obtain the required information. </td>
        </tr>
    </tbody>
</table>