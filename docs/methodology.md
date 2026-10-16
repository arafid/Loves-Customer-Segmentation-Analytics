# Methodology

## Source tables

The analysis uses five source tables:

1. `DRIVER_LOOKUP` — driver attributes, segment group, communication preferences, and most-visited store.
2. `DRIVER_3_YEAR_AGGS` — three-year driver-level sales, fuel, merchandise, transaction, and visit measures.
3. `DRIVER_MONTHLY_CAMPAIGNS` — campaign goals, rewards, joins, achievements, send channel, campaign-month behavior, prior-month behavior, and campaign cost.
4. `DRIVER_MONTHLY_PRODUCT_SALES` — monthly sales totals by driver and product type.
5. `STORE_LOOKUP` — store codes, division, state, and location attributes.

## Core joins

- Driver-level tables are joined with `DRIVER_ID`.
- `DRIVER_LOOKUP.MOSTVISITEDSTORE` is joined to `STORE_LOOKUP.STORE_CODE`.
- Product sales are aligned to campaign months using `DRIVER_ID` and month.

## KPI definitions

### Join rate

`joined campaigns / campaigns with a valid JOINED status`

This reproduces the segment-level rates shown in the final case write-up.

### Achieve rate

`achieved campaigns / joined campaigns`

### Channel success rate

`achieved campaigns / joined campaigns`

### Incremental campaign measures

- Incremental fuel gallons = campaign-month gallons − prior-month gallons
- Incremental visits = campaign-month visits − prior-month visits
- Incremental merchandise sales = campaign-month merchandise sales − prior-month merchandise sales

### Average gallons per visit

`TOTALFUELGALLONS / TOTALFUELTRANSACTIONS`

The project uses this metric to test whether driver age meaningfully explains fueling behavior.

## Analysis sequence

1. Validate keys and table coverage.
2. Engineer incremental campaign measures.
3. Compare campaign performance.
4. Merge campaign records to customer segments.
5. Compute join and achievement KPIs.
6. Compare total and monthly product sales by segment.
7. Measure send-channel success.
8. Summarize historical campaign performance.
9. Connect customers to most-visited-store divisions.
10. Test age against average gallons per visit.
