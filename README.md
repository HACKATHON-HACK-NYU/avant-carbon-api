## Inspiration
In order to create the overall idea behind the app, the team got inspiration from Mastercard's Priceless Planet Coalition initiative.  Mastercard offers a feature that enables users to have a positive impact on the planet every day by allowing the users to understand their carbon impact and how much carbon emissions they contribute every day.  They are able to view their carbon footprint across various spending categories and have access to a general list of tips for reducing their impact.

The idea behind Avant Carbon was to build an app for fashion credit cardholders.  Our app is useful because we offer sustainability tips within the fashion and beauty fields.  We are targeting fashionistas because the fashion and beauty industries are some of the biggest contributors with about 10% of global greenhouse gas emissions and consume “more energy than aviation and shipping”.   According to a 2020 McKinsey Fashion On Climate report, the global fashion industry produced around "2.1 billion tonnes of GHG emissions in 2018; equivalent to the combined annual GHG emissions of France, Germany, and the United Kingdom".
## What it does
Allow users to have an insight into their carbon emissions contributions due to purchases in the fashion and beauty industry through the use of credit card statements.
## How we built it
Python, React-native, Figma, Django and rest-framework, MongoDB

## Challenges we ran into
Machine Learning
- The categorization of purchases isn't specific enough - can't distinguish between shoes and clothing. For example, a transaction at H&M.
others
- Avant Carbon doesn't have the research for data on the average carbon output per dollar spent in skincare products or beauty products, so we currently only give the estimated carbon output produced by the clothing and shoes the user buys, not including other items.
## Accomplishments that we're proud of
Our app uses a temporal-agnostic statistical model that estimates the non-negative distribution of [$ spent in category X in a given week] using machine learning on past data, then labels the current week to be "a significant increase" if the $ spent is higher than the 75th percentile of the distribution. Since this suggests a significant uptick in purchasing in category X we can proceed to show the carbon-reducing tips related to category X.

## What we learned
Having to come up with an effective idea and build an app in under three days is definitely a challenge.  Some of the things that we as a team learned 

## What's next for Avant Carbon
In the future, some features that the team will like to implement for Avant Carbon is the ability to build business expertise in order to partner with companies with the end goal of having a direct connection between the small incentives users get from recycling and donating to stores (ex. Goodwill, bottle-recycling services) to a donations tab in the app where users would be able to donate to a sustainability cause of their choice.

Avant Carbon wants to empower consumers to contribute to the efforts by turning purchases into meaningful actions to help save the planet.

## Team
- Backend: Dev Raj Singh
- Frontend & UI: Kaitlyn Heard
- Backend: Timothy Xu
- UI: Dariana Gonzalez
