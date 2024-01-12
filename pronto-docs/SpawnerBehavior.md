<!-- Auto-generated from JSON by GDScript docs maker. Do not edit this document directly. -->

# SpawnerBehavior

**Extends:** [Behavior](../Behavior)

## Description

## Property Descriptions

### scene\_path

```gdscript
@export var scene_path: NodePath = ""
```

Spawns all children by default. Alternatively, provide a scene path here.

### container

```gdscript
@export var container: Node = null
```

When set, spawns new nodes as children of the given node.

### shape\_type

```gdscript
@export var shape_type: String = "Generic"
```

- **Setter**: `@shape_type_setter`

Type of shape used for the [method SpawnerBehavior.spawn_in_shape] method.

### spawn\_shape\_polygon

```gdscript
@export var spawn_shape_polygon: Polygon2D = null
```

- **Setter**: `@spawn_shape_polygon_setter`

Polygon used by [method SpawnerBehavior.spawn_in_shape] method. Dont set the [class PolygonShape2D] itself as child of the spawner.

### spawn\_shape\_generic

```gdscript
@export var spawn_shape_generic: Shape2D = null
```

- **Setter**: `@spawn_shape_generic_setter`

Shape used by [method SpawnerBehavior.spawn_in_shape] method. Supports [class CircleShape2D], [class RectangleShape2D] and [class CapsuleShape2D].

### spawn\_shape\_color

```gdscript
@export var spawn_shape_color: Color = "(0, 0.6, 0.702, 0.4196)"
```

- **Setter**: `@spawn_shape_color_setter`

Debug Color in Editor for the shape used by [method SpawnerBehavior.spawn_in_shape].

### last\_spawn\_shape\_size\_rectangle

```gdscript
var last_spawn_shape_size_rectangle: Vector2
```

### last\_spawn\_shape\_size\_circle

```gdscript
var last_spawn_shape_size_circle: float
```

### last\_spawn\_shape\_size\_capsule

```gdscript
var last_spawn_shape_size_capsule: float
```

### shape\_radius

```gdscript
var shape_radius: float
```

### shape\_height

```gdscript
var shape_height: float
```

### shape\_size

```gdscript
var shape_size: Vector2
```

- **Setter**: `@shape_size_setter`

### spawn\_shape\_polygon\_randomizer

```gdscript
var spawn_shape_polygon_randomizer: PolygonRandomPointGenerator
```

### scenes

```gdscript
var scenes = null
```

List of all blueprints the spawner can spawn gets calculated automatically in [method SpawnerBehavior._ready]

### scene\_offsets

```gdscript
var scene_offsets = null
```

A list of offsets that can be used for spawning the new instances. This was added so that the new instances don't spawn at the same position which might result in unwanted collision behavior etc. The offsets are mapped to the blueprints by their index in the respective arrays.

## Method Descriptions

### spawn

```gdscript
func spawn(indices: Array = null, pos: Vector2 = "(inf, inf)", toward: Vector2 = "(inf, inf)", use_shape: bool = false)
```

Spawns the selected blueprint(s) as the SpawnerBehavior's sibling node.  [param indices]: selects the blueprints to spawn. Specify the elements you want to spawn in an integer array. Pass an empty array to spawn every child. Default: [code][][/code]  [param pos]: The position to spawn the new instance(s) at. Overwrites other rules like [code]use_shape[/code] if specified  [param toward]: The position to rotate the new instance(s) towards Position is in global space.  [param use_shape]: Whether to use the with [member SpawnerBehavior.shape_typ] specified type of spawn shape for spawning.  [param relative]: selects whether the the [member SpawnerBehavior.scene_offsets] should be used for the spawning. If set to [code]false[/code], the new instance(s) will be spawned at the spawner's position. If set to [code]true[/code], the corresponding offset is applied afterwards.

### lines

```gdscript
func lines()
```

Override of [method Behavior.lines] in order to display dashed lines towards the spawner's blueprints (aka its childs)

### handles

```gdscript
func handles()
```

## Signals

- signal spawned(instance): Emitted when [method SpawnerBehavior.spawn] completed successfully.  [param instance]: the newly spawned node
