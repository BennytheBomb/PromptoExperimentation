### How do I connect two behaviors?
**Relevant information:**

> [[Readme](pronto/README.md#connections)] Connections are an extension of Godot signals to be more flexible. Connections can be dragged from any behavior to any arbitrary node in a scene. They are the primary means to assemble your game by wiring Behaviors together.

> [[Readme](pronto/README.md#connections)] Connections are created by hovering the "+" that appears below selected nodes. There are two types of connections.
The type "target" is created by dragging a signal from the list onto its receiver. From the list in the dialog, you can either choose any method to invoke or choose <statement(s)> to execute arbitrary code. In the expressions for the arguments or the arbitrary code, you can write Godot expression that can access from and to.
The type "expression" allows to execute arbitrary Godot code without a receiver node. Create an expression connection by double-clicking a signal in the list. You can access from in the code.

✅ Question can be answered!

### How do I adjust the properties of a PlatformerControllerBehavior?
**Relevant information:**

> [[Readme](pronto/README.md#behaviors)] PlatformerControllerBehavior makes the parent behave like a platformer character, meaning that it can jump, move horizontally, and is affected by gravity. Must be a child of a CharacterBody2D.

> [[Pronto-Docs](pronto-docs/PlatformerControllerBehavior.md)] Property descriptions [...]

❓ Unsure if question could be answered. No description of how to change properties on a behavior.

### How can I damage a player?
**Relevant information:**

> [[Readme](pronto/README.md#behaviors)] HealthBarBehavior shows a rectangular health bar. Offers methods to manipulate the current health and emits a signal when health drops to zero.

> [[Pronto-Docs](pronto-docs/HealthBarBehavior.md)] Method Descriptions - damage [...]

❓ Unsure if question could be answered. LLM would need to get creative and retrieve the HealthBarBehavior which contains the damage method.

### What does an AlwaysBehavior do?
**Relevant information:**

> [[Readme](pronto/README.md#behaviors)] AlwaysBehavior triggers every frame. Analog to Godot's _process function. Can be paused.

> [[Pronto-Docs](pronto-docs/AlwaysBehavior.md)] AlwaysBehavior [...]

✅ Question can be answered!

### How to change the sprite of a PlaceholderBehavior?
**Relevant information:**

> [[Readme](pronto/README.md#behaviors)] PlaceholderBehavior shows a colored rectangle with a label. Useful as a quick means to communicate a game object's function. Functions as a collision shape, so you don't need to add another. Instead of a rectangle a placeholder can also display a sprite instead (use the Sprite Library in the Inspector to choose an existing texture or load your own). Can be flash()ed in a different color.

> [[Pronto-Docs](pronto-docs/PlaceholderBehavior.md)] sprite_library\
> `@export var sprite_library: Texture2D`\
> Setter: `@sprite_library_setter`\
> The sprite library is described in [class SpriteInspector] as well as "addons/pronto/helpers/sprite_window.tscn". Search through a library of textures to choose your sprite.

✅ Question can be answered!

### How to access values in a StoreBehaviour?
**Relevant information:**

> [[Readme](pronto/README.md#behaviors)] StoreBehavior uses the Godot meta properties to store state. You can configure it to store values in the global dictionary G and access it via G.at(prop).

> [[Pronto-Docs](pronto-docs/StoreBehavior.md)] at
> `func at(prop: String, default = null)`

✅ Question can be answered!

### What is the difference between a BackgroundBehavior and a PlaceholderBehaviour?
**Relevant information:**

> [[Readme](pronto/README.md#behaviors)] PlaceholderBehavior shows a colored rectangle with a label. Useful as a quick means to communicate a game object's function. Functions as a collision shape, so you don't need to add another. Instead of a rectangle a placeholder can also display a sprite instead (use the Sprite Library in the Inspector to choose an existing texture or load your own). Can be flash()ed in a different color.

> [[Pronto-Docs](pronto-docs/PlaceholderBehavior.md)] sprite_library\
> `@export var sprite_library: Texture2D`\
> Setter: `@sprite_library_setter`\
> The sprite library is described in [class SpriteInspector] as well as "addons/pronto/helpers/sprite_window.tscn". Search through a library of textures to choose your sprite.

> [[Readme](pronto/README.md#behaviors)] BackgroundBehavior add to your scene to change the background color of the scene.

> [[Pronto-Docs](pronto-docs/BackgroundBehavior.md)] BackgroundBehavior

✅ Question can be answered but it probably needs to get a bit creative here!

### Can I add a custom behavior to the game?
**Relevant information:**

> [[Readme](pronto/README.md#phase-2-extending-the-framework)] Phase 2: Extending the Framework [...]

✅ Question can be answered!

### What behavior to use for finding a specific node in my scene?
**Relevant information:**

> [[Readme](pronto/README.md#behaviors)] QueryBehavior searches for nodes in the scene and emits signals for results. Properties allow to filter, sort, and limit results. Can be used for tasks such as destroying all enemies in a certain radius, infecting a random player, or finding the nearest health pack.

> [[Pronto-Docs](pronto-docs/QueryBehavior.md)] QueryBehavior Method Descriptions
query\
func query(emit_results = true)\
Initiate a query. Returns [param]

✅ Question can be answered!

### What does the GroupBehavior do?
**Relevant information:**

> [[Readme](pronto/README.md#behaviors)] GroupBehavior	Draws a shape around its children to group them visually. Only visible in the editor.

> [[Pronto-Docs](pronto-docs/GroupBehavior.md)] GroupBehavior [...]

✅ Question can be answered, although pronto docs is not very helpful here!

### What does the FPS warn property on the PerformanceUIBehavior do?
**Relevant information:**

> [[Pronto-Docs](pronto-docs/PerformanceUIBehavior.md)] PerformanceUIBehavior

> Property Descriptions\
fps_warn\
`@export var fps_warn: int = 0`\
Setter: `@fps_warn_setter`\
Set the lower limit of when the fps_warning signal should be fired. (0 means never)

❓ Unsure if question could be answered. No description in readme and description in class reference not helpful. 
LLM needs to be very creative.

### What kind of expressions are valid to evaluate in the BindBehavior?
**Relevant information:**

> [[Readme](pronto/README.md#behaviors)] BindBehavior optionally reads some properties and then writes one property of its parent. Changes to the properties it reads are synced every frame. The read properties are accessible in the convert expression; the first under value0, the second under value1 and so on. For example, create a Label node, add a Bind node as a child, use text as property and put any expression in its convert field. Another example would use a Clock with a Bind node as a child that uses duration_seconds as a property to change the trigger-time depending on a Value-Behavior.

> [[Pronto-Docs](pronto-docs/BindBehavior.md)] Bind Behavior - Property Descriptions\
evaluate\
@export var evaluate: ConnectionScript\
Script to evaluate to find the current property value to set.

✅ Question can be answered!

### What behavior to use for making UI?
**Relevant information:**

❌ No relevant information found. Question can't be answered

### How can I disable a behavior?
**Relevant information:**

> [[Readme](pronto/README.md#connections)] You can disable a connection by unchecking the checkbox in the top-right or in its context menu.

❌ Question can't be really answered. No details about disabling a behavior.

### How to disconnect two behaviors?
**Relevant information:**

> [[Readme](pronto/README.md#connections)] Deleting\
Open the connection, then click on the trash icon in the top-right.
Alternatively, right-click the connection and choose "Delete".

✅ Question can be answered!