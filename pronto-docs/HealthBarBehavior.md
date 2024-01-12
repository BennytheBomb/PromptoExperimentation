<!-- Auto-generated from JSON by GDScript docs maker. Do not edit this document directly. -->

# HealthBarBehavior

**Extends:** [Behavior](../Behavior)

## Description

It communicates the current live and the death via the signals [signal HealthBehavior.changed] and [signal HealthBehavior.death].

It communicates the current live and the death via the signals [signal HealthBehavior.changed] and [signal HealthBehavior.death].

## Constants Descriptions

### LABEL

```gdscript
enum LABEL{None = 0, Health = 1, Fraction = 2, Percentage = 3}
```

This enum defines how the label is supposed to be displayed.

## Property Descriptions

### max

```gdscript
@export var max: int = 100
```

- **Setter**: `@max_setter`

The maximum health value.

### current

```gdscript
@export var current: int = 100
```

- **Setter**: `@current_setter`

The current health value (cannot exceed max).

### healthbar\_size

```gdscript
@export var healthbar_size = "(50, 5)"
```

- **Setter**: `@healthbar_size_setter`

The size of the displayed healthbar.

### label

```gdscript
@export var label: HealthBarBehavior.LABEL = 1
```

- **Setter**: `@label_setter`

The style for displaying the current health as text inside the healthbar.

### background\_color

```gdscript
@export var background_color = "(0.251, 0.251, 0.251, 0.502)"
```

- **Setter**: `@background_color_setter`

The background color of the healthbar.

### text\_color

```gdscript
@export var text_color = "(1, 1, 1, 1)"
```

- **Setter**: `@text_color_setter`

The text color of the healthbar.

### progress\_gradient

```gdscript
@export var progress_gradient: Gradient
```

- **Setter**: `@progress_gradient_setter`

The progress_gradient is used for coloring the HealthBar according to the current health. The current color is chosen according to the value of [code]current/max[/code].

### invulnerable

```gdscript
@export var invulnerable = false
```

- **Setter**: `@invulnerable_setter`

If invulnerable the player cannot take damage via the [code]damage()[/code] method. [br]However, [code]set_health()[/code] will still work!

### allow\_healing\_when\_invulnerable

```gdscript
@export var allow_healing_when_invulnerable = false
```

If [i]false[/i], the player will not heal with [code]heal()[/code] or [code]heal_full()[/code] when invulnerable. [br]If [i]true[/i], the player will heal as usual even when he is invulnerable.

### invulnerability\_color

```gdscript
@export var invulnerability_color = "(0.8549, 0.6471, 0.1255, 1)"
```

- **Setter**: `@invulnerability_color_setter`

### size

```gdscript
var size: Vector2
```

- **Getter**: `@size_getter`

The height and width of the health bar

## Method Descriptions

### damage

```gdscript
func damage(amount)
```

Reduces the current health value by the given [code]amount[/code].

### heal

```gdscript
func heal(amount)
```

Increases the current health value by the given [code]amount[/code].

### heal\_full

```gdscript
func heal_full()
```

Sets the current health value to max.

### set\_health

```gdscript
func set_health(value)
```

Sets the current health value to the given [code]value[/code].

### show\_icon

```gdscript
func show_icon()
```

### handles

```gdscript
func handles()
```

## Signals

- signal changed(health): Emitted when the health value is changed.
- signal death(): Emitted when the health value drops to zero or below.
