<!-- Auto-generated from JSON by GDScript docs maker. Do not edit this document directly. -->

# AlwaysBehavior

**Extends:** [Behavior](../Behavior)

## Description

See [signal AlwaysBehavior.always] and [signal AlwaysBehavior.physics_always] for a description of which signal to listen to.

See [signal AlwaysBehavior.always] and [signal AlwaysBehavior.physics_always] for a description of which signal to listen to.

## Property Descriptions

### paused

```gdscript
@export var paused = false
```

If this is set to [code]true[/code] the AlwaysBehavior will stop emitting any signals. During runtime, do not set this directly. Instead use [method AlwaysBehavior.pause] and [method AlwaysBehavior.resume]

## Method Descriptions

### pause

```gdscript
func pause()
```

Calling this method results in pausing the execution of always Use [method AlwaysBehavior.resume] to continue the execution

### resume

```gdscript
func resume()
```

Calling this method results in continuing the paused execution Use [method AlwaysBehavior.pause] to stop it again.

## Signals

- signal always(delta): This Signal gets emitted every frame in the [method AlwaysBehavior._process] method if [member AlwaysBehavior.paused] is set to [code]false[/code]
- signal physiscs_always(delta): This Signal gets emitted every frame in the [method AlwaysBehavior._physics_process] method if [member AlwaysBehavior.paused] is set to [code]false[/code]
