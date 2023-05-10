# DRP Service Directories

This repository contains a bunch of JSON documents describing the various [businesses](./businesses) and [agents](./agents) involved in the [Data Rights Protocol](https://datarightsprotocol.org).

## Using the Directories

Directories are published automatically to GitHub Pages when changes are made to the `main` branch and available on https://XXX.datarightsprotocol.org/businesses.json and https://XXX.datarightsprotocol.org/agents.json 

### Update Notifications

If you want to receive webhook notifications when this repository is updated please
XXX
(rrix to figure this out, probably modify a GitHub action which makes HTTP requests)

## New Actors

### business onboarding

If you are adding businesses which use your DRP integration as a privacy infrastructure provider, you will have a directory like `businesses/$YOURBUSINESS_delegated` which will be listed as owned by you in CODEOWNERS. For an example of adding this see commit XXX. 

Each business in the DRP will be represented as a single JSON document in the `businesses/` directory, and contains the following fields:

```
{
    "id": "unique identifier matching [A-Z_]+ regular expression",
    "name": "Consumer Legible Business Name",
    "logo": "https link to hi-res or vector image square logo suitable for display in agent app",
    "api_base": "URL to DRP API base",
    "supported_actions": ["list", "of", "drp", "request types"],
    "web_url": "business's homepage",
    "technical_contact": "an email contact for the techical integration. this may be a contact at a PIP which the business has delegated to",
    "business_contact": "an email address for contacting a person within the business who is knowledgeable about the privacy program and DRP integration"
}
```

XXX other onboarding steps

### agent onboarding

Each agent will go through specific onboarding steps outlined XXX here, and once they have been approved to participate in the DRP their information will be added in a JSON document in the `agents/` directory, and their technical contact will be given control of this file in the CODEOWNERS document. The agent directory entry contains the following fields:

```
{
    "id": "unique identifier matching [A-Z_]+ regular expression",
    "name": "Consumer Legible Agent App Name",
    "verify_key": "Hex encoded Libsodium public verifying key for signed requests",
    "web_url": "business's homepage",
    "technical_contact": "an email contact for the techical integration. this may be a contact at a PIP which the business has delegated to",
    "business_contact": "an email address for contacting a person within the business who is knowledgeable about the privacy program and DRP integration",
    "identity_assurance_url": "a link to an HTML or PDF document describing the process the agent enacts to verify a consumer's identity; a signed request containing these identities should be understood to have gone through this process."
}
```

XXX other onboarding steps

## Updating an Existing Entry

Updates to the DRP service directories need to be approved by one of the repository owners, as well as any CODEOWNER which may be responsible for delegated businesses. Repository owners MUST NOT update the entries themselves without provable chain of custody. When an entry is updated in a GitHub pull request a simple test will run to make sure the files in the repository are valid, and when that pull request is merged, the service directory will reflect the new changes in a matter of moments.

