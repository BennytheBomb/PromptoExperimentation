<!-- Auto-generated from JSON by GDScript docs maker. Do not edit this document directly. -->

# DragBehavior

**Extends:** [Behavior](../Behavior)

## Description

## Property Descriptions

### button\_mask

```gdscript
@export var button_mask: int = 1
```

Mouse button mask for pick/drop. Only selected buttons can pick up the parent node.

### emit\_mouse\_position

```gdscript
@export var emit_mouse_position = false
```

If true, picked, dropped and dragged events emit the mouse position instead of the parent node's position.

### last\_position

```gdscript
var last_position: Vector2
```

### start\_position

```gdscript
var start_position: Vector2
```

### is\_hovering\_parent

```gdscript
var is_hovering_parent = false
```

## Method Descriptions

### event\_position

```gdscript
func event_position(position: Vector2) -> Vector2
```

Choose position based on emit_mouse_position

## Signals

- signal mouse_entered(position): Emitted when the mouse enters the parent node.  [param position] is the global position where the mouse entered the parent node
- signal mouse_exited(position): Emitted when the mouse leaves the parent node.  [param position] is the global position where the mouse exited the parent node
- signal picked(position): Emitted when picked up by clicking  [param position] is the global position of the parent node.
- signal dropped(position, start): Emitted when dropping  [param position] is the global position of the parent node.  [param  start_position] is the parent's global position at the start of dragging
- signal dragged(position, start, last): Emitted during dragging  [param position] is the global position of the parent node  [param start_position] is the global position at which the parent node was started to be dragged  [param last_position] is the global position where the last movement of the parent started
