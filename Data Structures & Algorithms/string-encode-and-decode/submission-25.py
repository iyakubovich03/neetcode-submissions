class Solution:

    def encode(self, strs: List[str]) -> str:
        return "_/_".join(strs) if strs else "****"

    def decode(self, s: str) -> List[str]:
        if s=="****":
            return []
        return s.split("_/_")

