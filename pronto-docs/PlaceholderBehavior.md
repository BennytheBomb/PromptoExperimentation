<!-- Auto-generated from JSON by GDScript docs maker. Do not edit this document directly. -->

# PlaceholderBehavior

**Extends:** [Behavior](../Behavior)

## Description

## Constants Descriptions

### OUTLINE\_SHADER

```gdscript
const OUTLINE_SHADER: String = "res://addons/pronto/shader/outline.gdshader"
```

## Property Descriptions

### label

```gdscript
@export var label = ""
```

- **Setter**: `@label_setter`

The label that is shown inside the Placeholder, unless a sprite is used.

### color

```gdscript
@export var color = "(1, 1, 1, 1)"
```

- **Setter**: `@color_setter`

The color used for the placeholder.

### keep\_in\_origin

```gdscript
@export var keep_in_origin = true
```

If [code]true[/code], this Placeholder's parent will be moved instead of the placeholder in the editor. Convenient for not having to switch selected items all the time.

### undefined\_shape\_string

```gdscript
var undefined_shape_string
```

### use\_sprite

```gdscript
@export var use_sprite = false
```

- **Setter**: `@use_sprite_setter`

If [code]true[/code] a [class Sprite2D] is shown.

### DEFAULT\_TEXTURE

```gdscript
var DEFAULT_TEXTURE
```

### sprite\_texture

```gdscript
@export var sprite_texture: Texture2D
```

- **Setter**: `@sprite_texture_setter`

The texture used for the [class Sprite2D]. Can be loaded from a file or from the sprite_library.

### sprite\_library

```gdscript
@export var sprite_library: Texture2D
```

- **Setter**: `@sprite_library_setter`

The sprite library is desribed in [class SpriteInspector] as well as "addons/pronto/helpers/sprite_window.tscn". Search through a library of textures to choose your sprite.

### outline\_visible

```gdscript
@export var outline_visible: bool = false
```

- **Setter**: `@outline_visible_setter`

If [code]true[/code], the outline is shown.

### outline\_color

```gdscript
@export var outline_color: Color = "(1, 1, 0, 1)"
```

- **Setter**: `@outline_color_setter`

The color used for the outline.

### outline\_width

```gdscript
@export var outline_width: float = 1
```

- **Setter**: `@outline_width_setter`

The width of the outline.

### outline\_pattern

```gdscript
@export var outline_pattern = 0
```

- **Setter**: `@outline_pattern_setter`

The rounding method for corners of the outline (only used if [class Sprite2D] is used).

### shape\_type

```gdscript
@export var shape_type: String = "Rect"
```

- **Setter**: `@shape_type_setter`

This will define the shape of the placeholder as well as the shape of the hitbox.

### placeholder\_size

```gdscript
var placeholder_size = "(20, 20)"
```

- **Setter**: `@placeholder_size_setter`

The size of the placeholder.

### capsule\_height

```gdscript
var capsule_height: float = 30
```

- **Setter**: `@capsule_height_setter`

The height of the capsule.

### capsule\_radius

```gdscript
var capsule_radius: float = 10
```

- **Setter**: `@capsule_radius_setter`

The radius of the capsule.

### circle\_radius

```gdscript
var circle_radius: float = 10
```

- **Setter**: `@circle_radius_setter`

The radius of the circle.

### sprite

```gdscript
var sprite: Sprite2D
```

### size

```gdscript
var size: Vector2
```

- **Getter**: `@size_getter`

### shape

```gdscript
var shape
```

## Method Descriptions

### show\_outline

```gdscript
func show_outline()
```

Shows an outline around the Placeholder.

### hide\_outline

```gdscript
func hide_outline()
```

Hides the outline around the Placeholder.

### set\_outline\_visible

```gdscript
func set_outline_visible(visible)
```

Toggles the visibility of the outline according to the given parameter.

### flash

```gdscript
func flash(color: Color, duration: float = 0.3)
```

Flashes this Placeholder a certain color for a duration. It will take on the desired color immediately and return to its original color over the given duration.

### should\_keep\_in\_origin

```gdscript
func should_keep_in_origin()
```

### show\_icon

```gdscript
func show_icon()
```

### find\_non\_transparent\_rect

```gdscript
func find_non_transparent_rect()
```

### handles

```gdscript
func handles()
```

