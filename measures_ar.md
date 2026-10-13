# مقاييس DAX

قائمة بأهم المقاييس المستخدمة في التقرير. أسماء الجداول والأعمدة حسب النموذج (`public finance` و`public results` و`public samples`). أكواد DAX تبقى بالإنجليزية كما هي.

## المالية (`public finance`)

```dax
Total Invoiced = SUM('public finance'[invoice_amount])

Total Paid = SUM('public finance'[paid_amount])

Total Outstanding = [Total Invoiced] - [Total Paid]

Collection Rate % =
DIVIDE([Total Paid], [Total Invoiced], 0)
```

صيغة تنسيق `Total Paid`: `"SAR" #,##0.00`

حصة طريقة الدفع (تُستخدم في مخطط *Share of Total Paid by Payment Method*):

```dax
Payment Share % =
DIVIDE(
    [Total Paid],
    CALCULATE([Total Paid], ALL('public finance'[payment_method]))
)
```

## العينات (`public samples`)

```dax
Total Sample Units = SUM('public samples'[sample_quantity])
```

## الإحالات القانونية

تُعدّ الحالات كمعرّفات عينات فريدة من جدول `public results`:

```dax
Legal Cases (IDs) =
CALCULATE(
    DISTINCTCOUNT('public results'[sample_id]),
    'public results'[Legal Status] = "Referred to Legal Administration"
)
```

وحدات العينات التابعة لهذه الحالات:

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

قيمة الحالات القانونية قبل الضريبة:

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

## زمن الإنجاز والتأخير (`public results`)

```dax
Avg Delay - All Samples (Days) =
AVERAGE('public results'[Delay])

Avg Delay When Delayed =
CALCULATE(
    AVERAGE('public results'[Delay]),
    'public results'[Delay] > 0
)
```

مقياس `% Delayed` هو نسبة الحالات التي تأخيرها أكبر من صفر (17.65% في البيانات الحالية).

## ملاحظات

- أسماء أعمدة مثل `invoice_amount` و`payment_method` تقديرية؛ عدّليها لتطابق النموذج عندك إن اختلفت.
- يستخدم `Legal Sample Units` الدالة `TREATAS` لأن العلاقة بين `public results` و`public samples` لا تنقل الفلاتر من تلقاء نفسها.
