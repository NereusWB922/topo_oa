from app.pipeline import Step


class ProcessAdhocPptx(Step):
    def execute(self, data):
        result = {}

        page1 = data[0]
        page2 = data[1]
        page3 = data[2]

        key_highlights = page1["texts"][1].split("\n")
        result["Key Highlights"] = self._parse_key_value_pairs(key_highlights[1:])

        result["Quarterly Metrics"] = page2["tables"][0]

        revenue_distribution = page3["texts"][1].split("\n")
        result["Revenue Distribution"] = self._parse_key_value_pairs(
            revenue_distribution[1:]
        )

        return result

    def _parse_key_value_pairs(self, lines):
        key_value_pairs = {}
        for line in lines:
            if ":" in line:
                key, value = line.split(":", 1)
                key_value_pairs[key.strip()] = value.strip()
        return key_value_pairs
