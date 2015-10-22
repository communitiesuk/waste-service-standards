---
layout: doc
title: Address
model: address
---

# Address

## Types

This uses the [Land Registry BS7666 type](http://landregistry.data.gov.uk/def/common/BS7666Address).


## Properties

Term     | Mapping | Definition
---------|---------|-----------
paon | [landreg:paon](http://landregistry.data.gov.uk/def/common/paon) | Primary Addressable Object Name (PAON), typically building name or street number (see BS7666).
saon | [landreg:saon](http://landregistry.data.gov.uk/def/common/saon) | Secondary Addressable Object Name (SAON), e.g. flat number (see BS7666).
street | [landreg:street](http://landregistry.data.gov.uk/def/common/street) | Name of any thoroughfare in England and Wales which is the first or only street name in an address.
locality | [landreg:locality](http://landregistry.data.gov.uk/def/common/locality) | Name of a place which is either a hamlet / village in a rural area or a subdivision of a town / city in an urban area.
town | [landreg:town](http://landregistry.data.gov.uk/def/common/town) | Name of an urban area.
county | [landreg:county](http://landregistry.data.gov.uk/def/common/county) | Name of a geographic area which comprises either a current of former county in England of Wales or a Unitary Authority. 
postcode | [landreg:postcode](http://landregistry.data.gov.uk/def/common/postcode) | Postcode.


## Serialisation

{% include serialisation.html %}

