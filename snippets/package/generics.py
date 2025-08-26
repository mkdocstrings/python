"""Some module showing generics.

Type Aliases:
    SomeType: Some type alias.
"""

type SomeType[Z] = int | list[Z]
"""Some type alias.

Type parameters:
    Z: Some type parameter.
"""


class MagicBag[T: (str, bytes) = str](list[T]):
    """A magic bag of items.

    Type parameters:
        T: Some type.
    """

    def __init__[U: (int, bool)](self, *args: T, flag1: U | None = None, flag2: U | None = None) -> None:
        """Initialize bag.

        Type parameters:
            U: Some flag type.

        Parameters:
            flag1: Some flag.
            flag2: Some flag.
        """
        super().__init__(args)
        self.flag1 = flag1
        self.flag2 = flag2

    def mutate[K](self, item: T, into: K) -> K:
        """Shake the bag to mutate an item into something else (and eject it).

        Type parameters:
            K: Some other type.

        Parameters:
            item: The item to mutate.
            into: Mutate the item into something like this.

        Returns:
            The mutated item.
        """
        ...
