# Digital-Blockchain-Will


We strive to design and deploy a smart contract designed to tokenize someone’s assets when someone dies and distribute them in accordance with their final wishes laid out in a will.

**User Stories**

"The process of organizing my affairs to ensure everything in my will is carried out is a logistically long and costly process, involving hiring several intermediaries."

"Legally having to go through the probate process is costly and logistically burdensome. i'd rather use the remaining time left to spend with my family."

"I hope my descendants don't end up finding out who's getting what, as this could foster feelings of resentment and jealousy." 

"I worry that the assets in my will may not be appraised correctly, as housing market prices may fluctuate between now and when I die. This could create in unfortunate situations where some of my children are unfairly allocated less than I intended. It could also lead to potential taxation and IRS penalties."

**Acceptance Criteria**

This product will streamline the process, by offering a cheaper end-to-end service that has users covered from the will writing to distributing the assets in exact accordance with users' wishes at the moment of death. User authentication and privacy is guaranteed by relying on blockchain technology.

The use of a legal probate might be voided, as the secure digital certificate can be used to prove that the will is indeed the last testament of the deceased. Privacy will be ensured by the product. 

At the moment that the deceased's expiration is registered, the smart contract will execute, spurring each person listed on the will to receive an email with a unique private key allowing them to view their digital assets. The assets can be distributed anonymously, such that beneficiaries can only view their own assets and not view what others are bequeathed. This anonymous form of delivery may help prevent future disputes that often end up tearing families apart. 

The fair price appraisal will be kept up to date, as our product can update its appraisals in real time by connecting to digital appraisal providers for various assets like Zillow for real estate, Quandl for financial assets, and Art Price for art.

**Tasks**

This product will streamline the process, by offering a cheaper end-to-end service that has users covered from the will writing to distributing the assets in exact accordance with users' wishes at the moment of death. User authentication and privacy is guaranteed by relying on blockchain technology. The use of a legal probate might be voided, as the secure digital certificate can be used to prove that the will is indeed the last testament of the deceased. Privacy will be ensured by the product. At the moment that the deceased's expiration is registered, the smart contract will executing, spurring each person listed on the will to receive an email with a unique private key allowing them to view their digital assets. The assets can be distributed anonymously, such that beneficiaries can only view their own assets and not view what others are bequeathed. This anonymous form of delivery may help prevent future disputes that often end up tearing families apart. The fair price appraisal will be kept up to date, as our product can update its appraisals in real time by connecting to digital appraisal providers for various assets like Zillow for real estate, Quandl for financial assets, and Art Price for art.

**Workflow**

The customer first relays their social security number to verify they are who they say they are. Then they relay their deeds/proofs of ownership to verify that they do indeed own the assets/properties they claim to own. This information will be stored in a SQL database and will be verified by the service provider, via manually cross-referencing public records. Once we [the provider] is able to corroborate this given information, we then retrieve the customer's information from the database and feed the customer's SSN into a hashing function to produce a uniquely identifying hexadecimal string.

** Attributes**

-Value 
-Asset
-Name
-Date of Birth



**Division of Labor**

Vishal: Frontend Python

Bethel: Conversion to Stablecoin/Addressing Ethereum Fluctuations


