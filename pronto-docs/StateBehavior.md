<!-- Auto-generated from JSON by GDScript docs maker. Do not edit this document directly. -->

# StateBehavior

**Extends:** [Behavior](../Behavior)

## Description

Each StateBehavior emits the signals [signal StateBehavior.entered] and [signal StateBehavior.exited] to communicate the state machine's state

Each StateBehavior emits the signals [signal StateBehavior.entered] and [signal StateBehavior.exited] to communicate the state machine's state

## Property Descriptions

### active

```gdscript
@export var active: bool = false
```

- **Setter**: `@active_setter`
- **Getter**: `@active_getter`

Modeles whether the state reacts to transitions at all. The sum of all [code]active[/code] variables is the state of the state machine Use this variable to determine the initial state.

## Method Descriptions

### enter

```gdscript
func enter()
```

Function that tells the state to become active. Works only if the state is not active yet.

### exit

```gdscript
func exit(target_state_name: String)
```

Function that tells the state to become inactive. Works only if the state is active. The [param transition_id] is forwarded to the [signal StateBehavior.exited] signal and can thus be used to determine which transition to trigger.

### line\_text\_function

```gdscript
func line_text_function(connection: Connection) -> Callable
```

Override of [method Behavior.line_text_function]. Used to display the node name of a target StateBehavior on a line

### lines

```gdscript
func lines()
```

Override of [method Behavior.lines] Used to add the State name below the icon

### icon\_texture

```gdscript
func icon_texture()
```

Override of the corresponding method in Behavior.gd Used to display the correct icon when the StateBehavior is active or inactive

## Signals

- signal entered(): Signal that gets emitted when the state becomes active
- signal exited(target_state_name): Signal that gets emitted when the state becomes inactive. Use [param transition_id] to determine in the transitions' condition which transition to trigger.
