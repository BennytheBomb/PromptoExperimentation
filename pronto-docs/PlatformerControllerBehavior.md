<!-- Auto-generated from JSON by GDScript docs maker. Do not edit this document directly. -->

# PlatformerControllerBehavior

**Extends:** [Behavior](../Behavior)

## Description

## Constants Descriptions

### Player

```gdscript
enum Player{Player_1 = 0, Player_2 = 1, Player_3 = 2}
```

Defines the available controls

## Property Descriptions

### player

```gdscript
@export var player: PlatformerControllerBehavior.Player = 0
```

Determines which controls (keys) are used. Which keys that are is defined in [member PlatformControllerBehavior.key_map]  See [enum PlatformControllerBehavior.Controls] for possible values

### jump\_velocity

```gdscript
@export var jump_velocity: float = 400
```

- **Setter**: `@jump_velocity_setter`

The speed with which the character jumps.

### horizontal\_velocity

```gdscript
@export var horizontal_velocity: float = 400
```

- **Setter**: `@horizontal_velocity_setter`

The speed with which the character moves sideways.

### coyote\_time

```gdscript
@export var coyote_time = 0.1
```

The amount of time after falling off a platform where the character can still jump, in seconds.

### jump\_buffer

```gdscript
@export var jump_buffer = 0.1
```

The amount of time a jump input will trigger a jump if the character is not touching the floor, in seconds.

### gravity\_paused

```gdscript
@export var gravity_paused: bool = false
```

- **Setter**: `@gravity_paused_setter`
- **Getter**: `@gravity_paused_getter`

### show\_trail

```gdscript
@export var show_trail: bool = false
```

If enabled, the parent leaves a trail of recent positions.

## Method Descriptions

### lines

```gdscript
func lines()
```

## Signals

- signal collided(last_collision): 
