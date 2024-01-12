<!-- Auto-generated from JSON by GDScript docs maker. Do not edit this document directly. -->

# CodeBehavior

**Extends:** [Behavior](../Behavior)

## Description

## Property Descriptions

### arguments

```gdscript
@export var arguments: PackedStringArray
```

- **Setter**: `@arguments_setter`
- **Getter**: `@arguments_getter`

The names of the arguments that the code receives. Those can be accessed in [member CodeBehavior.evaluate].

### evaluate

```gdscript
@export var evaluate: ConnectionScript
```

The Code that gets executed when the [method CodeBehavior.execute] method is called.

## Method Descriptions

### lines

```gdscript
func lines()
```

### execute

```gdscript
func execute(args: Array = null)
```

Executes the code provided in [member CodeBehavior.evaluate] and emits the [signal CodeBehavior.after] signal afterwards.

### wants\_expression\_inspector

```gdscript
func wants_expression_inspector(property_name)
```

## Signals

- signal after(result): Emittet when the execution of the code returns. [param result] is the result of the execution.
