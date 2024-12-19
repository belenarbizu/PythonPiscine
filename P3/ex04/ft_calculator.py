class calculator:
    """
    Calculator of vectors (dot product, add and subtract)
    """
    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """
        Calculates dot product of two vectors
        """
        result = sum(float(x * y) for x, y in zip(V1, V2))
        print("Dot product is:", result)

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """
        Adds corresponding elements of two vectors
        """
        result = [float(x + y) for x, y in zip(V1, V2)]
        print("Add Vector is:", result)

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """
        Subtracts corresponding elements of the
        second vector from the first vector.
        """
        result = [float(x - y) for x, y in zip(V1, V2)]
        print("Sous Vector is:", result)
