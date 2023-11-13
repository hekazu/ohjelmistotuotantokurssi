class Project:
    def __init__(self, name, description, licence, authors, dependencies, dev_dependencies):
        self.name = name
        self.description = description
        self.licence = licence
        self.authors = authors
        self.dependencies = dependencies
        self.dev_dependencies = dev_dependencies

    def _stringify_multiple_entries(self, multi_item):
        return "\n- ".join(multi_item) if len(multi_item) > 0 else "-"

    def __str__(self):
        return (
            f"Name: {self.name}"
            f"\nDescription: {self.description or '-'}"
            f"\nLicense: {self.licence}\n"
            f"\nAuthors:\n- {self._stringify_multiple_entries(self.authors)}\n"
            f"\nDependencies:\n- {self._stringify_multiple_entries(self.dependencies)}\n"
            f"\nDevelopment dependencies:\n- {self._stringify_multiple_entries(self.dev_dependencies)}"
        )
