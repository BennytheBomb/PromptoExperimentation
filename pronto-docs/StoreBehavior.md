<!-- Auto-generated from JSON by GDScript docs maker. Do not edit this document directly. -->

# StoreBehavior

**Extends:** [Behavior](../Behavior)

## Description

## Property Descriptions

### fields

```gdscript
@export var fields: Dictionary
```

Mapping from field names to expressions initializing each field

### data

```gdscript
var data
```

Mapping from field names to current values

## Method Descriptions

### inc

```gdscript
func inc(prop: String, amount = 1)
```

### dec

```gdscript
func dec(prop: String, amount = 1)
```

### put

```gdscript
func put(prop: String, value: Variant)
```

### update

```gdscript
func update(prop: String, call: Callable)
```

### at

```gdscript
func at(prop: String, default = null)
```

### at\_and\_remove

```gdscript
func at_and_remove(prop: String, default = null)
```

### has

```gdscript
func has(key: String)
```

### lines

```gdscript
func lines()
```

## Signals

- signal sync(prop, value, text): Emitted on change and when the store first becomes ready. Also provides a stringified version of the value.
- signal changed(prop, value): Emitted whenever the property changes
