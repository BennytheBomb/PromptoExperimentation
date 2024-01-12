<!-- Auto-generated from JSON by GDScript docs maker. Do not edit this document directly. -->

# CollisionBehavior

**Extends:** [Behavior](../Behavior)

## Description

## Property Descriptions

### limit\_to\_group

```gdscript
@export var limit_to_group: String = ""
```

Set this to a group label in order to limit collisions to nodes in that group. Leave it at [code]""[/code] to collide with every node.

### screen\_entered\_emitted

```gdscript
var screen_entered_emitted = false
```

### screen\_exited\_emitted

```gdscript
var screen_exited_emitted = false
```

## Method Descriptions

### on\_collision

```gdscript
func on_collision(other: Node)
```

### is\_valid\_parent

```gdscript
func is_valid_parent()
```

### lines

```gdscript
func lines()
```

## Signals

- signal collided(other, direction): Gets emitted when the parent collides with another node.  [param other] is the node that the parent collided with  [param direction] is the normalized direction in which the [param other] is from the parent node's position
- signal screen_exited(): 
- signal screen_entered(): 
