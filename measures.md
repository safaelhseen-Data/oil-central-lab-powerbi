# DAX Measures

Reference list of the main measures used in the report. Table and column names follow the model (`public finance`, `public results`, `public samples`).

## Finance (`public finance`)

```dax
Total Invoiced = SUM('public finance'[invoice_amount])

Total Paid = SUM('public finance'[paid_amount])

Total Outstanding = [Total Invoiced] - [Total Paid]

Collection Rate % =
DIVIDE([Total Paid], [Total Invoiced], 0)
```

`Total Paid` format string: `"SAR" #,##0.00`

Payment method share (used in *Share of Total Paid by Payment Method*):

```dax
Payment Share % =
DIVIDE(
    [Total Paid],
    CALCULATE([Total Paid], ALL('public finance'[payment_method]))
)
```

## Samples (`public samples`)

```dax
Total Sample Units = SUM('public samples'[sample_quantity])
```

## Legal Referrals

Cases are counted as unique Sample IDs in `public results`:

```dax
Legal Cases (IDs) =
CALCULATE(
    DISTINCTCOUNT('public results'[sample_id]),
    'public results'[Legal Status] = "Referred to Legal Administration"
)
```

Sample units belonging to those cases:

```dax
Legal Sample Units =
SUMX(
    FILTER(
        'public samples',
        CALCULATE(
            COUNTROWS('public results'),
            TREATAS(VALUES('public samples'[sample_id]), 'public results'[sample_id]),
            'public results'[Legal Status] = "Referred to Legal Administration"
        ) > 0
    ),
    'public samples'[sample_quantity]
)
```

Value of legal cases, before VAT:

```dax
Legal_Transfer_Value =
CALCULATE(
    SUM('public samples'[sample_price_before_vat]),
    FILTER(
        'public results',
        'public results'[Legal Status] = "Referred to Legal Administration"
    )
)
```

## Turnaround (`public results`)

```dax
Avg Delay - All Samples (Days) =
AVERAGE('public results'[Delay])

Avg Delay When Delayed =
CALCULATE(
    AVERAGE('public results'[Delay]),
    'public results'[Delay] > 0
)
```

`% Delayed` is the share of cases with a delay greater than zero (17.65% in the current data).

## Notes

- Column names such as `invoice_amount` and `payment_method` are assumed; adjust them to match the model if they differ.
- `Legal Sample Units` uses `TREATAS` because the relationship between `public results` and `public samples` does not propagate filters on its own.
