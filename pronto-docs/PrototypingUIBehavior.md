<!-- Auto-generated from JSON by GDScript docs maker. Do not edit this document directly. -->

# PrototypingUIBehavior

**Extends:** [Behavior](../Behavior)

## Description

## Property Descriptions

### show\_in\_export

```gdscript
@export var show_in_export = true
```

If true, the PrototypingUI will be visible in the export

### include\_all\_values

```gdscript
@export var include_all_values = true
```

If [code]true[/code], all values in the scene are added to the menu (if they are visible) [br]If [code]false[/code], only children ValueBehaviors are added to the menu (if they are visible)

### minimized

```gdscript
@export var minimized: bool = false
```

If [code]true[/code] the PrototypingUI starts minimized.

### panel\_size

```gdscript
@export var panel_size: Vector2 = "(300, 200)"
```

- **Setter**: `@panel_size_setter`

### panel

```gdscript
var panel: PanelContainer
```

### muted\_gray

```gdscript
var muted_gray: Color = "(0.69, 0.69, 0.69, 1)"
```

### vbox

```gdscript
var vbox: VBoxContainer
```

### header

```gdscript
var header: HBoxContainer
```

### start

```gdscript
var start: Vector2
```

### init\_position

```gdscript
var init_position: Vector2
```

### is\_moving

```gdscript
var is_moving: bool
```

### is\_resizing

```gdscript
var is_resizing: bool
```

### resize\_x

```gdscript
var resize_x: bool
```

### resize\_y

```gdscript
var resize_y: bool
```

### initial\_size

```gdscript
var initial_size: Vector2
```

### grab\_threshold

```gdscript
var grab_threshold: int = 30
```

### resize\_threshold

```gdscript
var resize_threshold: int = 10
```

## Method Descriptions

### maybe\_add\_config

```gdscript
func maybe_add_config(node: Node)
```

### create\_ui\_for\_value

```gdscript
func create_ui_for_value(value: ValueBehavior)
```

### create\_ui\_for\_value\_enum

```gdscript
func create_ui_for_value_enum(value: ValueBehavior)
```

### create\_ui\_for\_value\_bool

```gdscript
func create_ui_for_value_bool(value: ValueBehavior)
```

### create\_ui\_for\_code

```gdscript
func create_ui_for_code(code: CodeBehavior)
```

### create\_ui\_slider\_for\_value\_float

```gdscript
func create_ui_slider_for_value_float(value: ValueBehavior)
```

### create\_minimizing\_button

```gdscript
func create_minimizing_button()
```

### create\_header

```gdscript
func create_header()
```

### handle\_size\_button\_click

```gdscript
func handle_size_button_click(button: Button, initial: bool = false)
```

### handle\_value\_bool\_change

```gdscript
func handle_value_bool_change(index: int, value: ValueBehavior, optionButton: OptionButton)
```

### handle\_value\_enum\_change

```gdscript
func handle_value_enum_change(index: int, value: ValueBehavior, optionButton: OptionButton)
```

### handle\_update\_value\_float\_change

```gdscript
func handle_update_value_float_change(new_value: float, value: ValueBehavior, label_current: Label, slider: HSlider)
```

### handles

```gdscript
func handles()
```

