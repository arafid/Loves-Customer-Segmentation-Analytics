# Data Dictionary

This is a project-level dictionary of the fields used in the portfolio analysis, not an exhaustive dictionary of every source column.

## DRIVER_LOOKUP

| Field | Use |
|---|---|
| `DRIVER_ID` | Primary driver key |
| `SEGMENTGROUP` | Customer segment: NoDiscount, SmallDiscount, MediumDiscount, LargeDiscount |
| `BIRTHDATE` | Used to calculate driver age |
| `MOSTVISITEDSTORE` | Linked to `STORE_LOOKUP.STORE_CODE` |
| `STATE` | Driver/home-state field used in the submitted state analysis |

## DRIVER_3_YEAR_AGGS

| Field | Use |
|---|---|
| `DRIVER_ID` | Driver key |
| `TOTALFUELGALLONS` | Three-year fuel gallons |
| `TOTALFUELTRANSACTIONS` | Used to calculate average gallons per visit |
| Total sales / merchandise / visit measures | Customer value and behavior analysis |

## DRIVER_MONTHLY_CAMPAIGNS

| Field | Use |
|---|---|
| `DRIVER_ID` | Driver key |
| `AGGNAME` | Campaign type: DEF Extra, Gallons Extra, Merch Extra |
| `GOAL` | Campaign goal |
| `REWARD` | Reward value |
| `JOINED` | Campaign participation indicator |
| `ACHIEVE` | Goal achievement indicator |
| `CAMPAIGN_COST` | Campaign cost |
| `SEND_CHANNEL` | Email, Push, Receipt, SMS |
| `CAMPAIGNMONTHFUELGALLONS` | Campaign-month fuel gallons |
| `PRIORMONTHFUELGALLONS` | Prior-month fuel gallons |
| `CAMPAIGNMONTHMERCHSALES` | Campaign-month merchandise sales |
| `PRIORMONTHMERCHSALES` | Prior-month merchandise sales |
| `CAMPAIGNMONTHVISITS` | Campaign-month visits |
| `PRIORMONTHVISITS` | Prior-month visits |

## DRIVER_MONTHLY_PRODUCT_SALES

| Field | Use |
|---|---|
| `DRIVER_ID` | Driver key |
| `TRANSACTION_MONTH` | Month of product sales |
| `PRODUCTTYPE` | Fuel, Merch, Other |
| `SALESTOTAL` | Sales amount |

## STORE_LOOKUP

| Field | Use |
|---|---|
| `STORE_CODE` | Store key |
| `DIVISION` | Regional division used for geographic comparison |
| `STATE` | Store state |
