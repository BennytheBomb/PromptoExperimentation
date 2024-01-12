<!-- Auto-generated from JSON by GDScript docs maker. Do not edit this document directly. -->

# QueryBehavior

**Extends:** [Behavior](../Behavior)

## Description

## Property Descriptions

### queries

```gdscript
@export var queries: Array[Query]
```

## Method Descriptions

### query

```gdscript
func query(emit_results = true)
```

Initiate a query. Returns [param]

## Signals

- signal found(node): Emitted for each node found, ordered according to the priority strategy. [param node] The node that was found.)
- signal found_all(nodes): Emitted once all nodes have been found. [param nodes] The nodes that were found.
- signal found_none(): Emitted if no node was found.
