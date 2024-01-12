<!-- Auto-generated from JSON by GDScript docs maker. Do not edit this document directly. -->

# ClockBehavior

**Extends:** [Behavior](../Behavior)

## Description

## Property Descriptions

### cycle\_count

```gdscript
@export var cycle_count: int = -1
```

How often the signal [signal ClockBehavor.elapsed] will be emitted. A value of [code]-1[/code] means no limit.

### duration\_seconds

```gdscript
@export var duration_seconds: float = 1
```

- **Setter**: `@duration_seconds_setter`
- **Getter**: `@duration_seconds_getter`

Timer duration in seconds

### paused

```gdscript
@export var paused: bool
```

- **Setter**: `@paused_setter`
- **Getter**: `@paused_getter`

If set to [code]true[/code], the timere will pause itself and resume as soon as it is set to [code]false[/code] again.

### trigger\_every\_frame

```gdscript
@export var trigger_every_frame: bool
```

- **Setter**: `@trigger_every_frame_setter`
- **Getter**: `@trigger_every_frame_getter`

Determines the mode of operation. If this is set to [code]true[/code], the normal timer functionality is used.  Mutual exclusive to [member ClockBehavior.trigger_every_x_seconds]

### trigger\_every\_x\_seconds

```gdscript
@export var trigger_every_x_seconds: bool
```

- **Setter**: `@trigger_every_x_seconds_setter`
- **Getter**: `@trigger_every_x_seconds_getter`

Determines the mode of operation. If this is set to [code]true[/code], the custom "trigger every x seconds" functionality is used. This means the ClockBehavior will emit [signal ClockBehavior.until_elapsed] when the last emit of that signal was at least [member ClockBehavior.trigger_interval_in_seconds] seconds ago.  Mutual exclusive to [member ClockBehavior.trigger_every_frame]

### trigger\_interval\_in\_seconds

```gdscript
@export var trigger_interval_in_seconds: float
```

- **Setter**: `@trigger_interval_in_seconds_setter`
- **Getter**: `@trigger_interval_in_seconds_getter`

If [member ClockBehavior.trigger_every_x_seconds] is set to [code]true[/code], this determines the interval in which [signal ClockBehavior.until_elapsed] is emitted

## Method Descriptions

### reset\_and\_start

```gdscript
func reset_and_start()
```

## Signals

- signal elapsed(): Emitted on [method Timer.timeout]
- signal until_elapsed(): Emitted in one of two cases:  1. If [member ClockBehavior.trigger_every_frame] is set to [code]true[/code], then this is emitted every frame that the timer is active.  2. If [member ClockBehavior.trigger_every_x_seconds] is set to [code]true[/code], then this is emitted if the last trigger was [member ClockBehavior.trigger_interval_in_seconds] seconds ago.
