```
results = fob.compute_similarity(dataset, brain_key="img_sim")
results.find_unique(100)
vis_results = fob.compute_visualization(dataset, brain_key="img_vis")

plot = results.visualize_unique(visualization=vis_results)
```


```
dataset.list_brain_runs()
dataset.load_brain_view(dataset.list_brain_runs()[0])
dataset.load_brain_results("image_embeddings")

```
```
embeddings = dataset.compute_embeddings(model) # process takes time
results = fob.compute_visualization( dataset,
    embeddings=embeddings,
    num_dims=2,
    brain_key="image_embeddings",
    verbose=True,
    seed=51,)
plot = results.visualize(
    labels="ground_truth.label",
    labels_title="blabblabla",
    axis_equal=True,
)
plot.show(height=512)

# Attach plot to session
session_windows.plots.attach(plot)
```
```
null_view.match(F("uniqueness").is_null())
null_view.match(F("uniqueness").is_array())
null_view.match(F("uniqueness").is_number())

F("uniqueness").contains([])
F("uniqueness").contains([], all=True)#returns those samples that contain both dogs and cats
contains_str("ze")

```


```
dataset.list_evaluations()
dataset.get_evaluation_info("eval")
```

```
results.mAP()
```

```
results.plot_pr_curves(classes=)
```
```
result.print_report(classes=)
```
```
ds.get_field_schema().keys()
```


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

