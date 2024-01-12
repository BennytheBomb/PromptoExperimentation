<!-- Auto-generated from JSON by GDScript docs maker. Do not edit this document directly. -->

# ValueBehavior

**Extends:** [Behavior](../Behavior)

## Description

## Constants Descriptions

### BUFFER\_PCT

```gdscript
const BUFFER_PCT: float = 0.1
```

### WIDTH

```gdscript
const WIDTH: int = 120
```

## Property Descriptions

### value\_init

```gdscript
var value_init = false
```

### selectType

```gdscript
@export var selectType: String = "Float"
```

- **Setter**: `@selectType_setter`

### float\_min

```gdscript
var float_min: float = 0
```

- **Setter**: `@float_min_setter`

Min value for the float

### float\_max

```gdscript
var float_max: float = 100
```

- **Setter**: `@float_max_setter`

Max value for the float

### float\_default

```gdscript
var float_default: float = 0
```

### float\_step\_size

```gdscript
var float_step_size: float = 1
```

- **Setter**: `@float_step_size_setter`

### float\_value

```gdscript
var float_value: float = 0
```

- **Setter**: `@float_value_setter`

### enum\_choices

```gdscript
var enum_choices: Array[String]
```

- **Setter**: `@enum_choices_setter`

### enum\_default\_index

```gdscript
var enum_default_index: int
```

### enum\_value

```gdscript
var enum_value: String
```

- **Setter**: `@enum_value_setter`

### bool\_value

```gdscript
var bool_value: String = "TRUE"
```

- **Setter**: `@bool_value_setter`

### bool\_default

```gdscript
var bool_default: bool
```

## Method Descriptions

### handles

```gdscript
func handles()
```

## Signals

- signal value_changed(value): 

## Sub\-classes

### DropPropertyPrompt

#### Property Descriptions

### editor\_interface

```gdscript
var editor_interface
```

#### Method Descriptions

### \_init

```gdscript
func _init(editor_interface) -> DropPropertyPrompt
```

### empty\_script

```gdscript
func empty_script(a: Array, expr: String, return_value: bool)
```

