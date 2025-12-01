from typing import Any


class Pet:
    def __init__(
        self,
        name: Any,
        species: Any,
        gender: Any = "not defined",
        age: Any = 0,
        n_legs: Any = 4,
    ) -> None:
        # Go through the setters so we reuse validation/conversion logic
        self.name = name
        self.species = species
        self.gender = gender
        self.age = age
        self.n_legs = n_legs

    # --- string-like fields -------------------------------------------------

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: Any) -> None:
        try:
            self._name = str(value)
        except Exception as exc:
            raise ValueError("name must be convertible to str") from exc

    @property
    def species(self) -> str:
        return self._species

    @species.setter
    def species(self, value: Any) -> None:
        try:
            self._species = str(value)
        except Exception as exc:
            raise ValueError("species must be convertible to str") from exc

    @property
    def gender(self) -> str:
        return self._gender

    @gender.setter
    def gender(self, value: Any) -> None:
        try:
            self._gender = str(value)
        except Exception as exc:
            raise ValueError("gender must be convertible to str") from exc

    # --- int-like fields ----------------------------------------------------

    @property
    def age(self) -> int:
        return self._age

    @age.setter
    def age(self, value: Any) -> None:
        try:
            self._age = int(value)
        except (TypeError, ValueError) as exc:
            raise ValueError("age must be convertible to int") from exc

    @property
    def n_legs(self) -> int:
        return self._n_legs

    @n_legs.setter
    def n_legs(self, value: Any) -> None:
        try:
            self._n_legs = int(value)
        except (TypeError, ValueError) as exc:
            raise ValueError("n_legs must be convertible to int") from exc

    # --- behaviour ----------------------------------------------------------

    def have_birthday(self, b_day: Any = 1) -> int:
        try:
            increment = int(b_day)
        except (TypeError, ValueError) as exc:
            raise ValueError("birthday increment must be convertible to int") from exc
        self.age += increment
        return self.age

    def __str__(self) -> str:
        return (
            f"{self.name} the {self.gender} {self.species}, "
            f"age {self.age} has {self.n_legs} legs!"
        )