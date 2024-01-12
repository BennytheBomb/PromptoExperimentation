<!-- Auto-generated from JSON by GDScript docs maker. Do not edit this document directly. -->

# PerformanceUIBehavior

**Extends:** [Behavior](../Behavior)

## Description

## Constants Descriptions

### monitor

```gdscript
enum monitor{TIME_FPS = 0, TIME_PROCESS = 1, TIME_PHYSICS_PROCESS = 2, TIME_NAVIGATION_PROCESS = 3, MEMORY_STATIC = 4, MEMORY_STATIC_MAX = 5, MEMORY_MESSAGE_BUFFER_MAX = 6, OBJECT_COUNT = 7, OBJECT_RESOURCE_COUNT = 8, OBJECT_NODE_COUNT = 9, OBJECT_ORPHAN_NODE_COUNT = 10, RENDER_TOTAL_OBJECTS_IN_FRAME = 11, RENDER_TOTAL_PRIMITIVES_IN_FRAME = 12, RENDER_TOTAL_DRAW_CALLS_IN_FRAME = 13, RENDER_VIDEO_MEM_USED = 14, RENDER_TEXTURE_MEM_USED = 15, RENDER_BUFFER_MEM_USED = 16, PHYSICS_2D_ACTIVE_OBJECTS = 17, PHYSICS_2D_COLLISION_PAIRS = 18, PHYSICS_2D_ISLAND_COUNT = 19, PHYSICS_3D_ACTIVE_OBJECTS = 20, PHYSICS_3D_COLLISION_PAIRS = 21, PHYSICS_3D_ISLAND_COUNT = 22, AUDIO_OUTPUT_LATENCY = 23, NAVIGATION_ACTIVE_MAPS = 24, NAVIGATION_REGION_COUNT = 25, NAVIGATION_AGENT_COUNT = 26, NAVIGATION_LINK_COUNT = 27, NAVIGATION_POLYGON_COUNT = 28, NAVIGATION_EDGE_COUNT = 29, NAVIGATION_EDGE_MERGE_COUNT = 30, NAVIGATION_EDGE_CONNECTION_COUNT = 31, NAVIGATION_EDGE_FREE_COUNT = 32, MONITOR_MAX = 33}
```

## Property Descriptions

### fps\_warn

```gdscript
@export var fps_warn: int = 0
```

- **Setter**: `@fps_warn_setter`

Set the lower limit of when the fps_warning signal should be fired. (0 means never)

### TIME\_FPS

```gdscript
@export var TIME_FPS: bool = true
```

### OBJECT\_NODE\_COUNT

```gdscript
@export var OBJECT_NODE_COUNT: bool = true
```

### TIME\_PROCESS

```gdscript
@export var TIME_PROCESS: bool = false
```

### TIME\_PHYSICS\_PROCESS

```gdscript
@export var TIME_PHYSICS_PROCESS: bool = false
```

### TIME\_NAVIGATION\_PROCESS

```gdscript
@export var TIME_NAVIGATION_PROCESS: bool = false
```

### MEMORY\_STATIC

```gdscript
@export var MEMORY_STATIC: bool = false
```

### MEMORY\_STATIC\_MAX

```gdscript
@export var MEMORY_STATIC_MAX: bool = false
```

### MEMORY\_MESSAGE\_BUFFER\_MAX

```gdscript
@export var MEMORY_MESSAGE_BUFFER_MAX: bool = false
```

### OBJECT\_COUNT

```gdscript
@export var OBJECT_COUNT: bool = false
```

### OBJECT\_RESOURCE\_COUNT

```gdscript
@export var OBJECT_RESOURCE_COUNT: bool = false
```

### OBJECT\_ORPHAN\_NODE\_COUNT

```gdscript
@export var OBJECT_ORPHAN_NODE_COUNT: bool = false
```

### RENDER\_TOTAL\_OBJECTS\_IN\_FRAME

```gdscript
@export var RENDER_TOTAL_OBJECTS_IN_FRAME: bool = false
```

### RENDER\_TOTAL\_PRIMITIVES\_IN\_FRAME

```gdscript
@export var RENDER_TOTAL_PRIMITIVES_IN_FRAME: bool = false
```

### RENDER\_TOTAL\_DRAW\_CALLS\_IN\_FRAME

```gdscript
@export var RENDER_TOTAL_DRAW_CALLS_IN_FRAME: bool = false
```

### RENDER\_VIDEO\_MEM\_USED

```gdscript
@export var RENDER_VIDEO_MEM_USED: bool = false
```

### RENDER\_TEXTURE\_MEM\_USED

```gdscript
@export var RENDER_TEXTURE_MEM_USED: bool = false
```

### RENDER\_BUFFER\_MEM\_USED

```gdscript
@export var RENDER_BUFFER_MEM_USED: bool = false
```

### PHYSICS\_2D\_ACTIVE\_OBJECTS

```gdscript
@export var PHYSICS_2D_ACTIVE_OBJECTS: bool = false
```

### PHYSICS\_2D\_COLLISION\_PAIRS

```gdscript
@export var PHYSICS_2D_COLLISION_PAIRS: bool = false
```

### PHYSICS\_2D\_ISLAND\_COUNT

```gdscript
@export var PHYSICS_2D_ISLAND_COUNT: bool = false
```

### PHYSICS\_3D\_ACTIVE\_OBJECTS

```gdscript
@export var PHYSICS_3D_ACTIVE_OBJECTS: bool = false
```

### PHYSICS\_3D\_COLLISION\_PAIRS

```gdscript
@export var PHYSICS_3D_COLLISION_PAIRS: bool = false
```

### PHYSICS\_3D\_ISLAND\_COUNT

```gdscript
@export var PHYSICS_3D_ISLAND_COUNT: bool = false
```

### AUDIO\_OUTPUT\_LATENCY

```gdscript
@export var AUDIO_OUTPUT_LATENCY: bool = false
```

### NAVIGATION\_ACTIVE\_MAPS

```gdscript
@export var NAVIGATION_ACTIVE_MAPS: bool = false
```

### NAVIGATION\_REGION\_COUNT

```gdscript
@export var NAVIGATION_REGION_COUNT: bool = false
```

### NAVIGATION\_AGENT\_COUNT

```gdscript
@export var NAVIGATION_AGENT_COUNT: bool = false
```

### NAVIGATION\_LINK\_COUNT

```gdscript
@export var NAVIGATION_LINK_COUNT: bool = false
```

### NAVIGATION\_POLYGON\_COUNT

```gdscript
@export var NAVIGATION_POLYGON_COUNT: bool = false
```

### NAVIGATION\_EDGE\_COUNT

```gdscript
@export var NAVIGATION_EDGE_COUNT: bool = false
```

### NAVIGATION\_EDGE\_MERGE\_COUNT

```gdscript
@export var NAVIGATION_EDGE_MERGE_COUNT: bool = false
```

### NAVIGATION\_EDGE\_CONNECTION\_COUNT

```gdscript
@export var NAVIGATION_EDGE_CONNECTION_COUNT: bool = false
```

### NAVIGATION\_EDGE\_FREE\_COUNT

```gdscript
@export var NAVIGATION_EDGE_FREE_COUNT: bool = false
```

### minimized

```gdscript
@export var minimized: bool = false
```

If [code]true[/code] the PerformanceUI starts minimized.

### panel\_size

```gdscript
@export var panel_size: Vector2 = "(300, 200)"
```

- **Setter**: `@panel_size_setter`

### label\_cache

```gdscript
var label_cache
```

### panel

```gdscript
var panel: PanelContainer
```

### muted\_gray

```gdscript
var muted_gray: Color = "(0.69, 0.69, 0.69, 1)"
```

### vbox

```gdscript
var vbox: VBoxContainer
```

### header

```gdscript
var header: HBoxContainer
```

### start

```gdscript
var start: Vector2
```

### init\_position

```gdscript
var init_position: Vector2
```

### is\_moving

```gdscript
var is_moving: bool
```

### is\_resizing

```gdscript
var is_resizing: bool
```

### resize\_x

```gdscript
var resize_x: bool
```

### resize\_y

```gdscript
var resize_y: bool
```

### initial\_size

```gdscript
var initial_size: Vector2
```

### grab\_threshold

```gdscript
var grab_threshold: int = 30
```

### resize\_threshold

```gdscript
var resize_threshold: int = 10
```

## Method Descriptions

### create\_minimizing\_button

```gdscript
func create_minimizing_button()
```

### create\_header

```gdscript
func create_header()
```

### handle\_size\_button\_click

```gdscript
func handle_size_button_click(button: Button, initial: bool = false)
```

### handles

```gdscript
func handles()
```

## Signals

- signal fps_warning(current_fps): 
