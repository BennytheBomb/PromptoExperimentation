<!-- Auto-generated from JSON by GDScript docs maker. Do not edit this document directly. -->

# ExportBehavior

**Extends:** [Behavior](../Behavior)

## Description

## Constants Descriptions

### DEFAULT\_AUTHOR

```gdscript
const DEFAULT_AUTHOR: String = "<Author>"
```

### DEFAULT\_TITLE

```gdscript
const DEFAULT_TITLE: String = "<Title>"
```

## Property Descriptions

### title

```gdscript
@export var title: String = "<Title>"
```

- **Setter**: `@title_setter`

The display title of the game

### authors

```gdscript
@export var authors: PackedStringArray
```

- **Setter**: `@authors_setter`

All authors of the game

### description

```gdscript
@export var description = ""
```

- **Setter**: `@description_setter`

The description of the game

### take\_screenshot

```gdscript
@export var take_screenshot: bool = true
```

If true, a screenshot will be taken after a delay and saved as thumbnail.png

### wait\_seconds

```gdscript
@export var wait_seconds: int = 1
```

The delay until the screenshot is taken

### timer

```gdscript
var timer: Timer
```

### export\_path

```gdscript
var export_path
```

