class Solution:

    def encode(self, strs: List[str]) -> str:
        return "#".join(s.replace('#','##') for s in strs)

    def decode(self, s: str) -> List[str]:
        if not s:
            return [""]

        return [part.replace('##','#') for part in s.split('#')]
