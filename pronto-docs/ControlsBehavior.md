<!-- Auto-generated from JSON by GDScript docs maker. Do not edit this document directly. -->

# ControlsBehavior

**Extends:** [Behavior](../Behavior)

## Description

## Constants Descriptions

### Player

```gdscript
enum Player{Player_1 = 0, Player_2 = 1, Player_3 = 2}
```

Defines the available players

## Property Descriptions

### player

```gdscript
@export var player: ControlsBehavior.Player = 0
```

Determines which player these controls are for. This determines the keys that the controls react to. Which keys that are is defined in [member ControlsBehavior.key_map]  See [enum ControlsBehavior.Player] for possible values

### enable\_drag

```gdscript
var enable_drag = false
```

### held\_mouse\_buttons

```gdscript
var held_mouse_buttons
```

## Method Descriptions

### get\_held\_mouse\_buttons

```gdscript
func get_held_mouse_buttons()
```

## Signals

- signal left(): Emitted when the player's left key is pressed
- signal right(): Emitted when the player's right key is pressed
- signal up(): Emitted when the player's up key is pressed
- signal down(): Emitted when the player's down key is pressed
- signal direction(direction): Emitted when any of the player's movement keys is pressed.  [param direction] gives the direction as a normalized Vector2 depending on the keys that are pressed
- signal horizontal_direction(direction): Emitted when any of the player's horizontal movement keys is pressed  [param direction] gives the direction as [constant Vector2.LEFT] or [constant Vector2.RIGHT] or [constant Vector2.ZERO]
- signal vertical_direction(direction): Emitted when any of the player's vertival movement keys is pressed  [param direction] gives the direction as [constant Vector2.UP] or [constant Vector2.DOWN] or [constant Vector2.ZERO]
- signal mouse_down(pos, button): Emitted when a mouse button was pressed.  [param pos] gives the mouse position local to the viewport  [param button] gives the mouse button that was pressed down
- signal mouse_up(pos, button, duration): Emitted when a mouse button was raised.  [param pos] gives the mouse position local to the viewport  [param button] gives the mouse button that was raised  [param duration] gives the duration in milliseconds that the button was pressed
- signal mouse_move(pos): Emitted when the mouse moved.  [param pos] gives the mouse position local to the viewport
- signal mouse_drag(pos): Emitted when the mouse is moved while it is pressed.  [param pos] gives the mouse position local to the viewport
- signal mouse_down_global(pos, button): Emitted when a mouse button was pressed.  [param pos] gives the global mouse position  [param button] gives the mouse button that was pressed down
- signal mouse_up_global(pos, button, duration): Emitted when a mouse button was raised.  [param pos] gives the global mouse position  [param button] gives the mouse button that was raised  [param duration] gives the duration in milliseconds that the button was pressed
- signal mouse_move_global(pos): Emitted when the mouse moved.  [param pos] gives the global mouse position
- signal mouse_drag_global(pos): Emitted when the mouse is moved while it is pressed.  [param pos] gives the global mouse position
