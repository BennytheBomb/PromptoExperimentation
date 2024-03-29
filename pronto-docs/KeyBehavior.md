<!-- Auto-generated from JSON by GDScript docs maker. Do not edit this document directly. -->

# KeyBehavior

**Extends:** [Behavior](../Behavior)

## Description

Each KeyBehavior can react to exactly one key and emits signals corresponding to the user interactions with that key.

Each KeyBehavior can react to exactly one key and emits signals corresponding to the user interactions with that key.

## Property Descriptions

### key

```gdscript
@export var key: String
```

The key that the KeyBehavior reacts to. Its value has to be one of the keycodes generated by [method Event.as_text_keycode]. For special keys use 'Space' and 'Backslash' instead of ' ' or '\'

### is\_pressed

```gdscript
var is_pressed: bool = false
```

Shows whether the key is currently pressed

### pressed\_since

```gdscript
var pressed_since: int = 0
```

Shows the time in milliseconds that the key has been pressed Is [code]0[/code] as long as the key is not pressed.

## Method Descriptions

### lines

```gdscript
func lines()
```

Override of [method Behavior.lines] Used to add the [member KeyBehavior.key] below the icon

## Signals

- signal down(): Emitted in the [method Node._input] callback when the [member KeyBehavior.key] is pressed down
- signal up(): Emitted in the [method Node._input] callback when the [member KeyBehavior.key] is raised up
- signal toggled(down): Emitted with [signal KeyBehavior.down] and [signal KeyBehavior.up] [param down] tells in which direction the toggle happened
- signal pressed(): Emitted every frame as long as the [member KeyBehavior.key] is pressed
- signal just_down(): Emitted in the [method Node._input] callback the first moment, the down-event is catched.
- signal just_up(duration): Emitted in the [method Node._input] callback the first moment, the up-event is catched. [param duration] is the time in milliseconds that the key was down
