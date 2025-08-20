"""
Seed Data for Listings

This module contains seed data for property listings to populate the database
with sample data for development and testing purposes.
Data converted from TypeScript listingStore.ts file.
"""

from typing import List, Dict, Any

# Listing seed data converted from TypeScript interface structure  
LISTING_SEED_DATA: List[Dict[str, Any]] = [
    {
        "id": 187,
        "addressDetails": {
            "addressLine1": "5 Camden High Street",
            "addressLine2": "",
            "city": "London",
            "postcode": "N1 7AA",
            "shortenedPostcode": "N17",
            "country": "UK",
            "region": "London"
        },
        "propertyType": "apartment",
        "bedrooms": 1,
        "bathrooms": 1,
        "sizeSqFt": 50,
        "priceInCents": 12500000,
        "minimumDepositInCents": 1000000,
        "estimatedDepositInCents": 3125000,
        "monthlyRentalIncomeInCents": 110000,
        "isTenanted": True,
        "isCashOnly": False,
        "isNewBuild": False,
        "isCompany": False,
        "isShareSale": False,
        "description": "property",
        "photos": [
            {
                "originalURL": "https://storage.googleapis.com/assets-terranova-qa-module-core/listings/1b2b53fd-398b-4129-8f7d-c5932f90b3c3",
                "standardURL": "https://storage.googleapis.com/assets-terranova-qa-module-core/listings/1b2b53fd-398b-4129-8f7d-c5932f90b3c3_standard",
                "thumbnailURL": "https://storage.googleapis.com/assets-terranova-qa-module-core/listings/1b2b53fd-398b-4129-8f7d-c5932f90b3c3_thumbnail",
                "mimeType": "image/png"
            },
            {
                "originalURL": "https://storage.googleapis.com/assets-terranova-qa-module-core/listings/7c8d16b4-09d1-453b-8729-e7bfada38b2e",
                "standardURL": "https://storage.googleapis.com/assets-terranova-qa-module-core/listings/7c8d16b4-09d1-453b-8729-e7bfada38b2e_standard",
                "thumbnailURL": "https://storage.googleapis.com/assets-terranova-qa-module-core/listings/7c8d16b4-09d1-453b-8729-e7bfada38b2e_thumbnail",
                "mimeType": "image/png"
            }
        ],
        "grossYield": 0.1056,
        "madeVisibleAt": None
    },
    {
        "id": 185,
        "addressDetails": {
            "addressLine1": "2B fire blvd",
            "addressLine2": "",
            "city": "Ashford",
            "postcode": "",
            "shortenedPostcode": "ASF",
            "country": "UK",
            "region": "South East"
        },
        "propertyType": "apartment",
        "bedrooms": 1,
        "bathrooms": 1,
        "sizeSqFt": 2342,
        "priceInCents": 10000000,
        "minimumDepositInCents": 2550000,
        "estimatedDepositInCents": 2500000,
        "monthlyRentalIncomeInCents": 30000,
        "isTenanted": True,
        "isCashOnly": False,
        "isNewBuild": False,
        "isCompany": False,
        "isShareSale": False,
        "description": "asdf",
        "photos": [
            {
                "originalURL": "https://storage.googleapis.com/assets-terranova-qa-module-core/listings/ba11810b-30fc-4061-b3f5-126e2aae0a95",
                "standardURL": "https://storage.googleapis.com/assets-terranova-qa-module-core/listings/ba11810b-30fc-4061-b3f5-126e2aae0a95_standard",
                "thumbnailURL": "https://storage.googleapis.com/assets-terranova-qa-module-core/listings/ba11810b-30fc-4061-b3f5-126e2aae0a95_thumbnail",
                "mimeType": "image/jpeg"
            }
        ],
        "grossYield": 0.036,
        "madeVisibleAt": None
    },
    {
        "id": 79,
        "addressDetails": {
            "addressLine1": "37 John Snow Drive",
            "addressLine2": "",
            "city": "Wallington",
            "postcode": "SM6 4ER",
            "shortenedPostcode": "SM6",
            "country": "UK",
            "region": "London"
        },
        "propertyType": "apartment",
        "bedrooms": 2,
        "bathrooms": 1,
        "sizeSqFt": 300,
        "priceInCents": 10000000,
        "minimumDepositInCents": 1000000,
        "estimatedDepositInCents": 2500000,
        "monthlyRentalIncomeInCents": 60000,
        "isTenanted": True,
        "isCashOnly": False,
        "isNewBuild": False,
        "isCompany": False,
        "isShareSale": False,
        "description": "test",
        "photos": [
            {
                "originalURL": "https://storage.googleapis.com/assets-terranova-qa-module-core/listings/dc1c52ca-1061-4673-a3ae-92bd9098189d",
                "standardURL": "https://storage.googleapis.com/assets-terranova-qa-module-core/listings/dc1c52ca-1061-4673-a3ae-92bd9098189d_standard",
                "thumbnailURL": "https://storage.googleapis.com/assets-terranova-qa-module-core/listings/dc1c52ca-1061-4673-a3ae-92bd9098189d_thumbnail",
                "mimeType": "image/jpeg"
            },
            {
                "originalURL": "https://storage.googleapis.com/assets-terranova-qa-module-core/listings/82540ded-ea98-4279-a57d-742c0495ae73",
                "standardURL": "https://storage.googleapis.com/assets-terranova-qa-module-core/listings/82540ded-ea98-4279-a57d-742c0495ae73_standard",
                "thumbnailURL": "https://storage.googleapis.com/assets-terranova-qa-module-core/listings/82540ded-ea98-4279-a57d-742c0495ae73_thumbnail",
                "mimeType": "image/jpeg"
            },
            {
                "originalURL": "https://storage.googleapis.com/assets-terranova-qa-module-core/listings/bb5ad33a-717c-4525-beea-7f811fb828ef",
                "standardURL": "https://storage.googleapis.com/assets-terranova-qa-module-core/listings/bb5ad33a-717c-4525-beea-7f811fb828ef_standard",
                "thumbnailURL": "https://storage.googleapis.com/assets-terranova-qa-module-core/listings/bb5ad33a-717c-4525-beea-7f811fb828ef_thumbnail",
                "mimeType": "image/jpeg"
            },
            {
                "originalURL": "https://storage.googleapis.com/assets-terranova-qa-module-core/listings/57ef8821-1c60-4569-9999-21c23851d284",
                "standardURL": "https://storage.googleapis.com/assets-terranova-qa-module-core/listings/57ef8821-1c60-4569-9999-21c23851d284_standard",
                "thumbnailURL": "https://storage.googleapis.com/assets-terranova-qa-module-core/listings/57ef8821-1c60-4569-9999-21c23851d284_thumbnail",
                "mimeType": "image/jpeg"
            }
        ],
        "grossYield": 0.072,
        "madeVisibleAt": "2023-02-01T16:42:09Z"
    },
    {
        "id": 80,
        "addressDetails": {
            "addressLine1": "87 Scotts way",
            "addressLine2": "",
            "city": "Edinburgh",
            "postcode": "EH12 5AA",
            "shortenedPostcode": "EH12",
            "country": "UK",
            "region": "Scotland"
        },
        "propertyType": "apartment",
        "bedrooms": 0,
        "bathrooms": 1,
        "sizeSqFt": 355,
        "priceInCents": 23456700,
        "minimumDepositInCents": 3000000,
        "estimatedDepositInCents": 18798136,
        "monthlyRentalIncomeInCents": 200000,
        "isTenanted": True,
        "isCashOnly": True,
        "isNewBuild": False,
        "isCompany": False,
        "isShareSale": True,
        "description": "Share Sale Test",
        "photos": [
            {
                "originalURL": "https://storage.googleapis.com/assets-terranova-qa-module-core/listings/32cdb9d4-f02e-4d4c-84a0-35318874c9c7",
                "standardURL": "https://storage.googleapis.com/assets-terranova-qa-module-core/listings/32cdb9d4-f02e-4d4c-84a0-35318874c9c7_standard",
                "thumbnailURL": "https://storage.googleapis.com/assets-terranova-qa-module-core/listings/32cdb9d4-f02e-4d4c-84a0-35318874c9c7_thumbnail",
                "mimeType": "image/jpeg"
            },
            {
                "originalURL": "https://storage.googleapis.com/assets-terranova-qa-module-core/listings/ada31aac-71b6-4e89-b75b-20cbef617b8c",
                "standardURL": "https://storage.googleapis.com/assets-terranova-qa-module-core/listings/ada31aac-71b6-4e89-b75b-20cbef617b8c_standard",
                "thumbnailURL": "https://storage.googleapis.com/assets-terranova-qa-module-core/listings/ada31aac-71b6-4e89-b75b-20cbef617b8c_thumbnail",
                "mimeType": "image/jpeg"
            }
        ],
        "grossYield": 0.102316,
        "madeVisibleAt": "2023-02-01T16:52:50Z"
    },
    {
        "id": 81,
        "addressDetails": {
            "addressLine1": "202 Grunge street",
            "addressLine2": "",
            "city": "Manchester",
            "postcode": "M1 1AA",
            "shortenedPostcode": "M1",
            "country": "UK",
            "region": "North West"
        },
        "propertyType": "semi-detached",
        "bedrooms": 3,
        "bathrooms": 2,
        "sizeSqFt": 789,
        "priceInCents": 14400000,
        "minimumDepositInCents": 5200000,
        "estimatedDepositInCents": 3600000,
        "monthlyRentalIncomeInCents": 200000,
        "isTenanted": True,
        "isCashOnly": False,
        "isNewBuild": False,
        "isCompany": True,
        "isShareSale": True,
        "description": "GG Company test",
        "photos": [
            {
                "originalURL": "https://storage.googleapis.com/assets-terranova-qa-module-core/listings/44e55a81-c66e-48b6-abef-9b8cb3a5b674",
                "standardURL": "https://storage.googleapis.com/assets-terranova-qa-module-core/listings/44e55a81-c66e-48b6-abef-9b8cb3a5b674_standard",
                "thumbnailURL": "https://storage.googleapis.com/assets-terranova-qa-module-core/listings/44e55a81-c66e-48b6-abef-9b8cb3a5b674_thumbnail",
                "mimeType": "image/jpeg"
            },
            {
                "originalURL": "https://storage.googleapis.com/assets-terranova-qa-module-core/listings/f8fa432d-0306-4d2c-8d57-f33523372f26",
                "standardURL": "https://storage.googleapis.com/assets-terranova-qa-module-core/listings/f8fa432d-0306-4d2c-8d57-f33523372f26_standard",
                "thumbnailURL": "https://storage.googleapis.com/assets-terranova-qa-module-core/listings/f8fa432d-0306-4d2c-8d57-f33523372f26_thumbnail",
                "mimeType": "image/jpeg"
            }
        ],
        "grossYield": 0.166667,
        "madeVisibleAt": "2023-02-01T17:12:25Z"
    },
    {
        "id": 82,
        "addressDetails": {
            "addressLine1": "3 Knotting Lane",
            "addressLine2": "",
            "city": "London",
            "postcode": "W14 9AA",
            "shortenedPostcode": "W14",
            "country": "UK",
            "region": "London"
        },
        "propertyType": "terraced",
        "bedrooms": 3,
        "bathrooms": 3,
        "sizeSqFt": 300,
        "priceInCents": 100000000,
        "minimumDepositInCents": 20000000,
        "estimatedDepositInCents": 40827520,
        "monthlyRentalIncomeInCents": 850000,
        "isTenanted": False,
        "isCashOnly": False,
        "isNewBuild": False,
        "isCompany": False,
        "isShareSale": False,
        "description": "Image test",
        "photos": [
            {
                "originalURL": "https://storage.googleapis.com/assets-terranova-qa-module-core/listings/58e9d12f-95fd-4516-9611-cc6f4c828959",
                "standardURL": "https://storage.googleapis.com/assets-terranova-qa-module-core/listings/58e9d12f-95fd-4516-9611-cc6f4c828959_standard",
                "thumbnailURL": "https://storage.googleapis.com/assets-terranova-qa-module-core/listings/58e9d12f-95fd-4516-9611-cc6f4c828959_thumbnail",
                "mimeType": "image/jpeg"
            },
            {
                "originalURL": "https://storage.googleapis.com/assets-terranova-qa-module-core/listings/f8647f62-a6a2-4bb5-a3ac-b22759af1804",
                "standardURL": "https://storage.googleapis.com/assets-terranova-qa-module-core/listings/f8647f62-a6a2-4bb5-a3ac-b22759af1804_standard",
                "thumbnailURL": "https://storage.googleapis.com/assets-terranova-qa-module-core/listings/f8647f62-a6a2-4bb5-a3ac-b22759af1804_thumbnail",
                "mimeType": "image/jpeg"
            },
            {
                "originalURL": "https://storage.googleapis.com/assets-terranova-qa-module-core/listings/0ccd6f6a-9390-41b8-8102-8a205ffe73cd",
                "standardURL": "https://storage.googleapis.com/assets-terranova-qa-module-core/listings/0ccd6f6a-9390-41b8-8102-8a205ffe73cd_standard",
                "thumbnailURL": "https://storage.googleapis.com/assets-terranova-qa-module-core/listings/0ccd6f6a-9390-41b8-8102-8a205ffe73cd_thumbnail",
                "mimeType": "image/jpeg"
            },
            {
                "originalURL": "https://storage.googleapis.com/assets-terranova-qa-module-core/listings/fb1a1f3b-313d-45a4-b1d3-1ee5c5f21895",
                "standardURL": "https://storage.googleapis.com/assets-terranova-qa-module-core/listings/fb1a1f3b-313d-45a4-b1d3-1ee5c5f21895_standard",
                "thumbnailURL": "https://storage.googleapis.com/assets-terranova-qa-module-core/listings/fb1a1f3b-313d-45a4-b1d3-1ee5c5f21895_thumbnail",
                "mimeType": "image/jpeg"
            },
            {
                "originalURL": "https://storage.googleapis.com/assets-terranova-qa-module-core/listings/62ed85f1-00ac-40bd-9607-780f5245ce1e",
                "standardURL": "https://storage.googleapis.com/assets-terranova-qa-module-core/listings/62ed85f1-00ac-40bd-9607-780f5245ce1e_standard",
                "thumbnailURL": "https://storage.googleapis.com/assets-terranova-qa-module-core/listings/62ed85f1-00ac-40bd-9607-780f5245ce1e_thumbnail",
                "mimeType": "image/jpeg"
            },
            {
                "originalURL": "https://storage.googleapis.com/assets-terranova-qa-module-core/listings/a39d1c3b-8a93-4d9c-bdb4-d6cda911f8e4",
                "standardURL": "https://storage.googleapis.com/assets-terranova-qa-module-core/listings/a39d1c3b-8a93-4d9c-bdb4-d6cda911f8e4_standard",
                "thumbnailURL": "https://storage.googleapis.com/assets-terranova-qa-module-core/listings/a39d1c3b-8a93-4d9c-bdb4-d6cda911f8e4_thumbnail",
                "mimeType": "image/jpeg"
            }
        ],
        "grossYield": 0.102,
        "madeVisibleAt": "2023-02-02T08:36:00Z"
    },
    {
        "id": 68,
        "addressDetails": {
            "addressLine1": "27 Hill Road",
            "addressLine2": "",
            "city": "Sheffield",
            "postcode": "S1 2AB",
            "shortenedPostcode": "S1",
            "country": "UK",
            "region": "North East"
        },
        "propertyType": "apartment",
        "bedrooms": 1,
        "bathrooms": 1,
        "sizeSqFt": 301,
        "priceInCents": 13875000,
        "minimumDepositInCents": 3468700,
        "estimatedDepositInCents": 3468750,
        "monthlyRentalIncomeInCents": 95100,
        "isTenanted": True,
        "isCashOnly": True,
        "isNewBuild": False,
        "isCompany": False,
        "isShareSale": False,
        "description": "This property can be purchased via shares with 0% SDLT - this purchase option is only available with GetGround! \\n\\nWhen you buy shares, you usually pay stamp duty tax of 0.5% on the price you pay for the claims. As the property continues to be owned by the company no SDLT is payable.\\n\\nThis modern studio apartment is ideal for young professionals in the heart of Sheffield city centre. This flat is already tenanted generating a strong 8.2% yield for investors to benefit from. The rent is assured until the end of Q2 2025.\\n\\nBeing just a 10-minute walk from Sheffield Sheaf Street, you have fantastic access to all of the North's city hubs, with Manchester, Birmingham and Leeds all just a one-hour train journey away.",
        "photos": [
            {
                "originalURL": "https://storage.googleapis.com/assets-terranova-qa-module-core/listings/48d16039-5857-471e-a8ee-d427441e2604",
                "standardURL": "https://storage.googleapis.com/assets-terranova-qa-module-core/listings/48d16039-5857-471e-a8ee-d427441e2604_standard",
                "thumbnailURL": "https://storage.googleapis.com/assets-terranova-qa-module-core/listings/48d16039-5857-471e-a8ee-d427441e2604_thumbnail",
                "mimeType": "image/png"
            },
            {
                "originalURL": "https://storage.googleapis.com/assets-terranova-qa-module-core/listings/bd4a9d7b-9416-4d61-b550-0b01f2e7fa72",
                "standardURL": "https://storage.googleapis.com/assets-terranova-qa-module-core/listings/bd4a9d7b-9416-4d61-b550-0b01f2e7fa72_standard",
                "thumbnailURL": "https://storage.googleapis.com/assets-terranova-qa-module-core/listings/bd4a9d7b-9416-4d61-b550-0b01f2e7fa72_thumbnail",
                "mimeType": "image/jpeg"
            },
            {
                "originalURL": "https://storage.googleapis.com/assets-terranova-qa-module-core/listings/fff510fd-33d5-41a4-ab95-a2d5033551c7",
                "standardURL": "https://storage.googleapis.com/assets-terranova-qa-module-core/listings/fff510fd-33d5-41a4-ab95-a2d5033551c7_standard",
                "thumbnailURL": "https://storage.googleapis.com/assets-terranova-qa-module-core/listings/fff510fd-33d5-41a4-ab95-a2d5033551c7_thumbnail",
                "mimeType": "image/jpeg"
            },
            {
                "originalURL": "https://storage.googleapis.com/assets-terranova-qa-module-core/listings/7538ea96-08e3-4ce1-8c2c-dbadc24f7622",
                "standardURL": "https://storage.googleapis.com/assets-terranova-qa-module-core/listings/7538ea96-08e3-4ce1-8c2c-dbadc24f7622_standard",
                "thumbnailURL": "https://storage.googleapis.com/assets-terranova-qa-module-core/listings/7538ea96-08e3-4ce1-8c2c-dbadc24f7622_thumbnail",
                "mimeType": "image/jpeg"
            }
        ],
        "grossYield": 0.0822486,
        "madeVisibleAt": "2023-09-27T08:14:37Z"
    },
    {
        "id": 66,
        "addressDetails": {
            "addressLine1": "67 Kansas Street",
            "addressLine2": "",
            "city": "Preston",
            "postcode": "PR1 2TT",
            "shortenedPostcode": "PR1",
            "country": "UK",
            "region": "North West"
        },
        "propertyType": "apartment",
        "bedrooms": 2,
        "bathrooms": 1,
        "sizeSqFt": 686,
        "priceInCents": 3995000,
        "minimumDepositInCents": 3995000,
        "estimatedDepositInCents": 998750,
        "monthlyRentalIncomeInCents": 38000,
        "isTenanted": True,
        "isCashOnly": False,
        "isNewBuild": False,
        "isCompany": False,
        "isShareSale": False,
        "description": "2 bed flat in Preston with a rear terrace space and large garden area.",
        "photos": [
            {
                "originalURL": "https://storage.googleapis.com/assets-terranova-qa-module-core/listings/5d4d5076-2cf3-4d09-8818-6a8fe0993530",
                "standardURL": "https://storage.googleapis.com/assets-terranova-qa-module-core/listings/5d4d5076-2cf3-4d09-8818-6a8fe0993530_standard",
                "thumbnailURL": "https://storage.googleapis.com/assets-terranova-qa-module-core/listings/5d4d5076-2cf3-4d09-8818-6a8fe0993530_thumbnail",
                "mimeType": "image/jpeg"
            },
            {
                "originalURL": "https://storage.googleapis.com/assets-terranova-qa-module-core/listings/cca8f249-5946-44d3-98f6-2b7f1ec0c286",
                "standardURL": "https://storage.googleapis.com/assets-terranova-qa-module-core/listings/cca8f249-5946-44d3-98f6-2b7f1ec0c286_standard",
                "thumbnailURL": "https://storage.googleapis.com/assets-terranova-qa-module-core/listings/cca8f249-5946-44d3-98f6-2b7f1ec0c286_thumbnail",
                "mimeType": "image/jpeg"
            },
            {
                "originalURL": "https://storage.googleapis.com/assets-terranova-qa-module-core/listings/5db35350-6efa-4c23-b1df-b8d2bdce32e3",
                "standardURL": "https://storage.googleapis.com/assets-terranova-qa-module-core/listings/5db35350-6efa-4c23-b1df-b8d2bdce32e3_standard",
                "thumbnailURL": "https://storage.googleapis.com/assets-terranova-qa-module-core/listings/5db35350-6efa-4c23-b1df-b8d2bdce32e3_thumbnail",
                "mimeType": "image/jpeg"
            },
            {
                "originalURL": "https://storage.googleapis.com/assets-terranova-qa-module-core/listings/bdc6a7da-4405-4721-a820-897f907cbcc7",
                "standardURL": "https://storage.googleapis.com/assets-terranova-qa-module-core/listings/bdc6a7da-4405-4721-a820-897f907cbcc7_standard",
                "thumbnailURL": "https://storage.googleapis.com/assets-terranova-qa-module-core/listings/bdc6a7da-4405-4721-a820-897f907cbcc7_thumbnail",
                "mimeType": "image/jpeg"
            }
        ],
        "grossYield": 0.114143,
        "madeVisibleAt": None
    },
    {
        "id": 71,
        "addressDetails": {
            "addressLine1": "45 Larcher Street",
            "addressLine2": "",
            "city": "Preston",
            "postcode": "PR1 2AF",
            "shortenedPostcode": "PR1",
            "country": "UK",
            "region": "North West"
        },
        "propertyType": "apartment",
        "bedrooms": 3,
        "bathrooms": 1,
        "sizeSqFt": 840,
        "priceInCents": 88058000,
        "minimumDepositInCents": 7014500,
        "estimatedDepositInCents": 42397020,
        "monthlyRentalIncomeInCents": 875400,
        "isTenanted": False,
        "isCashOnly": False,
        "isNewBuild": False,
        "isCompany": False,
        "isShareSale": False,
        "description": "Apt 170 sits on the eleventh floor and provides a great investment opportunity into a high specification apartment in a prime location that has been identified by local and national government as an area of great potential and has been extremely well funded in recent years.",
        "photos": [
            {
                "originalURL": "https://storage.googleapis.com/assets-terranova-qa-module-core/listings/26e7679c-5ba9-4c9c-ba54-858b400e6863",
                "standardURL": "https://storage.googleapis.com/assets-terranova-qa-module-core/listings/26e7679c-5ba9-4c9c-ba54-858b400e6863_standard",
                "thumbnailURL": "https://storage.googleapis.com/assets-terranova-qa-module-core/listings/26e7679c-5ba9-4c9c-ba54-858b400e6863_thumbnail",
                "mimeType": "image/jpeg"
            },
            {
                "originalURL": "https://storage.googleapis.com/assets-terranova-qa-module-core/listings/5bee58eb-5bbd-4329-b884-eea1dad850e1",
                "standardURL": "https://storage.googleapis.com/assets-terranova-qa-module-core/listings/5bee58eb-5bbd-4329-b884-eea1dad850e1_standard",
                "thumbnailURL": "https://storage.googleapis.com/assets-terranova-qa-module-core/listings/5bee58eb-5bbd-4329-b884-eea1dad850e1_thumbnail",
                "mimeType": "image/jpeg"
            },
            {
                "originalURL": "https://storage.googleapis.com/assets-terranova-qa-module-core/listings/b9ecaccd-964e-4adb-aec6-863bef629166",
                "standardURL": "https://storage.googleapis.com/assets-terranova-qa-module-core/listings/b9ecaccd-964e-4adb-aec6-863bef629166_standard",
                "thumbnailURL": "https://storage.googleapis.com/assets-terranova-qa-module-core/listings/b9ecaccd-964e-4adb-aec6-863bef629166_thumbnail",
                "mimeType": "image/jpeg"
            },
            {
                "originalURL": "https://storage.googleapis.com/assets-terranova-qa-module-core/listings/19c9fd2f-67dc-4b87-855f-f023bbbb4e85",
                "standardURL": "https://storage.googleapis.com/assets-terranova-qa-module-core/listings/19c9fd2f-67dc-4b87-855f-f023bbbb4e85_standard",
                "thumbnailURL": "https://storage.googleapis.com/assets-terranova-qa-module-core/listings/19c9fd2f-67dc-4b87-855f-f023bbbb4e85_thumbnail",
                "mimeType": "image/jpeg"
            }
        ],
        "grossYield": 0.119294,
        "madeVisibleAt": None
    },
    {
        "id": 72,
        "addressDetails": {
            "addressLine1": "3 Button Street",
            "addressLine2": "",
            "city": "Preston",
            "postcode": "PR1 2AF",
            "shortenedPostcode": "PR1",
            "country": "UK",
            "region": "North West"
        },
        "propertyType": "apartment",
        "bedrooms": 2,
        "bathrooms": 1,
        "sizeSqFt": 678,
        "priceInCents": 22429100,
        "minimumDepositInCents": 5607300,
        "estimatedDepositInCents": 9514036,
        "monthlyRentalIncomeInCents": 140200,
        "isTenanted": False,
        "isCashOnly": False,
        "isNewBuild": False,
        "isCompany": False,
        "isShareSale": False,
        "description": "Apt 53 situated in Block B is a high specification apartment that sits on the third floor. The development itself encompasses a beautiful roof garden, residents lounge, concierge service, bike storage and a state of the art gym to complete this premium home in a well invested area, resulting in a rapidly developing cultural and economic landscape. \\n\\n\\nTEST",
        "photos": [
            {
                "originalURL": "https://storage.googleapis.com/assets-terranova-qa-module-core/listings/5f3758df-98cb-427a-84f2-afc7ea6c40ca",
                "standardURL": "https://storage.googleapis.com/assets-terranova-qa-module-core/listings/5f3758df-98cb-427a-84f2-afc7ea6c40ca_standard",
                "thumbnailURL": "https://storage.googleapis.com/assets-terranova-qa-module-core/listings/5f3758df-98cb-427a-84f2-afc7ea6c40ca_thumbnail",
                "mimeType": "image/jpeg"
            },
            {
                "originalURL": "https://storage.googleapis.com/assets-terranova-qa-module-core/listings/35658a75-7f58-4549-8008-e2bbbdbdb20a",
                "standardURL": "https://storage.googleapis.com/assets-terranova-qa-module-core/listings/35658a75-7f58-4549-8008-e2bbbdbdb20a_standard",
                "thumbnailURL": "https://storage.googleapis.com/assets-terranova-qa-module-core/listings/35658a75-7f58-4549-8008-e2bbbdbdb20a_thumbnail",
                "mimeType": "image/jpeg"
            },
            {
                "originalURL": "https://storage.googleapis.com/assets-terranova-qa-module-core/listings/365fc59a-4b48-448e-a110-3b790df58db9",
                "standardURL": "https://storage.googleapis.com/assets-terranova-qa-module-core/listings/365fc59a-4b48-448e-a110-3b790df58db9_standard",
                "thumbnailURL": "https://storage.googleapis.com/assets-terranova-qa-module-core/listings/365fc59a-4b48-448e-a110-3b790df58db9_thumbnail",
                "mimeType": "image/jpeg"
            }
        ],
        "grossYield": 0.0750097,
        "madeVisibleAt": "2023-02-17T18:20:03Z"
    },
    {
        "id": 105,
        "addressDetails": {
            "addressLine1": "4 High Street",
            "addressLine2": "",
            "city": "Wallington",
            "postcode": "SM6 9AA",
            "shortenedPostcode": "SM6",
            "country": "UK",
            "region": "South East"
        },
        "propertyType": "apartment",
        "bedrooms": 0,
        "bathrooms": 1,
        "sizeSqFt": 286,
        "priceInCents": 52500000,
        "minimumDepositInCents": 2500000,
        "estimatedDepositInCents": 13125000,
        "monthlyRentalIncomeInCents": 350000,
        "isTenanted": True,
        "isCashOnly": False,
        "isNewBuild": False,
        "isCompany": False,
        "isShareSale": True,
        "description": "ertggr rtg trtg etgtrgrt",
        "photos": [
            {
                "originalURL": "https://storage.googleapis.com/assets-terranova-qa-module-core/listings/fa320e9c-cb0b-4c0d-be21-2b992ee6c126",
                "standardURL": "https://storage.googleapis.com/assets-terranova-qa-module-core/listings/fa320e9c-cb0b-4c0d-be21-2b992ee6c126_standard",
                "thumbnailURL": "https://storage.googleapis.com/assets-terranova-qa-module-core/listings/fa320e9c-cb0b-4c0d-be21-2b992ee6c126_thumbnail",
                "mimeType": "image/png"
            }
        ],
        "grossYield": 0.08,
        "madeVisibleAt": "2023-03-01T13:39:00Z"
    },
    {
        "id": 106,
        "addressDetails": {
            "addressLine1": "13 Cliff st",
            "addressLine2": "",
            "city": "Dover",
            "postcode": "",
            "shortenedPostcode": "DOV",
            "country": "UK",
            "region": "South East"
        },
        "propertyType": "apartment",
        "bedrooms": 1,
        "bathrooms": 2,
        "sizeSqFt": 123,
        "priceInCents": 12300000,
        "minimumDepositInCents": 1230000,
        "estimatedDepositInCents": 1500000,
        "monthlyRentalIncomeInCents": 80000,
        "isTenanted": True,
        "isCashOnly": True,
        "isNewBuild": False,
        "isCompany": True,
        "isShareSale": True,
        "description": "UPDATE",
        "photos": [
            {
                "originalURL": "https://storage.googleapis.com/assets-terranova-qa-module-core/listings/9db6de1b-88b9-4030-b944-bd15544a23ed",
                "standardURL": "https://storage.googleapis.com/assets-terranova-qa-module-core/listings/9db6de1b-88b9-4030-b944-bd15544a23ed_standard",
                "thumbnailURL": "https://storage.googleapis.com/assets-terranova-qa-module-core/listings/9db6de1b-88b9-4030-b944-bd15544a23ed_thumbnail",
                "mimeType": "image/jpeg"
            },
            {
                "originalURL": "https://storage.googleapis.com/assets-terranova-qa-module-core/listings/b71de69c-cfe3-41bf-8e80-a0a3602026fa",
                "standardURL": "https://storage.googleapis.com/assets-terranova-qa-module-core/listings/b71de69c-cfe3-41bf-8e80-a0a3602026fa_standard",
                "thumbnailURL": "https://storage.googleapis.com/assets-terranova-qa-module-core/listings/b71de69c-cfe3-41bf-8e80-a0a3602026fa_thumbnail",
                "mimeType": "image/jpeg"
            }
        ],
        "grossYield": 0.0780488,
        "madeVisibleAt": None
    },
    {
        "id": 120,
        "addressDetails": {
            "addressLine1": "77 Regata Street",
            "addressLine2": "",
            "city": "Henley",
            "postcode": "RE1 1AA",
            "shortenedPostcode": "RE1",
            "country": "UK",
            "region": "South East"
        },
        "propertyType": "apartment",
        "bedrooms": 0,
        "bathrooms": 1,
        "sizeSqFt": 400,
        "priceInCents": 100000000,
        "minimumDepositInCents": 10000000,
        "estimatedDepositInCents": 25000000,
        "monthlyRentalIncomeInCents": 700000,
        "isTenanted": True,
        "isCashOnly": False,
        "isNewBuild": False,
        "isCompany": False,
        "isShareSale": False,
        "description": "test",
        "photos": [
            {
                "originalURL": "https://storage.googleapis.com/assets-terranova-qa-module-core/listings/86f3dadf-54bf-447c-a4fa-a8f067cf6aee",
                "standardURL": "https://storage.googleapis.com/assets-terranova-qa-module-core/listings/86f3dadf-54bf-447c-a4fa-a8f067cf6aee_standard",
                "thumbnailURL": "https://storage.googleapis.com/assets-terranova-qa-module-core/listings/86f3dadf-54bf-447c-a4fa-a8f067cf6aee_thumbnail",
                "mimeType": "image/jpeg"
            }
        ],
        "grossYield": 0.084,
        "madeVisibleAt": "2023-03-16T16:11:14Z"
    },
    {
        "id": 91,
        "addressDetails": {
            "addressLine1": "Animal Farm",
            "addressLine2": "",
            "city": "Eastbourne",
            "postcode": "BN20 1AA",
            "shortenedPostcode": "BN20",
            "country": "UK",
            "region": "South East"
        },
        "propertyType": "apartment",
        "bedrooms": 0,
        "bathrooms": 1,
        "sizeSqFt": 789,
        "priceInCents": 100000000,
        "minimumDepositInCents": 10000000,
        "estimatedDepositInCents": 25000000,
        "monthlyRentalIncomeInCents": 700000,
        "isTenanted": True,
        "isCashOnly": False,
        "isNewBuild": False,
        "isCompany": False,
        "isShareSale": False,
        "description": "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.",
        "photos": [
            {
                "originalURL": "https://storage.googleapis.com/assets-terranova-qa-module-core/listings/8816708f-9d0d-4c24-bac9-dad96fef53f4",
                "standardURL": "https://storage.googleapis.com/assets-terranova-qa-module-core/listings/8816708f-9d0d-4c24-bac9-dad96fef53f4_standard",
                "thumbnailURL": "https://storage.googleapis.com/assets-terranova-qa-module-core/listings/8816708f-9d0d-4c24-bac9-dad96fef53f4_thumbnail",
                "mimeType": "image/jpeg"
            }
        ],
        "grossYield": 0.084,
        "madeVisibleAt": "2023-02-17T17:47:45Z"
    },
    {
        "id": 94,
        "addressDetails": {
            "addressLine1": "12 Alfie Solomons Way",
            "addressLine2": "",
            "city": "London",
            "postcode": "N1 8LN",
            "shortenedPostcode": "N1",
            "country": "UK",
            "region": "London"
        },
        "propertyType": "apartment",
        "bedrooms": 2,
        "bathrooms": 3,
        "sizeSqFt": 1000,
        "priceInCents": 125000,
        "minimumDepositInCents": 10000,
        "estimatedDepositInCents": 31250,
        "monthlyRentalIncomeInCents": 1100,
        "isTenanted": False,
        "isCashOnly": True,
        "isNewBuild": False,
        "isCompany": True,
        "isShareSale": True,
        "description": "Free text",
        "photos": [
            {
                "originalURL": "https://storage.googleapis.com/assets-terranova-qa-module-core/listings/bea385af-17c5-4369-bf94-be6b9570f4db",
                "standardURL": "https://storage.googleapis.com/assets-terranova-qa-module-core/listings/bea385af-17c5-4369-bf94-be6b9570f4db_standard",
                "thumbnailURL": "https://storage.googleapis.com/assets-terranova-qa-module-core/listings/bea385af-17c5-4369-bf94-be6b9570f4db_thumbnail",
                "mimeType": "image/png"
            }
        ],
        "grossYield": 0.1056,
        "madeVisibleAt": "2023-02-20T09:57:55Z"
    },
    {
        "id": 97,
        "addressDetails": {
            "addressLine1": "123 Rainbow Road",
            "addressLine2": "",
            "city": "Brighton",
            "postcode": "BN1 1AA",
            "shortenedPostcode": "BN1",
            "country": "UK",
            "region": "South East"
        },
        "propertyType": "apartment",
        "bedrooms": 0,
        "bathrooms": 1,
        "sizeSqFt": 678,
        "priceInCents": 50000000,
        "minimumDepositInCents": 10000000,
        "estimatedDepositInCents": 12000000,
        "monthlyRentalIncomeInCents": 400000,
        "isTenanted": True,
        "isCashOnly": False,
        "isNewBuild": False,
        "isCompany": False,
        "isShareSale": False,
        "description": "0",
        "photos": [
            {
                "originalURL": "https://storage.googleapis.com/assets-terranova-qa-module-core/listings/c836d323-7548-47fd-82e8-f1529c87e51e",
                "standardURL": "https://storage.googleapis.com/assets-terranova-qa-module-core/listings/c836d323-7548-47fd-82e8-f1529c87e51e_standard",
                "thumbnailURL": "https://storage.googleapis.com/assets-terranova-qa-module-core/listings/c836d323-7548-47fd-82e8-f1529c87e51e_thumbnail",
                "mimeType": "image/jpeg"
            }
        ],
        "grossYield": 0.096,
        "madeVisibleAt": None
    },
    {
        "id": 103,
        "addressDetails": {
            "addressLine1": "4 Seaside Road",
            "addressLine2": "",
            "city": "Whitstable",
            "postcode": "CT5 1AB",
            "shortenedPostcode": "CT5",
            "country": "UK",
            "region": "South East"
        },
        "propertyType": "apartment",
        "bedrooms": 0,
        "bathrooms": 1,
        "sizeSqFt": 300,
        "priceInCents": 100000000,
        "minimumDepositInCents": 10000000,
        "estimatedDepositInCents": 12000000,
        "monthlyRentalIncomeInCents": 100000,
        "isTenanted": True,
        "isCashOnly": True,
        "isNewBuild": False,
        "isCompany": True,
        "isShareSale": False,
        "description": "66666",
        "photos": [
            {
                "originalURL": "https://storage.googleapis.com/assets-terranova-qa-module-core/listings/533f2688-23c2-4385-a272-0179f9d6b6db",
                "standardURL": "https://storage.googleapis.com/assets-terranova-qa-module-core/listings/533f2688-23c2-4385-a272-0179f9d6b6db_standard",
                "thumbnailURL": "https://storage.googleapis.com/assets-terranova-qa-module-core/listings/533f2688-23c2-4385-a272-0179f9d6b6db_thumbnail",
                "mimeType": "image/jpeg"
            }
        ],
        "grossYield": 0.012,
        "madeVisibleAt": None
    },
    {
        "id": 143,
        "addressDetails": {
            "addressLine1": "3 Chaucer Road",
            "addressLine2": "",
            "city": "Canterbury",
            "postcode": "CT1 3RF",
            "shortenedPostcode": "CT1",
            "country": "UK",
            "region": "South East"
        },
        "propertyType": "apartment",
        "bedrooms": 0,
        "bathrooms": 1,
        "sizeSqFt": 750,
        "priceInCents": 20000000,
        "minimumDepositInCents": 300000,
        "estimatedDepositInCents": 500000,
        "monthlyRentalIncomeInCents": 150000,
        "isTenanted": True,
        "isCashOnly": False,
        "isNewBuild": False,
        "isCompany": False,
        "isShareSale": False,
        "description": "Test",
        "photos": [
            {
                "originalURL": "https://storage.googleapis.com/assets-terranova-qa-module-core/listings/3a458a51-532c-456a-8814-5d488cac49f0",
                "standardURL": "https://storage.googleapis.com/assets-terranova-qa-module-core/listings/3a458a51-532c-456a-8814-5d488cac49f0_standard",
                "thumbnailURL": "https://storage.googleapis.com/assets-terranova-qa-module-core/listings/3a458a51-532c-456a-8814-5d488cac49f0_thumbnail",
                "mimeType": "image/png"
            }
        ],
        "grossYield": 0.09,
        "madeVisibleAt": "2023-03-27T11:01:38Z"
    },
    {
        "id": 144,
        "addressDetails": {
            "addressLine1": "115 Maidstone Road",
            "addressLine2": "",
            "city": "Maidstone",
            "postcode": "ME15 6AA",
            "shortenedPostcode": "MDS",
            "country": "UK",
            "region": "South East"
        },
        "propertyType": "apartment",
        "bedrooms": 0,
        "bathrooms": 1,
        "sizeSqFt": 40,
        "priceInCents": 15000000,
        "minimumDepositInCents": 1000000,
        "estimatedDepositInCents": 1500000,
        "monthlyRentalIncomeInCents": 40000,
        "isTenanted": True,
        "isCashOnly": False,
        "isNewBuild": False,
        "isCompany": False,
        "isShareSale": False,
        "description": "Test",
        "photos": [
            {
                "originalURL": "https://storage.googleapis.com/assets-terranova-qa-module-core/listings/0ee871a1-ecb8-43c7-aab0-30128baec351",
                "standardURL": "https://storage.googleapis.com/assets-terranova-qa-module-core/listings/0ee871a1-ecb8-43c7-aab0-30128baec351_standard",
                "thumbnailURL": "https://storage.googleapis.com/assets-terranova-qa-module-core/listings/0ee871a1-ecb8-43c7-aab0-30128baec351_thumbnail",
                "mimeType": "image/png"
            }
        ],
        "grossYield": 0.032,
        "madeVisibleAt": "2023-03-27T11:04:16Z"
    },
    {
        "id": 148,
        "addressDetails": {
            "addressLine1": "3 Buckingham Palace Road",
            "addressLine2": "",
            "city": "London",
            "postcode": "",
            "shortenedPostcode": "W14 8FF",
            "country": "UK",
            "region": "London"
        },
        "propertyType": "terraced",
        "bedrooms": 3,
        "bathrooms": 1,
        "sizeSqFt": 32,
        "priceInCents": 35000000,
        "minimumDepositInCents": 10000000,
        "estimatedDepositInCents": 8750000,
        "monthlyRentalIncomeInCents": 400000,
        "isTenanted": True,
        "isCashOnly": False,
        "isNewBuild": False,
        "isCompany": False,
        "isShareSale": False,
        "description": "test",
        "photos": [
            {
                "originalURL": "https://storage.googleapis.com/assets-terranova-qa-module-core/listings/70c29877-0654-49ed-8225-3189e81b7354",
                "standardURL": "https://storage.googleapis.com/assets-terranova-qa-module-core/listings/70c29877-0654-49ed-8225-3189e81b7354_standard",
                "thumbnailURL": "https://storage.googleapis.com/assets-terranova-qa-module-core/listings/70c29877-0654-49ed-8225-3189e81b7354_thumbnail",
                "mimeType": "image/png"
            }
        ],
        "grossYield": 0.137143,
        "madeVisibleAt": "2023-03-28T13:30:27Z"
    },
    {
        "id": 145,
        "addressDetails": {
            "addressLine1": "123 Main street",
            "addressLine2": "W14 9AA",
            "city": "London",
            "postcode": "",
            "shortenedPostcode": "W14",
            "country": "UK",
            "region": "London"
        },
        "propertyType": "apartment",
        "bedrooms": 0,
        "bathrooms": 1,
        "sizeSqFt": 40,
        "priceInCents": 25000000,
        "minimumDepositInCents": 10000000,
        "estimatedDepositInCents": 6250000,
        "monthlyRentalIncomeInCents": 400000,
        "isTenanted": True,
        "isCashOnly": False,
        "isNewBuild": False,
        "isCompany": False,
        "isShareSale": False,
        "description": "Classic house right on main street!",
        "photos": [
            {
                "originalURL": "https://storage.googleapis.com/assets-terranova-qa-module-core/listings/b73ac33d-b2de-4656-a92e-a7f4bde98b26",
                "standardURL": "https://storage.googleapis.com/assets-terranova-qa-module-core/listings/b73ac33d-b2de-4656-a92e-a7f4bde98b26_standard",
                "thumbnailURL": "https://storage.googleapis.com/assets-terranova-qa-module-core/listings/b73ac33d-b2de-4656-a92e-a7f4bde98b26_thumbnail",
                "mimeType": "image/png"
            }
        ],
        "grossYield": 0.192,
        "madeVisibleAt": "2023-03-27T12:36:10Z"
    },
    {
        "id": 178,
        "addressDetails": {
            "addressLine1": "331 High street",
            "addressLine2": "",
            "city": "Spooky City",
            "postcode": "",
            "shortenedPostcode": "SW2",
            "country": "UK",
            "region": "London"
        },
        "propertyType": "terraced",
        "bedrooms": 3,
        "bathrooms": 3,
        "sizeSqFt": 200,
        "priceInCents": 9999900,
        "minimumDepositInCents": 999900,
        "estimatedDepositInCents": 1050000,
        "monthlyRentalIncomeInCents": 99900,
        "isTenanted": True,
        "isCashOnly": False,
        "isNewBuild": False,
        "isCompany": True,
        "isShareSale": True,
        "description": "Boo! You've found our ghost listing for this Halloween season. You might have fallen for our trick, but using our buy-to-let marketplace is a treat. Scroll through our properties for some scarily good yields.",
        "photos": [
            {
                "originalURL": "https://storage.googleapis.com/assets-terranova-qa-module-core/listings/ab08a0af-0a78-4244-8f9e-985a517c85b4",
                "standardURL": "https://storage.googleapis.com/assets-terranova-qa-module-core/listings/ab08a0af-0a78-4244-8f9e-985a517c85b4_standard",
                "thumbnailURL": "https://storage.googleapis.com/assets-terranova-qa-module-core/listings/ab08a0af-0a78-4244-8f9e-985a517c85b4_thumbnail",
                "mimeType": "image/jpeg"
            },
            {
                "originalURL": "https://storage.googleapis.com/assets-terranova-qa-module-core/listings/e4df5172-4bde-4d7b-b11e-4ed8258c2bc6",
                "standardURL": "https://storage.googleapis.com/assets-terranova-qa-module-core/listings/e4df5172-4bde-4d7b-b11e-4ed8258c2bc6_standard",
                "thumbnailURL": "https://storage.googleapis.com/assets-terranova-qa-module-core/listings/e4df5172-4bde-4d7b-b11e-4ed8258c2bc6_thumbnail",
                "mimeType": "image/jpeg"
            },
            {
                "originalURL": "https://storage.googleapis.com/assets-terranova-qa-module-core/listings/4650d79c-196e-4a15-83ec-a146f8dbf64d",
                "standardURL": "https://storage.googleapis.com/assets-terranova-qa-module-core/listings/4650d79c-196e-4a15-83ec-a146f8dbf64d_standard",
                "thumbnailURL": "https://storage.googleapis.com/assets-terranova-qa-module-core/listings/4650d79c-196e-4a15-83ec-a146f8dbf64d_thumbnail",
                "mimeType": "image/jpeg"
            },
            {
                "originalURL": "https://storage.googleapis.com/assets-terranova-qa-module-core/listings/8779e7e5-4181-45b1-9d0f-f41e8a15dcd6",
                "standardURL": "https://storage.googleapis.com/assets-terranova-qa-module-core/listings/8779e7e5-4181-45b1-9d0f-f41e8a15dcd6_standard",
                "thumbnailURL": "https://storage.googleapis.com/assets-terranova-qa-module-core/listings/8779e7e5-4181-45b1-9d0f-f41e8a15dcd6_thumbnail",
                "mimeType": "image/jpeg"
            }
        ],
        "grossYield": 0.119988,
        "madeVisibleAt": None
    },
    {
        "id": 183,
        "addressDetails": {
            "addressLine1": "1 Maidstone Road",
            "addressLine2": "",
            "city": "Maidstone",
            "postcode": "ME15 6AA",
            "shortenedPostcode": "ME15",
            "country": "UK",
            "region": "South East"
        },
        "propertyType": "apartment",
        "bedrooms": 1,
        "bathrooms": 1,
        "sizeSqFt": 1234,
        "priceInCents": 10000000,
        "minimumDepositInCents": 2500000,
        "estimatedDepositInCents": 2500000,
        "monthlyRentalIncomeInCents": 150000,
        "isTenanted": True,
        "isCashOnly": False,
        "isNewBuild": False,
        "isCompany": False,
        "isShareSale": False,
        "description": "Apartment in central Maidstone",
        "photos": [
            {
                "originalURL": "https://storage.googleapis.com/assets-terranova-qa-module-core/listings/2889f267-fd95-43fd-8745-45e4e02f1e59",
                "standardURL": "https://storage.googleapis.com/assets-terranova-qa-module-core/listings/2889f267-fd95-43fd-8745-45e4e02f1e59_standard",
                "thumbnailURL": "https://storage.googleapis.com/assets-terranova-qa-module-core/listings/2889f267-fd95-43fd-8745-45e4e02f1e59_thumbnail",
                "mimeType": "image/jpeg"
            }
        ],
        "grossYield": 0.18,
        "madeVisibleAt": None
    },
    {
        "id": 181,
        "addressDetails": {
            "addressLine1": "5 Canterbury Road",
            "addressLine2": "",
            "city": "Cantebury",
            "postcode": "CT1 1AA",
            "shortenedPostcode": "CT1",
            "country": "UK",
            "region": "South East"
        },
        "propertyType": "apartment",
        "bedrooms": 1,
        "bathrooms": 1,
        "sizeSqFt": 566,
        "priceInCents": 25000000,
        "minimumDepositInCents": 5000000,
        "estimatedDepositInCents": 6500000,
        "monthlyRentalIncomeInCents": 150000,
        "isTenanted": True,
        "isCashOnly": False,
        "isNewBuild": False,
        "isCompany": False,
        "isShareSale": False,
        "description": "Very slick apartment in Canterbury",
        "photos": [
            {
                "originalURL": "https://storage.googleapis.com/assets-terranova-qa-module-core/listings/6306344f-423f-4e67-be20-207bdb11eed8",
                "standardURL": "https://storage.googleapis.com/assets-terranova-qa-module-core/listings/6306344f-423f-4e67-be20-207bdb11eed8_standard",
                "thumbnailURL": "https://storage.googleapis.com/assets-terranova-qa-module-core/listings/6306344f-423f-4e67-be20-207bdb11eed8_thumbnail",
                "mimeType": "image/png"
            }
        ],
        "grossYield": 0.072,
        "madeVisibleAt": None
    }
] 
