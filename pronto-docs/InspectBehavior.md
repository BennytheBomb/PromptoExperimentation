<!-- Auto-generated from JSON by GDScript docs maker. Do not edit this document directly. -->

# InspectBehavior

**Extends:** [Behavior](../Behavior)

## Description

## Constants Descriptions

### COOLDOWN\_LENGTH\_MS

```gdscript
const COOLDOWN_LENGTH_MS: int = 100
```

## Property Descriptions

### default\_property

```gdscript
var default_property = "position"
```

### default\_expression

```gdscript
var default_expression
```

### target

```gdscript
var target: Node2D
```

- **Getter**: `@target_getter`

### font\_size

```gdscript
var font_size = 10
```

- **Setter**: `@font_size_setter`
- **Getter**: `@font_size_getter`

### background\_color

```gdscript
var background_color = "(0, 0, 0, 0.2)"
```

- **Setter**: `@background_color_setter`

### color

```gdscript
var color = "(1, 1, 1, 1)"
```

- **Setter**: `@color_setter`
- **Getter**: `@color_getter`

### highlight\_color

```gdscript
var highlight_color: Color = "(1, 0, 0, 1)"
```

### shape\_rect

```gdscript
var shape_rect
```

### shape\_size

```gdscript
var shape_size
```

- **Setter**: `@shape_size_setter`

### size

```gdscript
var size
```

- **Getter**: `@size_getter`

### sticky\_transform

```gdscript
var sticky_transform
```

### sticky

```gdscript
var sticky: bool = false
```

- **Setter**: `@sticky_setter`
- **Getter**: `@sticky_getter`

### label

```gdscript
var label: RichTextLabel
```

### padding

```gdscript
var padding = 1
```

### shadow\_thickness

```gdscript
var shadow_thickness = 1
```

### items

```gdscript
var items: Array[Item]
```

## Method Descriptions

### get\_expression

```gdscript
func get_expression(i: int) -> String
```

### set\_expression

```gdscript
func set_expression(i: int, v: String)
```

### get\_property

```gdscript
func get_property(i: int) -> String
```

### set\_property

```gdscript
func set_property(i: int, v: String)
```

### update

```gdscript
func update()
```

### handles

```gdscript
func handles()
```

## Sub\-classes

### Item

#### Property Descriptions

### label

```gdscript
var label
```

### value

```gdscript
var value
```

### cooldown\_time

```gdscript
var cooldown_time: int = 0
```

### property

```gdscript
var property: String
```

### expression

```gdscript
var expression
```

### value\_string

```gdscript
var value_string: String
```

#### Method Descriptions

### update

```gdscript
func update(target: Node, index: int, inspect: InspectBehavior) -> bool
```

### add\_to\_label

```gdscript
func add_to_label(label: RichTextLabel, highlight_color: Color, should_truncate: bool = false)
```

### get\_display\_string

```gdscript
func get_display_string(should_truncate: bool = false) -> String
```

