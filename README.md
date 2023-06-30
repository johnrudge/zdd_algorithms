# Zdd Algorithms

Zdd Algorithms is a Python library that implements the zdd algorithms that are described on the wikipedia [page](https://en.wikipedia.org/wiki/Zero-suppressed_decision_diagram)

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install zdd_wiki_algorithms.

```bash
pip install zdd_algorithms
```

## Zero-suppressed decision diagram

Zdd are a special kind of Binary decision diagram that represents a set of sets.
![alt-text](https://en.wikipedia.org/wiki/Zero-suppressed_decision_diagram#/media/File:Figure_4_ZDD_family_set.svg)
This Zdd represents the set {{1,3},{2,3},{1,2}} \
Every node has a exactly 2 outgoing edges LO and HI. The LO edge is usally represented by a dotted line and the HI edge with a solid line.
The easiest way to get the set from a visual zdd by hand is to take every path from the root node to the {ø} node(⊤ is also often used as a label for this node).\
Every path represents a set and all paths combined is the set of sets that the Zdd represents.
In this example there are 3 paths. \
If a node has a LO edge in the path that nodes value is ignored. All the other values together represents a set \
3 → 2 → {ø} This path represents the set {3,2} \
3 ⇢ 2 → 1 → {ø} This path represents the set {1,2} \
3 → 2 ⇢ 1 → {ø} This path represents the set {1,3} \
Therefor this zdd represents the set {{1,3},{2,3},{1,2}}

## Usage

Since we cannot have a set of sets in python we use set of frozensets when converting a zdd to the set representation and vice versa

```python
import zdd

# Creates a zdd node that represents the set {{1,3,4},{2,4}}
foobar.pluralize('word')

# returns 'geese'
foobar.pluralize('goose')

# returns 'phenomenon'
foobar.singularize('phenomena')
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)
