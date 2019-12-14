class Tutorial:
    AUTHOR: str = "Volodymyr Yahello"

    def __init__(self, foo: str, bar: str) -> None:
        self._foo: str = foo
        self._bar: str = bar

    def foo(self) -> str:
        return self._foo

    def bar(self) -> str:
        return self._bar

    def meta(self) -> str:
        return f"Packaging tutorial by {self.AUTHOR}"
