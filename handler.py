from typing import Dict, Any

class InputHandler:
    def __init__(self) -> None:
        self.data: Dict[str, Any] = {}

    def update_input(self, input_id: str, value: Any) -> None:
        """Update the input with a new value."""
        self.data[input_id] = value

    def get_input(self, input_id: str) -> Any:
        """Retrieve the value of the specified input."""
        return self.data.get(input_id, None)

    def clear_inputs(self) -> None:
        """Clear all stored inputs."""
        self.data.clear()

    def __str__(self) -> str:
        """String representation of the input data."""
        return str(self.data)
