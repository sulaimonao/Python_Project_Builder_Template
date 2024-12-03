#placeholder_manager.py  manage placeholders systematically

class PlaceholderManager:
    def __init__(self, config):
        self.config = config

    def resolve_placeholders(self, text):
        """
        Replace placeholders in the text with actual values from the configuration.
        """
        for placeholder in self.config.get_value("placeholders", []):
            key = placeholder.strip("{{}}")
            value = self.config.get_value(key, placeholder)
            text = text.replace(placeholder, value)
        return text

