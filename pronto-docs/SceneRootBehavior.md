<!-- Auto-generated from JSON by GDScript docs maker. Do not edit this document directly. -->

# SceneRootBehavior

**Extends:** [Behavior](../Behavior)

## Description

## Property Descriptions

### scene\_tree

```gdscript
var scene_tree: SceneTree
```

The scene tree (calculated in [method SceneRootBehavior._ready])

## Method Descriptions

### apply

```gdscript
func apply(group: StringName, lamda_func: Callable, from: Node2D)
```

This will execute [param lamda_func] on all group elements in the given group.

### apply\_with\_filter

```gdscript
func apply_with_filter(group: StringName, lamda_func: Callable, filter_func: Callable, from: Node2D)
```

This will execute [param lamda_func] on all group elements in the given group, where [param filter_func] evaluates to true.

### apply\_within\_dist

```gdscript
func apply_within_dist(group: StringName, lamda_func: Callable, position: Vector2, max_dist: float, from: Node2D)
```

This will execute [param lamda_func] on all group elements in the given group, that have a maximum distance of [param max_dist] from the provied position.

### notify\_group

```gdscript
func notify_group(group: StringName, notification: int)
```

### notify\_group\_flags

```gdscript
func notify_group_flags(call_flags: int, group: StringName, notification: int)
```

### reload\_current\_scene

```gdscript
func reload_current_scene()
```

### set\_group

```gdscript
func set_group(group: StringName, property: String, value: Variant)
```

### set\_group\_flags

```gdscript
func set_group_flags(call_flags: int, group: StringName, property: String, value: Variant)
```

### quit

```gdscript
func quit(exit_code: int = 0)
```

### unload\_current\_scene

```gdscript
func unload_current_scene()
```

## Signals

- signal node_added(node): Emitted when a node was added to the [member SceneRootBehavior.scene_tree]  [param node]: the node that was added
- signal node_removed(node): Emitted when a node was removed from the [member SceneRootBehavior.scene_tree]  [param node]: the node that was removed
- signal tree_changed(): Emitted on any change in the [member SceneRootBehavior.scene_tree]
