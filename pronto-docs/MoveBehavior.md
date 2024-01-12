<!-- Auto-generated from JSON by GDScript docs maker. Do not edit this document directly. -->

# MoveBehavior

**Extends:** [Behavior](../Behavior)

## Description

## Property Descriptions

### max\_velocity

```gdscript
@export var max_velocity = 500
```

Maximum velocity the parent will reach while on the ground

### acceleration

```gdscript
@export var acceleration = 100
```

Acceleration added to the velocity while being asked to move while on the ground

### friction

```gdscript
@export var friction = 20
```

Friction applied to velocity while on the ground

### gravity

```gdscript
@export var gravity = 0
```

Gravity applied to parent. Set to zero to disable falling.

### friction\_air

```gdscript
@export var friction_air = 0
```

Friction applied to velocity while in the air

### acceleration\_air

```gdscript
@export var acceleration_air = 0
```

Acceleration added to the velocity while being asked to move while in the air

### rotated

```gdscript
@export var rotated = true
```

Whether the velocity is applied according to the parent's local rotation or in global coordinates.

### rotation\_speed

```gdscript
@export var rotation_speed = 300
```

Speed at which the parent rotates when asked to.

### rotate\_velocity

```gdscript
@export var rotate_velocity = true
```

Whether to also rotate the velocity vector when the character is rotated. Feels like the parent can drift when disabled.

### velocity

```gdscript
var velocity = "(0, 0)"
```

## Method Descriptions

### is\_on\_floor

```gdscript
func is_on_floor()
```

### add\_velocity

```gdscript
func add_velocity(velocity: Vector2)
```

### set\_velocity\_y

```gdscript
func set_velocity_y(num: float)
```

### set\_velocity\_x

```gdscript
func set_velocity_x(num: float)
```

### set\_veleocity

```gdscript
func set_veleocity(velocity: Vector2)
```

### set\_velocity

```gdscript
func set_velocity(velocity: Vector2)
```

### move\_direction

```gdscript
func move_direction(direction: Vector2)
```

### move\_left

```gdscript
func move_left()
```

### move\_right

```gdscript
func move_right()
```

### move\_down

```gdscript
func move_down()
```

### move\_up

```gdscript
func move_up()
```

### move\_toward

```gdscript
func move_toward(pos: Vector2)
```

### rotate\_left

```gdscript
func rotate_left()
```

### rotate\_right

```gdscript
func rotate_right()
```

### rotate\_direction

```gdscript
func rotate_direction(direction)
```

### lines

```gdscript
func lines()
```

## Signals

- signal touched_floor(velocity): Only available for [class CharacterBody2D] parents: the character touched the floor.
