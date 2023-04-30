```
counts = dataset.count_values("ground_truth.label")
```

```
match = F("label").is_in(("cat", "dog"))
unique_view = dataset.match(
    F("predictions.detections").filter(match).length() > 0
)
```


```
if dataset.get_field(label_field+"_"+detections_field) is not None:
  dataset.rename_sample_field(label_field+"_"+detections_field,detections_field)
```

```
len(dataset.sort_by("eval_predictions_fp", reverse=True).filter_labels("predictions", F("eval_predictions") == "fp"))
```

```
dataset.take(1).first()
```

```
dataset.match(F("eval_k") == False)
```

```
results.print_report(classes=classes)
```

```
dataset.list_evaluations()
```

