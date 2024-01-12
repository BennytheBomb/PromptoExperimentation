<!-- Auto-generated from JSON by GDScript docs maker. Do not edit this document directly. -->

# BindBehavior

**Extends:** [Behavior](../Behavior)

## Description

## Property Descriptions

### evaluate

```gdscript
@export var evaluate: ConnectionScript
```

Script to evaluate to find the current property value to set.

### to\_prop

```gdscript
@export var to_prop: String
```

Property of the parent node to write the result of evaluate to.

### one\_shot

```gdscript
@export var one_shot: bool = false
```

Update only when the update() function is called.

## Method Descriptions

### update

```gdscript
func update()
```

### lines

```gdscript
func lines()
```

### wants\_expression\_inspector

```gdscript
func wants_expression_inspector(property_name)
```

