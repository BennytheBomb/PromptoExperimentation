<!-- Auto-generated from JSON by GDScript docs maker. Do not edit this document directly. -->

# CameraShakeBehavior

**Extends:** [Behavior](../Behavior)

## Description

The functionality was adapted from https://kidscancode.org/godot_recipes/3.x/2d/screen_shake/

The functionality was adapted from https://kidscancode.org/godot_recipes/3.x/2d/screen_shake/

## Property Descriptions

### decay

```gdscript
@export var decay = 0.8
```

Determines how quickly the shake stops. Values must lie in [0, 1]. [code]0[/code] means it will never stop and [code]1[/code] will stop it instantly.

### max\_offset

```gdscript
@export var max_offset = "(100, 75)"
```

The maximum horizontal and vertical shake in pixels

### max\_roll

```gdscript
@export var max_roll = 0.1
```

The maximum rotation in radiants

### trauma

```gdscript
var trauma = 0
```

The current shake strength

### noise\_y

```gdscript
var noise_y = 0
```

### noise

```gdscript
var noise
```

## Method Descriptions

### add\_trauma

```gdscript
func add_trauma(amount)
```

### n

```gdscript
func n(factor: float)
```

